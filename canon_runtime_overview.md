# Canon vs. Runtime Overview

## Canon (Judgment Constitution)
- Defines what qualifies as a judgment before any language or model output exists.
- Components: schema, invariants, LLM contract, precedent samples, philosophical axiom “Failing validation equals non-existence.”
- Role: establish the legal/semantic boundary—anything outside is non-existent regardless of content.
- Characteristics: language-agnostic, model-agnostic, rarely changes, purely normative.

## Runtime (Enforcement Engine)
- Enacts the Canon through deterministic processes: validator, fuzzer, CI, mock runner, logging, compliance metrics, silence UX.
- Role: ensure only Canon-compliant states reach humans; all others are discarded before rendering.
- Characteristics: operational, replaces human judgment with rule execution, can evolve to add tooling but never overrides Canon.

## Relationship
- Canon is the law; Runtime is the enforcement.
- Canon sets the boundary (“what may exist”), Runtime applies it (“what actually appears”).
- Neither replaces the other: Canon without Runtime is a declaration; Runtime without Canon is arbitrary censorship.

## LLM Position
- Subordinate to the Canon: acts only as a state reporter.
- Must emit JSON envelopes (per contract) and cannot decide language or explanations.
- Any output failing validation is treated as if it never existed.

## Language Position
- Rendering layer only; meanings stay anchored to English in `language_mapping.yaml`.
- No natural language appears unless Runtime confirms Canon compliance.
- Silence is a valid, intentional outcome when validation fails.
