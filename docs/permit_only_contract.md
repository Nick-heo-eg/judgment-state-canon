# Permit-Only Contract

## Scope
Tier-1 reasoning and any downstream modules may execute **only** when the STOP-first gate returns a `PermitContext`.

## Constraints
- Inputs must be the exact `PermitContext` structure (state=`"PERMIT"`, evidence_state=`"SUFFICIENT"`, non-empty `retrieval_bundle`, explicit `evidence_budget`).
- Raw questions or raw retrieval outputs cannot be accessed directly.
- Generation is a privilege exercised inside Permit-only world; it is never the default path.
- Canon will later attach an explicit **Evidence Budget** (top_k, latency, token, source filters). All retrieval must operate within the budget issued alongside the permit.

## Enforcement
- Any module accepting inputs outside the `PermitContext` is unconstitutional.
- Permit-only tests remain disabled in CI until Canon authorizes their execution.
