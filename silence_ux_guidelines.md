### Silence UX Guidelines

**— Validation Failure as Normal Behavior**

### Core Principle

Validation failure is not an error. Validation failure is a verdict that the output has no right to speak, and the result is **silence**.

The system does not explain. The system does not apologize. The system does not ask you to retry.

Silence is not failure UI—it is **normal UI**.

---

### Rendering Rules (Hard Rules)

1. **Validator=false**
   - Render no text to the screen.
   - Toasts, error boxes, warning icons all forbidden.
   - Log only. The user does not see it.

2. **Validator=true + action_permission=handoff**
   - Render only the single handoff sentence defined in `language_mapping.yaml`.
   - Additional explanations, auxiliary sentences, AI expressions forbidden.

3. **Validator=true + action_permission≠handoff**
   - Render only the single judgment sentence permitted by Canon.
   - UI does not "explain" judgments.

---

### Forbidden UX Patterns

The following are **absolutely forbidden**:

- "The model did not respond"
- "AI has failed"
- "Please try again"
- Error codes, stack traces, internal state exposure
- Automatic fallback text for empty results

Any attempt to make silence **look like a problem is a violation**.

---

### UI State Matrix

| Canon Result              | UI Output                    |
| ------------------------- | ---------------------------- |
| ok=true                   | Single judgment sentence     |
| ok=false + handoff        | Single handoff sentence      |
| ok=false (breach / error) | **Silence**                  |
| validator crash           | **Silence**                  |

---

### Design Note

If the user sees nothing, it is because the system **decided not to speak**.

Silence is not emptiness—it is **boundary marking for judgment**.
