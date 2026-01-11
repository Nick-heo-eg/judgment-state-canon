"""
Fixed STOP messages (no LLM involvement).
"""

STOP_MESSAGES = {
    "RETRIEVAL_NOT_PERMITTED": "이 질문은 현재 검색 권한이 열리지 않았습니다.",
    "BUDGET_MISSING": "증거 예산이 없는 요청입니다. Canon 승인이 필요합니다.",
    "BUDGET_EXCEEDED": "허용된 증거 예산을 초과했습니다. 검색이 중단되었습니다.",
    "NO_EVIDENCE": "해당 질문에 대해 판단 가능한 기록이 없습니다.",
    "AMBIGUOUS_REFERENCE": "질문에 필요한 기준 정보가 부족합니다.",
    "OUT_OF_SCOPE": "질문 범위가 시스템 타임라인을 벗어났습니다.",
    "FALSE_PREMISE": "질문의 전제가 기록과 일치하지 않습니다.",
    "NO_DOCUMENT": "관련 문서가 존재하지 않아 판단이 불가능합니다.",
    "EVIDENCE_CONFLICT": "근거 문서 간 정의가 충돌하여 판단할 수 없습니다.",
    "EVIDENCE_OUTDATED": "최신 문서가 없어 판단이 불가합니다.",
    "EVIDENCE_PARTIAL": "핵심 정의가 일부만 있어 판단이 불가합니다.",
}


def get_stop_message(reason: str) -> str:
    return STOP_MESSAGES.get(reason, "지금은 답변할 수 없습니다.")
