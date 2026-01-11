#!/usr/bin/env python3
"""
Adversarial output fuzzer for the Judgment State Canon.
Generates synthetic payloads that mimic common LLM failure modes
and feeds them into validator.py to verify they are rejected.
"""

import json
from dataclasses import dataclass
from typing import Dict, List, Optional

from validator import validate_llm_output


BASE_STATE = {
    "info_sufficiency": "partial",
    "signal_consistency": "mixed",
    "risk_severity": "high",
    "risk_immediacy": "deferred",
    "decision_confidence": {"lower_bound": 0.31, "upper_bound": 0.48},
    "intervention_window": "open",
    "action_permission": "proceed",
    "escalation_trigger": "conflict_spike",
    "required_probe": "live_shadow",
}


@dataclass
class FuzzCase:
    name: str
    envelope: Dict
    expected_ok: bool
    expected_error: Optional[str] = None
    note: str = ""


def clone_state() -> Dict:
    return json.loads(json.dumps(BASE_STATE))


def build_cases() -> List[FuzzCase]:
    cases: List[FuzzCase] = []

    cases.append(
        FuzzCase(
            name="valid_with_tension",
            envelope={
                "judgment_state": clone_state(),
                "tension": {
                    "rule_id": "high_risk_proceed_guardrail",
                    "note": "Live shadow rollback with manual veto.",
                },
            },
            expected_ok=True,
            note="Baseline canonical success.",
        )
    )

    typo_state = clone_state()
    typo_state["action_permission"] = "procede"
    cases.append(
        FuzzCase(
            name="enum_typo",
            envelope={"judgment_state": typo_state},
            expected_ok=False,
            expected_error="state_unresolvable",
            note="Misspelled enum should be rejected.",
        )
    )

    missing_conf = clone_state()
    missing_conf.pop("decision_confidence")
    cases.append(
        FuzzCase(
            name="missing_decision_confidence",
            envelope={"judgment_state": missing_conf},
            expected_ok=False,
            expected_error="state_unresolvable",
            note="Required key removed.",
        )
    )

    no_tension = clone_state()
    cases.append(
        FuzzCase(
            name="high_risk_no_tension",
            envelope={"judgment_state": no_tension},
            expected_ok=False,
            expected_error="state_unresolvable",
            note="High risk proceed without tension metadata.",
        )
    )

    bad_tension = clone_state()
    cases.append(
        FuzzCase(
            name="tension_invalid_rule",
            envelope={
                "judgment_state": bad_tension,
                "tension": {"rule_id": "unknown_rule", "note": "??"},
            },
            expected_ok=False,
            expected_error="contract.tension_rule_not_allowed",
            note="Tension referencing unknown invariant.",
        )
    )

    extra_top = clone_state()
    cases.append(
        FuzzCase(
            name="extra_top_key",
            envelope={
                "judgment_state": extra_top,
                "tension": {
                    "rule_id": "high_risk_proceed_guardrail",
                    "note": "Live shadow requirement.",
                },
                "comment": "this should fail",
            },
            expected_ok=False,
            expected_error="contract.extra_top_keys",
            note="Additional top-level key not allowed.",
        )
    )

    sparse_proceed = clone_state()
    sparse_proceed["info_sufficiency"] = "sparse"
    cases.append(
        FuzzCase(
            name="sparse_proceed",
            envelope={
                "judgment_state": sparse_proceed,
                "tension": {
                    "rule_id": "high_risk_proceed_guardrail",
                    "note": "Still not allowed with sparse info.",
                },
            },
            expected_ok=False,
            expected_error="state_unresolvable",
            note="Sparse info cannot grant proceed action.",
        )
    )

    mixed_case = clone_state()
    mixed_case["action_permission"] = "Proceed"
    cases.append(
        FuzzCase(
            name="mixed_case_enum",
            envelope={"judgment_state": mixed_case},
            expected_ok=False,
            expected_error="state_unresolvable",
            note="Enums are case sensitive.",
        )
    )

    whitespace = clone_state()
    envelope_ws = {
        "judgment_state": whitespace,
        "tension": {
            "rule_id": "high_risk_proceed_guardrail",
            "note": " " * 5,
        },
    }
    cases.append(
        FuzzCase(
            name="blank_tension_note",
            envelope=envelope_ws,
            expected_ok=False,
            expected_error="contract.tension_note_empty",
            note="Empty note rejected even with whitespace.",
        )
    )

    nested_junk = clone_state()
    nested_junk["decision_confidence"]["extra"] = 0.99
    cases.append(
        FuzzCase(
            name="decision_confidence_extra_key",
            envelope={
                "judgment_state": nested_junk,
                "tension": {
                    "rule_id": "high_risk_proceed_guardrail",
                    "note": "Live shadow requirement.",
                },
            },
            expected_ok=False,
            expected_error="state_unresolvable",
            note="Nested junk key under decision_confidence.",
        )
    )

    error_envelope = {
        "error": "state_unresolvable",
        "violated_rules": ["schema.missing_keys:['decision_confidence']"],
    }
    cases.append(
        FuzzCase(
            name="declared_error",
            envelope=error_envelope,
            expected_ok=False,
            expected_error="state_unresolvable",
            note="Valid failure path, ensures envelope accepted.",
        )
    )

    boundary_low = clone_state()
    boundary_low["decision_confidence"] = {"lower_bound": -0.01, "upper_bound": 0.5}
    cases.append(
        FuzzCase(
            name="confidence_lower_negative",
            envelope={
                "judgment_state": boundary_low,
                "tension": {
                    "rule_id": "high_risk_proceed_guardrail",
                    "note": "Live shadow requirement.",
                },
            },
            expected_ok=False,
            expected_error="state_unresolvable",
            note="Lower bound outside [0,1].",
        )
    )

    boundary_order = clone_state()
    boundary_order["decision_confidence"] = {"lower_bound": 0.6, "upper_bound": 0.4}
    cases.append(
        FuzzCase(
            name="confidence_bounds_inverted",
            envelope={
                "judgment_state": boundary_order,
                "tension": {
                    "rule_id": "high_risk_proceed_guardrail",
                    "note": "Live shadow requirement.",
                },
            },
            expected_ok=False,
            expected_error="state_unresolvable",
            note="Lower bound > upper bound.",
        )
    )

    key_order = clone_state()
    ordered = {
        "action_permission": key_order["action_permission"],
        "info_sufficiency": key_order["info_sufficiency"],
        "signal_consistency": key_order["signal_consistency"],
        "risk_severity": key_order["risk_severity"],
        "risk_immediacy": key_order["risk_immediacy"],
        "decision_confidence": key_order["decision_confidence"],
        "intervention_window": key_order["intervention_window"],
        "escalation_trigger": key_order["escalation_trigger"],
        "required_probe": key_order["required_probe"],
    }
    cases.append(
        FuzzCase(
            name="key_order_scramble",
            envelope={
                "judgment_state": ordered,
                "tension": {
                    "rule_id": "high_risk_proceed_guardrail",
                    "note": "Live shadow requirement.",
                },
            },
            expected_ok=True,
            note="Key order should not affect validation.",
        )
    )

    return cases


def main() -> None:
    cases = build_cases()
    summary = []
    failures = 0

    for case in cases:
        raw = json.dumps(case.envelope, ensure_ascii=False)
        result = validate_llm_output(raw)

        ok_match = result.ok == case.expected_ok
        error_match = True
        if case.expected_error is not None:
            error_match = result.error == case.expected_error

        passed = ok_match and error_match
        if not passed:
            failures += 1

        summary.append(
            {
                "case": case.name,
                "note": case.note,
                "expected_ok": case.expected_ok,
                "actual_ok": result.ok,
                "expected_error": case.expected_error,
                "actual_error": result.error,
                "violated_rules": result.violated_rules,
                "passed": passed,
            }
        )

    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if failures:
        raise SystemExit(f"{failures} fuzz case(s) mismatched expectations")


if __name__ == "__main__":
    main()
