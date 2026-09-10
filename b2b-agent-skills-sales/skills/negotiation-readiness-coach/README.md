# Negotiation Readiness Coach

Prepare for a negotiation using BATNA analysis (Best Alternative to a Negotiated Agreement, from *Getting to Yes*) for both sides, plus a concession plan sequenced by cost-to-give-up-ratio — instead of a generic "know your walk-away number" reminder.

## When to use this

- Heading into a pricing or terms negotiation and the team hasn't explicitly mapped either side's alternatives.
- Reps concede on the first ask (usually price) because it's the easiest lever to pull, not because it's the cheapest one to give.
- Multiple concessions have been made in a deal and nobody's tracking what's been given away versus what's been gained in return.

## Methodology

**BATNA for both sides**: what happens if this specific negotiation fails?
- **Our BATNA**: do we have other pipeline that fills this quarter's gap, or is this deal load-bearing for the forecast? A weak BATNA (no fallback) should never be revealed to the buyer, and should make the negotiator more careful about conceding under self-imposed pressure.
- **Buyer's BATNA**: what's their real alternative — a competitor, the status quo, building in-house? A buyer with a weak BATNA (no good alternative) has less leverage than their negotiating posture suggests, even if they're using deadline pressure as a tactic.

**Concession planning**: not all discounts cost the same. Rank each possible concession by:
```
Concession Value Ratio = perceived_value_to_buyer / actual_cost_to_us

High ratio (>1.5): cheap for us, valuable to them — give these first (e.g., extended onboarding support, a reference call with a peer customer)
Low ratio (<0.7): expensive for us, less valued by them than the sticker cost suggests (e.g., a flat price cut past a certain point often reads as "there was room all along" rather than being appreciated proportionally)
```
Always pair any concession with an ask — an unreciprocated concession trains the buyer to expect more for free.

## Inputs

| Field | Type | Example |
|---|---|---|
| `our_batna` | string | e.g. `"pipeline is thin this quarter - this deal is load-bearing"` or `"strong - 3 other deals could fill the gap"` |
| `buyer_batna_signals` | list[string] | evidence about buyer's real alternatives, from discovery/competitive intel |
| `possible_concessions` | list[{concession, actual_cost, perceived_buyer_value}] | |
| `deal_context` | object | current ask, target terms |

## Worked example

Our BATNA: weak (this deal is needed to hit quarter). Buyer BATNA signals: evaluating one competitor, but competitor's implementation timeline is 3x longer per the buyer's own stated timeline pressure — **buyer's real BATNA is weaker than their negotiating posture suggests.**

Possible concessions:
| Concession | Actual cost to us | Perceived buyer value | Ratio |
|---|---|---|---|
| Extended white-glove onboarding (2 extra weeks of CS time) | Low | High (buyer stated implementation risk as a top concern) | 2.0 |
| 10% flat price cut | High (below approved discount band) | Moderate (buyer never named price as their top concern in discovery) | 0.6 |
| Reference call with a similar customer | Very low | High (addresses the buyer's stated trust/risk concern) | 3.0 |

Recommendation: lead concessions with the reference call and extended onboarding (both high-ratio, both directly answer the buyer's stated implementation-risk concern) before touching price — price was never the buyer's stated top concern, and their weak BATNA (slower competitor timeline) means they have less leverage to demand it than their tone suggests. Pair the onboarding concession with an ask: a signed commitment to a specific close date.

## Common failure patterns

- Conceding on price first because it's the fastest lever to pull, when discovery shows price wasn't the buyer's actual top concern — this gives away margin for something that doesn't move the deal.
- Revealing a weak internal BATNA to the buyer (e.g., "we really need to close this quarter") which hands the buyer leverage regardless of their own BATNA strength.
- Making a concession without pairing an ask, which trains the buyer that concessions are free and invites further asks with nothing given in return.
- Assuming the buyer's stated urgency ("we need a decision by Friday") reflects a strong BATNA rather than checking it — deadline pressure and real alternative strength are independent; a buyer can have real urgency and still have a weak alternative.

## Output schema

```json
{
  "our_batna": {"strength": "weak", "note": "deal is load-bearing for quarter - do not reveal"},
  "buyer_batna": {"strength": "weaker than posture suggests", "evidence": "competitor implementation timeline 3x longer than buyer's stated need"},
  "concessions_ranked": [
    {"concession": "reference call with similar customer", "ratio": 3.0, "sequence": 1, "pair_with_ask": "verbal commitment to timeline"},
    {"concession": "10% flat price cut", "ratio": 0.6, "sequence": 3, "note": "use only if higher-ratio concessions are insufficient"}
  ]
}
```

## Recommended prompt

> You are a negotiation strategist using BATNA analysis. Assess our BATNA strength (and whether it should be concealed) and the buyer's real BATNA strength based on the signals given, distinguishing stated urgency from actual alternative strength. For each possible concession, compute Concession Value Ratio = perceived buyer value / actual cost to us, and sequence concessions from highest to lowest ratio. Prioritize concessions that map to the buyer's actual stated concerns from discovery over the buyer's stated demands if they differ. Pair every recommended concession with a specific ask. Return JSON matching the schema above.

## Grounded in

BATNA analysis from principled negotiation theory (Fisher & Ury, *Getting to Yes*), applied to B2B deal negotiation with a value-ratio concession-sequencing method so concessions are made by leverage economics rather than by which lever is easiest to pull.

See [sources-and-frameworks.md](../../sources-and-frameworks.md) for the pack's general reference list.
