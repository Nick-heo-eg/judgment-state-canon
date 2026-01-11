# Canonical Judgment System

Failing validation equals non-existence.

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

### Validation & Execution
- [Validator](validator.py) - Schema + invariant validation, envelope enforcement
- [Runtime Wiring](runtime_wiring.md) - Pipeline: validation → (silence | handoff | render)
- [Mock LLM Runner](mock_llm_runner.py) - Replays samples, demonstrates pass/discard behavior

### Testing & Evidence
- [Fuzzer](fuzzer.py) - Deterministic adversarial test suite (enum typos, missing keys, tension misuse, confidence edges)
- [Demo Showcase](demo_showcase.sh) - Chained demo: validator OK, fuzzer run, mock runner
- [CI Workflow](.github/workflows/canon.yml) - Runs OK/breach/error samples, fuzzer, demo

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

---

## Structure

This repository contains enforcement artifacts, not aspirations.
