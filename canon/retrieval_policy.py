"""
Retrieval permit policy.

Minimal heuristics to decide whether retrieval should run. This version is intentionally conservative.
"""

from dataclasses import dataclass
from typing import Dict, Optional
import re


AMBIGUOUS_TOKENS = {"그거", "그것", "이거", "저거", "그녀", "그놈"}
DISALLOWED_YEARS = {"2024", "2025", "2026", "2027", "2028", "2029"}
DEFAULT_EVIDENCE_BUDGET = {"tokens": 4096, "docs": 4}
DEFAULT_CONSTRAINTS = {
    "top_k": 4,
    "max_latency_ms": 800,
    "token_budget": 2048,
    "evidence_budget": DEFAULT_EVIDENCE_BUDGET,
}


@dataclass
class RetrievalPermit:
    allowed: bool
    constraints: Dict[str, object]
    reason: str


def _is_ambiguous(question: str) -> bool:
    if len(question.strip()) < 4:
        return True
    return any(token in question for token in AMBIGUOUS_TOKENS)


def _is_out_of_scope(question: str) -> bool:
    for year in DISALLOWED_YEARS:
        if year in question:
            return True
    return False


def request_permit(question: str, context: Optional[Dict[str, object]] = None) -> RetrievalPermit:
    context = context or {}

    if _is_ambiguous(question):
        return RetrievalPermit(False, {}, "Retrieval denied: ambiguous reference.")

    if _is_out_of_scope(question):
        return RetrievalPermit(False, {}, "Retrieval denied: question outside supported timeline.")

    return RetrievalPermit(
        allowed=True,
        constraints=DEFAULT_CONSTRAINTS.copy(),
        reason="Retrieval permitted by policy.",
    )
