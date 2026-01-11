# Runtime Wiring Notes

## Execution Flow
1. Construct prompt using `prompt_scaffold.md`.
2. Invoke LLM and capture raw text.
3. Pass raw text directly into `validator.py`.
4. If `validator` returns `ok: true`, forward `judgment_state` to the Korean handoff mapping.
5. If `ok: false`, discard the LLM output, log `{error, violated_rules}`, emit the canonical handoff sentence (e.g., `action_permission=handoff` string) to the human.

## Pseudocode
```python
raw = llm.invoke(prompt)
result = run_validator(raw)

if not result.ok:
    log_violation(error=result.error, violated=result.violated_rules, raw=raw)
    return handoff_sentence("llm_contract_breach")

state = extract_state(raw)
return handoff_sentence(map_state_to_sentence(state))
```

## Non-Negotiables
- `result.ok == False` means the LLM output never existed for downstream consumers.
- Logs store the breach reason, but no partial content reaches users.
- Validator is the only authority that decides state admissibility; do not duplicate logic elsewhere.
- Language rendering occurs strictly after validation. Anchor language (English) is authoritative; all other languages are deterministic renderings with identical semantics using `language_mapping.yaml`.
