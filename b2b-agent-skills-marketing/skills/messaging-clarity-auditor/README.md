# Messaging Clarity Auditor

Score a piece of messaging against a four-dimension clarity rubric — specificity, differentiation, proof, jargon load — instead of judging it on tone. Built to catch the most common B2B messaging failure: copy that is fluent, on-brand, and says nothing a competitor couldn't also claim.

## When to use this

- A page or deck "reads well" in review but reps say prospects don't remember it after the call.
- You suspect messaging is generic (could apply to 3 competitors unchanged) but can't point to why.
- You're auditing a large set of pages/assets for consistency before a rebrand or repositioning rollout.

## Methodology

Four dimensions, each scored 1–5, applied sentence-by-sentence to the core claims (headline, subhead, and top 3 supporting points — not full body copy):

| Dimension | Test question | 1 (fails) | 5 (passes) |
|---|---|---|---|
| **Specificity** | Could this sentence describe a real, distinct thing, or does it use abstract nouns? | "We help you drive growth" | "We cut deal-risk review time from 3 hours to 15 minutes" |
| **Differentiation** | If you swapped in a competitor's name, would the sentence still sound true? | Sentence survives the swap unchanged | Sentence becomes false or absurd with a competitor's name |
| **Proof** | Is there a number, named customer, or mechanism backing the claim, or just an assertion? | "Trusted by leading teams" | "Used by 40+ RevOps teams; average 22% forecast variance reduction" |
| **Jargon load** | Would a buyer's peer (not an industry insider) understand this without translation? | "Unlock synergistic pipeline velocity" | "See which deals are actually going to close" |

## Scoring model

```
Clarity Score (per sentence) = Specificity + Differentiation + Proof + Jargon_clarity   (4-20)

Sentence-level bands:
17-20  Strong — safe to lead with
12-16  Needs one fix — usually Proof or Differentiation
< 12   Rewrite — generic enough to belong to any competitor

Page/asset score = average of headline + subhead + top 3 supporting points
```

## Inputs

| Field | Type | Example |
|---|---|---|
| `asset_type` | string | `"homepage hero"`, `"one-pager"`, `"email subject+body"` |
| `core_claims` | list[string] | headline, subhead, and top supporting points, as separate strings |
| `known_competitors` | list[string] | used for the differentiation swap test |
| `available_proof_points` | list[string] | real stats/customers the team could cite, for rewrite suggestions |

## Worked example

Claim: *"Our platform empowers revenue teams to unlock their full potential."*

- Specificity: 1 — "empowers," "unlock," "full potential" are abstract; nothing concrete is claimed.
- Differentiation: 1 — swap in any competitor's name, the sentence still reads as true.
- Proof: 1 — no number, name, or mechanism.
- Jargon: 2 — not technical jargon, but marketing-abstraction jargon, same failure mode.
- **Score: 5/20 — rewrite.**

Rewrite using available proof point (22% forecast variance reduction, 40+ customers): *"40+ RevOps teams use [Product] to cut forecast variance by 22% — by scoring every deal's risk from live CRM data, not gut feel."*
- Specificity: 5, Differentiation: 4 (a generic tool couldn't claim this specific mechanism+number), Proof: 5, Jargon: 4 — **Score: 18/20 — strong.**

## Common failure patterns

- Auditing full paragraphs instead of isolating the core claims — supporting detail can mask a weak headline.
- Scoring differentiation by asking "is this true about us" instead of "would this survive a competitor-name swap" — many true statements are still non-differentiating.
- Accepting a high proof score for social-proof claims with no number ("trusted by leading teams" is not proof; "40+ teams" is).
- Fixing jargon by simplifying vocabulary without adding specificity — plain language that's still vague scores no better.

## Output schema

```json
{
  "claims_scored": [
    {"claim": "Our platform empowers revenue teams to unlock their full potential.", "specificity": 1, "differentiation": 1, "proof": 1, "jargon_clarity": 2, "total": 5, "band": "rewrite", "suggested_rewrite": "40+ RevOps teams use [Product] to cut forecast variance by 22%..."}
  ],
  "asset_score": 5,
  "priority_fixes": ["headline lacks any proof point despite having usable stats available"]
}
```

## Recommended prompt

> You are a messaging strategist. Score each core claim below on four dimensions (1-5 each): Specificity (concrete vs. abstract), Differentiation (would it survive having a named competitor swapped in?), Proof (backed by a number/name/mechanism, or just asserted?), and Jargon clarity (would a buyer's peer understand it unaided?). Sum to a 4-20 total per claim. For any claim scoring below 12, rewrite it using the available proof points provided, and re-score the rewrite. Return JSON matching the schema above.

## Grounded in

A specificity/differentiation/proof clarity rubric, consistent with the "so what, who cares, prove it" test used in B2B messaging review and the plain-language principle behind frameworks like StoryBrand (Donald Miller) — built to make "this messaging feels generic" an auditable, sentence-level finding instead of a subjective impression.

See [sources-and-frameworks.md](../../sources-and-frameworks.md) for the pack's general reference list.
