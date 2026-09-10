# Skill usage guide

This guide is written for people who want to see the real business value quickly, not just the technical implementation.

## What problem this solves

This repo helps B2B teams improve the quality of decisions and execution across the funnel. It reduces guesswork in areas like:

- account prioritization
- customer qualification
- pipeline risk review
- forecast confidence
- messaging quality
- campaign performance diagnosis
- competitor signal interpretation

## Who should use it

### Sales leaders
Use this when you want to improve deal quality, increase focus, and reduce low-quality pipeline.

### Marketing leaders
Use this when you want better targeting, cleaner messaging, and clearer funnel diagnostics.

### RevOps teams
Use this when you want more predictable pipeline review quality, earlier risk detection, and stronger operational discipline.

### GTM and executive teams
Use this when you want faster decision support across account strategy, messaging, and market shifts.

### Technical builders
Use this when you want a structured skill library to power internal workflows, prompt-based tools, or automation stacks.

## When to use it

These skills are most valuable in the middle of real GTM work, not only in planning sessions.

Use them when:
- a deal is stalling and the team needs a clearer diagnosis
- campaign performance needs a deeper explanation
- sales and marketing are disagreeing on account quality
- a renewal or forecast risk appears to be forming
- competitor or category changes need structured interpretation
- executive teams need a sharper account or market lens

## How it improves a workflow

### Before
- decisions are based on intuition or fragmented signals
- sales and marketing operate on different account views
- pipeline review depends on manual interpretation
- competitor updates are anecdotal
- risk shows up late

### After
- decisions are guided by structured signals
- account and strategy work becomes more focused
- stage bottlenecks and business risks are easier to spot
- teams can align around the same summary and action plan
- leaders spend less time chasing noisy or weak signals

## Example real use cases

### Sales leader
"We need to know which accounts deserve immediate attention this week."

Use: lead prioritization, account priority matrix, multi-threading plan builder.

### Marketing manager
"Our campaign is getting traffic but conversion is weak and messaging is inconsistent."

Use: content gap analysis, customer journey friction audit, brand perception monitor.

### RevOps analyst
"Forecast confidence is falling and pipeline quality feels inconsistent."

Use: pipeline health audit, forecast bias detector, sales handoff quality skills.

### GTM strategist
"We need to understand where the market is shifting and what our competitors are doing." 

Use: market shift monitor, competitor signal clusterer, account intelligence skills.

## Quick value statement

This repo helps teams convert messy, scattered GTM signals into structured business actions. That is the practical value.

## Business-first summary

This is a practical library for revenue teams that want structured AI support for daily GTM work.

It helps with real operational questions such as:
- which accounts deserve attention first
- which deals are most at risk
- where messaging or funnel friction is occurring
- whether forecast confidence is being inflated or understated
- which competitor or market signals are actually important

The goal is not to generate generic content. The goal is to improve decisions and execution quality in the flow of real work.

## Local usage

Run a skill with a JSON input file:

```bash
PYTHONPATH=. python -m skills_ai.runner renewal_risk_scorer --input examples/fixtures/renewal_input.json
```

Run from the CLI wrapper:

```bash
./bin/skills-ai renewal_risk_scorer --input examples/fixtures/renewal_input.json
```

## Example output shape

### Renewal Risk Scorer

```json
{
  "skill": "renewal-risk-scorer",
  "result": {
    "risk_score": 7,
    "top_drivers": ["usage_decline", "exec_change"],
    "recommended_actions": ["exec_review", "resolve_issue"]
  }
}
```

### Executive Sponsor Identifier

```json
{
  "skill": "executive-sponsor-identifier",
  "result": {
    "executive_sponsor": "Thomas O'Brien",
    "buying_committee": ["CFO", "CTO", "VP Analytics"],
    "engagement_plan": ["Executive briefing", "Technical proof"]
  }
}
```

## API integration

Use the FastAPI example:

```bash
uvicorn examples.webhook_app:app --reload
```

Request body:

```json
{
  "skill": "renewal_risk_scorer",
  "payload": {
    "Account Name": "CloudOps",
    "Renewal Date": "2026-11-15"
  }
}
```

## Quality bar

Good outputs should be:
- grounded in the business context
- specific and actionable
- aligned to the operating reality of the team
- usable in a human decision process, not just a model output dump

## Important notes

- Add `OPENAI_API_KEY` to `.env` or GitHub Secrets before using the OpenAI provider.
- Use the mock provider for tests and local validation.
- Remove or redact sensitive identifiers before sending data to an LLM provider.
