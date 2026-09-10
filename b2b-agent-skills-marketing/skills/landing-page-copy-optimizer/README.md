# Landing Page Copy Optimizer

Audit a landing page against a message-match and friction checklist grounded in conversion-optimization practice, scoring each element instead of giving a general "make it punchier" review.

## When to use this

- Paid traffic converts well on the ad but drops sharply on landing — usually a message-match failure, not a traffic-quality problem.
- You're rewriting a page and want a structured pass instead of subjective copy opinions.
- Conversion rate is flat despite traffic growth and nobody can point to which page element is the blocker.

## Methodology

Two checks, run in this order — message match must pass before on-page friction is worth fixing, because no amount of on-page polish recovers a visitor who feels tricked by the ad-to-page jump:

### 1. Message match
Compare the referring ad/email/search-result copy to the landing page headline and hero. Score 0–2 per dimension:
- **Keyword/claim match**: does the headline repeat the specific claim or term that earned the click? (0 = unrelated, 1 = same general topic, 2 = same specific claim)
- **Visual continuity**: does the page's visual treatment (imagery, product screenshot) match what the ad promised? (0 = jarring mismatch, 1 = generic, 2 = direct continuation)

### 2. On-page friction checklist (score each 0–2: absent / present-but-weak / present-and-strong)
- Value proposition visible above the fold without scrolling
- Primary CTA is singular and unambiguous (not competing with 3 other equally-weighted links)
- Social proof (logo bar, named customer, or specific stat) visible above or just below the fold
- Form/action length matches the offer's perceived value (a "book a demo" form asking 12 fields for a free trial is mismatched effort)
- Objection is pre-empted near the CTA (pricing clarity, security/compliance badge, "no credit card required" — whatever the known top objection is for this offer)

## Scoring model

```
Message Match Score (0-4) = keyword_match + visual_continuity
On-Page Score (0-10) = sum of the 5 checklist items (0-2 each)

If Message Match Score < 3: fix message match first: do not proceed to on-page changes yet — the page is losing visitors before on-page elements can matter.
If Message Match Score >= 3: prioritize on-page items scoring 0 or 1, ordered: CTA clarity > value prop visibility > objection pre-empt > social proof > form length.
```

## Inputs

| Field | Type | Example |
|---|---|---|
| `referring_creative` | string | the ad headline/copy that drove the click |
| `page_headline` | string | landing page headline as currently written |
| `page_elements` | object | presence/description of CTA, social proof, form, objection-handling copy |
| `known_top_objection` | string | from sales/support, e.g. `"security/compliance concerns"` |

## Worked example

Ad: *"Cut forecast variance by 22% — see how RevOps teams do it."* Landing page headline: *"The all-in-one revenue platform."*

- Keyword/claim match: 0 (no mention of forecast variance or the 22% claim) — Message Match Score so far: 0+visual.
- Visual continuity: 1 (generic dashboard screenshot, not tied to the forecast-variance claim) → **Message Match Score = 1/4 — fails.**

Recommendation: fix the headline to carry the ad's specific claim forward (e.g., *"See how RevOps teams cut forecast variance by 22%"*) before auditing the CTA, form, or social proof — those fixes won't recover visitors who already bounced on the headline mismatch.

## Common failure patterns

- Optimizing on-page elements (CTA color, form length) before checking message match, which can improve on-page metrics slightly while missing the majority of lost visitors who bounce on the headline alone.
- Using one generic landing page for multiple ad campaigns with different claims, guaranteeing message-match failure for all but one.
- Scoring social proof present just because a logo bar exists, without checking whether the logos are relevant to the visitor's segment (an SMB visitor isn't reassured by enterprise-only logos).
- Pre-empting the wrong objection because it wasn't validated against actual sales/support data — guessing at objections instead of using the known top one.

## Output schema

```json
{
  "message_match_score": 1,
  "message_match_status": "fail - fix before on-page changes",
  "on_page_checklist": [
    {"item": "value_prop_above_fold", "score": 1, "note": "present but generic, doesn't carry the ad's specific claim"}
  ],
  "on_page_score": 0,
  "priority_fix": "headline does not match referring ad's specific claim"
}
```

## Recommended prompt

> You are a conversion optimization analyst. Compare the referring ad copy to the landing page headline and score message match (0-4: keyword/claim match 0-2 + visual continuity 0-2). If below 3, recommend the message-match fix and stop there. If 3 or above, score the on-page checklist (CTA clarity, value prop visibility, social proof, form/offer match, objection pre-empt using the known top objection) 0-2 each, and rank the weakest items in priority order: CTA clarity, value prop visibility, objection pre-empt, social proof, form length. Return JSON matching the schema above.

## Grounded in

Message-match and on-page friction auditing as practiced in conversion rate optimization (the discipline associated with CXL, Unbounce, and similar CRO practice), sequenced so ad-to-page continuity is fixed before on-page polish, since message-match failures lose the largest share of visitors before on-page elements are ever evaluated.

See [sources-and-frameworks.md](../../sources-and-frameworks.md) for the pack's general reference list.
