# Objection Response Coach

Classify an objection by type before generating a response — price, product-fit, trust/risk, timing, or competitor — using the LAER model (Listen, Acknowledge, Explore, Respond), because the same surface objection ("it's too expensive") often has a different underlying cause that requires a different response.

## When to use this

- Reps have a stock response to "it's too expensive" that works sometimes and fails other times, with no way to tell in advance which it'll be.
- You're building objection-handling enablement and want responses tied to root cause, not a generic FAQ.
- A specific deal hit an objection and the rep needs a tailored response now, not a battlecard lookup.

## Methodology

Most objection-handling failures come from responding to the *words* of the objection instead of its *type*. The same sentence ("this is too expensive") can mean at least three different things, each needing a different response:

| Underlying type | What it actually means | Wrong response | Right response direction |
|---|---|---|---|
| **Price** (real budget constraint) | Genuinely doesn't have or can't access the budget | ROI pitch | Explore phasing, smaller initial scope, or a different budget line |
| **Value gap** (disguised as price) | Doesn't yet believe the value is worth *any* price at this level | Discount | Return to Implication-stage discovery (see [`discovery-question-generator`](../discovery-question-generator/README.md)) to rebuild the cost of the status quo |
| **Trust/risk** (disguised as price) | Worried about implementation risk, not the number itself | Discount or ROI pitch | Address the risk directly (references, pilot structure, guarantees) |

The LAER sequence prevents responding before diagnosing: **Listen** fully without interrupting, **Acknowledge** without immediately defending, **Explore** with a question that reveals the underlying type, **Respond** only once the type is known.

## Decision logic

Use one diagnostic Explore question per objection category before responding:

- Surface objection sounds like price → ask: *"Help me understand — is it that the budget isn't there right now, or that you're not yet convinced it's worth this investment?"* Answer reveals Price vs. Value-gap.
- Surface objection sounds like "we're not ready" → ask what specifically needs to happen first; reveals genuine Timing vs. a soft no covering Trust/risk or a competing priority.
- Surface objection names a competitor → ask what's most appealing about the alternative; reveals whether it's a real Competitor preference or a Value-gap objection using the competitor as cover.

## Inputs

| Field | Type | Example |
|---|---|---|
| `objection_text` | string | the buyer's stated objection, as close to verbatim as possible |
| `deal_context` | object | stage, MEDDPICC evidence if available, prior discovery notes |
| `explore_answer` | string (optional) | the buyer's answer to the diagnostic Explore question, if already asked |

## Worked example

Objection: *"This is more than we budgeted for."*

Without `explore_answer`: classify as **ambiguous — could be Price or Value-gap**, and the output leads with the diagnostic question rather than a response: *"Is the budget genuinely not available this cycle, or is it more that the case for this specific investment level isn't fully there yet?"*

With `explore_answer` = *"Honestly we're not sure it's worth it at this number yet"*: classify as **Value-gap disguised as price**. Response direction: do not discount — return to quantifying the cost of the status quo established (or missed) in discovery. Suggested response: *"Fair — let's go back to the numbers. You mentioned forecast misses cost you a board conversation roughly once a quarter. What's that actually cost in credibility or time, compared to the price difference we're discussing?"*

## Common failure patterns

- Responding to "too expensive" with a discount before diagnosing type — if it's actually a Value-gap objection, a discount doesn't fix the underlying disbelief and just trains the buyer to hold out for one next time.
- Treating every "we're not ready" as genuine Timing and backing off, when it's frequently a softened Trust/risk or Value-gap objection.
- Skipping Listen/Acknowledge and moving straight to Explore, which reads as dismissive and makes buyers less willing to reveal the real underlying concern.
- Responding to a Competitor objection with feature comparison when the Explore answer reveals it's actually a Value-gap objection using the competitor's lower price as justification.

## Output schema

```json
{
  "objection_text": "This is more than we budgeted for.",
  "classification": "ambiguous - price or value-gap",
  "explore_question": "Is the budget genuinely not available this cycle, or is it more that the case for this specific investment level isn't fully there yet?",
  "response_if_price": "explore phased scope or a different budget line",
  "response_if_value_gap": "return to quantifying the cost of the status quo from discovery; do not discount"
}
```

## Recommended prompt

> You are a sales coach using the LAER model (Listen, Acknowledge, Explore, Respond). Given the objection text and deal context below, first classify the likely underlying type(s) — price, value-gap, trust/risk, timing, or competitor — noting if it's ambiguous between two types. If ambiguous and no explore_answer is provided, generate the specific diagnostic Explore question to ask before responding, rather than a generic response. If explore_answer is provided, classify definitively and generate a response matched to that specific type, not the surface wording of the objection. Return JSON matching the schema above.

## Grounded in

The LAER objection-handling model (Listen, Acknowledge, Explore, Respond) combined with a type-diagnosis step, used to prevent the common failure of responding to an objection's surface wording (e.g., "price") when the underlying cause is often value perception, trust, or timing.

See [sources-and-frameworks.md](../../sources-and-frameworks.md) for the pack's general reference list.
