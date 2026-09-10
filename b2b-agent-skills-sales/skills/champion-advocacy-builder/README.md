# Champion Advocacy Builder

Score champion strength using the Challenger Sale's "Mobilizer" test — does this person actually move the deal internally, versus just being friendly and responsive — and generate the specific enablement content the champion needs for their next internal conversation.

## When to use this

- A contact is enthusiastic and responsive but the deal isn't progressing internally — a sign they may be a "Friend," not a Mobilizer.
- You need to know what to arm a champion with before their next internal meeting, not just "check in with them."
- Multiple contacts seem champion-like and you need to identify which one actually has the internal capital to move the deal.

## Methodology

Challenger Sale research found that the contacts who feel most helpful (responsive, friendly, generous with their time — "Friends" and "Talkers") are frequently *not* the ones who move deals internally. True Mobilizers show a different, checkable pattern:

| Signal | Friend/Talker (low mobilizing power) | Mobilizer (high mobilizing power) |
|---|---|---|
| Meeting behavior | Agrees readily, avoids friction | Pushes back, asks hard questions, challenges the pitch |
| Internal action | Talks about helping, rarely produces artifacts | Has independently built a business case doc, looped in others unprompted |
| Risk appetite | Avoids introducing you to skeptical colleagues | Willingly brings you to a skeptical stakeholder |
| Motivation | Personal rapport with the rep | Genuine belief the org needs to change |

## Scoring model

```
Mobilizer Score (0-12) = sum of 4 signals, each scored 0-3:
  meeting_behavior: 0=only agrees, 1=asks clarifying Qs, 2=asks hard Qs, 3=challenges assumptions constructively
  internal_action: 0=no evidence, 1=says they'll help, 2=has talked to one other stakeholder, 3=produced an artifact (doc, deck) unprompted
  risk_appetite: 0=shields you from skeptics, 1=neutral, 2=offers an intro, 3=proactively brought a skeptic into a call
  motivation_signal: 0=purely social rapport, 1=likes the product, 2=cites team-level benefit, 3=cites org-level change reason

9-12  Confirmed Mobilizer — invest enablement time here
5-8   Developing — possible Mobilizer, needs a specific test (e.g., ask them to produce an artifact) to confirm
0-4   Friend/Talker — valuable for information, not for internal movement; find the real Mobilizer elsewhere
```

## Inputs

| Field | Type | Example |
|---|---|---|
| `contact_name` | string | |
| `observed_signals` | object | `{meeting_behavior: 2, internal_action: 3, risk_appetite: 2, motivation_signal: 3}` with supporting notes |
| `deal_stage` | string | used to tailor what enablement content is needed next |

## Worked example

Contact: M. Chen, RevOps Manager. Observed: asks hard questions on calls (2), independently built an internal one-pager comparing options before being asked (3), offered to loop in the skeptical Director of Sales Ops (2), motivation cites team-wide process change need (3).

Mobilizer Score = 2+3+2+3 = **10/12 — confirmed Mobilizer.**

Next enablement need (deal stage: mid-evaluation): Chen is about to present to the skeptical Director. Generate a one-page internal-facing brief Chen can present *without the rep in the room* — framed in Chen's language from the artifacts they've already produced, addressing the specific skepticism the Director is known for (cost scrutiny), not a generic product one-pager.

## Common failure patterns

- Investing the most enablement time in the most responsive/friendly contact without checking whether they're actually a Mobilizer — responsiveness to the rep and internal influence are different things.
- Scoring a contact as a Mobilizer based on stated enthusiasm ("I love this, I'll push it through") without an actual produced artifact or internal action as evidence.
- Giving a confirmed Mobilizer generic product marketing collateral instead of content shaped for their specific next internal conversation and audience.
- Missing that a Mobilizer's motivation signal (org-level change belief) is the most durable driver — a Mobilizer motivated only by personal rapport with the rep is more likely to go quiet if the rep changes territories or the relationship cools.

## Output schema

```json
{
  "contact_name": "M. Chen",
  "signal_scores": {"meeting_behavior": 2, "internal_action": 3, "risk_appetite": 2, "motivation_signal": 3},
  "mobilizer_score": 10,
  "classification": "confirmed mobilizer",
  "next_enablement_need": {"audience": "skeptical Director of Sales Ops", "content_type": "internal-facing one-pager addressing cost scrutiny", "deliver_before": "Chen's next internal presentation"}
}
```

## Recommended prompt

> You are a sales strategist applying the Challenger Sale Mobilizer test. Score the contact on 4 signals (0-3 each): meeting behavior (pushback/challenge vs. agreement), internal action (produced artifacts vs. just talk), risk appetite (brings you to skeptics vs. shields you), and motivation (org-level change belief vs. personal rapport). Sum to a 0-12 score and classify as confirmed Mobilizer (9-12), developing (5-8, suggest a specific test to confirm), or Friend/Talker (0-4, recommend finding the real Mobilizer elsewhere). For confirmed Mobilizers, specify the next enablement content needed, tailored to their next internal audience and conversation. Return JSON matching the schema above.

## Grounded in

The Challenger Sale's Mobilizer concept (Dixon & Adamson, CEB/Gartner research), which found that the most responsive, friendliest buying-committee contacts are frequently not the ones who move deals internally — used here to make "champion strength" a checkable score instead of an impression.

See [sources-and-frameworks.md](../../sources-and-frameworks.md) for the pack's general reference list.
