# Deal Committee Readiness Coach

Score readiness for an internal deal-committee review (forecast call, deal desk, exec pipeline review) against the same MEDDPICC evidence standard used in [`deal-risk-assessor`](../deal-risk-assessor/README.md), producing the specific questions the committee will ask and whether the rep can currently answer them with evidence.

## When to use this

- Before a forecast call or deal desk review, to pressure-test the deal before someone else does.
- A rep is confident about a deal but hasn't had to defend it to a skeptical internal audience yet.
- Deal reviews are inconsistent because reps prep differently — this gives every deal the same bar.

## Methodology

A deal committee's job is to find the weakest MEDDPICC pillar and ask about it. This skill simulates that: for each pillar, generate the question a sharp deal-desk reviewer would ask, and check whether the current evidence (from the deal-risk-assessor output or raw notes) actually answers it.

| Pillar | Committee question they'll ask | Answerable only if... |
|---|---|---|
| Economic Buyer | "Who signs, and have you spoken to them directly?" | EB pillar score ≥ 2 |
| Decision Process | "What are the exact remaining steps to signature, and by when?" | Decision Process score ≥ 2 |
| Paper Process | "Has legal/procurement seen this? What's their typical cycle time?" | Paper Process score ≥ 2 |
| Champion | "What has your champion actually done to move this internally, beyond talking to you?" | Champion score ≥ 2 with a specific action cited |
| Competition | "Who else are they evaluating, and why do you win?" | Competition score ≥ 2 |

## Scoring model

```
Readiness Score = (number of pillars answerable with cited evidence) / 8 x 100

>= 75%   Ready for committee — minor gaps only
50-74%   Prep needed — 2-4 pillars will draw pushback
< 50%    Not ready — recommend deal desk prep session before the review, not the live meeting
```

For any pillar below score 2, the output must include the *specific unanswered question*, not just "Decision Process is weak" — the rep needs the exact question to prepare for, matched to what the evidence currently supports.

## Inputs

| Field | Type | Example |
|---|---|---|
| `deal_id` | string | `opp_5521` |
| `meddpicc_scores` | object | from deal-risk-assessor, or raw notes per pillar |
| `committee_type` | enum | `forecast_call \| deal_desk \| exec_review` — changes which pillars get emphasized |

## Worked example

Using the deal-risk-assessor worked example (EB=1, Decision Process=1, Paper Process=0, others ≥2):

Readiness Score = 5 pillars ≥2 (Metrics, Decision Criteria, Identify Pain, Champion, Competition) / 8 = **62.5% — prep needed.**

Unanswered questions to prepare for:
- "Who signs, and have you spoken to them directly?" (EB=1) — rep needs a plan, not just an answer; recommend citing the multi-threading plan's next step.
- "What are the exact remaining steps to signature?" (Decision Process=1) — rep should get this directly from the champion before the review, not guess.
- "Has legal/procurement seen this?" (Paper Process=0) — rep has no answer; flag this as the highest-priority pre-review action since a "we don't know" on paper process is the fastest way to lose forecast credibility.

## Common failure patterns

- Prepping only for the questions the rep expects, rather than the questions the weakest pillars will actually generate — a confident rep on Metrics and Pain can still get blindsided on Paper Process.
- Treating "I'll find out" as an adequate committee answer for a pillar that's been unknown for multiple review cycles — repeated "I'll find out" on the same pillar is itself a red flag reviewers will notice.
- Running this the morning of the committee meeting instead of with enough lead time to actually close a gap (e.g., get the EB conversation done) before being asked about it live.
- Scoring readiness only on pillar count without weighting Economic Buyer and Paper Process more heavily — these two disproportionately determine whether a deal that "sounds good" is actually going to close on time.

## Output schema

```json
{
  "deal_id": "opp_5521",
  "readiness_score_pct": 62.5,
  "readiness_band": "prep needed",
  "unanswered_questions": [
    {"pillar": "economic_buyer", "committee_question": "Who signs, and have you spoken to them directly?", "current_answer_quality": "weak - named by champion only", "prep_action": "complete step 1-2 of the multi-threading plan before the review"},
    {"pillar": "paper_process", "committee_question": "Has legal/procurement seen this?", "current_answer_quality": "none", "prep_action": "ask champion directly before the review; treat as highest priority"}
  ]
}
```

## Recommended prompt

> You are a deal desk coach preparing a rep for committee review. Given the MEDDPICC pillar scores/evidence below, generate the specific question a skeptical reviewer would ask for each pillar, and mark whether current evidence answers it (pillar score >= 2 with cited evidence = answerable). Compute Readiness Score = answerable pillars / 8 x 100 and assign a band. For every unanswered pillar, give the exact question and a specific prep action the rep can complete before the review — not a restatement of the gap. Weight Economic Buyer and Paper Process gaps as highest priority regardless of overall score. Return JSON matching the schema above.

## Grounded in

MEDDPICC-based deal-desk and forecast-review practice, reframed as a committee-question simulation so preparation targets the specific evidence gaps a reviewer will probe, not a generic confidence check.

See [sources-and-frameworks.md](../../sources-and-frameworks.md) for the pack's general reference list.
