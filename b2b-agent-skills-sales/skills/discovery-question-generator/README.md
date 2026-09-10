# Discovery Question Generator

Generate a discovery flow using the SPIN sequence (Situation → Problem → Implication → Need-payoff) — the framework built specifically to move a buyer from acknowledging a problem to feeling its cost, which is what creates urgency, rather than a flat list of open-ended questions.

## When to use this

- Discovery calls surface a problem but never build enough urgency for the buyer to prioritize solving it now.
- Reps ask good rapport-building questions but the call doesn't progress toward a business case.
- You're prepping for a first call with a specific persona and want questions sequenced, not just a topic list.

## Methodology

SPIN's core insight: buyers don't act on problems, they act on the *implications* of problems once those implications are made explicit — a Situation or Problem question alone rarely creates urgency by itself.

| Stage | Purpose | Example shape |
|---|---|---|
| **Situation** | Establish facts (use sparingly — over-asking Situation questions reads as an unprepared rep) | "How does your team currently track deal risk?" |
| **Problem** | Surface a difficulty, dissatisfaction, or gap | "Where does that process break down?" |
| **Implication** | Make the *cost* of the problem explicit — this is the stage most discovery calls skip | "When a deal risk gets missed, what happens to the forecast call?" |
| **Need-payoff** | Get the buyer to state the value of solving it, in their own words | "If you could see that risk two weeks earlier, what would that change?" |

## Sequencing rule

Never ask more than 1-2 Situation questions before moving to Problem — Situation questions should use information already available from research (firmographic, job postings, public data) as a starting point, not rediscover it live. The call should reach at least one Implication question before the midpoint, because Implication is what converts a stated problem into a business case; a call that stays in Situation/Problem the whole time produces information but not urgency.

## Inputs

| Field | Type | Example |
|---|---|---|
| `persona` | string | `"VP Sales, mid-market SaaS"` |
| `known_context` | list[string] | facts already known from research, to skip redundant Situation questions |
| `hypothesis_problem` | string | the problem you believe this persona likely has, to focus the Problem/Implication questions |
| `call_length_minutes` | int | used to calibrate how many questions per stage fit |

## Worked example

Persona: VP Sales, mid-market SaaS. Known context: company grew reps 40% YoY (from research — skip asking about headcount). Hypothesis: forecast accuracy is straining as the team scales.

- **Situation** (1 question, using known context to seed it): "You've grown the team significantly this year — how has that changed the way you review pipeline?"
- **Problem**: "Where do you feel the most uncertainty in your forecast today?"
- **Implication** (the critical stage): "When a deal you forecasted as Commit slips, what's the ripple effect — board conversation, hiring plan, next quarter's number?"
- **Implication** (deepen it): "How often has that happened in the last two quarters?"
- **Need-payoff**: "If you had reliable visibility into deal risk two weeks before the forecast call, what would that let you do differently?"

The two Implication questions do the real work — they convert "our forecast is sometimes off" into a quantified, felt cost (board conversations, hiring plan risk) before the rep says anything about the product.

## Common failure patterns

- Asking 4-5 Situation questions before reaching Problem, which burns call time on facts often available from research and signals an unprepared rep.
- Skipping Implication entirely and jumping from Problem straight to pitching the solution — this is the single most common discovery failure and the reason "good discovery calls" still produce low urgency.
- Asking Implication questions but accepting a vague answer ("yeah it's annoying") without a follow-up that quantifies it (frequency, dollar impact, who else is affected).
- Writing Need-payoff questions that describe the product's features instead of asking the buyer to state the value themselves — the buyer's own words carry more weight later in the deal than the rep's.

## Output schema

```json
{
  "persona": "VP Sales, mid-market SaaS",
  "sequence": [
    {"stage": "situation", "question": "...", "purpose": "seed context from known research, not rediscover it"},
    {"stage": "problem", "question": "..."},
    {"stage": "implication", "question": "...", "purpose": "quantify the cost - this is the critical stage"},
    {"stage": "need_payoff", "question": "..."}
  ],
  "coaching_note": "ensure at least one implication question lands before the call midpoint"
}
```

## Recommended prompt

> You are a B2B sales strategist using the SPIN framework. Given the persona, known context, and hypothesis problem below, generate a discovery sequence: 1 Situation question that uses the known context (don't rediscover known facts), 1-2 Problem questions, 2 Implication questions that push for quantified cost/impact (not just acknowledgment), and 1 Need-payoff question that asks the buyer to state the value in their own words. Flag if the sequence risks front-loading too many Situation questions. Return JSON matching the schema above.

## Grounded in

SPIN Selling (Neil Rackham, based on research across 35,000+ sales calls), the foundational framework for B2B discovery sequencing — chosen because it explains *why* many discovery calls produce information without urgency (skipping the Implication stage) rather than just listing question categories.

See [sources-and-frameworks.md](../../sources-and-frameworks.md) for the pack's general reference list.
