# Executive Sponsor Identifier

Identify the most likely Economic Buyer (MEDDPICC) from an org chart and engagement signals, ranked by budget authority and engagement likelihood — instead of guessing from job title alone.

## When to use this

- The champion won't or can't name who actually approves the budget.
- Multiple senior contacts are engaged and it's unclear which one is the real decision-maker vs. an interested observer.
- You need a specific person and angle to ask your champion to broker an introduction to, not just "someone senior."

## Methodology

Two independent signals, because title alone is a weak predictor of who actually controls budget in flat or matrixed org structures:

- **Authority signal**: org position relative to the budget line this purchase would come from (does their function typically own this budget, and are they senior enough within it — VP+ for most mid-market SaaS deals, director-level in smaller orgs).
- **Engagement signal**: any direct or indirect interaction — attended a call, replied to an email, was referenced by the champion as someone who "needs to see this."

A person can rank high on authority and never surface as an actual approver (delegated authority), so both signals are needed, and the **gap** between them is itself informative.

## Scoring model

```
Authority Score (0-5): 0=no budget relationship to this purchase, 1-2=adjacent function, 3-4=owns the relevant budget line but below typical approval seniority, 5=owns the budget line at typical approval seniority for this deal size

Engagement Score (0-5): 0=no signal at all, 1=named by champion only, 2=named + one indirect signal (e.g. cc'd on email), 3=attended one call, 4=directly asked a substantive question on a call, 5=proactively engaged (scheduled time, asked for follow-up)

Sponsor Likelihood = Authority Score x Engagement Score (0-25)
```

Rank all candidates by Sponsor Likelihood. A candidate with Authority 5 / Engagement 0 is your target to *pursue*; a candidate with Authority 2 / Engagement 5 is enthusiastic but may not be the actual approver — useful as a secondary champion, not the EB ask.

## Inputs

| Field | Type | Example |
|---|---|---|
| `candidates` | list[{name, title, function, seniority, engagement_evidence}] | every senior contact identified so far |
| `deal_size` | number | used to calibrate typical approval seniority |
| `champion_notes` | string | anything the champion has said about who approves |

## Worked example

Deal size: $180K (mid-market — typical approval seniority: VP or above in Sales Ops/RevOps).

| Candidate | Title | Authority | Engagement | Score |
|---|---|---|---|---|
| J. Alvarez | VP Sales Ops | 5 (owns budget, right seniority) | 1 (named by champion only) | 5 |
| M. Torres | Director IT | 3 (adjacent, procurement-adjacent, not deal owner) | 4 (asked technical questions on a call) | 12 |
| R. Kim | CRO | 5 (owns budget at top seniority) | 0 (no signal at all) | 0 |

Ranking by score: Torres (12) is the most *engaged* senior contact but Authority is only adjacent — good secondary influencer, not the EB target. Alvarez (5) has the right authority profile but low engagement — **this is the primary target for an introduction**, not Torres, despite Torres's higher raw score, because Authority is the harder constraint to substitute for (you can build engagement; you can't make someone the budget owner). Kim, despite perfect authority, has zero engagement signal — worth a targeted move (e.g., exec-to-exec outreach) but not yet actionable through the current deal team.

## Common failure patterns

- Ranking purely by the multiplied score without checking which factor is low — a high-engagement, low-authority contact and a high-authority, low-engagement contact need completely different next actions, not the same "keep engaging" plan.
- Assuming CRO/C-level title always means Economic Buyer for this specific purchase — for a $180K sales-ops tool, a VP Sales Ops may hold real approval authority while the CRO delegates entirely.
- Treating "named by the champion" as engagement-equivalent to a direct interaction — champion nomination is a weak signal (score 1) precisely because champions sometimes over-claim influence of people they want you to think matter.
- Stopping the search after finding one plausible EB candidate instead of ranking all candidates — the second-ranked candidate is often the better near-term target if the top one has zero engagement.

## Output schema

```json
{
  "candidates_ranked": [
    {"name": "J. Alvarez", "title": "VP Sales Ops", "authority_score": 5, "engagement_score": 1, "sponsor_likelihood": 5, "recommended_action": "request champion-brokered introduction"},
    {"name": "M. Torres", "title": "Director IT", "authority_score": 3, "engagement_score": 4, "sponsor_likelihood": 12, "recommended_action": "engage as influencer, not primary EB target"}
  ],
  "primary_eb_target": "J. Alvarez",
  "rationale": "correct authority profile for deal size despite low current engagement; engagement is buildable, budget authority is not"
}
```

## Recommended prompt

> You are a sales strategist identifying the likely Economic Buyer. For each candidate, score Authority (0-5, based on whether their function owns the relevant budget line and their seniority relative to typical approval level for this deal size) and Engagement (0-5, based on the strength of direct interaction evidence, not just being named by the champion). Compute Sponsor Likelihood = Authority x Engagement. Rank candidates, and separately call out the recommended primary EB target — favoring authority fit over raw score if the top-scoring candidate's authority is only adjacent, since engagement is buildable but budget authority is not substitutable. Return JSON matching the schema above.

## Grounded in

The Economic Buyer identification practice within MEDDPICC-based enterprise sales qualification, scored on independent authority and engagement axes so a highly engaged but non-budget-owning contact isn't mistaken for the actual approver.

See [sources-and-frameworks.md](../../sources-and-frameworks.md) for the pack's general reference list.
