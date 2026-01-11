#!/usr/bin/env python3
"""
Deterministic validator enforcing the Judgment State Canon contract.
Reads JSON from stdin and reports validation outcome.
"""

import json
import sys
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Set, Tuple

ENUMS: Dict[str, Set[str]] = {
    "info_sufficiency": {"full", "partial", "sparse"},
    "signal_consistency": {"aligned", "mixed", "conflicting"},
    "risk_severity": {"none", "low", "medium", "high"},
    "risk_immediacy": {"deferred", "emerging", "imminent"},
    "intervention_window": {"closed", "narrowing", "open"},
    "action_permission": {"proceed", "monitor", "hold", "stop", "handoff"},
    "escalation_trigger": {"none", "data_gap", "conflict_spike", "guardrail_violation"},
    "required_probe": {"none", "simulation", "closed_track", "live_shadow", "governance_review"},
}

REQUIRED_KEYS: Set[str] = set(ENUMS.keys()) | {"decision_confidence"}
DECISION_CONF_KEYS = {"lower_bound", "upper_bound"}
ALLOWED_TOP_KEYS = {"judgment_state", "tension", "error", "violated_rules"}
ALLOWED_ERRORS = {"state_unresolvable", "insufficient_context"}
TENSION_RULES = {"high_risk_proceed_guardrail"}


@dataclass
class ValidationResult:
    ok: bool
    error: Optional[str]
    violated_rules: List[str]


def _is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def _collect_schema_violations(state: Dict[str, Any]) -> List[str]:
    violations: List[str] = []

    extra = set(state.keys()) - REQUIRED_KEYS
    missing = REQUIRED_KEYS - set(state.keys())
    if extra:
        violations.append(f"schema.extra_keys:{sorted(extra)}")
    if missing:
        violations.append(f"schema.missing_keys:{sorted(missing)}")

    for key, allowed in ENUMS.items():
        if key in state:
            if state[key] not in allowed:
                violations.append(f"schema.enum:{key}={state.get(key)}")

    dc = state.get("decision_confidence")
    if not isinstance(dc, dict):
        violations.append("schema.decision_confidence:not_object")
        return violations

    if set(dc.keys()) != DECISION_CONF_KEYS:
        violations.append(f"schema.decision_confidence.keys:{sorted(dc.keys())}")
        return violations

    lb = dc.get("lower_bound")
    ub = dc.get("upper_bound")
    if not _is_number(lb) or not _is_number(ub):
        violations.append("schema.decision_confidence:not_number")
        return violations

    if not (0.0 <= lb <= ub <= 1.0):
        violations.append("confidence_bounds_ordered")

    return violations


def _collect_invariant_violations(state: Dict[str, Any], has_tension: bool) -> List[str]:
    v: List[str] = []

    if state["risk_severity"] == "high" and state["action_permission"] == "proceed":
        if state["required_probe"] != "live_shadow":
            v.append("high_risk_proceed_guardrail")
        if state["intervention_window"] != "open":
            v.append("high_risk_proceed_guardrail")
        if not has_tension:
            v.append("high_risk_proceed_guardrail")

    if state["action_permission"] == "handoff":
        if state["escalation_trigger"] == "none":
            v.append("handoff_requires_escalation")
        if state["required_probe"] != "governance_review":
            v.append("handoff_requires_escalation")

    if state["risk_immediacy"] == "imminent":
        if state["intervention_window"] not in {"closed", "narrowing"}:
            v.append("imminent_forces_closure")
        if state["action_permission"] not in {"stop", "hold"}:
            v.append("imminent_forces_closure")

    if state["info_sufficiency"] == "sparse":
        if state["action_permission"] in {"proceed", "monitor"}:
            v.append("sparse_info_blocks_forward_motion")
        if state["escalation_trigger"] not in {"data_gap", "guardrail_violation"}:
            v.append("sparse_info_blocks_forward_motion")

    if state["action_permission"] == "stop":
        if state["risk_severity"] != "high":
            v.append("stop_demands_guardrail")
        if state["escalation_trigger"] not in {"conflict_spike", "guardrail_violation"}:
            v.append("stop_demands_guardrail")

    return v


def _validate_tension(obj: Any) -> Tuple[bool, Optional[str]]:
    if obj is None:
        return True, None
    if not isinstance(obj, dict):
        return False, "contract.tension_not_object"
    if set(obj.keys()) != {"rule_id", "note"}:
        return False, "contract.tension_keys"
    rule_id = obj.get("rule_id")
    note = obj.get("note")
    if rule_id not in TENSION_RULES:
        return False, "contract.tension_rule_not_allowed"
    if not isinstance(note, str) or not note.strip():
        return False, "contract.tension_note_empty"
    return True, None


def validate_llm_output(raw: str) -> ValidationResult:
    try:
        payload = json.loads(raw)
    except Exception:
        return ValidationResult(ok=False, error="invalid_json", violated_rules=[])

    if not isinstance(payload, dict):
        return ValidationResult(ok=False, error="contract.top_not_object", violated_rules=[])

    extra_top = set(payload.keys()) - ALLOWED_TOP_KEYS
    if extra_top:
        return ValidationResult(
            ok=False,
            error="contract.extra_top_keys",
            violated_rules=[f"extra:{sorted(extra_top)}"],
        )

    has_state = "judgment_state" in payload
    has_error = "error" in payload
    if has_state == has_error:
        return ValidationResult(
            ok=False,
            error="contract.envelope_conflict",
            violated_rules=[],
        )

    if has_error:
        if not isinstance(payload["error"], str):
            return ValidationResult(ok=False, error="contract.error_not_string", violated_rules=[])
        if payload["error"] not in ALLOWED_ERRORS:
            return ValidationResult(ok=False, error="contract.invalid_error_code", violated_rules=[])

        violated_rules = payload.get("violated_rules", [])
        if payload["error"] == "state_unresolvable":
            if not isinstance(violated_rules, list) or not all(
                isinstance(x, str) and x for x in violated_rules
            ):
                return ValidationResult(
                    ok=False,
                    error="contract.invalid_violated_rules",
                    violated_rules=[],
                )
        else:
            if violated_rules not in ([], None):
                return ValidationResult(
                    ok=False,
                    error="contract.unexpected_violated_rules",
                    violated_rules=[],
                )

        if "tension" in payload:
            return ValidationResult(ok=False, error="contract.tension_with_error", violated_rules=[])

        return ValidationResult(ok=False, error=payload["error"], violated_rules=violated_rules or [])

    if "violated_rules" in payload:
        return ValidationResult(ok=False, error="contract.violated_rules_without_error", violated_rules=[])

    state = payload["judgment_state"]
    if not isinstance(state, dict):
        return ValidationResult(ok=False, error="contract.state_not_object", violated_rules=[])

    tension_obj = payload.get("tension")
    tension_valid, tension_error = _validate_tension(tension_obj)
    if not tension_valid:
        return ValidationResult(ok=False, error=tension_error, violated_rules=[])

    schema_violations = _collect_schema_violations(state)
    invariant_violations = _collect_invariant_violations(state, has_tension=tension_obj is not None)
    violated = sorted(set(schema_violations + invariant_violations))

    if violated:
        return ValidationResult(ok=False, error="state_unresolvable", violated_rules=violated)

    return ValidationResult(ok=True, error=None, violated_rules=[])


def _main() -> None:
    raw = sys.stdin.read()
    result = validate_llm_output(raw.strip())
    print(json.dumps(result.__dict__, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    _main()
