## Human Responsibility Boundary

### Position
- Humans are not inside the Canon or the Runtime.
- They exist outside the automated loop and are invoked only when the Canon issues a handoff.
- Role: authority assumer—the only entity permitted to act beyond the automated boundary.

### Trigger for Responsibility Transfer
- Occurs exactly when `action_permission=handoff` is validated and rendered.
- Sequence:
  1. Canon declares the system lacks authority.
  2. Runtime blocks further automation.
  3. Language renders the handoff sentence.
  4. A human seeing that sentence becomes responsible for the subsequent decision.
- No clicks, confirmations, or secondary approvals required; awareness establishes accountability.

### Post-Handoff Behavior
- Canon, Runtime, LLM, and language cease further action.
- The system offers no advice, suggestions, or monitoring beyond logging the handoff event.
- The outcome from that point is solely the human’s choice.

### Summary
- Humans do not automate the judgment; they inherit it.
- The system’s job is to stop and call them; their job is to decide.
