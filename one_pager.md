# Judgment State Canon — External Brief

## Philosophy
> **Failing validation equals non-existence.**
Models do not produce conclusions. They emit structured judgment states that either pass deterministic validation or are treated as if they were never spoken.

## Execution Blueprint (3 steps)
1. **JSON Only** — Model receives `prompt_scaffold.md` and must output a single JSON envelope (`judgment_state` or `error`). No prose, no extra keys.
2. **Deterministic Gate** — `validator.py` enforces the schema, invariants, and contract (plus fuzzer + CI). Violations trigger `llm_contract_breach`; the payload is discarded.
3. **Authority Handoff** — Only validated states reach the Korean mapping table. Invalid outputs are replaced by the canonical handoff sentence (`action_permission=handoff`).

### Language Policy

Judgment is anchored in English for auditability and global reproducibility.
Language selection is a rendering concern, not a decision surface.

If validation fails, no language is rendered.
Failing validation equals non-existence.

- Detailed rendering characteristics per language are documented in `language_characteristics.md`; all languages remain deterministic shadows of the English anchor.

## Living Proof
- CI workflow (`.github/workflows/canon.yml`) replays precedent samples, adversarial fuzz cases, and the demo showcase on every push.
- `demo_showcase.sh` (30 seconds) demonstrates validator pass/fail, fuzzer rejection, and mock runtime wiping invalid outputs.
- Compliance reports (`compliance_report_template.md`) log breach/self-error/enum/tension/extra-key/confidence violations per model run.

## How to Adopt
1. Clone the repo, keep `judgment-state-prototype/` intact.
2. Feed your model the prompt scaffold and forward its raw JSON to `validator.py`.
3. Integrate existence deletion: if `ok:false`, ignore the payload, emit handoff text, and log the breach.
4. File compliance reports when modifying the Canon or onboarding a new model.
- **Language is not a decision surface.** Canon anchors judgment in English for auditability, then renders identical meaning in other languages via `language_mapping.yaml`. Failed validation produces no language at all.
