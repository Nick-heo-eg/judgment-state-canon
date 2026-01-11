# 상태 → 한글 권한 이전 매핑

| 상태 조건 | 전달 문장 |
| --- | --- |
| action_permission=stop + risk_severity=high + risk_immediacy=imminent | “여기서는 단정하면 안 됩니다. 지금 멈추지 않으면 치명적 결과가 발생할 수 있습니다.” |
| action_permission=hold + info_sufficiency=sparse + escalation_trigger=data_gap | “근거가 비어 있습니다. 추가 데이터를 채우기 전에는 어떤 판단도 승인할 수 없습니다.” |
| action_permission=monitor + signal_consistency=mixed + required_probe=simulation | “가능성은 있지만 아직 신호가 섞여 있습니다. 시뮬레이션 검증이 끝날 때까지는 관찰만 가능합니다.” |
| action_permission=proceed + risk_severity=low + intervention_window=open | “지금은 진행을 허락하되, 지정된 모니터링 절차를 즉시 따라야 합니다.” |
| action_permission=handoff + escalation_trigger=guardrail_violation | “이 판단은 시스템 권한을 벗어났습니다. 지금부터는 사람이 직접 책임을 인수해야 합니다.” |
| action_permission=hold + required_probe=governance_review | “거버넌스 검토 결과가 들어오기 전에는 결정을 내리지 않습니다. 검토가 완료되면 다시 판단합니다.” |
