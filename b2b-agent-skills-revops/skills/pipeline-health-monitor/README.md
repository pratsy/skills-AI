# Pipeline Health Monitor

Score pipeline health against pipeline coverage ratio and stage-conversion benchmarks — the two standard RevOps pipeline-quality metrics — instead of a narrative "pipeline looks weak" read. Distinguishes a coverage problem (not enough pipeline) from a conversion problem (enough pipeline, but it's not moving).

## When to use this

- Pipeline volume looks adequate but leadership is nervous about the number — need to know if the nervousness is justified.
- Comparing pipeline health across segments/reps and need an objective basis, not a stage-count table.
- Preparing for a QBR and need to show whether current pipeline actually supports the forecast, not just its size.

## Methodology

**Pipeline coverage ratio**: total open pipeline value divided by the remaining quota/target for the period. The standard benchmark range is **3–4x** for a typical B2B sales motion (varies by win rate and cycle length — a business with a 40% win rate needs less coverage than one with 15%).

```
Required Coverage Ratio ≈ 1 / historical_win_rate
(a 25% win rate implies needing roughly 4x pipeline coverage to reliably hit target)
```

**Stage conversion health**: for each stage transition, compare current-period conversion rate to the trailing historical median for that same transition (not an external benchmark — internal history is the right comparison once you have ~6 months of data).

## Scoring model

```
Coverage Status:
  Actual Coverage >= Required Coverage (1/win_rate)           → sufficient
  Actual Coverage between 0.75x and 1x of Required             → marginal
  Actual Coverage < 0.75x of Required                          → insufficient

Stage Health (per transition):
  current_rate >= 0.9 x historical_median   → healthy
  current_rate 0.7-0.9x historical_median   → weakening
  current_rate < 0.7x historical_median     → broken

Overall Pipeline Health = "at risk" if EITHER coverage is insufficient OR any single stage is broken,
regardless of how healthy the other metric looks - a broken stage can undermine sufficient coverage,
and insufficient coverage can't be masked by healthy stage conversion.
```

## Inputs

| Field | Type | Example |
|---|---|---|
| `open_pipeline_value` | number | `2400000` |
| `remaining_quota` | number | `700000` |
| `historical_win_rate` | float | `0.22` |
| `stage_conversion_rates` | list[{transition, current_rate, historical_median}] | |

## Worked example

Open pipeline: $2.4M. Remaining quota: $700K. Historical win rate: 22%.
```
Required Coverage = 1 / 0.22 ≈ 4.5x
Actual Coverage = 2,400,000 / 700,000 ≈ 3.4x
```
3.4x is below the 4.5x required (ratio 3.4/4.5 = 0.76) → **marginal, not sufficient.**

Stage conversion: "Discovery → Proposal" current rate 28% vs. historical median 45% → ratio 0.62 → **broken.** Other stages within 0.9x of median → healthy.

Overall read: **at risk** — driven specifically by the Discovery→Proposal breakdown, not by coverage alone (coverage is marginal but not the primary driver). The recommended action targets that specific transition (qualification discipline or proposal-readiness criteria), not a generic "generate more pipeline" response, which wouldn't fix a conversion problem.

## Common failure patterns

- Reporting coverage ratio against a flat industry rule of thumb ("we hit 3x, we're fine") instead of computing the ratio actually required by this team's own win rate — a lower win rate needs proportionally more coverage.
- Treating "pipeline looks big" as healthy without checking stage conversion, which misses pipelines that are large but structurally broken at a specific stage.
- Comparing stage conversion to an external benchmark instead of internal trailing history, which produces false alarms when a business's normal conversion profile legitimately differs from generic industry numbers.
- Recommending "generate more pipeline" as the default fix regardless of diagnosis — the correct fix depends entirely on whether the problem is coverage or a specific stage conversion break.

## Output schema

```json
{
  "coverage_ratio": {"actual": 3.4, "required": 4.5, "status": "marginal"},
  "stage_health": [
    {"transition": "discovery_to_proposal", "current_rate": 0.28, "historical_median": 0.45, "status": "broken"}
  ],
  "overall_health": "at risk",
  "primary_driver": "discovery_to_proposal conversion broken (0.62x historical median)",
  "recommended_action": "review qualification discipline entering discovery, not pipeline generation volume"
}
```

## Recommended prompt

> You are a RevOps analyst. Compute Required Coverage Ratio = 1 / historical_win_rate, and Actual Coverage = open_pipeline_value / remaining_quota. Classify coverage as sufficient (actual >= required), marginal (0.75-1x of required), or insufficient (<0.75x). For each stage transition, compare current_rate to historical_median and classify as healthy (>=0.9x), weakening (0.7-0.9x), or broken (<0.7x). Set overall_health to "at risk" if either coverage is insufficient or any stage is broken. Identify the primary driver and recommend an action specific to that diagnosis. Return JSON matching the schema above.

## Grounded in

Pipeline coverage ratio (calibrated to the team's own win rate, standard RevOps practice) combined with trailing-internal-history stage-conversion benchmarking, so pipeline health reflects this team's actual historical pattern rather than a generic external rule of thumb.

See [sources-and-frameworks.md](../../sources-and-frameworks.md) for the pack's general reference list.
