# Canon Runtime Brief (Architecture Track)

## Thesis
LLMs do not answer questions; they propose judgment states. Canon + Runtime decide existence. Outputs that fail validation are deleted before any language renders.

## Key Points for Technical Stakeholders
- **State Pipeline**: Input → LLM proposal → validator (schema+invariants) → pass/delete → language render.
- **LLM Demotion**: Models are state reporters only; no conclusions, explanations, or multi-language text.
- **Deterministic Enforcement**: `validator.py`, CI, fuzzers, and mock runners ensure every change re-proves “Failing validation equals non-existence.”
- **Silence UX**: Validation failure produces no UI. “If nothing is shown, the system has correctly refused to speak.”
- **Compliance Loop**: JSONL logs + `compute_compliance_metrics.py` track breach/self-error rates; reports gate Canon changes.

## Recommended Messaging
- Lead with the Canon axiom: “Failing validation equals non-existence.”
- Show the architectural diagram (Canon/Runtme/Language + LLM proposer).
- Highlight immutable boundaries (LLM placement, language role, validator primacy, silence).
- Demonstrate demo_showcase.sh to prove runtime attitude in 30 seconds.

## Sample Abstract
“We describe a Canon Runtime that forces LLM outputs through structured validation before any language can appear. The system treats validation failure as non-existence, deleting outputs silently. Immutable boundaries prevent LLMs from regaining decision authority, and compliance metrics document every breach. The result is an AI architecture that stops talking when judgment is invalid.”
