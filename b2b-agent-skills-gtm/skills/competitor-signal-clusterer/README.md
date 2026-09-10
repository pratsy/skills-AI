# Competitor Signal Clusterer

Cluster a batch of individual competitor signals (from [`competitor-monitor`](../competitor-monitor/README.md)) into strategic themes and classify each theme's trajectory — accelerating, stable, or fading — instead of presenting a flat list of unconnected events.

## When to use this

- You have weeks or months of logged competitor signals and need the strategic story they collectively tell, not a re-read of each one.
- Individual signals scored "moderate" materiality on their own might be part of a "high materiality" pattern together.
- Preparing a quarterly competitive strategy review and need themes, not a chronological event log.

## Methodology

Individual signals are clustered by shared strategic implication, not just by move type — e.g., a pricing change, a new low-touch onboarding flow, and a self-serve signup page from the same competitor might all cluster under one theme: "moving down-market toward PLG."

**Trajectory classification**, based on signal frequency over time (not a single snapshot):

```
Accelerating: 3+ signals in this theme in the most recent quarter, more than the prior quarter
Stable: consistent signal rate across the last 2+ quarters, no clear increase or decrease
Fading: signals in this theme have decreased for 2+ consecutive quarters, or none in the most recent quarter
```

## Scoring model

```
Theme Strategic Weight = avg(signal materiality scores in the theme) x trajectory_multiplier

trajectory_multiplier: accelerating = 1.5, stable = 1.0, fading = 0.5

Rank themes by Theme Strategic Weight, not by raw signal count - a theme with fewer but highly
material, accelerating signals outranks a theme with many low-materiality, fading signals.
```

## Inputs

| Field | Type | Example |
|---|---|---|
| `signals` | list[{signal_id, competitor, description, materiality_score, move_type, date}] | output from competitor-monitor, batched over a period |
| `lookback_quarters` | int | how many quarters of signal history to analyze for trajectory |

## Worked example

12 signals from Competitor X over 2 quarters, clustered into theme "moving down-market toward PLG": self-serve signup launch (materiality 65), free-tier pricing change (materiality 72), simplified onboarding flow (materiality 58), reduced minimum contract size (materiality 70) — 2 signals in Q1, 2 in Q2, increasing pace within Q2 itself.

```
Avg materiality = (65+72+58+70)/4 = 66.25
Trajectory: signal count increasing within the lookback window → accelerating (multiplier 1.5)
Theme Strategic Weight = 66.25 x 1.5 = 99.4
```

This theme should rank above a higher-materiality single signal or a fading theme with a higher average score — the combination of decent materiality *and* an accelerating pattern indicates a deliberate strategic shift by the competitor (moving down-market), which has different and broader implications (pricing pressure, new buyer persona to counter) than any single signal in isolation would suggest.

## Common failure patterns

- Clustering signals only by move-type category (all "pricing" signals together) instead of by shared strategic implication, which misses cross-category patterns like the PLG-shift example above that spans pricing, product, and GTM motion signals.
- Ranking themes by raw signal count instead of materiality-weighted, trajectory-adjusted score, which can over-rank a theme with many trivial signals over one with fewer, highly material, accelerating ones.
- Classifying trajectory from too short a window (a single quarter) — trajectory requires at least 2 quarters of comparison to distinguish a real pattern from a one-time cluster of unrelated events.
- Presenting themes without a recommended response owner or action, leaving strategic findings without a clear next step.

## Output schema

```json
{
  "themes": [
    {
      "theme": "moving down-market toward PLG",
      "signal_count": 4,
      "avg_materiality": 66.25,
      "trajectory": "accelerating",
      "strategic_weight": 99.4,
      "implication": "competitor is pursuing a new buyer segment with different pricing/adoption expectations",
      "recommended_response": "assess whether our own down-market packaging needs a counter-response"
    }
  ]
}
```

## Recommended prompt

> You are a competitive strategist. Cluster the signals below by shared strategic implication (not just move type). For each theme, compute avg materiality across its signals, classify trajectory (accelerating: more signals in the most recent quarter vs. prior; stable: consistent rate over 2+ quarters; fading: declining for 2+ quarters) using the lookback window given, and compute Theme Strategic Weight = avg_materiality x trajectory_multiplier (1.5/1.0/0.5). Rank themes by strategic weight. State the strategic implication and a recommended response owner for each. Return JSON matching the schema above.

## Grounded in

Thematic clustering of competitive intelligence signals with a trajectory-weighted scoring method, so that a pattern of moderately material but accelerating signals is surfaced as more strategically important than isolated high-materiality events or fading patterns.

See [sources-and-frameworks.md](../../sources-and-frameworks.md) for the pack's general reference list.
