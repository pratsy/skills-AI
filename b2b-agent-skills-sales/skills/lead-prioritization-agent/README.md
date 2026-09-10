# Lead Prioritization Agent

## Why this skill exists

Most sales teams do not have a prioritization problem. They have a focus problem.

They are doing too much at once, chasing weak-fit accounts, and treating activity as a substitute for buying signal. This skill helps reduce that noise.

It is designed to rank accounts by the combination of:

- fit with the target buyer profile
- urgency and buying signal strength
- commercial value and strategic importance
- likelihood of conversion in the current motion
- risk of wasting time on low-quality opportunities

This is not a generic lead score. It is a practical decision aid for sales teams that need to decide where attention should go today.

## Expert memory layer

A strong prioritization model should learn from the patterns that matter in real sales execution:

- which accounts consistently convert when they show early buying urgency
- which segments look promising but stall because the buying process is too complex
- which signals indicate real intent versus noise
- which accounts are attractive on paper but weak in execution reality

This skill encodes those patterns into a simpler, more useful output: a ranked list, clear rationale, and a recommended next action.

## Business objective

This skill helps a sales team answer a very practical question:

> Which accounts deserve real attention this week, and which should be deprioritized or nurtured?

## Inputs

- CRM records and opportunity context
- company firmographics and segment fit
- buyer engagement and intent signals
- past conversion or win patterns
- stage progression and deal momentum
- account-level strategic value

## What good output looks like

The output should not just say “high, medium, low.” It should explain:

- why the account matters now
- which buying signals are strongest
- what risk or friction is likely
- what action should happen next

## Decision logic

Use the following logic when ranking accounts:

1. Fit: Does this account match the target profile?
2. Urgency: Is the buyer showing actual movement or just passive interest?
3. Value: Is this deal strategically or commercially meaningful?
4. Execution risk: Is this account likely to stall, delay, or require heavy internal effort?
5. Conversion quality: Is this opportunity likely to convert with the current motion?

Accounts with strong fit, clear urgency, and manageable execution risk should rise to the top.

## Common failure patterns

This skill should explicitly guard against weak reasoning such as:

- over-prioritizing large logos with poor fit
- treating high activity as equivalent to buying intent
- ignoring stakeholder complexity and multi-threading needs
- prioritizing account size over conversion realism
- using static scorecards without business context

## Outputs

A useful output should include:

- ranked account list
- score or priority band
- explanation of fit and urgency
- likely conversion quality
- risk flags
- next-best action for the rep or manager

## Example result

### Priority 1: Account A
- Fit: very strong
- Urgency: high
- Buying signal: active stakeholder engagement and positive buying motion
- Value: strategic and commercially meaningful
- Risk: low-to-medium due to evaluation complexity
- Recommendation: book executive review and push multi-threading plan

### Priority 2: Account B
- Fit: moderate
- Urgency: medium
- Buying signal: consistent but not urgent
- Value: medium
- Risk: moderate because internal alignment remains unclear
- Recommendation: nurture with targeted next-step sequence and continue qualification

### Priority 3: Account C
- Fit: weak
- Urgency: low
- Value: low
- Risk: strong mismatch with current ICP
- Recommendation: deprioritize or move to long-tail nurturing

## Recommended prompt

Use a prompt like this:

> You are a senior B2B sales strategist. Review the accounts below and rank them by commercial value, fit, urgency, and likely conversion quality. Focus on where sales attention should go this week. For each account, explain the decision using real sales logic, call out early risk signals, and recommend the next best action for the rep or team.

## Source basis

This skill is grounded in public B2B sales and revenue practices, including:

- sales qualification logic familiar in MEDDIC and related enterprise buying frameworks
- ICP and segment fit practices used in sales planning and territory design
- deal-quality thinking from public revenue operations and sales enablement guidance
- prioritization models used in account planning and enterprise pipeline reviews

## References

- Salesforce Blog
- Gong Blog
- HubSpot Sales Blog
- Gartner sales and revenue research
- Forrester B2B sales research
- McKinsey Growth & Sales

## Why this is different from a generic prompt

This is not just a generic “rank these leads” prompt.

It is built to reflect how experienced sales teams think:

- not all activity is buying intent
- not every large account deserves equal attention
- not every weak-fit company is worth chasing
- the best output combines fit, urgency, and execution reality

That is the expert memory that makes this skill useful.
