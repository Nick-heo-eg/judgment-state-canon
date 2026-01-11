# Immutable Boundaries

These boundaries define what the Canon will never permit. They are non-negotiable and configuration-proof.

## LLM Placement
- LLMs remain outside the Canon and Runtime; they are state proposers only.
- They will never receive decision, output, or explanation authority.
- This boundary is not configurable.

## Language Role
- Language layers may only render validated states using `language_mapping.yaml`.
- Language never changes judgment content, introduces explanations, or softens outcomes.
- This boundary is not configurable.

## Validator Primacy
- Validator verdicts are final. If validation fails, no layer may emit language, fallback strings, or substitute outputs.
- There are no exceptions, retries, or best-effort answers.
- This boundary is not configurable.

## Silence as Normalcy
- Silence (no UI/UX output) is a valid and intended state for validation failures.
- Product, UX, or PM requests cannot redefine silence as an error condition.
- This boundary is not configurable.
