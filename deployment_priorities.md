# Deployment Priorities

| Domain | Fit | Risk | Priority |
| --- | --- | --- | --- |
| Law | Very high | Low | 1 |
| Healthcare | High | Medium | 2 |
| Corporate decision-making | Medium | High | 3 |
| Defense | Technically high | Ethical high | 4 |

## Rationale

### 1. Law
- Legal systems already operate on canonical ideas: admissibility, procedural validity, dismissal, jurisdiction, handoff, silence.
- Canon maps directly to procedural law, runtime mirrors judicial enforcement, handoff mirrors judicial authority.
- LLMs remain state proposers (case summaries), never decision-makers—courts already understand this structure.

### 2. Healthcare
- Clinical workflows have clear handoff triggers (guideline bounds, contraindications, informed consent).
- Canon failure → silence + handoff, physicians inherit the decision moment they see the message.
- Risk: ethical pressure may push for explanations, but structure aligns well.

### 3. Corporate Decision-Making
- Structural fit exists, but incentives (KPIs, “AI recommendations,” exception culture) create strong pressure to weaken silence/handoff.
- Deploy only after law/healthcare establish precedent; otherwise Canon likely degrades into “nice AI feature.”

### 4. Defense
- Technically ideal but ethically dangerous: “AI stopped, so humans fired” could become a shield for misuse.
- Adoption should wait until society accepts silence/responsibility norms; treat as last stage.

## Principle
> Canon should be applied first where silence and procedural dismissal are already normalized. That is law.
