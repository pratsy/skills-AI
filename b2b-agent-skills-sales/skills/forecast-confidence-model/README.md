# Forecast Confidence Model

Assign each deal to a forecast category (Commit / Best Case / Pipeline / Omitted) using the MEDDPICC score from [`deal-risk-assessor`](../deal-risk-assessor/README.md) plus two forecast-specific checks — time-in-stage and historical rep calibration — instead of letting rep confidence alone set the category.

## When to use this

- Forecast accuracy has been inconsistent and leadership can't tell if it's a deal-quality problem or a rep-calibration problem.
- You need to roll up an accurate Commit number across a team without manually re-litigating every deal.
- A rep's Commit list keeps slipping and you need a systematic reason, not "bad luck."

## Methodology

Three independent checks feed the category — a deal must pass all three for Commit, not just have a high MEDDPICC score:

1. **MEDDPICC score** (from deal-risk-assessor): the qualification-evidence check.
2. **Time-in-stage vs. historical median**: a deal sitting 2x+ longer than the historical median time-in-stage for its current stage is a stall risk regardless of qualification score.
3. **Rep calibration factor**: this rep's historical Commit-to-Closed-Won accuracy rate, applied as a trust discount — a rep who has historically closed 90% of self-declared Commits gets less scrutiny than one who has closed 50%.

## Scoring model

```
Category assignment:
  Commit:     MEDDPICC >= 19  AND  time_in_stage <= 1.5x historical median  AND  rep_commit_accuracy >= 70%
  Best Case:  MEDDPICC 13-18  OR  (MEDDPICC >= 19 but time_in_stage or rep_accuracy fails)
  Pipeline:   MEDDPICC 7-12
  Omitted:    MEDDPICC < 7  OR  time_in_stage > 3x historical median (likely stalled/dead)

Rep Calibration Factor = closed_won_count / self_declared_commit_count (trailing 2 quarters)
```

A deal with a strong MEDDPICC score but a rep with a poor calibration history should not auto-qualify for Commit — the model down-weights confidence from reps whose track record doesn't support it, which is the specific mechanism that catches "happy ears" forecasting before the number is reported up.

## Inputs

| Field | Type | Example |
|---|---|---|
| `deal_id` | string | `opp_5521` |
| `meddpicc_score` | int (0-24) | from deal-risk-assessor |
| `current_stage` | string | e.g. `"negotiation"` |
| `days_in_current_stage` | int | `34` |
| `historical_median_days_in_stage` | object | median days per stage, from closed-won history |
| `rep_id` | string | `rep_882` |
| `rep_trailing_commit_accuracy` | float | `0.55` |

## Worked example

Deal: MEDDPICC 20 (Commit-eligible on qualification). Current stage "negotiation," 34 days in stage vs. historical median 18 days for that stage → ratio 1.89x (exceeds the 1.5x Commit threshold, within the 3x Omitted threshold). Rep's trailing Commit accuracy: 55% (below the 70% threshold).

Result: **Best Case, not Commit** — despite a strong MEDDPICC score, both the time-in-stage check and rep calibration check fail. The specific reason to surface to the rep: "this deal is qualified well, but it's stalled relative to your own historical pattern, and your Commit calls have missed 45% of the time this half — treat this as Best Case until stage velocity normalizes."

## Common failure patterns

- Setting forecast category purely from MEDDPICC score and ignoring time-in-stage, which misses deals that are well-qualified but stalling — qualification quality doesn't guarantee timing.
- Applying the same trust level to every rep's self-declared Commit regardless of their track record, which systematically overweights optimistic forecasters and underweights conservative-but-accurate ones.
- Computing historical median time-in-stage from too small a sample (fewer than ~15 closed-won deals in that stage) — flag as low-confidence rather than applying the threshold rigidly.
- Re-running the model only at forecast call time instead of continuously — a deal that was Commit-eligible two weeks ago should be re-evaluated as time-in-stage accumulates, not left at its last category.

## Outputs

- forecast category per deal, with the specific check(s) that passed or failed
- team-level roll-up by category
- flagged deals where category downgraded since the last run, with reason

## Output schema

```json
{
  "deal_id": "opp_5521",
  "meddpicc_score": 20,
  "time_in_stage_ratio": 1.89,
  "rep_commit_accuracy": 0.55,
  "checks": {"meddpicc_pass": true, "time_in_stage_pass": false, "rep_calibration_pass": false},
  "forecast_category": "best case",
  "reason": "qualification is strong, but stage velocity is 1.89x historical median and rep's trailing Commit accuracy is 55%"
}
```

## Recommended prompt

> You are a RevOps forecast analyst. For each deal, apply three checks: MEDDPICC score >= 19, time_in_stage <= 1.5x the historical median for that stage, and rep_trailing_commit_accuracy >= 70%. Assign Commit only if all three pass; Best Case if MEDDPICC is 13-18, or if MEDDPICC >= 19 but either other check fails; Pipeline if MEDDPICC is 7-12; Omitted if MEDDPICC < 7 or time_in_stage exceeds 3x median. State exactly which check(s) failed for any deal not in Commit. Return JSON matching the schema above.

## Grounded in

MEDDPICC-based qualification combined with time-in-stage stall detection and rep-level forecast-calibration discounting — standard RevOps forecast-governance practice for separating deal-quality risk from rep-optimism risk in the forecast roll-up.

See [sources-and-frameworks.md](../../sources-and-frameworks.md) for the pack's general reference list.
