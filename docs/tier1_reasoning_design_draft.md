# Tier-1 Reasoning Design Draft (Permit-Only World)

- Tier-1 executes **only** with a valid `PermitContext` (state=`PERMIT`, evidence_state=`SUFFICIENT`, evidence budget attached).
- Tier-1 is prohibited from “recovering” a STOP. If STOP occurred upstream, Tier-1 must not run.
- Generation remains optional; it is a privilege exercised under the issued evidence budget.

This draft reserves the structure for future design discussions. No Tier-1 code may be committed until the Canon explicitly authorizes it.
