# Judgment-State Adversarial Fuzzer

- Purpose: simulate common LLM failure modes (enum typos, missing keys, tension misuse, sparse-proceed, extra keys, self-declared errors) without requiring model access.
- Command: `python3 judgment-state-prototype/fuzzer.py`
- Expected result: JSON summary per case plus zero exit status. Any mismatch between expected/actual validator verdicts raises `SystemExit` and fails CI.
- Usage contexts:
  1. Local regression before editing schema, invariants, or contract.
  2. Continuous integration (`.github/workflows/canon.yml`) to guarantee Canon changes do not reopen historical attack vectors.
  3. Generating additional target cases—extend `build_cases()` with new envelopes whenever a novel model failure is observed.

The fuzzer reuses `validator.validate_llm_output`, so validator changes automatically propagate to adversarial checks.
