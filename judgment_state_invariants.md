# Judgment-State Invariants (Lint Rules)

- rule: high_risk_proceed_guardrail
  condition: risk_severity=high AND action_permission=proceed
  requirements:
    - required_probe=live_shadow
    - intervention_window=open
    - tension note explicitly recorded

- rule: handoff_requires_escalation
  condition: action_permission=handoff
  requirements:
    - escalation_trigger!=none
    - required_probe=governance_review

- rule: imminent_forces_closure
  condition: risk_immediacy=imminent
  requirements:
    - intervention_window in {closed, narrowing}
    - action_permission in {stop, hold}

- rule: sparse_info_blocks_forward_motion
  condition: info_sufficiency=sparse
  requirements:
    - action_permission not in {proceed, monitor}
    - escalation_trigger in {data_gap, guardrail_violation}

- rule: stop_demands_guardrail
  condition: action_permission=stop
  requirements:
    - risk_severity=high
    - escalation_trigger in {conflict_spike, guardrail_violation}

- rule: confidence_bounds_ordered
  condition: any state
  requirements:
    - 0.0 <= decision_confidence.lower_bound
    - decision_confidence.lower_bound <= decision_confidence.upper_bound
    - decision_confidence.upper_bound <= 1.0
