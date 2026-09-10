# Market Shift Monitor

Classify external market signals using a PESTEL-style category breakdown (regulatory, economic, technological, social, competitive-structural) and score each by velocity and breadth — distinguishing a real structural shift from noise — instead of a general "market is changing" narrative.

## When to use this

- Leadership asks whether a recent piece of market news (a regulation, a funding trend, a technology shift) actually matters strategically or is background noise.
- You're tracking multiple external signals and need to know which represent an actual shift worth planning around.
- Building the "market context" input for annual or quarterly strategic planning.

## Methodology

Classify every signal into a category — the category determines who should own the response and how fast:

| Category | Examples | Typical response speed |
|---|---|---|
| **Regulatory** | new compliance requirement, data privacy law | Often mandatory, fixed timeline |
| **Economic** | funding environment shift, budget-tightening trend in the buyer segment | Affects deal cycle length/budget scrutiny |
| **Technological** | a new underlying technology (e.g., a new AI capability) changing what's buildable | Can be fast-moving, product-relevant |
| **Social/behavioral** | shift in how buyers research or make decisions | Slow-moving but durable once real |
| **Competitive-structural** | new entrant category, business model shift industry-wide (not one competitor — see [`competitor-monitor`](../competitor-monitor/README.md) for single-competitor tracking) | Varies |

## Scoring model

```
Shift Materiality (0-100) = 
    35 x Breadth (0-1: is this affecting one company/segment, or the whole category?)
  + 35 x Velocity (0-1: how fast is this developing - a single data point vs. an accelerating multi-source pattern)
  + 30 x Durability (0-1: is this likely a lasting structural change or a temporary blip - regulatory and
        technological shifts tend to score high here; a single economic data point tends to score low
        until confirmed by a trend)

Shift Band:
  70-100  Structural - warrants explicit strategic planning response
  40-69   Emerging - monitor closely, prepare contingency, don't over-react yet
  <40     Noise - log, no dedicated response needed
```

## Inputs

| Field | Type | Example |
|---|---|---|
| `signal_description` | string | |
| `category` | enum | regulatory \| economic \| technological \| social \| competitive_structural |
| `breadth_evidence` | string | how many sources/companies/segments show this signal |
| `velocity_evidence` | string | how fast/recently this has developed |
| `durability_rationale` | string | why this is/isn't likely a lasting shift |
| `breadth_score`, `velocity_score`, `durability_score` | float (0-1) each | |

## Worked example

Signal: a new data-privacy regulation affecting how B2B vendors can process buyer engagement data, confirmed across multiple jurisdictions, phased implementation over 18 months.

Breadth: affects the entire category, not one company → 0.9. Velocity: confirmed regulatory timeline, moving on a fixed schedule → 0.8. Durability: regulatory changes are structurally durable (not a blip) → 1.0.

```
Shift Materiality = 35(0.9) + 35(0.8) + 30(1.0) = 31.5 + 28 + 30 = 89.5 → Structural
```

Recommended response: this crosses into explicit strategic planning territory — not just a competitive-intel note, but an input to product/legal roadmap given the fixed regulatory timeline, distinct from a lower-scoring "economic sentiment" signal that would warrant monitoring but not a structural planning response.

## Common failure patterns

- Reacting to every piece of market news with the same urgency, which either causes strategic whiplash or trains the org to ignore market signals entirely.
- Scoring durability from how dramatic a signal sounds rather than from actual evidence of a lasting pattern — a single quarter's economic data point is not yet a durable trend.
- Missing breadth by evaluating a signal only against your own company's experience instead of checking whether it's category-wide.
- Classifying a competitive-structural shift (a new business model emerging industry-wide) as if it were a single-competitor signal, missing that the right response is strategic repositioning, not a battlecard update.

## Output schema

```json
{
  "signal_description": "new data-privacy regulation affecting buyer engagement data processing",
  "category": "regulatory",
  "breadth_score": 0.9,
  "velocity_score": 0.8,
  "durability_score": 1.0,
  "shift_materiality": 89.5,
  "shift_band": "structural",
  "recommended_response": "add to strategic planning agenda; coordinate product/legal roadmap given fixed 18-month implementation timeline"
}
```

## Recommended prompt

> You are a market intelligence strategist. Classify the signal below into a category (regulatory, economic, technological, social/behavioral, competitive-structural). Score breadth (0-1: single company/segment vs. category-wide), velocity (0-1: isolated data point vs. accelerating confirmed pattern), and durability (0-1: temporary blip vs. lasting structural change), each with a brief rationale. Compute Shift Materiality = 35xbreadth + 35xvelocity + 30xdurability, and assign a band (structural/emerging/noise) with a recommended response appropriate to that band. Return JSON matching the schema above.

## Grounded in

A PESTEL-style categorization of external market signals, scored by breadth, velocity, and durability so a genuine structural market shift is distinguished from a single noteworthy data point that doesn't yet warrant a strategic planning response.

See [sources-and-frameworks.md](../../sources-and-frameworks.md) for the pack's general reference list.
