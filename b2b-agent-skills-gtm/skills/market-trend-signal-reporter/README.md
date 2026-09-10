# Market Trend Signal Reporter

Score raw market signals (search trend data, hiring pattern shifts, funding announcements, category discussion volume) by signal-to-noise ratio before reporting them as a "trend" — the discipline most market-trend reporting skips, which is why trend reports are often just a list of anything that happened recently.

## When to use this

- Producing a regular market trend digest and want to avoid reporting single anecdotal data points as trends.
- Comparing several candidate "trends" and need to know which are actually well-supported versus speculative.
- A stakeholder cites a "trend" they read somewhere and you need to evaluate whether it holds up.

## Methodology

**Signal-to-noise scoring**: every candidate trend needs multiple independent, corroborating data sources before being reported as a trend rather than an anecdote. This mirrors how legitimate trend/forecasting analysis works — one data point is an observation, not a trend.

```
Independent Source Count: how many genuinely independent sources show this pattern
  (two articles citing the same original study count as 1 independent source, not 2)

Corroboration Types: does the pattern show up in more than one KIND of signal -
  e.g., search trend data AND hiring pattern data AND funding pattern data showing
  the same direction is much stronger than three articles all making the same claim
  from secondhand commentary

Time Span: is this observed over multiple periods (weeks/months), or a single spike
  that could be a one-time event (a single viral post, a single conference cycle)
```

## Scoring model

```
Signal-to-Noise Score (0-100) = 
    40 x min(independent_source_count / 3, 1) x 100/100   [caps benefit at 3+ independent sources]
  + 30 x (corroborating_signal_types / 3)   [search, hiring, funding/spend - or other relevant types]
  + 30 x (1 if observed_over_multiple_periods else 0)

Reporting threshold: only report as a "trend" if Signal-to-Noise Score >= 60.
Below 60: report as "early/unconfirmed signal" explicitly, not as a trend, if reported at all.
```

## Inputs

| Field | Type | Example |
|---|---|---|
| `candidate_trend` | string | |
| `sources` | list[{source, independent, signal_type}] | signal_type e.g. search/hiring/funding/media |
| `observed_periods` | int | number of distinct time periods (e.g. months) this has been observed |

## Worked example

Candidate trend: "B2B buyers increasingly expect AI-native features as a baseline, not a differentiator."

Sources: 4 articles, but 3 of them cite the same original analyst report (1 independent source) + 1 genuinely independent survey (2nd independent source). Signal types: media commentary only (1 type — no corroborating hiring or spend data provided). Observed over: only the current period (1 month), no prior-period comparison.

```
Independent sources: 2 → 40 x min(2/3, 1) = 40 x 0.67 = 26.7
Corroborating types: 1 of 3 → 30 x (1/3) = 10
Multi-period: no → 0
Signal-to-Noise Score = 26.7 + 10 + 0 = 36.7 → below 60 threshold
```

This should be reported as an **early/unconfirmed signal**, not a confirmed trend — the underlying claim may well be directionally correct, but the current evidence base (mostly derivative media coverage of one report, single time period, no corroborating behavioral data) doesn't yet support presenting it with trend-level confidence. The report should say exactly that, rather than upgrading it to "trend" because it's an interesting or plausible claim.

## Common failure patterns

- Counting multiple articles that all cite the same original source as multiple independent sources, which inflates apparent corroboration.
- Reporting a single-period spike as a trend without checking whether it persists — many "trends" are one-time events (a viral post, a single conference) that don't recur.
- Relying only on media/commentary signal types without checking for corroborating behavioral data (search volume, hiring patterns, spend data) where available — commentary about a trend is weaker evidence than behavioral data showing it.
- Reporting every candidate trend at the same confidence level instead of explicitly distinguishing confirmed trends from early signals — this is the single biggest credibility risk in trend reporting.

## Output schema

```json
{
  "candidate_trend": "B2B buyers increasingly expect AI-native features as baseline",
  "independent_source_count": 2,
  "corroborating_signal_types": ["media"],
  "observed_over_multiple_periods": false,
  "signal_to_noise_score": 36.7,
  "classification": "early/unconfirmed signal",
  "reporting_recommendation": "report as an early signal to watch, not a confirmed trend; revisit after 2+ more periods of data"
}
```

## Recommended prompt

> You are a market intelligence analyst. For the candidate trend below, count genuinely independent sources (sources citing the same original report count as one), count distinct corroborating signal types (e.g. search, hiring, funding/spend, media - not just multiple media mentions), and note whether it's observed over multiple time periods. Compute Signal-to-Noise Score = 40 x min(independent_sources/3, 1) + 30 x (corroborating_types/3) + 30 x (1 if multi-period else 0). Classify as a confirmed trend only if the score is 60 or above; otherwise classify as an early/unconfirmed signal and say so explicitly. Return JSON matching the schema above.

## Grounded in

Signal-to-noise evaluation practice from trend/forecasting analysis (requiring independent, multi-type, multi-period corroboration before elevating an observation to "trend" status), applied to market intelligence reporting to prevent single-source anecdotes from being reported with trend-level confidence.

See [sources-and-frameworks.md](../../sources-and-frameworks.md) for the pack's general reference list.
