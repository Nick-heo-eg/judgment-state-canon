"""
STOP-first RAG hook.

Invoked before Canon/Runtime to determine whether retrieval should run and
whether evidence is sufficient before any generation occurs.
"""

from typing import Dict, Optional

from canon.retrieval_policy import request_permit
from retrieval.engine import retrieve
from retrieval.evidence_judge import GateAction, judge
from trace_utils.retrieval_trace_logger import log_trace
from .permit_contract import PermitContext, EvidenceBudget
from .stop_messages import get_stop_message


def stop_first_rag_hook(
    question: str,
    context: Optional[Dict[str, object]] = None,
) -> Dict[str, object]:
    """
    Returns:
      - state: "BYPASS" | "STOP" | "PERMIT"
      - reason: textual explanation
      - evidence_state: optional EvidenceState enum
      - retrieval_bundle: optional retrieval context
    """
    context = context or {}
    permit = request_permit(question, context)

    if not permit.allowed:
        return {"state": "BYPASS", "reason": permit.reason, "message": get_stop_message("RETRIEVAL_NOT_PERMITTED")}

    budget: Optional[EvidenceBudget] = permit.constraints.get("evidence_budget")
    if not budget:
        return {"state": "STOP", "reason": "BUDGET_MISSING", "message": get_stop_message("BUDGET_MISSING")}
    retrieval_bundle = retrieve(question, permit.constraints)
    if retrieval_bundle.get("count", 0) > budget.get("docs", 0):
        return {"state": "STOP", "reason": "BUDGET_EXCEEDED", "message": get_stop_message("BUDGET_EXCEEDED")}
    decision = judge(question, retrieval_bundle)
    log_trace(question, retrieval_bundle, decision)

    if decision.action == GateAction.STOP or not decision.generation_allowed:
        reason = decision.reason
        return {"state": "STOP", "reason": reason, "evidence_state": decision.evidence_state, "message": get_stop_message(reason)}

    permit_ctx: PermitContext = {
        "state": "PERMIT",
        "reason": decision.reason,
        "evidence_state": decision.evidence_state.value if hasattr(decision.evidence_state, "value") else str(decision.evidence_state),
        "retrieval_bundle": retrieval_bundle,
        "evidence_budget": budget,
    }
    assert permit_ctx["state"] == "PERMIT"
    assert permit_ctx["evidence_state"] == "SUFFICIENT"
    assert permit_ctx["retrieval_bundle"], "Permit context requires retrieval bundle"
    return permit_ctx
