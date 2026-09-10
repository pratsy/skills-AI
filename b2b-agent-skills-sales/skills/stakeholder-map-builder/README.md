# Stakeholder Map Builder

Map every known contact in a deal to a buying-committee role (Economic Buyer, Champion, Influencer, Blocker, User) with a confirmed-vs-assumed status for each, and surface coverage gaps — instead of a flat contact list with titles.

## When to use this

- A deal has several contacts in the CRM but no one can say who actually decides, versus who's just been responsive.
- You suspect single-threading risk (one relationship carrying the whole deal) but haven't quantified it.
- Preparing for a deal review or committee meeting and need to know which roles in the buying committee are still uncovered.

## Methodology

Five buying-committee roles (consistent with the MEDDPICC/Challenger view of a B2B buying group):

| Role | Definition | Risk if uncovered |
|---|---|---|
| **Economic Buyer (EB)** | Controls budget, final approval authority | deal cannot legally close without them |
| **Champion** | Actively sells internally on your behalf, has influence and motivation | no internal advocate when you're not in the room |
| **Influencer** | Shapes the decision (technical evaluator, end-user lead) but doesn't approve | technical/criteria risk if unaddressed |
| **Blocker** | Actively or passively resists (status quo bias, competing priority, competitor loyalty) | deals die from unidentified blockers more often than from competitors |
| **User** | Will use the product day-to-day, rarely decides but can veto via poor adoption signal | post-sale expansion/renewal risk if ignored pre-sale |

Each contact gets a **role** and a **confirmation status**: `confirmed` (role validated through direct behavior/statement, not assumed from title) or `assumed` (inferred from title/seniority only).

## Scoring model

```
Coverage Gap = any of {Economic Buyer, Champion} with zero confirmed contacts
Single-Threading Risk = true if total confirmed contacts across all roles <= 1
Blocker Risk = any confirmed or suspected Blocker with no mitigation plan noted
```

A deal can look "well staffed" with 6 contacts and still have a Coverage Gap if all 6 are Influencers or Users and none is a confirmed EB or Champion — role coverage matters more than contact count.

## Inputs

| Field | Type | Example |
|---|---|---|
| `contacts` | list[{name, title, role_assumed, role_confirmed, evidence}] | every known contact |
| `deal_id` | string | `opp_5521` |

## Worked example

| Name | Title | Role (assumed from title) | Role (confirmed?) | Evidence |
|---|---|---|---|---|
| J. Alvarez | VP Sales Ops | Economic Buyer | assumed | title suggests budget authority, unconfirmed by direct statement |
| M. Chen | RevOps Manager | Champion | confirmed | has scheduled 3 internal meetings on our behalf, shared internal eval doc |
| S. Patel | Sales Manager | Influencer | confirmed | asked detailed product questions, no decision authority indicated |
| — | — | Blocker | — | no contact identified in this role |

Coverage Gap: **Economic Buyer is only assumed, not confirmed** — flagged as the top risk. Single-Threading Risk: false (2 confirmed contacts). Blocker Risk: unknown — no blocker identified yet, which is itself a flag, since most enterprise deals have at least one; recommend the rep probe for who might resist (e.g., an incumbent-tool owner).

## Common failure patterns

- Assigning roles from title alone and marking them "confirmed" — a VP title suggests Economic Buyer but doesn't confirm it; confirmation requires the person's own words or documented approval authority.
- Missing the Blocker role entirely because no one has said anything negative — silence from a likely stakeholder (e.g., the owner of the tool being replaced) is itself a signal worth flagging, not evidence of no risk.
- Counting Influencers and Users toward "good coverage" when Economic Buyer and Champion are still unconfirmed — role coverage, not headcount, determines deal health.
- Not updating roles after new information — a contact who goes quiet after being enthusiastic may have shifted from Champion to passive Blocker.

## Output schema

```json
{
  "deal_id": "opp_5521",
  "contacts_mapped": [
    {"name": "J. Alvarez", "title": "VP Sales Ops", "role": "economic_buyer", "status": "assumed", "evidence": "title only"}
  ],
  "coverage_gaps": ["economic_buyer not confirmed"],
  "single_threading_risk": false,
  "blocker_identified": false,
  "priority_action": "confirm economic buyer directly or via champion-facilitated introduction"
}
```

## Recommended prompt

> You are a sales strategist mapping the buying committee for this deal. Assign each contact to one role (Economic Buyer, Champion, Influencer, Blocker, User) and mark the role as "confirmed" (validated by direct statement or documented behavior) or "assumed" (inferred only from title/seniority). Flag a coverage gap if Economic Buyer or Champion has zero confirmed contacts. Flag single-threading risk if 1 or fewer contacts are confirmed across all roles. Note if no Blocker has been identified, since most enterprise deals have one even if unstated, and this should prompt the rep to probe for it. Return JSON matching the schema above.

## Grounded in

The buying-committee role model (Economic Buyer / Champion / Influencer / Blocker / User) used across MEDDPICC-based and Challenger-style enterprise sales qualification, with an explicit confirmed-vs-assumed distinction so title-based guessing isn't mistaken for real coverage.

See [sources-and-frameworks.md](../../sources-and-frameworks.md) for the pack's general reference list.
