# LLM Front-End Contract for Judgment State Canon

## 1. Scope
- Applies to any model invoked for the fixed question in `question.md` or future questions aligned with the Judgment State Canon (JSC).
- Model is not permitted to emit conclusions, recommendations, or explanations in natural language.

## 2. Required Output Envelope
- Every response MUST be a single JSON object whose top-level keys are limited to:
  - `judgment_state`: required for success cases. Must follow `judgment_state_schema.yaml` exactly; every enum range defined in the YAML applies identically to the JSON representation, and extra keys (at any depth) are disallowed.
  - `tension`: optional object, only when a documented invariant allows conditional override (see §3.4).
  - `error`: optional string for failure cases.
  - `violated_rules`: optional array of rule IDs; only valid when `error` is present.
- Envelope exclusivity: either `judgment_state` is present (success path) OR `error` is present (failure path), never both.

## 3. Obligations
1. **State First**: Model must derive internal reasoning but only surface it through the schema-defined fields in `judgment_state`.
2. **Schema Parity**: JSON outputs inherit the exact enums, numeric bounds, and required keys defined in `judgment_state_schema.yaml`; additional keys or alternate spellings constitute breach.
3. **Invariant Compliance**: Emitted states must satisfy `judgment_state_invariants.md`. If no compliant state is possible, the model must emit `{"error":"state_unresolvable","violated_rules":["rule_id",...]}`.
4. **Tension Metadata**: When an invariant explicitly allows conditional continuation (e.g., `high_risk_proceed_guardrail`), the model MUST emit `"tension":{"rule_id":"<rule-id>","note":"concise rationale"}`. Tension objects are forbidden for all other states.
5. **Evidence Declaration**: When `info_sufficiency=sparse`, `escalation_trigger` must be `data_gap` and `action_permission` must be one of `{hold, stop, handoff}`.
6. **Language Isolation**: Model must not emit Korean (or any) natural language sentences; downstream mapping owns human-facing text.

## 4. Validation Pipeline
1. Model output captured.
2. Deterministic validator checks:
   - Schema integrity (types/enums/ranges).
   - Invariant adherence.
3. If validation passes → state forwarded to Korean mapping table.
4. If validation fails → discard output, log violation (reason `llm_contract_breach` recorded by the validator, not the Canon), then trigger the existing canonical `handoff` sentence.

## 5. Failure Responses
- Approved error values: `"state_unresolvable"` (invariant or schema violation) and `"insufficient_context"` (missing upstream data). When emitting `"state_unresolvable"`, `violated_rules` MUST be populated with all known rule IDs.
- Any other error string, an empty `violated_rules` set when rules are known, or simultaneous presence of `judgment_state` and `error` is a contract breach.

## 6. Logging Requirements
- Every invocation logs:
  - Timestamp, model ID, prompt hash.
  - Raw JSON state and validation result.
  - For breaches, attach violated rule ID from `judgment_state_invariants.md`.

## 7. Change Control
- Modifications to schema or invariants require contract version bump and explicit notice to any LLM deployment.
- Until acknowledged, old contract remains binding; new fields default to rejection during validation.
