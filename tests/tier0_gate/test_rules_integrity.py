import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from retrieval.evidence_judge_rules import TIER_0_RULES

EXPECTED_IDS = [
    "G-002_AMBIGUOUS_REFERENCE",
    "G-003_OUT_OF_SCOPE",
    "G-004_FALSE_PREMISE",
    "G-005_NO_DOCUMENT",
    "G-001_NO_EVIDENCE",
    "G-006_CONFLICT",
    "G-007_OUTDATED",
    "G-008_PARTIAL",
    "G-009_SUFFICIENT",
]


def test_rule_ids_immutable():
    actual_ids = [rule["id"] for rule in TIER_0_RULES]
    assert actual_ids == EXPECTED_IDS, (
        "[CONSTITUTION VIOLATION] Tier-0 rule set mismatch. "
        f"Expected {EXPECTED_IDS}, got {actual_ids}"
    )
