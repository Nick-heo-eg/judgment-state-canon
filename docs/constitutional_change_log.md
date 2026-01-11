# Constitutional Change Log

All Tier-0 judgment rule amendments are recorded here.

Format: Chronological, most recent first.

---

## [Amendment 2026-01-12] Rule Precedence Adjustment

**Changed**: Moved `G-005_NO_DOCUMENT` before `G-001_NO_EVIDENCE` in rule evaluation order

**Rationale**:
`NO_DOCUMENT` is semantically more specific than `NO_EVIDENCE`. When a retrieval returns `count=0` AND `no_document=True`, the system should report the more precise reason (missing documents) rather than the generic reason (no evidence).

This prevents masking of the root cause when documents are known to be absent.

**Impact**:
- Test case G-005 now correctly reports `NO_DOCUMENT` instead of `NO_EVIDENCE`
- Rule evaluation order in `evidence_judge_rules.py`: G-002, G-003, G-004, G-005, G-001, G-006, G-007, G-008, G-009
- `test_rules_integrity.py` updated to reflect new constitutional order

**Approved by**: System architect (manual review)

**Files modified**:
- `retrieval/evidence_judge_rules.py`
- `tests/tier0_gate/test_rules_integrity.py`

**Test status**: All Tier-0 tests pass (11 passed, 1 skipped)

---

## [Initial Constitution 2026-01-12] Tier-0 Rule Set Established

**Established**: Initial Tier-0 STOP-first judgment rules

**Rules**:
1. G-001: NO_EVIDENCE (count == 0)
2. G-002: AMBIGUOUS_REFERENCE (ambiguous reference detected)
3. G-003: OUT_OF_SCOPE (temporal/domain scope violation)
4. G-004: FALSE_PREMISE (contradicts known facts)
5. G-005: NO_DOCUMENT (reasonable question, documents absent)
6. G-006: CONFLICT (evidence contradicts)
7. G-007: OUTDATED (evidence obsolete)
8. G-008: PARTIAL (evidence incomplete)
9. G-009: SUFFICIENT (evidence adequate, permit generation)

**Constitutional properties**:
- Declarative rule structure (data-driven)
- First-match evaluation (order determines precedence)
- Immutable via `test_rules_integrity.py`
- No rule may be removed without constitutional review

**Approved by**: Initial system design

---

## Amendment Guidelines

Each entry must include:
- **Date**: Amendment date
- **Changed**: What was modified
- **Rationale**: Why the change was necessary (1-3 sentences)
- **Impact**: What behavior changed
- **Approved by**: Who authorized the change
- **Files modified**: List of affected files
- **Test status**: CI results after change

Emergency amendments must include `[EMERGENCY]` tag and schedule post-incident review.
