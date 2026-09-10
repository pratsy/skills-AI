# Account Plan Generator

Build a strategic account plan using whitespace analysis (mapping what the account already owns vs. what they could plausibly buy, weighted by business-unit budget authority) — instead of a generic relationship-and-notes summary that doesn't identify a specific next expansion motion.

## When to use this

- Planning a strategic/named account for the next planning cycle and need more than a contact list and deal history.
- An account has expansion potential but nobody's mapped which specific business unit or use case to target next.
- Preparing for an account-level QBR and need a structured plan, not a narrative recap.

## Methodology

Whitespace = the gap between what an account currently owns and their total addressable opportunity within your product/service line, mapped by business unit — because expansion potential concentrated in units you have no relationship with is very different from expansion sitting in a unit where you already have a champion.

**Three-part map:**
1. **Owned**: current product/module usage, by business unit, with usage health (healthy/at-risk/unused).
2. **Addressable whitespace**: business units or use cases within your product line that this account doesn't yet own, sized by the account's own scale signals (headcount, revenue, or a comparable customer's adoption pattern).
3. **Relationship coverage per whitespace area**: does a relationship (any confirmed stakeholder contact — see [`stakeholder-map-builder`](../stakeholder-map-builder/README.md)) already exist in the business unit that owns that whitespace, or does expansion require cold entry into a new unit.

## Scoring model

```
Whitespace Priority Score = whitespace_size_estimate x relationship_coverage_multiplier

relationship_coverage_multiplier:
  1.0 = confirmed champion or EB already exists in the target business unit
  0.5 = some relationship exists in an adjacent unit, no direct contact yet
  0.2 = no relationship in or near the target unit - cold entry required

Rank whitespace areas by this score, not by raw opportunity size alone - a smaller opportunity with an existing relationship is usually a faster, higher-probability motion than a larger one requiring cold entry.
```

## Inputs

| Field | Type | Example |
|---|---|---|
| `account_name` | string | |
| `owned_products` | list[{business_unit, product, usage_health}] | current footprint |
| `whitespace_candidates` | list[{business_unit, opportunity_estimate, comparable_customer_reference}] | |
| `relationship_map` | list[{business_unit, has_contact, contact_role}] | from the stakeholder map |

## Worked example

Account: Meridian Capital. Owned: Sales Ops uses the core deal-risk module (usage_health: healthy, high adoption). Whitespace candidates: (a) Marketing Ops — forecast-adjacent campaign attribution module, opportunity estimate $80K/yr, sized against a comparable customer's adoption; (b) Customer Success — renewal risk module, opportunity estimate $120K/yr.

Relationship map: Sales Ops has a confirmed champion (existing relationship). Marketing Ops: no contact identified. Customer Success: one contact exists, unconfirmed role.

```
Marketing Ops:      $80,000 x 0.2  = 16,000
Customer Success:    $120,000 x 0.5 = 60,000
```

Despite Customer Success being the same order of magnitude bigger and Marketing Ops being untouched, Customer Success ranks as the priority whitespace target — the existing (even unconfirmed) relationship makes it a faster path than a cold entry into Marketing Ops, which would need relationship-building from zero before any expansion conversation is possible.

## Common failure patterns

- Ranking whitespace by raw dollar opportunity alone, which favors large cold-entry opportunities over smaller ones with an existing relationship and much higher near-term probability.
- Sizing whitespace from generic market-sizing assumptions instead of a comparable customer's actual adoption pattern, which produces numbers that don't survive scrutiny in a QBR.
- Treating "owned, healthy usage" as done and not monitoring it — an at-risk owned product should be stabilized before pursuing expansion in the same account, since expansion pitches land poorly against an unhealthy existing relationship.
- Building the plan once a year instead of updating relationship coverage as the stakeholder map changes — a new contact in a previously cold business unit should immediately re-rank that whitespace area.

## Output schema

```json
{
  "account_name": "Meridian Capital",
  "owned": [{"business_unit": "Sales Ops", "product": "deal-risk module", "usage_health": "healthy"}],
  "whitespace_ranked": [
    {"business_unit": "Customer Success", "opportunity_estimate": 120000, "relationship_multiplier": 0.5, "priority_score": 60000, "next_action": "confirm the existing contact's role and use them to scope a renewal-risk pilot"},
    {"business_unit": "Marketing Ops", "opportunity_estimate": 80000, "relationship_multiplier": 0.2, "priority_score": 16000, "next_action": "identify a first contact before pursuing"}
  ]
}
```

## Recommended prompt

> You are a strategic account planner. Given the account's owned products (with usage health), whitespace candidates (with opportunity estimates sized against comparable customers), and relationship map, compute Whitespace Priority Score = opportunity_estimate x relationship_coverage_multiplier (1.0 confirmed contact in-unit, 0.5 adjacent relationship, 0.2 no relationship). Rank whitespace areas by this score, not raw size. Flag any owned product with at-risk or unused usage health as needing stabilization before expansion is pursued in that account. Return JSON matching the schema above.

## Grounded in

Whitespace analysis as used in strategic/named account planning, weighted by relationship coverage so account plans prioritize the fastest realistic expansion path rather than the largest theoretical one.

See [sources-and-frameworks.md](../../sources-and-frameworks.md) for the pack's general reference list.
