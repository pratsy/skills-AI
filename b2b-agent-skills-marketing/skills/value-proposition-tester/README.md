# Value Proposition Tester

Stress-test a value proposition using Strategyzer's Value Proposition Canvas (Osterwalder et al.) — map customer jobs/pains/gains against product pain relievers/gain creators and score the fit, instead of judging copy on how it "sounds."

## When to use this

- A value prop reads well internally but doesn't move pipeline or conversion.
- You have several candidate value props (from different personas or positioning tests) and need to rank them before committing budget.
- You're validating a new offer against a segment you haven't sold to before.

## Methodology

The canvas has two halves that must be scored independently before comparing them:

**Customer profile** (from research — interviews, win/loss, support tickets, not assumptions):
- **Jobs**: what the customer is trying to get done (functional, social, emotional)
- **Pains**: what frustrates them before/during/after the job (risks, obstacles, undesired outcomes)
- **Gains**: what outcomes or benefits they want (required, expected, desired, unexpected)

**Value map** (from the product):
- **Products/services**: what you actually offer
- **Pain relievers**: how specifically each pain is alleviated
- **Gain creators**: how specifically each gain is produced

**Fit** exists only where a pain reliever or gain creator maps to a *pain or gain the customer actually ranked as significant* — a pain reliever for a pain the customer doesn't care about is not fit, it's a feature looking for a problem.

## Scoring model

For each customer pain/gain (ranked by the customer as Extreme / High / Moderate / Low), check whether a pain reliever or gain creator addresses it, and score the match:

```
Fit Score = Σ (customer_importance_weight × match_strength) / Σ (customer_importance_weight)

customer_importance_weight: Extreme=4, High=3, Moderate=2, Low=1
match_strength: Direct & specific=3, Partial/generic=1.5, No match=0
```

Score ranges 0–3. **Above 2.0** = strong fit, safe to lead with in messaging. **1.0–2.0** = partial fit, needs sharper proof or a different angle. **Below 1.0** = weak fit — the value prop is solving a problem the customer didn't rank as significant.

## Inputs

| Field | Type | Example |
|---|---|---|
| `customer_jobs` | list[string] | `["Hit quarterly forecast accurately"]` |
| `customer_pains` | list[{pain, importance}] | `[{"pain": "Spend 6+ hrs/week manually updating deal risk in spreadsheets", "importance": "Extreme"}]` |
| `customer_gains` | list[{gain, importance}] | `[{"gain": "Catch at-risk deals before they slip", "importance": "High"}]` |
| `value_prop_candidates` | list[{claim, pain_relievers, gain_creators}] | candidate messages to test |

## Worked example

Customer pain (Extreme): "Spend 6+ hrs/week manually updating deal risk in spreadsheets."
Customer gain (High): "Catch at-risk deals before they slip, not after."

Candidate value prop A: *"AI-powered sales intelligence platform."*
- Maps to the pain? No direct reliever named → match_strength 0.
- Maps to the gain? Generic "intelligence" claim, no specific mechanism → match_strength 1.5.
- Fit Score = (4×0 + 3×1.5) / (4+3) = 4.5/7 = **0.64 — weak fit.**

Candidate value prop B: *"Automatically flags at-risk deals from your CRM data, no manual spreadsheet updates."*
- Maps to the pain directly (eliminates manual updates) → match_strength 3.
- Maps to the gain directly (flags risk automatically = catches it before it slips) → match_strength 3.
- Fit Score = (4×3 + 3×3) / (4+3) = 21/7 = **3.0 — strong fit.**

B should lead top-of-funnel messaging; A should be retired or used only as a supporting line lower in the page.

## Common failure patterns

- Writing the customer profile from internal assumptions about what buyers care about instead of from interview/win-loss evidence.
- Scoring "match strength" generously because the team likes the copy — match strength should be judged by whether a skeptical customer would recognize the specific mechanism, not the sentiment.
- Testing only one value prop instead of 2–3 candidates against the same customer profile, which hides that the customer profile itself might be wrong.
- Treating a high fit score as permanent — jobs/pains/gains shift as the market matures; re-test when win rate or sales cycle length moves.

## Output schema

```json
{
  "customer_profile": {"jobs": [], "pains": [{"pain": "", "importance": "Extreme"}], "gains": []},
  "candidates_scored": [
    {"claim": "", "fit_score": 3.0, "verdict": "strong fit", "unmatched_high_importance_items": []}
  ],
  "recommended_lead_message": ""
}
```

## Recommended prompt

> You are a product marketer using Strategyzer's Value Proposition Canvas. Given the customer jobs/pains/gains (with importance ratings) and the candidate value propositions below, score each candidate's fit using: Fit Score = weighted sum of (importance × match strength) / sum of importance, where match strength is 3 for a direct specific match, 1.5 for partial/generic, 0 for none. List which high-importance pains or gains each candidate fails to address. Recommend which candidate to lead with. Return JSON matching the schema above.

## Grounded in

Strategyzer's Value Proposition Canvas (Osterwalder, Pigneur, Bernarda, Smith — *Value Proposition Design*, 2014), the standard framework for testing product-message fit against researched (not assumed) customer needs.

See [sources-and-frameworks.md](../../sources-and-frameworks.md) for the pack's general reference list.
