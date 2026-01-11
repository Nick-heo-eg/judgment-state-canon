# LLM and Language Positioning

## LLM: State Proposer (Pre-Canon, Pre-Runtime)
- LLMs do not belong to the Canon (law) or Runtime (enforcement).
- Role: propose `JudgmentState` candidates given inputs.
- Limitations: no decision authority, no guarantee of truth, proposals may be incomplete or invalid.
- Every proposal must face the validator before it can exist; LLMs wait outside the Canon/Runtime boundary.

```
input → LLM (state proposal) → validator/runtime → exists or deleted
```

## Why LLMs Are Demoted
- Canon demands accountable judgment; LLM outputs are probabilistic and unverifiable.
- They cannot answer “why this judgment may exist” or “who approved it.”
- Therefore they are constrained to the role of proposer; existence depends entirely on Canon + Runtime.

## Language: Post-Validation Rendering
- Language is not part of judgment construction.
- Once Runtime accepts a state, language renderers (per `language_mapping.yaml`) surface it.
- Language never mutates semantics, never explains, never softens; failure means no language is produced.

## Combined Ordering
```
Canon (what may exist)
   ↓
Runtime (enforce: pass/delete)
   ↓
Language (render validated states only)

LLM (state proposer) sits before Canon/Runtime, not above them.
```

## Takeaway
- LLMs propose, Canon + Runtime decide, Language merely shows.
- If validation fails, nothing is displayed: **Failing validation equals non-existence.**
