# Canonical Judgment System

Failing validation equals non-existence.

**Recommended first read:** [Law-First Public Post](law_first_public_post.md)

**For maintainers/contributors:**
- [Constitution Change Protocol](CONSTITUTION_CHANGE_PROTOCOL.md) - Tier-0 amendment procedure
- [Agent Authority Boundaries](AGENT_AUTHORITY_BOUNDARIES.md) - What automated agents can/cannot do
- [Constitutional Change Log](docs/constitutional_change_log.md) - Amendment history

## System Map

```
Canon → Runtime → (silence | human handoff)
         ↑
    Validator (enforcement)
         ↑
    LLM (proposer only)
         ↓
    Language (post-validation rendering)
```

- **Canon**: Immutable rules, schemas, invariants
- **Runtime**: Validation, execution, evidence collection
- **LLM**: State proposer (never judge)
- **Language**: Rendering only (post-validation)
- **Human**: Authority at handoff only

---

## Canon Definition

### Core Artifacts
- [Judgment State Schema](judgment_state_schema.yaml) - Machine-readable judgment states
- [Judgment State Invariants](judgment_state_invariants.md) - Lint rules (high-risk proceed guardrail, handoff escalation)
- [Immutable Boundaries](immutable_boundaries.md) - Non-configurable clauses

### Domain Anchors
- [Question (Autonomous Vehicle)](question.md) - High-stakes AV scenario
- [Question (Medical)](question_medical.md) - High-stakes medical scenario
- [AV Judgment Instances](judgment_state_instances.yaml) - 5 cases with tension metadata
- [Medical Judgment Instances](judgment_state_instances_medical.yaml) - 4 cases with tension metadata

### Language & Rendering
- [Language Mapping](language_mapping.yaml) - English anchor, deterministic KO/JA/ZH rendering
- [Language Characteristics](language_characteristics.md) - Tone policy per language, no semantic mutation
- [Silence UX Guidelines](silence_ux_guidelines.md) - Validation fail = no UI; silence is normal

---

## Runtime Enforcement

### Validation & Execution (Constitutional Tier-0)
- [Validator](validator.py) - Schema + invariant validation, envelope enforcement
- [Runtime Wiring](runtime_wiring.md) - Pipeline: validation → (silence | handoff | render)
- [STOP-first RAG Hook](runtime/stop_first_rag_hook.py) - Permit/evidence enforcement before Canon runtime
- [Retrieval Policy](canon/retrieval_policy.py) / [Engine](retrieval/engine.py) / [Evidence Judge](retrieval/evidence_judge.py) / [Trace Logger](trace_utils/retrieval_trace_logger.py) / [STOP Messages](runtime/stop_messages.py) - Modules backing the STOP-first hook
- [Mock LLM Runner](mock_llm_runner.py) - Replays samples, demonstrates pass/discard behavior

#### STOP-first RAG Rules
- Tier-0 is a constitutional gate, not a tunable configuration. Changing the rules requires Canon review.
- No generation occurs before `retrieval/evidence_judge.py` declares `generation_allowed=True`.
- Retrieval context never flows downstream when `generation_allowed=False`.
- `CONFLICT`, `OUTDATED`, `PARTIAL`, `NO_DOCUMENT`, `FALSE_PREMISE`, `NO_EVIDENCE`, `AMBIGUOUS_REFERENCE`, `OUT_OF_SCOPE` are normal STOP states with fixed reason codes.
- Tier 0 gate tests fail-fast (1 failure = system failure) and are enforced in CI.
- STOP trace logs capture only permit reason and rule ID; no documents/chunks are recorded when generation is blocked. STOP is a refusal, not a model error.

## STOP-first RAG is not general RAG
- It does not try to improve answers; it decides whether answering is allowed.
- Retrieval is a permissioned probe, not a context supplier.
- All mentions of “RAG” in this repo refer to STOP-first / judgment-gated retrieval only.
- All future retrieval runs under an explicit evidence budget controlled by Canon; no module may exceed the budget attached to its permit.

### Testing & Evidence
- [Fuzzer](fuzzer.py) - Deterministic adversarial test suite (enum typos, missing keys, tension misuse, confidence edges)
- [Demo Showcase](demo_showcase.sh) - Chained demo: validator OK, fuzzer run, mock runner
- [CI Workflow](.github/workflows/canon.yml) - Runs OK/breach/error samples, fuzzer, demo
- [Tier 0 Gate Tests](tests/tier0_gate/test_judgment_gate.py) - STOP-first RAG unit tests

### Compliance Reporting
- [Compliance Report Template](compliance_report_template.md) - Log format specification
- [Compliance Metrics](compute_compliance_metrics.py) - Aggregates breach rates, tension omission
- [Sample Logs](compliance_sample_logs.jsonl) - Example log entries

---

## Architectural Position

### LLM & Language
- [LLM and Language Position](llm_and_language_position.md) - LLM outside Canon/Runtime; language render-only
- [Human Responsibility](human_responsibility.md) - Humans assume authority only at handoff

### Canon-Runtime Boundary
- [Canon/Runtime Overview](canon_runtime_overview.md) - Separation of law vs execution
- [Permit-Only Contract](docs/permit_only_contract.md) - API contract for Tier-1 world (requires PermitContext + evidence budget)
- [Tier-1 Design Draft](docs/tier1_reasoning_design_draft.md) - Placeholder; Tier-1 cannot run without explicit Canon approval

---

## Philosophy & Briefs

### Core Rationale
- [Why Silence (One-Pager)](why_silence_onepager.md) - Justification for silence as normal state
- [One-Pager](one_pager.md) - System overview for external audiences

### Public Briefs
- [Law-First Public Post](law_first_public_post.md) - Procedural brief for legal audiences
- [Law Track Brief](release_brief_law.md) - Law track framing
- [Architecture Track Brief](release_brief_ai_architecture.md) - Architecture track framing

### Deployment
- [Deployment Priorities](deployment_priorities.md) - Law → Healthcare → Enterprise → Defense

---

## Evidence Paths

- CI: `.github/workflows/canon.yml`
- Validator: `validator.py`
- Fuzzer: `fuzzer.py`
- Demo: `demo_showcase.sh`
- Compliance: `compute_compliance_metrics.py`
- Samples: `samples/` directory
- Failure scenario: `docs/failure_scenarios/false_confident_answer.md`
- System failure log schema: `trace/system_failure_event.json`

---

## Structure

This repository contains enforcement artifacts, not aspirations.

> If Echo answers when it should have stopped, that is a system failure — not a model error.

---

Future work, if any, will occur outside this Canon.
This repository defines boundaries, not evolution.
