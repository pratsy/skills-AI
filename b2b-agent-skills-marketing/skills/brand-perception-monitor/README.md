# Brand Perception Monitor

Score brand health across the four stages of the classic brand funnel (awareness, favorability, consideration, differentiation) using signal proxies from owned/earned data, and flag which stage is actually weak — instead of reporting raw social-listening volume as if more mentions always means healthier brand.

## When to use this

- Mention volume or social engagement is up but win rate or unaided brand recall isn't moving — a sign the funnel is breaking somewhere volume metrics don't show.
- You're tracking brand health without survey budget and need to build a defensible proxy from data you already have.
- Leadership wants a brand health read before a repositioning or rebrand decision.

## Methodology

The brand funnel — awareness → favorability → consideration → differentiation — is sequential: a buyer can't be favorable toward a brand they're not aware of, can't consider a brand they're not favorable toward, and so on. Each stage needs its own signal, because aggregate "brand sentiment" collapses stages that move independently.

| Stage | Question | Proxy signal (no survey required) |
|---|---|---|
| **Awareness** | Do buyers know we exist? | branded search volume trend, direct traffic trend, share of voice vs. named competitors in category mentions |
| **Favorability** | Do they think well of us? | sentiment of mentions (positive/neutral/negative ratio), review-site rating trend (G2/Capterra), employee-advocacy reach |
| **Consideration** | Do they put us on the shortlist? | % of closed-lost deals where we were in the final 2-3 vendors considered, RFP/demo-request rate vs. category traffic |
| **Differentiation** | Do they know why we're different from alternatives? | win/loss interview theme: can the buyer articulate our differentiator unprompted, without being fed it |

## Scoring model

Score each stage 1–5 against its own proxy signal trend (not an absolute scale — trend direction and magnitude relative to your own baseline matter more than a universal benchmark):

```
1 = declining trend, below prior period
3 = flat / roughly stable
5 = improving trend, meaningfully above prior period

Funnel Health Read: find the lowest-scoring stage that is upstream of (or equal to) any higher-scoring stage below it.
A downstream stage cannot be fixed by working on messaging alone if an upstream stage is the actual bottleneck.
```

## Inputs

| Field | Type | Example |
|---|---|---|
| `branded_search_trend` | {current, prior_period} | awareness proxy |
| `share_of_voice_vs_competitors` | {current, prior_period} | awareness proxy |
| `mention_sentiment` | {positive, neutral, negative, prior_period_positive_pct} | favorability proxy |
| `review_site_rating_trend` | {current, prior_period} | favorability proxy |
| `shortlist_rate_in_closed_lost` | {current, prior_period} | consideration proxy |
| `unprompted_differentiator_recall` | {pct_of_winloss_interviews_citing_it, prior_period_pct} | differentiation proxy |

## Worked example

Awareness: branded search up 15% QoQ, share of voice up 3pts → **score 5, improving.**
Favorability: review-site rating flat at 4.2, sentiment mix unchanged → **score 3, flat.**
Consideration: shortlist rate in closed-lost deals dropped from 62% to 41% → **score 1, declining.**
Differentiation: only 20% of win/loss interviewees could name a differentiator unprompted (down from 35%) → **score 1, declining.**

Read: awareness is genuinely improving, but consideration and differentiation are both declining — and consideration is upstream of differentiation in a practical sense (you need to make the shortlist before differentiation matters in a specific deal). The brand is getting *known* but not getting *chosen* — the fix is a positioning/differentiation problem (see [`brand-positioning-synthesizer`](../brand-positioning-synthesizer/README.md)), not an awareness/reach problem, even though raw mention volume would have looked like a "brand health win" if reported alone.

## Common failure patterns

- Reporting mention volume or social engagement as the headline brand metric when it only measures the awareness stage, while consideration or differentiation is where the real problem lives.
- Treating one bad quarter of review-site rating as a trend without checking review volume — a small number of new reviews can swing an average without reflecting a real shift.
- Skipping the differentiation stage because it requires win/loss interview data instead of a dashboard pull — it's the hardest stage to proxy but often the most diagnostic.
- Scoring stages on an absolute 1-5 scale without a prior-period comparison, which can't distinguish "always been average" from "declining."

## Output schema

```json
{
  "stages": [
    {"stage": "awareness", "score": 5, "trend": "improving", "evidence": "branded search +15% QoQ, SOV +3pts"},
    {"stage": "consideration", "score": 1, "trend": "declining", "evidence": "shortlist rate in closed-lost fell from 62% to 41%"}
  ],
  "bottleneck_stage": "consideration",
  "diagnosis": "brand is gaining awareness but not converting it into shortlist inclusion or differentiation"
}
```

## Recommended prompt

> You are a brand strategist. Score each stage of the brand funnel (awareness, favorability, consideration, differentiation) 1-5 based on trend vs. the prior period for the proxy signals given (not an absolute scale). Identify the lowest-scoring upstream stage as the bottleneck, and explain why fixing a downstream stage alone (e.g. messaging/differentiation) won't help if an upstream stage (e.g. awareness) is actually the constraint, or vice versa. Return JSON matching the schema above.

## Grounded in

The classic sequential brand funnel (awareness → favorability → consideration → differentiation, related to Keller's Customer-Based Brand Equity model), scored from owned/earned data proxies so brand health tracking doesn't require survey budget, and structured to avoid collapsing independently-moving stages into one sentiment number.

See [sources-and-frameworks.md](../../sources-and-frameworks.md) for the pack's general reference list.
