"""
Evidence judge: determines whether retrieval results allow generation.

Implements Tier 0 STOP-first rules.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List

from .evidence_judge_rules import TIER_0_RULES


class EvidenceState(str, Enum):
    SUFFICIENT = "SUFFICIENT"
    PARTIAL = "PARTIAL"
    CONFLICT = "CONFLICT"
    OUTDATED = "OUTDATED"
    NONE = "NONE"


class GateAction(str, Enum):
    STOP = "STOP"
    PERMIT = "PERMIT"


@dataclass
class GateDecision:
    action: GateAction
    reason: str
    evidence_state: EvidenceState
    generation_allowed: bool


def _check_condition(bundle: Dict[str, Any], condition: Dict[str, Any]) -> bool:
    field = condition.get("field")
    op = condition.get("op")
    value = condition.get("value")
    field_value = bundle.get(field)

    if op == "eq":
        return field_value == value
    if op == "bool_true":
        return bool(field_value)
    return False


def _evaluate_rules(bundle: Dict[str, Any]) -> Dict[str, Any]:
    for rule in TIER_0_RULES:
        conditions: List[Dict[str, Any]] = rule.get("conditions", [])
        if all(_check_condition(bundle, cond) for cond in conditions):
            return rule
    return TIER_0_RULES[-1]


def judge(question: str, retrieval_bundle: Dict[str, Any]) -> GateDecision:
    rule = _evaluate_rules(retrieval_bundle or {})
    action = GateAction(rule["action"])
    state = EvidenceState(rule["evidence_state"])
    return GateDecision(
        action=action,
        reason=rule["reason"],
        evidence_state=state,
        generation_allowed=bool(rule["generation_allowed"]),
    )
