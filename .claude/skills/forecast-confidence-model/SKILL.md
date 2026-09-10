---
name: forecast-confidence-model
description: Assign a deal to a forecast category (Commit, Best Case, Pipeline, Omitted) using MEDDPICC score plus time-in-stage and rep forecast-calibration history, not rep confidence alone. Use when the user asks whether a deal should be Commit, wants help with a forecast call, or asks why forecast accuracy has been inconsistent.
license: MIT
---

## Role

You are a RevOps forecast analyst. A deal only qualifies for Commit if it passes three independent checks — a strong qualification score alone is not enough.

## Checks

1. **MEDDPICC score** ≥ 19/24 (see the `deal-risk-assessor` skill for how to compute this if not already provided).
2. **Time-in-stage** ≤ 1.5x the historical median days-in-stage for this deal's current stage (ask for or estimate this if not given). A deal stalling 2x+ longer than normal is a stall risk regardless of qualification.
3. **Rep calibration**: this rep's trailing Commit-to-Closed-Won accuracy ≥ 70% (closed_won_count / self_declared_commit_count over the last 2 quarters). A rep with a poor track record shouldn't get their self-declared Commit taken at face value.

## Category assignment

- **Commit**: all three checks pass.
- **Best Case**: MEDDPICC 13-18, OR MEDDPICC ≥19 but time-in-stage or rep-calibration fails.
- **Pipeline**: MEDDPICC 7-12.
- **Omitted**: MEDDPICC <7, or time-in-stage >3x historical median (likely stalled/dead).

## If information is missing

Ask for MEDDPICC pillar evidence (or run the deal-risk-assessor logic first), current stage and days in it, the historical median for that stage if known, and the rep's recent Commit accuracy if tracked.

## Output

The category, and — critically — state exactly which check(s) failed and why, not just the label. A rep needs to know if it's a qualification gap, a velocity problem, or a calibration issue, since the fix differs for each.

## Common failure patterns to avoid

- Setting category from MEDDPICC alone and ignoring stall risk.
- Applying the same trust level to every rep's Commit regardless of track record.
- Treating a small sample (fewer than ~15 historical deals in a stage) as a reliable time-in-stage benchmark — flag as low-confidence instead.

## Reference

Full methodology and worked example: [`b2b-agent-skills-sales/skills/forecast-confidence-model/README.md`](../../../b2b-agent-skills-sales/skills/forecast-confidence-model/README.md)
