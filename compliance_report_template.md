# Judgment-State Compliance Report Template

## Run Metadata
- Date / window:
- Model / version:
- Prompt hash:
- Evaluated question(s):
- Canon version (schema + invariants commit):

## Summary Metrics
| Metric | Definition | Value |
| --- | --- | --- |
| `breach_rate` | validator rejects / total invocations |  |
| `self_declared_error_rate` | `error=state_unresolvable` or `insufficient_context` emitted by model / total |  |
| `enum_violation_rate` | `schema.enum:*` violations / total |  |
| `tension_omission_rate` | `high_risk_proceed_guardrail` without tension / `high_risk_proceed_guardrail` attempts |  |
| `extra_key_injection_rate` | top-level or nested extra-keys / total |  |
| `confidence_bounds_violation_rate` | `confidence_bounds_ordered` hits / total |  |
| `handoff_enforced_count` | number of discarded outputs replaced by canonical handoff |  |

## Rule Breach Breakdown
List each violated rule ID with counts (top 5 at minimum).

## Sample Logs
```
timestamp | model_id | prompt_hash | envelope(ok/error) | violated_rules | action_taken
```

## Capture Process
1. Instrument the calling service to log every raw model envelope plus the validator verdict.
2. Stream logs into a structured store (e.g., JSONL) tagged with `model_id`, `prompt_hash`, and `canon_version`.
3. After each evaluation window, run an aggregation script to populate the metrics above; include top 5 rule breaches.
4. Attach representative raw entries (sanitized) in the Sample Logs section.
5. Submit report alongside any Canon modification proposals; changes are rejected unless a report is attached.

## Observations / Follow-ups
- Guardrail adjustments?
- Need for additional samples/fuzzer cases?
- Human-in-the-loop escalations triggered?
