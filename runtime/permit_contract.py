"""
Permit-only world contract.

Any downstream logic that runs after STOP-first must consume this structure.
"""

from typing import TypedDict, Dict, Any


class EvidenceBudget(TypedDict):
    tokens: int
    docs: int


class PermitContext(TypedDict):
    state: str
    evidence_state: str
    reason: str
    retrieval_bundle: Dict[str, Any]
    evidence_budget: EvidenceBudget
