# Nurture Sequence Architect

Design a lead nurture sequence mapped to lifecycle stage and lead-score decay, with explicit exit criteria per step — instead of a generic "5-email drip" template that runs the same way regardless of engagement.

## When to use this

- Nurture emails run on a fixed schedule regardless of whether the lead is engaging, and open/click rates decline steadily through the sequence with no branching logic to catch it.
- Leads are scored once at entry and never re-evaluated as they move through nurture.
- You're building nurture for a new segment or offer and need a structure, not just subject-line ideas.

## Methodology

Two things happen in parallel and must both be designed for: content mapped to buying-journey stage (see [`content-gap-analysis-agent`](../content-gap-analysis-agent/README.md) for the stage model), and **lead score decay** — engagement signals lose predictive value over time, so the sequence must re-qualify, not just deliver content on a timer.

```
Decayed Lead Score = Base Score × decay_factor(days_since_last_engagement)

decay_factor:
  0-14 days   → 1.0
  15-30 days  → 0.7
  31-60 days  → 0.4
  60+ days    → 0.15  (route to a separate re-engagement track, not standard nurture)
```

## Sequence design rules

1. **Entry criteria**: what lead score/behavior qualifies someone to enter this track (e.g., downloaded a mid-funnel asset but hasn't requested a demo).
2. **Step cadence**: space steps by engagement, not a fixed calendar — an engaged lead (opened + clicked last 2 sends) can receive the next step sooner than a cold one.
3. **Exit criteria per step** — every step needs an explicit "graduate" condition (e.g., clicked a bottom-funnel CTA → route to sales) and a "suppress" condition (e.g., no opens in 3 consecutive sends → move to re-engagement track, stop standard cadence).
4. **Content stage match**: early steps = problem-aware content, later steps = vendor-aware content, matching the recipient's demonstrated engagement level, not just time elapsed.

## Inputs

| Field | Type | Example |
|---|---|---|
| `entry_segment` | string | `"downloaded buyer's guide, no demo request"` |
| `available_content` | list[{title, stage, format}] | content inventory tagged by funnel stage |
| `lead_score_at_entry` | int | `62` |
| `engagement_history` | list[{step, opened, clicked, date}] | per-lead send history, for the decay calculation |

## Worked example

Entry: lead scored 62 after downloading a buyer's guide (solution-aware). Sequence:

| Step | Day | Content stage | Cadence rule | Exit: graduate | Exit: suppress |
|---|---|---|---|---|---|
| 1 | 0 | Solution-aware (comparison guide) | immediate | clicked pricing page → route to sales | n/a (first send) |
| 2 | 4 if engaged / 7 if not | Solution-aware (customer story) | shortens if step 1 opened+clicked | requested demo → route to sales | no open on step 1 → hold, resend step 1 subject line variant |
| 3 | 10 | Vendor-aware (case study w/ ROI numbers) | only sent if step 2 opened | replied or clicked CTA → route to sales | no opens in steps 1-2 → move to re-engagement track |
| 4 | 18 | Vendor-aware (comparison/objection-handling) | only sent if decayed score ≥ 0.7 × entry score | any click → route to sales | decayed score < 0.4 → move to re-engagement track |

A lead who opens and clicks steps 1–2 reaches step 4 with a still-high decayed score and vendor-aware content by day 18. A lead who never opens step 1 is diverted to re-engagement by day 7 instead of continuing to receive four more irrelevant sends.

## Common failure patterns

- Building the sequence entirely on a fixed day-based calendar with no branch logic, so disengaged leads keep receiving sends that just train them to ignore the sender.
- Using the entry lead score for the entire sequence instead of recalculating decay at each step — a lead who goes cold after step 1 shouldn't receive vendor-aware, late-stage content at step 4.
- Sending vendor-aware content (case studies, ROI proof) too early, before engagement confirms the lead has moved past problem-awareness.
- No defined re-engagement track — leads that go cold just fall off with no plan, instead of being moved to a lower-frequency, different-angle track.

## Output schema

```json
{
  "sequence_name": "solution-aware nurture - buyer's guide entry",
  "steps": [
    {"step": 1, "day": 0, "content_stage": "solution-aware", "asset": "comparison guide", "graduate_condition": "clicked pricing page", "suppress_condition": "n/a"}
  ],
  "reengagement_track_trigger": "decayed_score < 0.4 or 3 consecutive no-opens"
}
```

## Recommended prompt

> You are a lifecycle marketer. Design a nurture sequence for the entry segment and available content below. For each step, specify: day/cadence rule (adjust based on prior-step engagement), which content-stage asset to send, an explicit graduate condition (route to sales), and an explicit suppress condition (move to re-engagement track). Apply lead score decay: full weight 0-14 days since last engagement, 0.7x at 15-30 days, 0.4x at 31-60 days, 0.15x beyond — route anyone below 0.4x to re-engagement instead of continuing standard cadence. Return JSON matching the schema above.

## Grounded in

Lifecycle-stage nurture design combined with engagement-based lead-score decay, standard practice in B2B marketing automation (Marketo/HubSpot-style lifecycle programs) for keeping nurture content matched to demonstrated buyer engagement rather than elapsed time alone.

See [sources-and-frameworks.md](../../sources-and-frameworks.md) for the pack's general reference list.
