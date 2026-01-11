# Constitution Change Protocol

## Principle

> **Tier-0 변경은 코드 작업이 아니라 선언 작업이다.**

Any modification to Tier-0 judgment rules is a constitutional amendment, not a feature update.

---

## What Requires This Protocol

Changes to any of the following trigger constitutional review:

- **Rule IDs** (`G-001`, `G-002`, etc.)
- **Rule order** (priority/precedence)
- **Rule conditions** (field checks, operators)
- **Rule actions** (STOP/PERMIT decisions)
- **Evidence state mappings**
- **Generation permission logic**

---

## Amendment Procedure (Mandatory Order)

### Step 1: Document Intent

Create or update:
```
docs/constitutional_change_log.md
```

Entry format:
```markdown
## [Amendment YYYY-MM-DD] Rule Order Adjustment

**Changed**: Moved G-005_NO_DOCUMENT before G-001_NO_EVIDENCE

**Rationale**: NO_DOCUMENT is more specific than NO_EVIDENCE.
When count=0 AND no_document=True, the more precise reason
should be reported.

**Impact**: Test case G-005 now correctly reports NO_DOCUMENT
instead of NO_EVIDENCE.

**Approved by**: [maintainer name/role]
```

**No code changes until this step is complete.**

---

### Step 2: Update Constitutional Tests

Modify:
```
tests/tier0_gate/test_rules_integrity.py
```

Update `EXPECTED_IDS` to reflect the new rule order or set.

**This acts as formal ratification.**

---

### Step 3: Implement Code Changes

Only after Steps 1-2:

- Modify `retrieval/evidence_judge_rules.py`
- Update related logic if needed

---

### Step 4: Verify Integrity

Run:
```bash
python3 -m pytest tests/tier0_gate/test_rules_integrity.py -v
```

**Must pass. No exceptions.**

---

## What Happens If You Skip Steps

- **Skip Step 1**: Future maintainers cannot tell if the change was intentional
- **Skip Step 2**: CI fails with `CONSTITUTION VIOLATION`
- **Skip Step 3**: Tests pass but system behaves incorrectly
- **Any order violation**: Constitutional drift begins

---

## Who Can Approve Amendments

- **Tier-0 changes**: Require explicit human approval (maintainer/architect)
- **Tier-1+ changes**: May be delegated to automated agents (with constraints)

**Automated agents (Codex, Claude Code, etc.) cannot approve Tier-0 amendments autonomously.**

They may:
- Propose amendments
- Draft Step 1 documentation
- Implement Step 3 code changes

They cannot:
- Skip Step 1
- Modify Step 2 without human review
- Bypass integrity tests

---

## Emergency Amendments

If a critical bug requires immediate Tier-0 changes:

1. Create emergency change log entry with `[EMERGENCY]` tag
2. Update tests
3. Implement fix
4. **Schedule post-incident constitutional review within 48 hours**

Emergency amendments are provisional until reviewed.

---

## Constitutional Freeze

During a freeze (e.g., pre-audit, production deployment):

- **All Tier-0 changes are prohibited**
- Even bug fixes require explicit unfreeze
- Emergency procedure does not apply

Freeze status is declared in:
```
FREEZE_NOTICE.md
```

---

## Change Log Location

All constitutional amendments are recorded in:
```
docs/constitutional_change_log.md
```

Format: Chronological, most recent first.

This log is **append-only** during active development.

---

## Rationale

This protocol exists because:

1. **Judgment changes are not refactorings** - they alter system behavior in high-stakes scenarios
2. **Order matters** - rule precedence determines which reason gets reported
3. **Automated agents can propose but not decide** - constitutional changes require human judgment
4. **Auditability requires intent** - code alone doesn't explain "why this order"
5. **Tests are ratification** - updating `EXPECTED_IDS` is saying "yes, this is the new constitution"

---

## Non-Constitutional Changes

The following do **not** require this protocol:

- Documentation clarifications (no semantic change)
- Test case additions (new scenarios, not new rules)
- Runtime optimizations (same output, different performance)
- Trace logging changes
- Integration examples

When in doubt: **Use the protocol.**
