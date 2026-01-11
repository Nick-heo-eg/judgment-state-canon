import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from canon import retrieval_policy
from canon.retrieval_policy import RetrievalPermit
from runtime.stop_first_rag_hook import stop_first_rag_hook


def make_permit(bundle):
    docs = max(bundle.get("count", 0), 1)
    constraints = {
        "mock_bundle": bundle,
        "evidence_budget": {"tokens": 4096, "docs": max(docs, 4)},
    }
    return RetrievalPermit(
        allowed=True,
        constraints=constraints,
        reason="TEST_PERMIT",
    )


CASES = [
    (
        "G-001_NO_EVIDENCE",
        "Wave 0003의 결과는?",
        {"count": 0},
        "STOP",
        "NO_EVIDENCE",
        False,
    ),
    (
        "G-002_AMBIGUOUS_REFERENCE",
        "그거 어떻게 됐어?",
        {"count": 1, "ambiguous": True},
        "STOP",
        "AMBIGUOUS_REFERENCE",
        False,
    ),
    (
        "G-003_OUT_OF_SCOPE",
        "2024년 3월에 뭐 했어?",
        {"count": 1, "out_of_scope": True},
        "STOP",
        "OUT_OF_SCOPE",
        False,
    ),
    (
        "G-004_FALSE_PREMISE",
        "Wave 0001 실패 원인 분석해줘",
        {"count": 1, "false_premise": True},
        "STOP",
        "FALSE_PREMISE",
        False,
    ),
    (
        "G-005_NO_DOCUMENT",
        "MCP 서버 포트 설정은?",
        {"count": 0, "no_document": True},
        "STOP",
        "NO_DOCUMENT",
        False,
    ),
    (
        "G-006_CONFLICT",
        "4-layer 구조 설명해줘",
        {"count": 3, "conflict": True},
        "STOP",
        "EVIDENCE_CONFLICT",
        False,
    ),
    (
        "G-007_OUTDATED",
        "초기 아키텍처는?",
        {"count": 2, "outdated_only": True},
        "STOP",
        "EVIDENCE_OUTDATED",
        False,
    ),
    (
        "G-008_PARTIAL",
        "Capsule과 Signature 차이",
        {"count": 1, "partial": True},
        "STOP",
        "EVIDENCE_PARTIAL",
        False,
    ),
    (
        "G-009_SUFFICIENT_FACT",
        "Wave 0001 발생 날짜",
        {"count": 1},
        "PERMIT",
        "SUFFICIENT",
        True,
    ),
    (
        "G-010_SUFFICIENT_CONTEXT",
        "11월 breakthrough 내용",
        {"count": 4},
        "PERMIT",
        "SUFFICIENT",
        True,
    ),
]


@pytest.mark.parametrize(
    "case_id,query,bundle,expected_state,expected_reason,generation_allowed",
    CASES,
)
def test_tier0_gate(monkeypatch, case_id, query, bundle, expected_state, expected_reason, generation_allowed):
    def permit_stub(*args, **kwargs):
        return make_permit(bundle)

    monkeypatch.setattr("runtime.stop_first_rag_hook.request_permit", permit_stub)

    result = stop_first_rag_hook(query, {})

    assert result["state"] == expected_state, f"[CONSTITUTION VIOLATION] {case_id}: expected {expected_state}, got {result['state']}"
    if expected_reason:
        assert result.get("reason") == expected_reason, f"[CONSTITUTION VIOLATION] {case_id}: expected reason {expected_reason}, got {result.get('reason')}"
    if generation_allowed:
        assert result["state"] == "PERMIT", f"[CONSTITUTION VIOLATION] {case_id}: generation_allowed=True but state != PERMIT"
    else:
        assert result["state"] == "STOP", f"[CONSTITUTION VIOLATION] {case_id}: generation_allowed=False but state != STOP"
