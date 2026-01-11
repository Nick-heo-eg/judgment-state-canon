# Memory Governance Canon (FROZEN)

This document defines the legal status of memory artifacts. It is a constitutional statute and must not be altered without Canon amendment.

## 1. Legal Statuses

### 1.1 Citizen Memory
- Definition: records that have completed promotion and are recognized as authoritative history.
- Rights:
  - May be referenced in judgments and audits.
  - Immutable except via explicit invalidation ritual.
- Prohibitions:
  - No automated modification, pruning, or relocation.
  - No model-driven reinterpretation.

### 1.2 Evidence Candidate
- Definition: artifacts awaiting promotion (logs, traces, experimental notes).
- Rights:
  - May be inspected manually to justify promotion or invalidation.
  - Must remain read-only for automated systems.
- Prohibitions:
  - Cannot influence judgments until promoted.
  - No automatic promotion/escalation.

### 1.3 Residue / Invalidated State
- Definition: artifacts explicitly declared non-authoritative.
- Rights:
  - Retained for historical transparency.
  - Accessible for manual review only.
- Prohibitions:
  - Must never re-enter promotion pipeline.
  - Cannot be deleted except by separate archival policy (manual, intentional).

## 2. Promotion Ritual
- Triggered only by a human authority.
- Automation, schedulers, or triggers are forbidden.
- Declaration must include:
  1. Timestamp
  2. Declarant identity
  3. Artifact identifier
  4. Action (`promote` / `invalidate`)
  5. One-sentence justification
- Declaration produces a record in the compliance template (see section 4).

## 3. Invalidation Ritual
- Converts Citizen Memory or Evidence Candidate into Residue.
- Does not delete the artifact; it revokes authority.
- Requires human declaration with the same fields as promotion.
- Original files remain intact; only their status changes.

## 4. Non-Automation Clauses
- Garbage collection, lifecycle management, auto-pruning, or auto-promotion are prohibited.
- “Not implemented” is insufficient; these behaviors are banned unless the Canon is amended.
- Any tooling that alters memory status must require human confirmation and log the declaration.
