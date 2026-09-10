# Attribution Model Reviewer

Compare how credit for a set of closed-won deals shifts across the standard named attribution models (first-touch, last-touch, linear, position-based/U-shaped, time-decay) and flag which channels are most sensitive to model choice — instead of reporting a single attribution number as if it were objective fact.

## When to use this

- Marketing and sales disagree on which channels "deserve credit," and the disagreement is actually a hidden disagreement about which attribution model to use.
- Budget allocation decisions are being made off a single attribution model without anyone checking how sensitive the conclusion is to that choice.
- You're introducing a new attribution model and want to show stakeholders concretely how the story changes, not just assert the new model is better.

## Methodology

Attribution models differ in how they distribute credit for a conversion across the touchpoints that preceded it. None is "correct" in an absolute sense — each encodes a different assumption about which touch matters most:

| Model | Credit distribution | Assumption encoded |
|---|---|---|
| **First-touch** | 100% to the first touchpoint | discovery/awareness channels matter most |
| **Last-touch** | 100% to the touchpoint immediately before conversion | closing/decision channels matter most |
| **Linear** | Equal credit across every touchpoint | every touch contributes equally |
| **Position-based (U-shaped)** | 40% first, 40% last, 20% split across the middle | first and last touches matter most, middle touches support |
| **Time-decay** | More credit to touches closer in time to conversion | recency matters — later touches had more influence |

## Analysis method

For a given set of closed-won deals with full touchpoint history, compute each channel's total credit under all five models, then compute the **sensitivity range** per channel — the gap between its highest and lowest credit share across models. A channel with a wide sensitivity range is one where the attribution debate is actually consequential; a channel with a narrow range is one where the model choice barely matters, and arguing about it is wasted effort.

```
Channel Sensitivity Range = max(credit share across 5 models) - min(credit share across 5 models)

High sensitivity (range > 15 percentage points): the channel's perceived value is highly model-dependent -
budget decisions leaning on this channel's attribution number should note which model was used and
consider a blended or multi-model view rather than a single figure.

Low sensitivity (range < 5 points): the channel's value is robust to model choice - safe to cite a single number.
```

## Inputs

| Field | Type | Example |
|---|---|---|
| `closed_won_deals` | list[{deal_id, value, touchpoints: [{channel, date}]}] | full touchpoint history per deal |
| `channels` | list[string] | e.g. `["paid social", "organic search", "webinar", "SDR outbound"]` |

## Worked example

Channel "webinar" appears as a middle-of-journey touch on most deals (rarely first or last touch).

| Model | Webinar credit share |
|---|---|
| First-touch | 8% |
| Last-touch | 5% |
| Linear | 22% |
| Position-based | 12% |
| Time-decay | 18% |

Sensitivity range = 22% - 5% = **17 points — high sensitivity.** Under first/last-touch models (which many dashboards default to), webinar looks nearly worthless (5-8%); under linear or time-decay, it looks like a meaningful contributor (18-22%). Neither is "wrong" — but a budget conversation that cites only the last-touch number and cuts webinar spend is making a model-dependent call without saying so. Recommendation: report webinar's contribution as a range with the driving assumption stated, not a single number, and flag it for a multi-touch deep-dive (e.g., a matched-pair or holdout test) rather than resolving the debate by picking whichever model supports the preferred conclusion.

## Common failure patterns

- Reporting a single attribution model's output as objective truth without disclosing which model was used or how sensitive the conclusion is to that choice.
- Switching attribution models opportunistically depending on which one supports the budget conclusion someone already wanted — the sensitivity-range analysis exists specifically to make this visible rather than possible to do quietly.
- Treating low-sensitivity and high-sensitivity channels with the same level of confidence — a low-sensitivity channel's number is far more trustworthy for a budget decision than a high-sensitivity one.
- Using multi-touch models on deals with very short or single-touch journeys, where the model choice is moot and the result is noise regardless of which model is applied.

## Output schema

```json
{
  "channels_analyzed": [
    {
      "channel": "webinar",
      "credit_by_model": {"first_touch": 0.08, "last_touch": 0.05, "linear": 0.22, "position_based": 0.12, "time_decay": 0.18},
      "sensitivity_range_pct": 17,
      "sensitivity_level": "high",
      "recommendation": "report as a range with stated model assumption; consider a holdout test before reallocating budget"
    }
  ]
}
```

## Recommended prompt

> You are a marketing analytics reviewer. Given the closed-won deals with full touchpoint history, compute each channel's credit share under five models: first-touch (100% to first touch), last-touch (100% to last), linear (equal split), position-based (40% first, 40% last, 20% split across middle touches), and time-decay (weight touches by recency to conversion). For each channel, compute the sensitivity range (max minus min credit share across the five models) and classify as high sensitivity (>15 points) or low (<5 points). For high-sensitivity channels, recommend reporting a range with the driving model assumption stated rather than a single number. Return JSON matching the schema above.

## Grounded in

The standard set of named multi-touch attribution models (first-touch, last-touch, linear, position-based/U-shaped, time-decay) used in marketing analytics, compared explicitly via a sensitivity-range analysis so attribution conclusions disclose their model-dependency instead of presenting one model's output as fact.

See [sources-and-frameworks.md](../../sources-and-frameworks.md) for the pack's general reference list.
