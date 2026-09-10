# Renewal Risk Scorer

Score renewal risk from a customer health model that weights usage trend and engagement more heavily than support-ticket volume — because ticket volume is a weak and often backwards predictor of churn (engaged customers file more tickets), while usage decline is the strongest leading indicator across published SaaS churn research.

## When to use this

- A renewal is 90+ days out and you want an early, evidence-based risk read instead of waiting for the customer to signal intent.
- CS is triaging a large book of accounts and needs to know where to spend limited proactive-outreach time.
- Leadership wants renewal risk reported with the same rigor as pipeline risk, not a subjective red/yellow/green gut call.

## Methodology

Four weighted components, calibrated so the strongest churn predictors carry the most weight — usage trend and engagement depth are consistently the strongest leading indicators in published SaaS retention research, stronger than raw support volume or even NPS in isolation:

```
Renewal Risk Score (0-100, higher = more risk) =
    0.35 x Usage Decline Score
  + 0.25 x Engagement Breadth Score (inverse - low breadth = high risk)
  + 0.20 x Stakeholder Continuity Score (inverse)
  + 0.20 x Sentiment/Support Score
```

**Usage Decline Score** (0-100): based on trailing 90-day usage trend vs. the prior 90 days. `0` = flat or growing usage, `50` = 10-25% decline, `100` = >25% decline or usage dropped to near-zero.

**Engagement Breadth Score** (0-100 risk, inverse of breadth): measures how many distinct users/seats are actively using the product, not just total usage volume — a single power-user carrying all usage is a concentration risk. `0` = broad adoption across the buying unit, `100` = single-user dependency.

**Stakeholder Continuity Score** (0-100 risk): `100` if the original champion or economic buyer has left the company or changed roles with no replacement relationship built, `0` if the original relationship is intact or a new one is already confirmed.

**Sentiment/Support Score** (0-100 risk): weighted more toward *unresolved* escalations and explicit dissatisfaction statements than raw ticket count — a customer filing many tickets that get resolved quickly is a lower risk signal than one filing few tickets that stay open or contain explicit frustration.

## Risk bands

```
70-100  Critical — proactive executive-level outreach this week
45-69   Elevated — CS outreach plan within 30 days, identify root cause
20-44   Watch — monitor, no immediate action required
0-19    Healthy
```

## Inputs

| Field | Type | Example |
|---|---|---|
| `account_id` | string | |
| `usage_trend_90d` | {current_period, prior_period} | |
| `active_users` | {count, total_licensed_seats} | |
| `champion_status` | enum | `intact \| departed_no_replacement \| departed_replaced` |
| `support_signals` | {ticket_count, unresolved_count, explicit_dissatisfaction_flag} | |

## Worked example

Account: usage down 30% over trailing 90 days vs. prior 90 days → Usage Decline Score 100. Active users: 2 of 15 licensed seats → severe concentration → Engagement Breadth Score 85. Champion departed 6 weeks ago, no replacement relationship built → Stakeholder Continuity Score 100. Support: 2 tickets, both resolved quickly, no explicit dissatisfaction → Sentiment/Support Score 15.

```
Renewal Risk = 0.35(100) + 0.25(85) + 0.20(100) + 0.20(15)
             = 35 + 21.25 + 20 + 3
             = 79.25 → Critical
```

Despite a low, unremarkable support-ticket signal (which a ticket-volume-weighted model would read as "healthy"), the combination of steep usage decline, severe seat concentration, and an unreplaced champion departure correctly flags this as Critical — the champion departure in particular means there may be no one left internally to advocate for renewal at all.

## Common failure patterns

- Weighting support ticket volume heavily, which inverts the actual signal — engaged, healthy customers often generate more tickets (they're using the product enough to hit edge cases) while quietly disengaging customers generate few.
- Missing champion/stakeholder departure because it's not captured anywhere systematic — this is one of the single strongest and most missed renewal risk signals and should be tracked explicitly, not inferred from silence.
- Scoring usage from total volume instead of trend — a large account with flat-but-low usage looks different in trend terms than one with the same absolute usage actively declining.
- Treating engagement breadth as equivalent to usage volume — one power user generating high total usage can mask that the rest of the buying unit has disengaged, which is itself a renewal risk even if the volume number looks fine.

## Output schema

```json
{
  "account_id": "acct_7734",
  "usage_decline_score": 100,
  "engagement_breadth_score": 85,
  "stakeholder_continuity_score": 100,
  "sentiment_support_score": 15,
  "renewal_risk_score": 79.25,
  "risk_band": "critical",
  "primary_driver": "champion departed 6 weeks ago with no replacement relationship, compounding a 30% usage decline",
  "recommended_action": "executive-level proactive outreach this week; prioritize rebuilding a relationship with the buying unit"
}
```

## Recommended prompt

> You are a customer success analyst scoring renewal risk. Compute: Usage Decline Score (0/50/100 for flat-or-growing/10-25% decline/>25% decline in trailing 90-day usage vs. prior 90 days), Engagement Breadth Score (0-100 risk, inverse of the share of licensed seats actively used), Stakeholder Continuity Score (100 if champion/EB departed with no replacement, 0 if intact or replaced), and Sentiment/Support Score (weighted toward unresolved tickets and explicit dissatisfaction, not raw ticket count). Combine as 0.35 x usage + 0.25 x breadth + 0.20 x continuity + 0.20 x sentiment. Assign a risk band and state the primary driver in plain language. Return JSON matching the schema above.

## Grounded in

A usage-trend and stakeholder-continuity weighted customer health scoring model, consistent with published SaaS retention research showing usage decline and engagement breadth as stronger leading churn indicators than raw support ticket volume, which alone is often a weak or inverted predictor.

See [sources-and-frameworks.md](../../sources-and-frameworks.md) for the pack's general reference list.
