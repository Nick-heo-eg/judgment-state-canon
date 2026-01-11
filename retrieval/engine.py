"""
Retrieval engine stub.

In production this would query vector stores / indices. For Tier 0 tests we
allow injecting mock bundles via constraints.
"""

from typing import Dict, Any


def retrieve(question: str, constraints: Dict[str, Any]) -> Dict[str, Any]:
    """
    Returns a retrieval bundle containing at least:
      - count: number of matching chunks
      - documents: optional list of source snippets
      - flags (booleans): conflict, ambiguous, outdated_only, etc.

    Tests may pass `mock_bundle` inside constraints to bypass real retrieval.
    """
    if "mock_bundle" in constraints:
        return constraints["mock_bundle"]

    # Default empty response
    return {"count": 0, "documents": []}
