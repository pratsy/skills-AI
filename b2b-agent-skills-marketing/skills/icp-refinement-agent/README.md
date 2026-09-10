# ICP Refinement Agent

Rebuild the Ideal Customer Profile definition from evidence — win rate, retention, and expansion by account attribute — instead of from stated assumptions about "who we sell to." Produces a ranked attribute list and a revised ICP definition with a confidence level per attribute.

## When to use this

- The current ICP was written at founding and hasn't been checked against actual win/loss or retention data since.
- Marketing and sales are targeting different definitions of "good fit."
- Win rate or net revenue retention varies a lot by segment and nobody has quantified which attributes actually predict it.

## Methodology

This is a look-alike analysis, not a survey of opinions: for every candidate attribute, compare its rate among your best accounts to its rate in the general pipeline.

**Best accounts** = closed-won deals in the top half by one or more of: net revenue retention, expansion revenue, sales-cycle length (shorter = better fit signal), or win rate against competition.

**Candidate attributes**: industry, employee band, revenue band, tech stack, buying trigger, org structure (dedicated function vs. not), geography.

## Scoring model

For each attribute value (e.g., "industry = Financial Services"), compute a **lift score**:

```
Lift = (% of best accounts with this attribute) / (% of all pipeline accounts with this attribute)

Lift > 1.5  → strong positive ICP signal
Lift 1.0–1.5 → weak/no signal
Lift < 1.0  → negative signal (this attribute predicts worse-than-average outcomes)
```

Also compute a **confidence level** from sample size — an attribute observed in fewer than ~15 best accounts should be flagged `low confidence` regardless of lift, since small samples produce noisy ratios.

## Inputs

| Field | Type | Example |
|---|---|---|
| `closed_won_accounts` | list[{account_id, attributes, nrr, expansion_revenue, sales_cycle_days}] | full closed-won dataset |
| `all_pipeline_accounts` | list[{account_id, attributes}] | full pipeline for comparison base rates |
| `best_account_definition` | object | e.g. `{"metric": "nrr", "threshold": "top 50%"}` |
| `current_icp_definition` | object | the ICP as currently documented, for comparison |

## Worked example

Best accounts (top 50% by NRR, n=42): 30 are in "Financial Services or SaaS" (71%). All pipeline (n=310): 35% are in those industries.
```
Lift = 71% / 35% = 2.03 → strong positive signal, n=42 → sufficient confidence
```
Best accounts: 8 of 42 (19%) have a dedicated RevOps function. All pipeline: 22% have one.
```
Lift = 19% / 22% = 0.86 → negative signal
```
Interpretation: the current ICP assumes "companies with a dedicated RevOps function" are the target — the data says the opposite; the product may be winning specifically *because* the buyer lacks that function and needs the tool more.

## Common failure patterns

- Defining "best accounts" only by deal size, which selects for large logos rather than accounts that actually retain and expand.
- Computing lift without a comparison base rate — "60% of our best accounts are mid-market" means nothing without knowing what share of all pipeline is mid-market.
- Treating every attribute with lift > 1.0 as ICP-defining instead of ranking by lift magnitude and confidence together.
- Refreshing the ICP once and never again — lift shifts as the product and competitive landscape change; attributes that predicted fit 18 months ago may not now.

## Outputs

- ranked attribute list with lift score and confidence level
- a revised ICP definition (attributes with lift > 1.5 and sufficient sample size)
- a list of attributes in the *current* ICP definition that the data contradicts, with the evidence

## Output schema

```json
{
  "attribute_lift_ranking": [
    {"attribute": "industry = Financial Services or SaaS", "lift": 2.03, "sample_size": 42, "confidence": "high", "signal": "positive"},
    {"attribute": "has dedicated RevOps function", "lift": 0.86, "sample_size": 42, "confidence": "high", "signal": "negative"}
  ],
  "revised_icp": {"include": [], "exclude": []},
  "contradictions_with_current_icp": [
    {"current_assumption": "target companies with dedicated RevOps", "evidence": "lift 0.86 — negative signal", "recommendation": "remove from ICP"}
  ]
}
```

## Recommended prompt

> You are a RevOps analyst running a look-alike ICP analysis. Given closed-won accounts (with performance metrics) and the full pipeline base rates below, define "best accounts" using the provided threshold. For each candidate attribute, compute lift = (rate among best accounts) / (rate among all pipeline). Flag any attribute with fewer than 15 best-account observations as low confidence. Rank attributes by lift and confidence, and list any attribute in the current ICP definition that the data contradicts. Return JSON matching the schema above.

## Grounded in

Look-alike / attribute-lift analysis as used in ICP definition work by B2B growth and RevOps teams (the same underlying logic as look-alike audience modeling in paid media, applied to closed-won account data instead of ad platform audiences).

See [sources-and-frameworks.md](../../sources-and-frameworks.md) for the pack's general reference list.
