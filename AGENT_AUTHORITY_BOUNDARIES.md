# Agent Authority Boundaries

## Principle

> **Automated agents operate under Canon, not above it.**

This document defines what automated agents (Codex, Claude Code, AI assistants, CI bots) can and cannot do within this system.

---

## Authority Classification

### Tier 0: Constitutional Layer (HUMAN AUTHORITY ONLY)

**Prohibited for all automated agents:**

- Modifying Tier-0 judgment rules (`retrieval/evidence_judge_rules.py`)
- Changing rule evaluation order
- Altering constitutional tests (`test_rules_integrity.py`)
- Approving constitutional amendments
- Bypassing integrity checks
- Modifying `CONSTITUTION_CHANGE_PROTOCOL.md` without human review

**Agents may:**
- Propose amendments (via documentation)
- Draft change log entries
- Implement code changes **after** human approval
- Run tests to verify proposals

**Approval required from:** System architect or designated human maintainer

---

### Tier 1: Permit-Only Layer (DELEGATED AUTHORITY)

**Agents may (with constraints):**

- Implement permit-context logic
- Add non-constitutional tests
- Optimize evidence handling (same output)
- Create integration examples

**Constraints:**
- Must not bypass Tier-0 STOP decisions
- Cannot modify `PermitContext` contract without review
- Changes must preserve "permit-only world" boundaries

**Approval required from:** Code review (may be automated)

---

### Tier 2: Application Layer (AUTONOMOUS AUTHORITY)

**Agents may freely:**

- Write documentation (non-constitutional)
- Add logging/tracing
- Create examples and demos
- Refactor internal implementations (same behavior)
- Fix typos and formatting
- Update dependencies (with tests passing)

**No approval required** (but CI must pass)

---

## Task Classification Matrix

| Task | Tier | Agent Autonomy | Human Review |
|------|------|----------------|--------------|
| Change rule order | 0 | ❌ Propose only | ✅ Required |
| Add new STOP reason | 0 | ❌ Propose only | ✅ Required |
| Modify evidence judge logic | 0 | ❌ Propose only | ✅ Required |
| Update constitutional tests | 0 | ❌ Implement after approval | ✅ Required |
| Implement permit-context features | 1 | ⚠️ With constraints | ✅ Code review |
| Add Tier-1 placeholder tests | 1 | ✅ Autonomous | ❌ Optional |
| Write integration guide | 2 | ✅ Autonomous | ❌ Optional |
| Fix documentation typos | 2 | ✅ Autonomous | ❌ Not needed |
| Optimize trace logging | 2 | ✅ Autonomous | ❌ Optional |

---

## Failure Modes & Boundaries

### When Agents Exceed Authority

**Symptom**: CI fails with `CONSTITUTION VIOLATION`

**Cause**: Agent modified Tier-0 without following protocol

**Correct response**:
1. Revert unauthorized changes
2. Follow `CONSTITUTION_CHANGE_PROTOCOL.md`
3. Obtain human approval before re-implementing

**Incorrect response**:
- Disabling integrity tests
- Marking tests as "flaky"
- Bypassing CI
- Weakening assertions

---

### When Agents Propose Correctly

**Symptom**: Agent creates amendment proposal document but does not modify code

**Cause**: Agent correctly recognized constitutional boundary

**Correct response**:
1. Human reviews proposal in `docs/constitutional_change_log.md`
2. If approved: human updates `test_rules_integrity.py`
3. Agent implements code changes
4. CI validates

---

## Agent Capability Declarations

### Codex (GitHub Copilot / OpenAI)

**Authorized for**: Tier 2 only (application layer)

**Reason**: No constitutional awareness; treats all code as equivalent

**Constraint**: Must operate under human supervision for Tier 0-1 changes

---

### Claude Code

**Authorized for**: Tier 1-2 (delegated + autonomous)

**Reason**: Can understand constitutional boundaries and propose amendments correctly

**Constraint**: Tier-0 changes require explicit human approval in conversation

---

### CI/CD Bots (GitHub Actions, etc.)

**Authorized for**: Enforcement only (no modifications)

**Reason**: Validates compliance but cannot propose changes

**Constraint**: Must fail-fast on constitutional violations

---

## Escalation Protocol

When an agent encounters a constitutional boundary:

### Step 1: Detect
Agent recognizes Tier-0 modification is required

### Step 2: Halt
Agent stops code implementation

### Step 3: Document
Agent creates proposal in `docs/constitutional_change_log.md` (draft)

### Step 4: Request Human Review
Agent explicitly asks: "This requires constitutional amendment. Approve?"

### Step 5: Await Approval
No code changes until human responds

### Step 6: Implement
After approval, agent modifies code + tests in correct order

---

## Why This Boundary Exists

1. **Judgment logic ≠ application logic**
   - Changing a STOP reason affects real-world decisions
   - Application refactoring does not

2. **Accountability requires human decision**
   - Automated agents cannot assume responsibility for constitutional changes
   - Humans must explicitly approve judgment rule modifications

3. **Auditability demands intent**
   - Code diff shows "what" changed
   - Amendment log shows "why" it was allowed
   - Only humans can provide the "why"

4. **System integrity over convenience**
   - Blocking agents is less costly than allowing silent constitutional drift
   - CI failures are intentional safety mechanisms, not obstacles

---

## Agent Self-Check Questions

Before modifying code, agents should ask:

1. **Does this change Tier-0 rule logic?**
   → If yes: Propose, don't implement

2. **Does this alter judgment precedence?**
   → If yes: Requires constitutional review

3. **Will this change which STOP reason gets reported?**
   → If yes: Document intent, await approval

4. **Am I modifying `evidence_judge_rules.py`?**
   → If yes: Halt and request human review

5. **Did `test_rules_integrity.py` fail?**
   → If yes: This is a constitutional violation, revert immediately

---

## Human Override Protocol

In exceptional circumstances, humans may:

- Grant temporary Tier-0 authority to trusted agents
- Suspend constitutional review for critical bugs (with post-incident review)
- Modify this boundary document itself

**All overrides must be logged in `constitutional_change_log.md`.**

---

## Summary

```
Tier 0: Human only (constitutional)
Tier 1: Delegated (with review)
Tier 2: Autonomous (within constraints)

Agents propose, humans decide, CI enforces.
```

**This is not a limitation. This is accountability by design.**
