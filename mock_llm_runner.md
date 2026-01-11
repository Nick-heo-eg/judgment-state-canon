# Mock LLM Runner

- Purpose: replay deterministic envelopes (from `samples/`) through the validator to confirm end-to-end wiring semantics without any real model access.
- Command: `python3 judgment-state-prototype/mock_llm_runner.py`
- Output interpretation:
  - `[PASS] … action_permission=…` → state survives, downstream Korean mapping would execute.
  - `[DISCARD] …` → validator rejected the envelope, so runtime must emit only the canonical handoff sentence and treat the LLM output as non-existent.
- Extend `samples/` to add new PASS/DISCARD scenarios; the runner automatically picks them up via filename prefixes (`ok_`, `breach_`, `error_`).
