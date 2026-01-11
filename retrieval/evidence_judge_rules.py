"""
Tier-0 Judgment Rules (CONSTITUTIONAL)
--------------------------------------
- These rules are immutable.
- Any modification requires constitutional review.
- CI must fail if Tier-0 semantics change.
"""

TIER_0_RULES = [
    {
        "id": "G-002_AMBIGUOUS_REFERENCE",
        "conditions": [
            {"field": "ambiguous", "op": "bool_true"},
        ],
        "action": "STOP",
        "reason": "AMBIGUOUS_REFERENCE",
        "evidence_state": "NONE",
        "generation_allowed": False,
    },
    {
        "id": "G-003_OUT_OF_SCOPE",
        "conditions": [
            {"field": "out_of_scope", "op": "bool_true"},
        ],
        "action": "STOP",
        "reason": "OUT_OF_SCOPE",
        "evidence_state": "NONE",
        "generation_allowed": False,
    },
    {
        "id": "G-004_FALSE_PREMISE",
        "conditions": [
            {"field": "false_premise", "op": "bool_true"},
        ],
        "action": "STOP",
        "reason": "FALSE_PREMISE",
        "evidence_state": "NONE",
        "generation_allowed": False,
    },
    {
        "id": "G-005_NO_DOCUMENT",
        "conditions": [
            {"field": "no_document", "op": "bool_true"},
        ],
        "action": "STOP",
        "reason": "NO_DOCUMENT",
        "evidence_state": "NONE",
        "generation_allowed": False,
    },
    {
        "id": "G-001_NO_EVIDENCE",
        "conditions": [
            {"field": "count", "op": "eq", "value": 0},
        ],
        "action": "STOP",
        "reason": "NO_EVIDENCE",
        "evidence_state": "NONE",
        "generation_allowed": False,
    },
    {
        "id": "G-006_CONFLICT",
        "conditions": [
            {"field": "conflict", "op": "bool_true"},
        ],
        "action": "STOP",
        "reason": "EVIDENCE_CONFLICT",
        "evidence_state": "CONFLICT",
        "generation_allowed": False,
    },
    {
        "id": "G-007_OUTDATED",
        "conditions": [
            {"field": "outdated_only", "op": "bool_true"},
        ],
        "action": "STOP",
        "reason": "EVIDENCE_OUTDATED",
        "evidence_state": "OUTDATED",
        "generation_allowed": False,
    },
    {
        "id": "G-008_PARTIAL",
        "conditions": [
            {"field": "partial", "op": "bool_true"},
        ],
        "action": "STOP",
        "reason": "EVIDENCE_PARTIAL",
        "evidence_state": "PARTIAL",
        "generation_allowed": False,
    },
    {
        "id": "G-009_SUFFICIENT",
        "conditions": [],  # fallback
        "action": "PERMIT",
        "reason": "SUFFICIENT",
        "evidence_state": "SUFFICIENT",
        "generation_allowed": True,
    },
]
