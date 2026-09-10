# Content Gap Analysis Agent

Map existing content against a buyer-journey-stage × persona matrix and score coverage, instead of listing "content ideas." Identifies exactly which stage/persona cells are empty or weak, using the funnel-stage content model demand-gen teams standardize on (early/problem-aware, mid/solution-aware, late/vendor-aware).

## When to use this

- Traffic is healthy but conversion to opportunity is weak, and you suspect content isn't supporting the actual buying decision.
- You're planning next quarter's content calendar and want gaps prioritized by funnel impact, not by topic brainstorming.
- Sales says prospects keep asking questions your content doesn't answer.

## Methodology

Build a coverage matrix: rows = buyer journey stages, columns = personas (or segments). Each cell needs at least one asset that satisfies both the stage's *job* and the persona's *concern*.

| Stage | Buyer's job at this stage | What content must do |
|---|---|---|
| **Problem-aware** (early) | Realizing a problem exists and costs something | Name the problem in the buyer's own language; no product mention needed |
| **Solution-aware** (mid) | Evaluating approaches/categories to solve it | Compare approaches; establish evaluation criteria |
| **Vendor-aware** (late) | Choosing between specific vendors | Proof, differentiation, objection-handling, implementation detail |

## Scoring model

For each stage × persona cell, score coverage 0–3:

```
0 = no asset exists
1 = an asset exists but doesn't address this persona's specific concern (generic)
2 = an asset exists and addresses the persona, but lacks proof/specificity for the stage
3 = a strong asset: stage-appropriate job + persona-specific concern + adequate proof

Matrix Coverage % = (sum of cell scores) / (num_cells × 3) × 100
```

Cells scoring 0–1 at **vendor-aware** stage are highest priority — that's closest to the buying decision and most directly tied to conversion.

## Inputs

| Field | Type | Example |
|---|---|---|
| `personas` | list[string] | `["RevOps Manager", "VP Sales", "CFO"]` |
| `existing_content` | list[{title, format, target_persona, stage_estimate}] | current content inventory |
| `sales_objection_themes` | list[string] | recurring objections from call notes — used to sanity-check vendor-aware coverage |
| `conversion_data_by_stage` | object (optional) | drop-off rates by funnel stage if available |

## Worked example

Personas: RevOps Manager, VP Sales, CFO. 3 stages × 3 personas = 9 cells, 27 max points.

| | RevOps Manager | VP Sales | CFO |
|---|---|---|---|
| Problem-aware | 3 (blog: "Why forecasts miss") | 2 (generic, not VP-specific) | 0 |
| Solution-aware | 3 (buyer's guide) | 1 (one generic comparison page) | 0 |
| Vendor-aware | 2 (case study, but no ROI numbers) | 0 | 0 |

Coverage = (3+2+0+3+1+0+2+0+0)/27 = 11/27 = **41%**.

Highest-priority gap: **CFO, all three stages = 0**, and **VP Sales, vendor-aware = 0** — both are buying-committee roles with zero content, and vendor-aware is the stage closest to the deal. Sales objection theme "CFO pushes back on ROI" directly confirms this gap is costing deals, not just a content-inventory nicety.

## Common failure patterns

- Building the matrix by persona/topic without the stage dimension, which hides that "we have lots of content for VP Sales" is all early-stage and none of it helps at the point deals actually stall.
- Scoring an asset a 3 because it's well-produced, when it doesn't actually address the persona's specific concern (production quality isn't the same as coverage quality).
- Treating every 0-cell as equally urgent instead of weighting by proximity to the buying decision (vendor-aware) and by whether sales objection data confirms it's actually costing deals.
- Auditing content inventory without cross-checking against real objections/drop-off data — a coverage gap that doesn't show up in sales friction may not be a priority yet.

## Output schema

```json
{
  "coverage_matrix": [
    {"stage": "vendor-aware", "persona": "CFO", "score": 0, "existing_assets": []}
  ],
  "overall_coverage_pct": 41,
  "priority_gaps": [
    {"stage": "vendor-aware", "persona": "CFO", "confirmed_by_sales_objections": true, "recommended_asset": "ROI/TCO calculator or CFO-specific case study with hard numbers"}
  ]
}
```

## Recommended prompt

> You are a content strategist. Build a buyer-journey-stage (problem-aware / solution-aware / vendor-aware) × persona coverage matrix from the content inventory below. Score each cell 0-3: 0=no asset, 1=generic asset not persona-specific, 2=persona-specific but lacking stage-appropriate proof, 3=strong stage+persona+proof fit. Compute overall coverage %. Rank gaps by priority, weighting vendor-aware-stage gaps and any gap confirmed by the sales objection themes provided as highest priority. Return JSON matching the schema above.

## Grounded in

The problem-aware / solution-aware / vendor-aware buyer-journey content model standard in B2B demand generation, combined with a persona × stage coverage-matrix method for making "content gap" a scored, auditable finding rather than a brainstorm.

See [sources-and-frameworks.md](../../sources-and-frameworks.md) for the pack's general reference list.
