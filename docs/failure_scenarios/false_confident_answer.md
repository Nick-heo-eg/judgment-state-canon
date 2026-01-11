# Failure Scenario: False Confident Answer (Prevented)

## Scenario
- Query: “Wave 0001 실패 원인 분석해줘”
- Reality: Wave 0001 never failed.
- Naive RAG behavior: retrieve loosely related documents, hallucinate a failure narrative, and present it confidently.

## STOP-first Behavior
1. Question reaches STOP-first hook.
2. Retrieval bundle marks `false_premise=True`.
3. Tier-0 rule **G-004_FALSE_PREMISE** fires:
   - Action: STOP
   - Reason: `FALSE_PREMISE`
   - Generation allowed: False
4. Runtime surfaces only the STOP reason; no answer is generated or rendered.

## Result
- There is no confident-but-wrong answer.
- Logs show the canonical reason `FALSE_PREMISE`.
- Users see a normal STOP message, not an “error.”
