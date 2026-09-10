# Ad Copy Variant Generator

Generate ad copy variants across distinct persuasion structures (PAS, AIDA, and a proof-led variant) rather than five stylistic rewrites of the same angle — and specify the test design (sample size, primary metric) needed to actually learn which angle wins.

## When to use this

- Existing ad variants all make the same argument in different words, so a "losing" test doesn't tell you anything about what angle would work better.
- You're launching a new campaign and want variants that test genuinely different hypotheses about what will move this audience.
- Past A/B tests were called before reaching statistical significance, so the team doesn't trust its own test history.

## Methodology

Generate one variant per persuasion structure, not per wording style — each structure makes a different bet about what moves this buyer:

| Structure | Pattern | Bets that the buyer responds to... |
|---|---|---|
| **PAS** (Problem-Agitate-Solve) | Name the problem → intensify why it hurts → present the fix | pain-avoidance |
| **AIDA** (Attention-Interest-Desire-Action) | Hook → build relevance → build desire → clear CTA | aspirational/gain-seeking |
| **Proof-led** | Lead with the strongest stat or named-customer result, then explain | skepticism — needs evidence before attention |

## Test design (required output, not optional)

Before running variants live, specify:

```
Minimum detectable effect (MDE): smallest CTR/CVR lift worth detecting, e.g. 20% relative lift
Required sample size per variant ≈ 16 × p × (1-p) / MDE²   (standard two-proportion z-test approximation)
  where p = baseline conversion rate
Do not call a winner before each variant reaches this sample size, regardless of interim results.
```

## Inputs

| Field | Type | Example |
|---|---|---|
| `product_value_prop` | string | core claim to build variants around |
| `target_persona` | string | who the ad targets |
| `proof_points_available` | list[string] | real stats/customer names usable in the proof-led variant |
| `baseline_conversion_rate` | float | current CTR or CVR, for sample-size calculation |
| `minimum_detectable_effect` | float | default 0.20 (20% relative lift) |

## Worked example

Product: AI deal-risk scoring tool. Persona: VP Sales. Proof point available: "40+ RevOps teams, 22% forecast variance reduction." Baseline CTR: 1.8%.

- **PAS**: *"Deals slip and nobody sees it coming until the forecast call. [Product] flags at-risk deals two weeks before your reps do. See what you're missing — free trial."*
- **AIDA**: *"What if you never got surprised by a slipped deal again? [Product] shows you exactly which deals are at risk, why, and what to do — so your forecast call has no surprises. Start free."*
- **Proof-led**: *"40+ RevOps teams cut forecast variance 22% with [Product]. See your at-risk deals in 15 minutes — no setup required."*

Sample size: MDE 20%, baseline p=0.018 → required ≈ 16 × 0.018 × 0.982 / (0.018×0.20)² ≈ 0.283 / 0.0000130 ≈ **~21,700 impressions per variant** before calling a result — flagged explicitly so the team doesn't call the test at day 3 on partial data.

## Common failure patterns

- Generating 5 variants that are all the same structure (usually all PAS) with different adjectives, which tests wording, not persuasion angle — the actual thing worth learning.
- Calling a test winner from early results before reaching the calculated sample size, which produces false positives that don't replicate at scale.
- Writing a proof-led variant with an invented or unverified statistic — only use `proof_points_available` that are real and approved.
- Testing all variants against the same audience segment when the structures may work differently by segment (proof-led often outperforms with skeptical/technical buyers, PAS with buyers in acute pain) — segment the test if budget allows.

## Output schema

```json
{
  "variants": [
    {"structure": "PAS", "copy": "...", "hypothesis": "pain-avoidance framing outperforms with this audience"},
    {"structure": "AIDA", "copy": "...", "hypothesis": "aspirational framing outperforms"},
    {"structure": "proof-led", "copy": "...", "hypothesis": "skeptical buyers need evidence before attention"}
  ],
  "test_design": {"baseline_rate": 0.018, "mde": 0.20, "required_sample_size_per_variant": 21700, "do_not_call_before": "each variant reaches required sample size"}
}
```

## Recommended prompt

> You are a B2B performance marketer. Generate three ad copy variants for the product/persona below, one each in PAS (problem-agitate-solve), AIDA (attention-interest-desire-action), and proof-led structure — using only the real proof points provided for the proof-led variant, never an invented statistic. Then calculate the required sample size per variant using required_n ≈ 16 × p × (1-p) / MDE², given the baseline conversion rate and minimum detectable effect provided, and state that the test should not be called before each variant reaches that sample size. Return JSON matching the schema above.

## Grounded in

Classic direct-response copy structures (PAS, AIDA) applied to distinct persuasion hypotheses rather than stylistic variation, paired with the standard two-proportion sample-size approximation used in A/B testing so test conclusions are statistically defensible rather than read from partial data.

See [sources-and-frameworks.md](../../sources-and-frameworks.md) for the pack's general reference list.
