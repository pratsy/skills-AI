# Brand Positioning Synthesizer

Build a positioning statement using April Dunford's competitive-alternatives framework (from *Obviously Awesome*) — the standard modern B2B positioning method, built specifically to fix vague positioning rather than write taglines.

## When to use this

- Prospects say "so you're like [competitor] but cheaper/nicer" — a sign your differentiation isn't landing.
- Sales reps each describe the product differently in the first two minutes of a call.
- You're entering a new segment or category and the old positioning no longer fits the buyer you're now selling to.

## Methodology

Dunford's framework works backward from competitive context, not forward from features. Five components, filled in this order:

1. **Competitive alternatives** — what would the buyer do if you didn't exist? (Not just named competitors — often "do nothing," "build it in-house," or "use a spreadsheet.")
2. **Unique attributes** — what do you have that the alternatives don't?
3. **Value (and proof)** — what does each unique attribute enable the customer to do or achieve? What evidence backs the claim?
4. **Target market characteristics** — who cares the most about that value, and who will therefore choose you fastest?
5. **Market category** — the frame of reference that makes the value obvious to that target market (sometimes an existing category, sometimes a deliberately redefined one).

The output is a positioning statement in this shape, plus the reasoning behind each slot (not just the final sentence):

```
For [target market characteristic],
[product] is the [market category]
that [key value/differentiator],
unlike [primary competitive alternative],
because [unique attribute that enables the value, with proof].
```

## Inputs

| Field | Type | Example |
|---|---|---|
| `competitive_alternatives` | list[string] | `["Manual spreadsheet tracking", "Clari", "Status quo / no tool"]` |
| `product_attributes` | list[string] | `["Real-time CRM sync", "Explainable AI risk scoring", "No-code rule builder"]` |
| `win_loss_notes` | list[string] | quotes/themes from closed-won and closed-lost deals |
| `customer_segments` | list[object] | candidate target markets with size, urgency, current alternative |
| `category_candidates` | list[string] | existing categories buyer already searches for, or a new frame |

## Decision logic

For each candidate target market, score fit on three questions (1–5 each, 15 max):

- **Value magnitude**: how much does this segment gain from our unique attributes vs. their current alternative?
- **Urgency**: how painful is the status quo for this segment right now?
- **Winnability**: do win/loss records show we actually beat the competitive alternative with this segment, or only claim to?

Pick the target market with the highest score, not the largest addressable market — positioning that's true for a smaller, sharply-defined segment outperforms positioning that's vague across a broad one.

## Worked example

**Product**: an AI deal-risk scoring tool for B2B sales teams.

- Competitive alternatives: gut-feel forecasting in spreadsheets; incumbent forecasting tools (Clari) that require heavy setup.
- Unique attributes: explainable risk scoring (shows *why*, not just a score) + 15-minute setup with no admin required.
- Value: reps trust the score because they can see the reasoning, so they act on it instead of ignoring it (win/loss notes show 40% of reps ignored their previous tool's black-box score).
- Target market: mid-market sales orgs (50–300 reps) without a dedicated RevOps team to run a heavyweight tool — scored 5/5/4 = 14/15 (highest of 3 candidates tested).
- Category: "AI deal risk scoring" (buyers already search this term; no need to redefine a category).

**Output statement**: *"For mid-market sales teams without a dedicated RevOps function, [Product] is the AI deal risk scoring tool that reps actually trust and act on — unlike black-box forecasting tools, because every score comes with a plain-English reason, and it's running in 15 minutes with no admin setup."*

## Common failure patterns

- Writing the target market as "enterprise B2B companies" — too broad to be a real competitive-alternatives comparison; alternatives differ by segment.
- Listing feature attributes instead of *unique* ones (a CRM integration isn't unique if every competitor has it too).
- Skipping the value/proof step and jumping straight from attribute to category — "we have AI" is an attribute, not a reason to believe the value claim.
- Choosing the category buyers *should* want instead of the one they already search for, without budget to do category-creation marketing.

## Output schema

```json
{
  "target_market_ranked": [
    {"segment": "mid-market sales orgs, 50-300 reps", "value_score": 5, "urgency_score": 5, "winnability_score": 4, "total": 14}
  ],
  "selected_target_market": "mid-market sales orgs, 50-300 reps",
  "unique_attributes": ["explainable risk scoring", "15-minute no-admin setup"],
  "primary_competitive_alternative": "black-box forecasting tools (Clari)",
  "category": "AI deal risk scoring",
  "positioning_statement": "For mid-market sales teams ..."
}
```

## Recommended prompt

> You are a positioning strategist using April Dunford's competitive-alternatives framework. Given the competitive alternatives, unique attributes, win/loss notes, and candidate target markets below, score each target market on value magnitude, urgency, and winnability (1-5 each). Select the highest-scoring segment, identify the market category buyers already search for, and produce a positioning statement in the "For [target], [product] is the [category] that [value], unlike [alternative], because [attribute+proof]" format. Return JSON matching the schema above.

## Grounded in

April Dunford's competitive-alternatives positioning framework (*Obviously Awesome*, 2019) — the standard reference method in modern B2B product marketing, chosen over generic "positioning statement" templates because it forces differentiation to be relative to a real alternative rather than asserted in the abstract.

See [sources-and-frameworks.md](../../sources-and-frameworks.md) for the pack's general reference list.
