# Campaign Performance Diagnostician

Diagnose *why* a campaign underperformed by walking the MQL→SQL→Opportunity→Closed-Won funnel stage by stage against benchmark conversion rates, instead of reporting only top-line metrics like impressions or leads.

## When to use this

- A campaign hit its lead-volume target but pipeline contribution was weak, and nobody can say which stage broke.
- You're comparing two campaigns with similar spend and wildly different pipeline outcomes.
- Leadership wants to know whether to kill, scale, or fix a campaign before next quarter's budget is set.

## Methodology

Walk the standard B2B demand funnel and compute the conversion rate at each transition, then compare each to a benchmark range (use your own trailing-12-month median by channel if you have ≥20 campaigns of history; the ranges below are industry-typical starting points if you don't):

| Stage transition | Typical benchmark range | What a below-range result usually means |
|---|---|---|
| Impression/Click → Lead (form fill) | 2–5% (paid), 1–3% (organic/content) | offer/landing page mismatch, not audience |
| Lead → MQL (meets scoring threshold) | 25–50% | audience/targeting mismatch — wrong people are filling the form |
| MQL → SQL (accepted by sales) | 30–50% | lead quality or scoring-threshold miscalibration |
| SQL → Opportunity (qualified, in pipeline) | 40–60% | sales process or qualification-call quality |
| Opportunity → Closed-Won | varies by motion (often 15–30% for mid-market) | deal-stage/competitive or pricing issue, not a campaign issue |

## Decision logic

1. Compute each transition's conversion rate for the campaign under review.
2. Compare each to the benchmark (or trailing internal median).
3. Find the **first** stage from the top of the funnel where the rate falls meaningfully below benchmark (>25% relative gap) — that's the primary bottleneck. Stages below a broken stage are usually *symptoms*, not separate problems, because a broken early stage starves later stages of enough volume to read reliably.
4. Only diagnose a downstream stage as an independent issue if the upstream stages are all within benchmark range.

## Inputs

| Field | Type | Example |
|---|---|---|
| `campaign_name` | string | `"Q3 RevOps LinkedIn ABM"` |
| `funnel_counts` | object | `{"impressions": 82000, "clicks": 1400, "leads": 58, "mqls": 21, "sqls": 9, "opportunities": 5, "closed_won": 1}` |
| `spend` | number | `18500` |
| `channel` | string | `"paid social - LinkedIn"` |
| `internal_benchmark_rates` | object (optional) | trailing-12-month median rates per transition, if available |

## Worked example

Campaign funnel: 1,400 clicks → 58 leads (4.1%, in range) → 21 MQLs (36%, in range) → 9 SQLs (43%, in range) → 5 opportunities (56%, in range) → 1 closed-won (20%, in typical range for the motion).

All transitions are within benchmark — so a "campaign underperformed" complaint here is actually a **volume** problem, not a **conversion** problem: only 1,400 clicks were generated from 82,000 impressions (1.7% CTR, below the 2–3% typical for this channel/format). The fix is creative/targeting to lift CTR, not a funnel-stage fix — a common misdiagnosis when teams jump straight to "leads are bad quality" without checking whether the funnel is actually converting normally on too little top-of-funnel volume.

## Common failure patterns

- Diagnosing MQL→SQL as the problem when the real issue is upstream (Lead→MQL) starving it of enough qualified volume to convert well.
- Comparing a paid-social campaign's conversion rates to a content/organic benchmark — rates differ meaningfully by channel and intent level.
- Judging a campaign on Closed-Won rate within the campaign's first 60–90 days when the sales cycle for the motion is 120+ days — most of its pipeline hasn't had time to close yet.
- Treating small-sample stages (fewer than ~20 leads) as reliable conversion-rate signals rather than flagging them as low-confidence.

## Outputs

- conversion rate at each funnel transition, vs. benchmark
- the single primary bottleneck stage, with likely cause category
- a volume-vs-conversion diagnosis (is the problem "not enough top-of-funnel" or "leaking at a specific stage")
- recommended next action scoped to the actual bottleneck

## Output schema

```json
{
  "funnel_conversion_rates": [
    {"transition": "click_to_lead", "rate": 0.041, "benchmark_range": [0.02, 0.05], "status": "in range"}
  ],
  "primary_bottleneck": {"stage": "impression_to_click", "rate": 0.017, "benchmark_range": [0.02, 0.03], "likely_cause": "creative/targeting - low CTR", "confidence": "high"},
  "diagnosis_type": "volume, not conversion",
  "recommended_action": "revise ad creative/targeting to lift CTR; downstream funnel is converting normally"
}
```

## Recommended prompt

> You are a demand-gen analyst. Given the campaign funnel counts and channel below, compute the conversion rate at each stage transition (impression→click, click→lead, lead→MQL, MQL→SQL, SQL→opportunity, opportunity→closed-won) and compare each to the provided or typical benchmark range. Identify the first stage from the top of the funnel where the rate falls more than 25% below benchmark — treat that as the primary bottleneck, and downstream low stages as likely symptoms unless they're also independently out of range. Distinguish a volume problem (top-of-funnel too small) from a conversion problem (a specific stage leaking). Return JSON matching the schema above.

## Grounded in

The standard B2B demand-generation funnel (impression → lead → MQL → SQL → opportunity → closed-won) and stage-conversion benchmarking practice used in revenue operations and demand-gen reporting; benchmark ranges are directional industry medians, not audited figures — replace with your own trailing-12-month data where you have it.

See [sources-and-frameworks.md](../../sources-and-frameworks.md) for the pack's general reference list.
