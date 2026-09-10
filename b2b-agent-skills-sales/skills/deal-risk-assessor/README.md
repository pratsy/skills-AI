# Deal Risk Assessor

Score deal risk against the eight MEDDPICC pillars, each rated by evidence quality (not just presence/absence), instead of a general "gut check" risk narrative. MEDDPICC is the enterprise qualification standard this skill operationalizes into a repeatable score.

## When to use this

- A deal "feels" fine in the CRM (right stage, right close date) but something about it makes the rep uneasy.
- You're prepping for a forecast call and need a defensible reason a deal is Commit vs. Best Case, beyond rep confidence.
- Deal review meetings are inconsistent — different managers probe different things on different deals.

## Methodology

MEDDPICC: Metrics, Economic Buyer, Decision Criteria, Decision Process, Paper Process, Identify Pain, Champion, Competition. Each pillar is scored on **evidence quality**, not whether the rep believes it's true:

| Score | Evidence quality |
|---|---|
| 0 | Unknown or assumed — rep has an opinion, no confirmation from the buying org |
| 1 | Stated by a single non-champion contact, unverified |
| 2 | Confirmed by the champion, but not by the economic buyer or in writing |
| 3 | Confirmed by the economic buyer directly, or documented in a mutual action plan / buyer-shared artifact |

## Scoring model

```
MEDDPICC Score = sum of 8 pillar scores (0-24)

24-19  Low risk — Commit-eligible
18-13  Moderate risk — Best Case, name the specific weak pillars
12-7   High risk — Pipeline only, do not forecast as closing this period
<7     Critical — deal is likely qualified on assumption, not evidence
```

Compute this in addition to a **single-point-of-failure flag**: if either Economic Buyer or Champion scores 0-1, flag the deal as high risk regardless of the total score — a strong total can mask total dependence on one unconfirmed relationship.

## Inputs

| Field | Type | Example |
|---|---|---|
| `deal_id` | string | `opp_5521` |
| `pillar_evidence` | object | one entry per MEDDPICC pillar, each with `{score: 0-3, source, notes}` |
| `stage` | string | current CRM stage |
| `close_date` | date | current forecast close date |

## Worked example

| Pillar | Score | Evidence |
|---|---|---|
| Metrics | 3 | Economic buyer confirmed target: "cut forecast variance 20%" |
| Economic Buyer | 1 | Only the champion has named who signs; EB unconfirmed |
| Decision Criteria | 2 | Champion shared eval criteria doc, not EB-confirmed |
| Decision Process | 1 | Rep believes it's a 2-step approval, unconfirmed |
| Paper Process | 0 | Legal/procurement process unknown |
| Identify Pain | 3 | EB stated pain directly on a call |
| Champion | 2 | Strong champion, but no track record of championing past deals here |
| Competition | 2 | Champion named the competitor, not independently verified |

Total = 3+1+2+1+0+3+2+2 = **14/24 — Moderate/High risk boundary.** Single-point-of-failure flag triggers: Economic Buyer = 1. Recommendation: this deal should not be Commit even though Metrics and Pain are strong — the immediate action is an EB-level conversation to confirm decision process and paper process, not more champion engagement.

## Common failure patterns

- Scoring a pillar on rep confidence ("I'm pretty sure...") instead of evidence source — MEDDPICC fails as a risk tool the moment scores reflect optimism instead of documentation.
- Averaging pillar scores into a single number without checking the single-point-of-failure flag, which hides an EB or Champion gap behind a decent total.
- Treating a high Champion score as a substitute for Economic Buyer confirmation — a strong champion who hasn't gotten the deal in front of the EB is a risk, not a mitigant.
- Re-scoring only at forecast call time instead of after every substantive buyer interaction — MEDDPICC evidence should update in real time as calls happen.

## Output schema

```json
{
  "deal_id": "opp_5521",
  "pillar_scores": {"metrics": 3, "economic_buyer": 1, "decision_criteria": 2, "decision_process": 1, "paper_process": 0, "identify_pain": 3, "champion": 2, "competition": 2},
  "total_score": 14,
  "risk_band": "moderate-high",
  "single_point_of_failure": ["economic_buyer"],
  "forecast_recommendation": "Best Case at most, not Commit",
  "priority_action": "get a direct economic-buyer conversation to confirm decision process and paper process"
}
```

## Recommended prompt

> You are a sales operations analyst scoring deal risk using MEDDPICC. For each pillar (Metrics, Economic Buyer, Decision Criteria, Decision Process, Paper Process, Identify Pain, Champion, Competition), assign a score 0-3 based on evidence quality: 0=unknown/assumed, 1=stated by a non-champion unverified, 2=confirmed by champion only, 3=confirmed by economic buyer or documented. Sum to a total (0-24) and assign a risk band. Flag single-point-of-failure risk if Economic Buyer or Champion scores 0-1, regardless of total. Recommend a forecast category and the single highest-priority action. Return JSON matching the schema above.

## Grounded in

MEDDPICC (an extension of MEDDIC, itself originating at PTC in the 1990s and now the dominant enterprise B2B sales qualification framework), scored by evidence source rather than binary presence so the output distinguishes confirmed facts from rep assumptions.

See [sources-and-frameworks.md](../../sources-and-frameworks.md) for the pack's general reference list.
