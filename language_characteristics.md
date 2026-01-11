# Language Rendering Characteristics (Canonical Appendix)

## Common Premises
- Judgment semantics exist only in the English anchor sentences.
- All other languages are deterministic renderings; they never generate new meaning.
- Sentences avoid emotion, mitigation, persuasion, or rhetorical tone.
- Length, tone, and honorifics follow language conventions but semantics stay 1:1.
- If validation fails, no language renders.

## English (Anchor Language)
- Role: semantic anchor for audit, reproducibility, legal review.
- Style: direct, condition-centric, explicit subjects, modal verbs for authority states.
- Principles: one sentence per judgment state, minimal interpretation, structurally simple to avoid translation loss.

## Korean (Authority Handoff Language)
- Role: transfer responsibility to humans in operational contexts.
- Style: formal register only, action-centric vocabulary (허용/불가/위임), no emotional cushioning.
- Principles: imply human responsibility, deliver decisions not explanations.

## Japanese (Procedural Compliance Language)
- Role: express procedural or governance status.
- Style: です/ます register, prefer 「〜できません」「〜必要があります」 structures, avoid emotive phrasing.
- Principles: read as procedural state, never as opinion.

## Chinese (Mandarin) (Directive Clarity Language)
- Role: deliver rapid go/stop directives.
- Style: concise declaratives, modal verbs (必须 / 不能 / 需要), minimal softeners.
- Principles: emphasize clear permission/ban signals, avoid multiple conditions per sentence.

## Language Policy Summary
- Default/fallback: English.
- Locale present: render in that language.
- Locale missing: fall back to English.
- Validation failure: render nothing.

> Language does not create judgment. Language is the shadow of a validated judgment. The meaning is singular; the expressions are multiple.
