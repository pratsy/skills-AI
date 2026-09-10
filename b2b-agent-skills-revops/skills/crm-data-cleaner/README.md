# CRM Data Cleaner

Score CRM record quality across the four standard data-quality dimensions — completeness, accuracy, consistency, timeliness — and prioritize cleanup by which records actually affect active decisions (open pipeline, upcoming renewals), instead of a flat field-completeness percentage across the whole database.

## When to use this

- Reports and dashboards are inconsistent because underlying CRM data has gaps, but nobody knows which records matter most to fix first.
- Planning a CRM cleanup project with limited ops time and need to prioritize by business impact, not by record count.
- A specific analysis (pipeline health, attribution, forecast) is producing suspicious output and you suspect the input data quality, not the analysis, is the problem.

## Methodology

Four standard data-quality dimensions, each scored independently because a record can fail on one and pass on others:

| Dimension | Question | Example failure |
|---|---|---|
| **Completeness** | Are required fields populated? | close date missing on an open opportunity |
| **Accuracy** | Does the data reflect reality? | stage says "negotiation" but no activity in 60 days |
| **Consistency** | Do related fields agree with each other? | deal stage is "closed-won" but amount is $0 |
| **Timeliness** | Was the record updated recently enough to trust? | last modified 90+ days ago on an active deal |

## Scoring model

```
Record Quality Score (0-100) = 
    30 x Completeness (required fields populated / required fields total)
  + 25 x Accuracy (1 if stage matches activity recency pattern, 0 if stage/activity mismatch detected)
  + 25 x Consistency (1 if cross-field logic checks pass, 0 if any fail - e.g. closed-won with $0 amount)
  + 20 x Timeliness (1 if modified within expected cadence for its stage, 0 if stale)

Business Impact Weight:
  open pipeline deal, closing this quarter        = 3x
  open pipeline deal, later quarter                = 2x
  active renewal account                           = 3x
  closed/inactive record                           = 1x

Cleanup Priority = (100 - Record Quality Score) x Business Impact Weight
```

Rank cleanup work by Priority score, not by raw error count — a low-quality record on a closed deal from two years ago is lower priority than a moderately imperfect record on a deal closing this month.

## Inputs

| Field | Type | Example |
|---|---|---|
| `record_id` | string | |
| `required_fields` | list[{field, populated}] | |
| `stage` | string | |
| `last_activity_date` | date | |
| `last_modified_date` | date | |
| `amount` | number | |
| `business_context` | enum | `open_this_quarter \| open_later \| active_renewal \| closed` |

## Worked example

Record: opportunity, stage "negotiation," amount $0 (consistency fail), 8 of 10 required fields populated (completeness 0.8), last activity 65 days ago while stage implies active engagement (accuracy fail), last modified 70 days ago (timeliness fail, stale for an active-stage deal). Business context: open, closing this quarter.

```
Record Quality Score = 30(0.8) + 25(0) + 25(0) + 20(0) = 24 + 0 + 0 + 0 = 24
Cleanup Priority = (100 - 24) x 3 = 76 x 3 = 228
```

This record ranks near the top of the cleanup queue — not primarily because of the completeness gap (which is fairly minor at 80%), but because it fails accuracy, consistency, *and* timeliness simultaneously on a deal that's supposed to close this quarter, meaning the forecast number currently includes an opportunity that's very likely misrepresented or stalled.

## Common failure patterns

- Prioritizing cleanup by raw field-completeness percentage alone, which misses records that are "complete" but inaccurate or inconsistent (all fields filled in, but stage doesn't match reality).
- Treating every incomplete record as equal priority regardless of whether it's an active deal or a two-year-old closed record — cleanup time is wasted on records with no current business impact.
- Flagging accuracy issues only from missing data, without checking activity-vs-stage mismatches, which catch a different and often more consequential class of "stale but technically complete" record.
- Running cleanup as a one-time project instead of a standing scored queue — new records decay into the same quality issues on the same timeline as old ones did.

## Output schema

```json
{
  "record_id": "opp_5521",
  "completeness": 0.8,
  "accuracy_pass": false,
  "consistency_pass": false,
  "timeliness_pass": false,
  "record_quality_score": 24,
  "business_context": "open_this_quarter",
  "cleanup_priority": 228,
  "issues": ["stage/activity mismatch (65 days no activity in negotiation stage)", "closed-won-style amount inconsistency", "stale (70 days since last modification)"]
}
```

## Recommended prompt

> You are a RevOps data quality analyst. For each record, score completeness (populated required fields / total), and pass/fail accuracy (does activity recency match the stage), consistency (do cross-field values agree logically), and timeliness (was it modified recently enough for its stage). Compute Record Quality Score = 30xcompleteness + 25xaccuracy + 25xconsistency + 20xtimeliness. Apply a business impact weight (3x for open-this-quarter or active-renewal records, 2x for later-quarter open records, 1x for closed/inactive) and compute Cleanup Priority = (100 - quality score) x weight. Rank records by priority, not raw error count. Return JSON matching the schema above.

## Grounded in

The completeness/accuracy/consistency/timeliness data-quality framework standard in data management practice, applied to CRM records with a business-impact weighting so cleanup effort targets records that actually affect current pipeline and forecast decisions.

See [sources-and-frameworks.md](../../sources-and-frameworks.md) for the pack's general reference list.
