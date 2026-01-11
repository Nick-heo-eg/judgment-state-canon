# EchoJudgmentSystem v10-1 — Memory Governance Boundary Map

This document illustrates the canonical boundaries: EchoJudgmentSystem v10-1 legally recognizes memory only when a human declares it. It is a map, not an implementation guide.

## 1. Canon Core
> EchoJudgmentSystem v10-1 is a system that legally recognizes memory only when a human declares it.

## 2. Boundary Diagram
```
┌───────────────────────────────┐
│            CANON              │
│  memory_governance.md (FROZEN)│
│  - memory legal status        │
│  - promotion / invalidation   │
│  - automation banned          │
└───────────────▲───────────────┘
                │ (legal authority)
┌───────────────┴───────────────┐
│            HUMAN              │
│  - declares memory            │
│  - assumes responsibility     │
│  - signs promotion log        │
└───────────────▲───────────────┘
                │ (declaration)
┌───────────────┴───────────────┐
│           RUNTIME             │
│  - stores artifacts/logs      │
│  - cannot promote memory      │
│  - cannot invalidate memory   │
└───────────────▲───────────────┘
                │ (interpretation)
┌───────────────┴───────────────┐
│             LLM               │
│  - state/language tool        │
│  - no memory authority        │
└───────────────▲───────────────┘
                │
┌───────────────┴───────────────┐
│           LANGUAGE            │
│  - expression only            │
│  - saying ≠ remembering       │
└───────────────────────────────┘
```

## 3. Memory Status Flow
```
[ Artifact / Log / State ]
          │
          ▼
┌───────────────────────┐
│ Evidence Candidate    │
└───────────┬───────────┘
            │ (Human declaration only)
            ▼
┌───────────────────────┐
│ Citizen Memory        │
└───────────┬───────────┘
            │ (Human invalidation)
            ▼
┌───────────────────────┐
│ Residue / Invalidated │
└───────────────────────┘
```

## 4. Memory Promotion Log
```
timestamp | declarant | artifact_id | action (promote/invalidate) | justification
```

Only human declarations appear; the system cannot auto-fill entries.

## 5. Closed Boundaries
- Runtime cannot create or revoke memory.
- LLMs can propose content but cannot promote.
- Language renders validated decisions only.
- Automation in memory lifecycle is banned.
- Human declaration is the sole open gate.

## 6. Status
- Canon: FROZEN
- Automation: Banned
- Next Action: None (Observation Only)
