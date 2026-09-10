# B2B Agent Skills for Sales, Marketing, and GTM

Curated AI skills for revenue teams that need better decisions, clearer execution, and less guesswork across the funnel.

This repo is designed for the people who actually run GTM work: sales leaders, marketing teams, RevOps leaders, founders, and operators who need practical AI support for real business work.

## Expert memory layer: the difference between generic AI and useful AI

Most AI repos are generic because they only give you a model and a prompt.

This repo is different.

This is a domain memory system for B2B revenue execution. It is designed to capture the things that real operators learn over time:

- which accounts matter and why
- which objections tend to show up in specific buying motions
- what good pipeline quality looks like in practice
- how messaging breaks down at different funnel stages
- what market signals deserve attention versus noise
- which patterns repeatedly cause missed forecast, stalled deals, or weak conversion

In other words, this is not just a library of prompts. It is a structured way to encode business judgment, field experience, and source-backed operating patterns into repeatable AI workflows.

That is the real value. Generic AI generates text. Expert memory produces decision support.

## Who this is for

This repo is built for:

- sales leaders and account teams
- marketing and lifecycle teams
- RevOps and forecasting teams
- GTM operators and founders
- technical teams building AI workflows around real business tasks

## 5-minute quick start

If you want to understand the value fast, start here:

1. Pick the business problem you already have.
   - weak pipeline quality
   - poor account prioritization
   - unclear messaging
   - weak conversion or high drop-off
   - risk or forecast uncertainty

2. Go to the skill pack that matches the problem.
   - sales
   - marketing
   - RevOps
   - GTM

3. Open the README for that skill and read the purpose, inputs, output, and example result.

4. Use the plain-English prompts in `docs/prompt-packs.md` to test the idea quickly.

5. Turn the result into a clear next action for your team, not just a model output.

## The business problems this solves

Most GTM teams are not short on activity. They are short on clarity.

This repo helps teams solve the problems that usually slow revenue execution down:

- too many accounts with no clear prioritization
- weak pipeline disguised as full pipeline
- campaign activity without conversion clarity
- unclear marketing positioning and buyer messaging
- late-stage deal risk that could have been spotted earlier
- no consistent way to interpret market or competitor signals
- too much operational noise and not enough practical action

## The value in one sentence

Instead of generic AI output, this gives teams structured playbooks for the business work that matters most in B2B sales and marketing.

## Workflow examples people immediately understand

### Example 1: sales prioritization
A sales leader wants to know which accounts deserve attention this week.

Result: use a prioritization skill to rank accounts by value, urgency, fit, and likely conversion quality.

### Example 2: pipeline quality review
A RevOps lead wants to know why the pipeline feels weak despite high volume.

Result: use pipeline health and forecast bias skills to identify stage bottlenecks, weak qualification, and forecast risk early.

### Example 3: content and conversion diagnosis
A marketing leader sees traffic but weak conversion and unclear messaging.

Result: use content gap analysis and friction audit skills to find where buyer interest drops and what content or messaging is missing.

### Example 4: market and competitor monitoring
A GTM leader wants to see whether market change or competitor movement is becoming important.

Result: use market shift and competitor signal skills to cluster noisy signals into real strategic implications and recommended response actions.

### Example 5: executive deal readiness
A team is preparing for a high-stakes customer conversation and does not know which objections or stakeholder themes matter most.

Result: use executive briefing, committee readiness, and champion strategy skills to prepare better before the conversation starts.

## Why this matters

Most AI tools are generic. Most teams do not need another chat assistant.

They need practical, repeatable playbooks for business work that happens every day:

- prioritizing accounts worth pursuing
- improving pipeline quality
- reducing stalled deals
- clarifying messaging and positioning
- diagnosing campaign bottlenecks
- identifying forecast risk earlier
- shortening the gap between signal and action

This library is built for that real work.

## How this fits into a real workflow

This repo is not meant to replace business judgment. It is meant to make business judgment faster and more structured.

Typical usage pattern:

1. Identify the GTM problem
   - weak pipeline quality
   - unclear messaging
   - low account prioritization confidence
   - stalled renewals
   - lack of executive alignment

2. Feed in relevant context
   - account data
   - sales notes
   - CRM signals
   - campaign performance
   - customer or market feedback

3. Run a skill
   - prioritize account list
   - assess risk
   - analyze signal quality
   - evaluate campaign or messaging gaps

4. Review the output with business context
   - compare against actual experience
   - choose actions that are realistic and operationally feasible

5. Improve the workflow
   - faster qualification
   - better strategy conversations
   - less guesswork at leadership reviews
   - cleaner handoffs between teams

## When to use it

Use these skills in the moments when the business is already doing the work but needs better signal or clarity.

Good moments to use this repo:
- before a quarterly pipeline review
- during renewal risk assessment
- when preparing for a major deal review
- when messaging feels vague or inconsistent
- when campaign performance looks weak but the root cause is unclear
- when GTM teams disagree on which accounts matter most
- when competitor pressure or market change is creating confusion

## What improvements it creates in day-to-day work

This repo helps teams improve workflow quality in practical ways:

- better prioritization of account attention
- stronger discovery and qualification depth
- clearer sales messaging and objection handling
- better understanding of pipeline bottlenecks
- earlier detection of renewal or risk issues
- more structured GTM planning and execution
- less time wasted on low-value accounts or low-quality campaigns
- better alignment between teams using the same operating signals

## Real value in plain English

This is valuable when a team wants to move from intuition to structured decision support.

Examples:
- Instead of guessing which accounts deserve attention, use a prioritization skill.
- Instead of reacting to weak campaign performance, use a content or funnel diagnostics skill.
- Instead of relying on gut feeling for forecast risk, use a RevOps quality and bias analysis skill.
- Instead of generic competitor updates, use a signal clustering approach to identify business-relevant shifts.

## What makes this competitive

This repo is competitive because it is not just a prompt library. It is a structured operating library for B2B revenue work.

It stands apart by combining:
- business use cases
- clear skill structure
- workflow-oriented design
- source-backed references
- real GTM and revenue context
- examples that look like actual operating tasks, not toy demos
- expert memory patterns that encode operator learning and decision context

It is most competitive for teams that want AI to support execution, not just generate content.

## What this is not

This is not:
- a raw prompt dump
- a generic productivity assistant
- a technical-only engineering repo
- a fake business framework with no operational structure

This is a practical library for revenue and GTM teams who want more usable, repeatable AI support built around real business motions.

## Repo map

- `b2b-agent-skills-sales` — sales execution, deal strategy, and commercial workflows
- `b2b-agent-skills-marketing` — messaging, lifecycle, campaign, and audience optimization
- `b2b-agent-skills-revops` — pipeline health, forecasting, and operational clarity
- `b2b-agent-skills-gtm` — strategic planning, market intelligence, and account prioritization
- `skills_ai/` — runtime engine for using the skills programmatically
- `examples/` — quick runnable examples and app patterns
- `memory/` — operational memory model, skill schema, and domain quality checklist

## Quick start for non-technical users

You do not need to understand the code to see the value.

Start with the skill packs that match your immediate workflow:

- Sales leader: lead prioritization, deal risk, committee readiness
- Marketing leader: content gap analysis, brand perception, journey friction
- RevOps leader: pipeline health, forecast bias, attribution quality
- GTM leader: market shift monitor, competitor signal clustering, account priority matrices

Read the skill README, identify the business problem, and use the output as a decision aid.

## Roadmap

Planned expansion areas for the public repo:

- deeper B2B sales playbooks for discovery, objection handling, and enterprise deal strategy
- stronger RevOps coverage for forecasting discipline, handoff quality, and pipeline governance
- expanded GTM market intelligence skills for competitor monitoring and strategic prioritization
- more evaluation examples and benchmark-ready outputs for real-world usage
- stronger contributor and citation patterns to keep the library source-backed and trustable

## Recently expanded skill additions

New additions in the public library include:

- `Competitive Differentiation Coach` — sales-facing differentiation and objection support
- `Content Gap Analysis Agent` — marketing messaging and funnel coverage analysis
- `Pipeline Health Audit Agent` — RevOps-focused pipeline quality and forecast risk analysis
- `Account Priority Matrix Builder` — GTM prioritization and strategic account planning
- `Market Shift Monitor` — category and competitor monitoring for enterprise GTM teams
- `Multi-threading Plan Builder` — enterprise stakeholder coverage and deal progression strategy
- `Champion Advocacy Builder` — converting stakeholder enthusiasm into buying momentum
- `Deal Committee Readiness Coach` — executive meeting prep and buying-group strategy
- `Brand Perception Monitor` — market signal tracking for brand and messaging quality
- `Customer Journey Friction Audit` — funnel and lifecycle optimization analysis
- `Forecast Bias Detector` — bias review for pipeline quality and forecast confidence
- `Competitor Signal Clusterer` — strategic grouping of competitive movement and message themes

These additions reinforce the repo’s aim: source-backed, operational AI skills that are useful in real B2B sales and marketing execution.

## Memory architecture

This repo is designed around an expert memory system for B2B revenue work.

Each skill is expected to include business context, decision logic, failure patterns, and source-backed references so the output is useful in a real operating environment.

Key files:

- `memory/README.md` — memory model and design logic
- `memory/skill-memory-template.yaml` — reusable skill memory schema
- `memory/domain-memory-checklist.md` — checklist for keeping the repo from becoming generic

This is the part that separates real domain intelligence from a basic prompt library.

## Notes

This is a curated operating library for B2B revenue teams, grounded in public industry practice and structured for real-world workflow use.

## 3-minute repo summary

If you run a B2B revenue motion, this repo gives you a practical toolkit for making better decisions with less guesswork.

Use it to:
- prioritize the right accounts
- reduce stalled deals
- improve pipeline quality
- sharpen marketing messaging
- diagnose campaign and funnel issues
- detect forecast and renewal risk earlier
- turn noisy data into clear action plans

This is not a generic AI playground. It is a business-use library built for the people running GTM work every day.

## Role-based workflow map

Use the right skill for the right operational question.

- Sales leader: account prioritization, deal risk, multi-threading, committee readiness
- Marketing leader: content gap analysis, brand perception, journey friction, messaging clarity
- RevOps leader: pipeline health, forecast bias, handoff quality, operational risk review
- GTM operator: market shift monitoring, competitor signal clustering, strategic account planning
- Founder: strategic prioritization, executive summary, cross-functional GTM alignment

## Prompt packs

This repo includes plain-English prompt patterns for common business scenarios.

- `docs/prompt-packs.md` — role-specific business prompts
- `docs/business-use-cases.md` — practical examples by function
- `docs/skill-usage.md` — technical setup and execution guide

## Why this works for real users

People do not buy a repo because it has code. They buy a repo because it helps them solve a business problem.

This library is designed to turn operational GTM questions into structured, decision-friendly outputs that teams can actually use in meetings, planning, reviews, and daily execution.

## Use cases by role

### Sales leader
- improve account prioritization
- reduce weak pipeline and wasted effort
- strengthen coaching and discovery quality
- improve executive readiness and deal momentum

### Marketing leader
- diagnose funnel drop-off and content gaps
- refine positioning and messaging
- improve conversion quality with fewer wasted campaigns
- align brand perception with buyer reality

### RevOps leader
- improve pipeline health visibility
- reduce forecast bias and improve forecast confidence
- surface stage-level bottlenecks and operational gaps
- create cleaner operating rhythm for reviews and planning

### Founder or GTM operator
- align teams around shared GTM signals
- prioritize the right accounts and motions
- monitor market and competitor shifts faster
- turn strategic intent into repeatable operational action

### Technical builder
- turn business workflows into structured agent patterns
- build AI flows around real operating tasks
- integrate AI into CRM, sales, and growth workflows with clearer context

## Before and after workflow

### Before
- teams rely on intuition, scattered notes, and late-stage surprises
- account attention is spread too thin
- pipeline review is noisy and inconsistent
- messaging and content are vague or misaligned
- competitor shifts are noticed too late

### After
- teams work from structured decision support
- account prioritization becomes more targeted and repeatable
- deal risk and pipeline quality are reviewed with more clarity
- marketing and sales use clearer signals and fewer blind spots
- GTM decisions become easier to defend and operationalize

## Why this feels usable to real people

The value is immediate when a person sees a business problem they already have:

- “We are spending time on the wrong accounts.”
- “Our pipeline looks full but is not converting.”
- “Our messaging is not landing consistently.”
- “We do not know which deals are actually risky.”
- “We are reacting to market shifts too late.”

This repo gives people a structured way to work through those problems.

## Copy-paste business examples

These are plain-English prompts anyone in a revenue team can understand and use immediately.

### Sales priority prompt

> Review the list of accounts below and rank them by strategic priority, buying urgency, fit, and likely commercial value. For each account, explain why it deserves attention now or later and suggest the next best sales action.

### Marketing diagnosis prompt

> Analyze the campaign, funnel, and audience data below. Identify the most likely bottlenecks in the customer journey, the content or message gaps creating friction, and the highest-priority opportunities to improve conversion.

### Pipeline risk prompt

> Review the current pipeline data and identify stage health issues, forecast risk, and likely sources of bias. Highlight which deals are likely overstated, which segments are underperforming, and what operational changes would improve forecast quality.

### Market intelligence prompt

> Review the market, competitor, and customer signal data below. Identify the strongest market shifts, the most important competitor themes, and the business implications for our GTM positioning and account strategy.

### Founder alignment prompt

> Summarize the recent sales, marketing, and market signal data and identify the top business issues, the highest-value opportunities, and the actions that should be prioritized in the next 30 days.

## Why people should use this repo

You should use this repo if your team has to make better decisions with less guesswork across the revenue engine.

If your challenge is one of these, this is for you:
- too much pipeline, not enough clarity
- campaigns are active but conversion is weak
- sales is working hard but not focusing on the right deals
- messaging is inconsistent across the funnel
- forecast accuracy is unreliable
- competitor shifts are happening faster than the team can react

This repo helps convert messy operational signals into clearer next steps.

## Quick link

- Business use cases: `docs/business-use-cases.md`
- Skill usage guide: `docs/skill-usage.md`
