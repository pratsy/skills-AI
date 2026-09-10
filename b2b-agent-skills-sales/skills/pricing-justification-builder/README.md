# Pricing Justification Builder

Build a value-based (not cost-based) price justification using a TCO/ROI model tied to the buyer's own quantified pain from discovery — output includes the actual math, not just a narrative claim of value.

## When to use this

- A buyer or their CFO wants written justification for the spend before approval.
- Reps default to feature-based justification ("here's what you get") when the buyer's real question is "what does this return."
- Price objections keep surfacing late in the cycle because value was never quantified early enough to anchor against.

## Methodology

Value-based pricing justification requires converting the buyer's own discovery-stated pain into a dollar figure, then comparing that to price — not describing features and hoping the buyer does the math themselves.

**Three components, each must trace back to something the buyer said or a number they confirmed:**

1. **Cost of the status quo** — the dollar (or time, converted to a loaded-cost dollar figure) impact of the problem continuing, per year.
2. **Expected impact of the solution** — the % or absolute improvement, ideally anchored to a comparable reference customer's actual result, not a best-case vendor claim.
3. **Net value** — cost of status quo × expected impact, compared to price, expressed as a ratio and payback period.

## Scoring model

```
Annual Cost of Status Quo = frequency_of_problem_per_year × cost_per_occurrence
  (cost_per_occurrence should be the buyer's own estimate or a defensible proxy - e.g., loaded hourly cost × hours lost)

Expected Annual Value = Annual Cost of Status Quo × expected_improvement_pct
  (expected_improvement_pct should cite a reference customer's actual result, not a rounded marketing claim)

ROI Ratio = Expected Annual Value / Annual Price
Payback Period (months) = (Annual Price / Expected Annual Value) × 12

Credibility check: if expected_improvement_pct has no reference-customer citation, flag the whole justification as "directional, not verified" rather than presenting it with false precision.
```

## Inputs

| Field | Type | Example |
|---|---|---|
| `status_quo_pain` | object | `{"description": "manual forecast review", "frequency_per_year": 4, "cost_per_occurrence": 45000}` |
| `expected_improvement_pct` | float | `0.22` |
| `improvement_source` | string | which reference customer/data this % comes from |
| `annual_price` | number | `60000` |

## Worked example

Status quo pain (from discovery, buyer-confirmed): forecast misses happen ~4x/year, each costing an estimated $45,000 in re-planning/credibility cost (buyer's own estimate, given in a discovery call).

```
Annual Cost of Status Quo = 4 × $45,000 = $180,000
```
Expected improvement: 22% reduction in forecast variance, sourced from a named reference customer of similar size (not a rounded marketing claim).
```
Expected Annual Value = $180,000 × 0.22 = $39,600
Annual Price = $60,000
ROI Ratio = $39,600 / $60,000 = 0.66
Payback Period = ($60,000 / $39,600) × 12 = 18.2 months
```

Result: **ROI ratio below 1 — the value case as currently quantified does not justify the price on hard numbers alone.** This is a more useful (and more credible) output than a generic "strong ROI" claim — it tells the rep the real conversation needed is either (a) find additional quantifiable value the buyer hasn't stated yet, (b) address a smaller initial scope at lower price, or (c) treat this as a longer-payback strategic investment and set that expectation explicitly, rather than oversell a weak ROI number.

## Common failure patterns

- Using a vendor-marketing improvement percentage instead of a specific reference customer's actual result — buyers and their finance teams increasingly ask for the source, and an unsourced number damages credibility more than a modest sourced one helps.
- Presenting the ROI ratio without flagging it when the case is weak (ratio below 1) — the honest output is the model's finding, not a forced positive spin.
- Estimating cost-per-occurrence from an internal assumption instead of a number the buyer themselves confirmed or plausibly would confirm — a buyer-sourced number survives CFO scrutiny; a vendor-estimated one often doesn't.
- Building the justification after the price objection surfaces instead of during discovery, when the status-quo-cost inputs are easiest to gather directly from the buyer.

## Output schema

```json
{
  "annual_cost_of_status_quo": 180000,
  "expected_improvement_pct": 0.22,
  "improvement_source": "reference customer X, similar size/segment",
  "expected_annual_value": 39600,
  "annual_price": 60000,
  "roi_ratio": 0.66,
  "payback_period_months": 18.2,
  "credibility_flag": "improvement_pct is sourced - full confidence",
  "interpretation": "ROI ratio below 1 on hard numbers; recommend scoping conversation or explicit longer-payback framing rather than overselling"
}
```

## Recommended prompt

> You are a value engineer building a price justification. Compute Annual Cost of Status Quo = frequency_per_year x cost_per_occurrence, Expected Annual Value = that figure x expected_improvement_pct, ROI Ratio = Expected Annual Value / Annual Price, and Payback Period in months. If expected_improvement_pct has no cited reference-customer source, flag the output as directional/unverified rather than presenting it with false confidence. State plainly whether the ROI ratio supports the price on hard numbers, and if not, suggest scoping or framing alternatives instead of inflating the narrative. Return JSON matching the schema above.

## Grounded in

Value-based pricing justification / TCO-ROI modeling as practiced in enterprise B2B sales, built to trace every input back to a buyer-confirmed number or a cited reference result rather than presenting vendor-asserted improvement percentages as fact.

See [sources-and-frameworks.md](../../sources-and-frameworks.md) for the pack's general reference list.
