# Competitive Differentiation Coach

Build a differentiation response using a win/loss-evidence-weighted battlecard structure — every claim tagged with whether it's confirmed by actual win/loss outcomes or just an asserted strength — instead of a static feature-comparison table that goes stale and overstates weak claims.

## When to use this

- Reps default to feature comparison ("we have X, they don't") when the real differentiation that wins deals is usually not feature-level.
- Battlecards exist but haven't been updated against recent win/loss data, so reps are citing differentiators that no longer hold or were never actually decisive.
- A specific deal named a competitor and the rep needs a response tailored to *why deals against this competitor are actually won or lost*, not the generic battlecard.

## Methodology

For each named competitor, classify every claimed differentiator by **evidence tier**, using actual win/loss outcomes, not marketing/product assertion:

| Tier | Definition |
|---|---|
| **Tier 1 — Proven decisive** | Cited as the specific reason in 3+ independent win/loss interviews as why the deal was won or lost |
| **Tier 2 — Supported** | Present in product/feature reality and mentioned in at least 1 win/loss interview, but not yet a repeated pattern |
| **Tier 3 — Asserted only** | A claimed strength with no win/loss evidence either way — often true but unproven as a deciding factor |

Lead differentiation conversations with Tier 1 claims. Tier 3 claims should not be presented with the same confidence as Tier 1 — if a rep needs a differentiator and only Tier 3 is available, the honest move is to say so internally and prioritize gathering evidence, not oversell the claim to the buyer.

## Decision logic

1. Identify the named competitor.
2. Pull all differentiators tagged for that competitor, ranked by evidence tier.
3. Match differentiators to the buyer's own stated priorities from discovery (a Tier 1 differentiator the buyer doesn't care about is weaker in this deal than a Tier 2 differentiator that maps directly to their stated pain).
4. Generate the response framed around the buyer's priority, using the highest-tier matching differentiator.

## Inputs

| Field | Type | Example |
|---|---|---|
| `competitor` | string | `"Clari"` |
| `differentiators` | list[{claim, evidence_tier, win_loss_citations}] | the pack's tagged battlecard data |
| `buyer_stated_priorities` | list[string] | from discovery notes |

## Worked example

Competitor: Clari. Differentiators on file:
- "Explainable AI scoring" — Tier 1 (cited in 5 of 8 recent win/loss interviews against Clari as the deciding factor: "reps didn't trust the black-box score").
- "Lower price point" — Tier 2 (mentioned once, not a repeated pattern).
- "Better UI" — Tier 3 (asserted internally, zero win/loss citations either way).

Buyer's stated priority from discovery: "our reps ignored our last tool's recommendations."

Match: Tier 1 differentiator ("explainable AI scoring") maps directly to the buyer's stated pain (rep trust/adoption). Recommended response leads with this, not price or UI: *"That's actually the exact pattern we've seen break other Clari rollouts — reps stop trusting a score they can't see the reasoning behind. Every score here comes with the specific factors driving it, which is what's driven adoption in [similar reference]."* Price and UI are held in reserve, not led with, since they're lower-tier and don't map to the stated priority.

## Common failure patterns

- Leading with the differentiator the sales/marketing team is proudest of instead of the one with the strongest win/loss evidence for this specific competitor.
- Presenting a Tier 3 (asserted-only) claim with the same confidence as a Tier 1 claim, which is discoverable by a buyer doing reference calls and damages credibility when it doesn't hold up.
- Using a generic differentiator list instead of matching to the buyer's specific stated priority from discovery — the "best" differentiator on paper is often not the most persuasive one in a specific deal.
- Never updating evidence tiers after new win/loss interviews, so the battlecard keeps citing an old Tier 1 claim that's actually decayed as the competitor closed the gap.

## Output schema

```json
{
  "competitor": "Clari",
  "differentiators_ranked": [
    {"claim": "explainable AI scoring", "evidence_tier": 1, "citations": 5, "matches_buyer_priority": true},
    {"claim": "lower price point", "evidence_tier": 2, "citations": 1, "matches_buyer_priority": false}
  ],
  "recommended_lead_claim": "explainable AI scoring",
  "response_framing": "...",
  "held_in_reserve": ["lower price point", "better UI"]
}
```

## Recommended prompt

> You are a competitive strategist. Given the named competitor, the tagged differentiators (with evidence tier and win/loss citation count), and the buyer's stated priorities from discovery, rank differentiators by evidence tier first, then by match to the buyer's stated priority. Recommend the single differentiator to lead with — favoring a Tier 1 or 2 claim that matches a stated buyer priority over a higher-tier claim that doesn't map to anything the buyer said they care about. Flag any Tier 3 (asserted-only) claim explicitly as unproven if it would otherwise be the only available response. Return JSON matching the schema above.

## Grounded in

Win/loss-evidence-weighted battlecard practice in competitive sales enablement, built to prevent the common failure of leading with an internally-favored but evidentially weak differentiator instead of the claim actually shown to decide deals against a specific competitor.

See [sources-and-frameworks.md](../../sources-and-frameworks.md) for the pack's general reference list.
