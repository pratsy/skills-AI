# Lifecycle Email Optimizer

Diagnose underperforming lifecycle email programs (welcome, activation, nurture, win-back) against stage-specific benchmarks, and isolate whether the problem is deliverability, subject/open, or content/click — instead of optimizing subject lines on a program that's actually failing at a different layer.

## When to use this

- Open rates look fine but the program isn't driving the intended lifecycle outcome (activation, reactivation, expansion).
- You manage multiple lifecycle stages and need to know which one is actually underperforming, not just "email performance" in aggregate.
- Deliverability may be degrading and it's showing up as an "engagement" problem instead.

## Methodology

Every lifecycle email program sits in one of four stages, each with a different job and different benchmark ranges (use trailing internal medians once you have ≥90 days of your own data; use the ranges below as a starting point):

| Stage | Job | Typical open rate | Typical CTR | Primary success metric |
|---|---|---|---|---|
| **Welcome** (first 0-7 days) | Set expectations, drive first activation action | 50–60% | 8–12% | % completing first key action |
| **Activation** (7-30 days) | Get the user to the product's core value moment | 35–45% | 5–8% | activation rate, time-to-value |
| **Nurture/engagement** (ongoing) | Sustain usage, surface underused features | 20–30% | 2–4% | feature adoption, usage frequency |
| **Win-back** (post-churn/dormancy) | Re-activate a lapsed user or account | 12–20% | 1–3% | reactivation rate |

## Diagnostic sequence (layered — check in order)

A program can fail at any of three layers; fixing content when deliverability is broken wastes the effort:

1. **Deliverability**: is the send actually reaching the inbox? Check bounce rate (should be <2%) and spam-complaint rate (should be <0.1%). If either is elevated, everything downstream is unreliable — fix this first.
2. **Open** (subject/sender/timing): if deliverability is healthy but open rate is below the stage benchmark, the subject line, sender name, or send time is the issue — not the body content.
3. **Click/action** (content/CTA): if open rate is at or above benchmark but CTR or the stage's success metric is below benchmark, the body content, offer, or CTA is the issue.

## Inputs

| Field | Type | Example |
|---|---|---|
| `lifecycle_stage` | enum | `welcome \| activation \| nurture \| winback` |
| `send_metrics` | object | `{"sent": 5000, "bounced": 45, "spam_complaints": 3, "opened": 1400, "clicked": 210}` |
| `stage_success_metric` | object | e.g. `{"metric": "activation_rate", "value": 0.18, "benchmark": 0.30}` |
| `internal_benchmark_rates` | object (optional) | trailing internal medians per stage, if available |

## Worked example

Activation-stage email: sent 5,000, bounced 45 (0.9%, healthy), spam complaints 3 (0.06%, healthy) → **deliverability layer passes**.
Opened 1,400/4,955 delivered = 28.3% — below the 35–45% activation benchmark → **open layer fails**.
Clicked 210/1,400 opens = 15% CTR — actually *above* the 5–8% benchmark for those who did open.

Diagnosis: the content that gets opened is working well (high CTR among openers); the problem is entirely at the open layer — subject line, sender name, or send timing — not the email body. Optimizing body copy here would not move the metric that's actually broken.

## Common failure patterns

- Optimizing subject lines when deliverability is the real problem (elevated bounce/spam rates suppress opens regardless of subject quality, and can also suppress future deliverability via sender reputation).
- Comparing a win-back program's metrics to a welcome-series benchmark — the same "28% open rate" is a red flag in welcome and a fine result in win-back.
- Judging the program only on open/click rates instead of the stage's actual success metric (activation rate, reactivation rate) — high engagement with no lifecycle outcome is a content-relevance problem, not a win.
- Re-testing subject lines repeatedly on a program where CTR-among-openers is already fine, missing that the real fix is elsewhere in the funnel.

## Output schema

```json
{
  "lifecycle_stage": "activation",
  "deliverability_layer": {"bounce_rate": 0.009, "spam_rate": 0.0006, "status": "pass"},
  "open_layer": {"open_rate": 0.283, "benchmark_range": [0.35, 0.45], "status": "fail"},
  "click_layer": {"ctr_among_opens": 0.15, "benchmark_range": [0.05, 0.08], "status": "pass"},
  "diagnosis": "open-layer failure — subject/sender/timing issue, not content",
  "recommended_action": "test subject line, sender name, and send-time changes; do not revise body content yet"
}
```

## Recommended prompt

> You are a lifecycle email analyst. Given the lifecycle stage, send metrics, and stage success metric below, evaluate three layers in order: (1) deliverability — bounce rate should be under 2%, spam complaints under 0.1%; (2) open rate vs. the stage benchmark; (3) click-through rate among those who opened, vs. the stage benchmark. Identify the first layer (in that order) that fails, and state that as the diagnosis — do not recommend content changes if the failure is at the deliverability or open layer. Compare the stage success metric to its benchmark separately. Return JSON matching the schema above.

## Grounded in

Standard lifecycle email segmentation (welcome / activation / nurture / win-back) used in B2B and PLG marketing automation, combined with a layered deliverability → open → click diagnostic sequence so the fix targets the actual broken layer instead of the most commonly-tweaked one (subject lines).

See [sources-and-frameworks.md](../../sources-and-frameworks.md) for the pack's general reference list.
