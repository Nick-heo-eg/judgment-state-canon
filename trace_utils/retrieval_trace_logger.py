"""
Trace logging for STOP-first RAG.

STOP decisions record only permit reason, rule ID, and evidence state.
No retrieval metadata is stored when generation is blocked.
"""

from typing import Any, Dict


def log_trace(question: str, retrieval_bundle: Dict[str, Any], decision: Any) -> None:
    if decision.generation_allowed:
        payload = {
            "question": question,
            "retrieval_count": retrieval_bundle.get("count", 0),
            "decision": {
                "action": decision.action,
                "reason": decision.reason,
                "evidence_state": decision.evidence_state,
                "generation_allowed": decision.generation_allowed,
            },
        }
    else:
        payload = {
            "decision": {
                "action": decision.action,
                "reason": decision.reason,
                "evidence_state": decision.evidence_state,
                "generation_allowed": decision.generation_allowed,
            },
        }
    print("[STOP-FIRST-RAG]", payload)
