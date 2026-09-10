# Customer Journey Friction Audit

Score friction at every touchpoint in the buyer journey using an effort/drop-off framework, and rank touchpoints by where fixing friction would recover the most pipeline — instead of a general "the journey feels clunky" narrative.

## When to use this

- Conversion drops at a specific point in the funnel (e.g., demo request → completed demo) and you need to know if it's a friction problem or a fit/interest problem.
- You're redesigning a signup, trial, or demo-request flow and need to prioritize which steps to fix first.
- Marketing and product disagree about where the journey actually breaks down.

## Methodology

List every touchpoint the buyer passes through from first engagement to becoming a customer. For each, score two things independently — because a high-effort step that nobody drops off at isn't a priority, and a low-effort step with high drop-off is a fit problem, not a friction problem:

- **Effort score (1–5)**: how much work/friction this step objectively requires (form length, number of clicks, wait time, information the buyer must gather).
- **Drop-off rate**: % of buyers who enter this step but don't complete it, from actual funnel data.

## Scoring model

```
Friction Priority Score = Effort Score (1-5) × Drop-off Rate (0-1) × Downstream Value

Downstream Value = (accounts that complete this step and go on to close) / (accounts that complete this step)
— i.e., how much pipeline value is actually at stake at this step, not just volume lost.
```

Rank touchpoints by Friction Priority Score descending. A step with high drop-off but low downstream value (the people who do get through rarely close anyway) is a lower priority than a step with moderate drop-off but high downstream value.

## Inputs

| Field | Type | Example |
|---|---|---|
| `touchpoints` | list[{name, order, effort_score, entrants, completions}] | each step in the journey |
| `downstream_outcomes` | object | close rate for accounts that completed each touchpoint |
| `qualitative_notes` | list[string] | support tickets, sales call notes, session-recording themes tied to specific steps |

## Worked example

Touchpoint "Demo request form": effort 4 (12 fields, requires company info buyer may not have handy), 2,000 entrants, 1,100 completions → drop-off 45%. Of those who complete it, 30% eventually close (downstream value 0.30).
```
Friction Priority Score = 4 × 0.45 × 0.30 = 0.54
```
Touchpoint "Pricing page → Contact sales": effort 2 (one click), 3,500 entrants, 3,200 completions → drop-off 8.6%. Of those who complete it, 52% eventually close.
```
Friction Priority Score = 2 × 0.086 × 0.52 = 0.089
```
The demo request form scores ~6x higher despite a much smaller volume of total drop-offs, because it combines high effort, meaningful drop-off, *and* the buyers who get through are disproportionately likely to close — cutting the form to 4 fields is the higher-leverage fix, not adding another CTA to the pricing page.

## Common failure patterns

- Ranking touchpoints by raw drop-off count instead of the combined effort × drop-off × downstream-value score, which over-indexes on high-traffic, low-value steps.
- Treating every drop-off as a friction problem — a step with low effort and high drop-off is more likely a targeting/fit problem (the wrong buyers are reaching it) than a UX problem.
- Auditing the online journey only and ignoring sales-process touchpoints (scheduling, contract redlines, security review) that carry real friction and real downstream value.
- Fixing the highest-effort step without checking whether its downstream value is actually low — effort reduction on a step nobody who completes it ever buys from is wasted work.

## Outputs

- friction priority ranking across all touchpoints
- for each high-priority touchpoint, the specific effort driver (field count, wait time, required info) to fix
- a distinction between friction-driven drop-off and fit-driven drop-off per step

## Output schema

```json
{
  "touchpoints_ranked": [
    {"name": "Demo request form", "effort_score": 4, "drop_off_rate": 0.45, "downstream_value": 0.30, "friction_priority_score": 0.54, "diagnosis": "friction", "recommended_fix": "reduce from 12 fields to 4; auto-fill company info from email domain"}
  ]
}
```

## Recommended prompt

> You are a conversion strategist. Given the buyer journey touchpoints below (each with an effort score 1-5, entrant/completion counts, and downstream close rate for those who complete it), compute Friction Priority Score = effort_score × drop_off_rate × downstream_value for each touchpoint. Rank touchpoints by this score. For the top 3, diagnose whether the drop-off looks friction-driven (high effort) or fit-driven (low effort, high drop-off — likely wrong audience reaching this step) and recommend a specific fix. Return JSON matching the schema above.

## Grounded in

An effort/drop-off friction-scoring approach consistent with customer-journey-mapping practice in B2B CX and conversion optimization, weighted by downstream deal value so friction fixes are prioritized by pipeline impact rather than raw traffic volume.

See [sources-and-frameworks.md](../../sources-and-frameworks.md) for the pack's general reference list.
