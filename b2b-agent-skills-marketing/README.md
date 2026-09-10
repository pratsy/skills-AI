# B2B Agent Skills — Marketing

Open-source AI playbooks for B2B marketing strategy, messaging, campaign optimization, and demand generation.

## Coverage

- ICP refinement
- messaging clarity
- campaign performance diagnosis
- ABM prioritization
- lifecycle optimization
- content gap analysis
- audience targeting

## Featured skills

- icp-refinement-agent
- messaging-clarity-auditor
- campaign-performance-diagnostician
- abm-account-priority-ranker
- value-proposition-tester
- brand-positioning-synthesizer
- audience-segmentation-optimizer
- nurture-sequence-architect
- content-gap-analysis-agent
- brand-perception-monitor
- customer-journey-friction-audit
- persona-insight-extractor
- landing-page-copy-optimizer
- lifecycle-email-optimizer
- ad-copy-variant-generator

## Standard skill format

Every skill in this library follows the same operational structure — see [`memory/skill-template.md`](../memory/skill-template.md):

- when to use it, in concrete situations
- the named methodology it operationalizes (see below)
- an explicit scoring model or decision rubric, not a narrative description
- an input schema and a fully worked example with real numbers
- an output JSON schema so the skill can be wired into a pipeline, not just pasted as a prompt

## Named methodologies used in this pack

Rather than one generic "informed by industry practice" claim per skill, each skill names the specific method it's built on:

- **April Dunford's competitive-alternatives framework** (*Obviously Awesome*) — `brand-positioning-synthesizer`
- **Strategyzer's Value Proposition Canvas** — `value-proposition-tester`
- **Firmographic/technographic/engagement/intent ABM segmentation model** — `audience-segmentation-optimizer`
- **ITSMA ABM tiering model** (1:1 / 1:few / 1:many) — `abm-account-priority-ranker`
- **Look-alike / attribute-lift analysis** against closed-won data — `icp-refinement-agent`
- **Specificity/differentiation/proof/jargon clarity rubric** — `messaging-clarity-auditor`
- **Standard B2B demand funnel with stage-conversion benchmarking** — `campaign-performance-diagnostician`
- **Problem-aware/solution-aware/vendor-aware content coverage matrix** — `content-gap-analysis-agent`
- **Effort × drop-off × downstream-value friction scoring** — `customer-journey-friction-audit`
- **JTBD interview method** — `persona-insight-extractor`
- **Lifecycle nurture design with engagement-based lead-score decay** — `nurture-sequence-architect`
- **Deliverability → open → click layered diagnostic** — `lifecycle-email-optimizer`
- **Message-match and on-page friction auditing** (CRO practice) — `landing-page-copy-optimizer`
- **PAS/AIDA/proof-led persuasion structures with A/B sample-size design** — `ad-copy-variant-generator`
- **Sequential brand funnel** (awareness → favorability → consideration → differentiation) — `brand-perception-monitor`

See [sources-and-frameworks.md](sources-and-frameworks.md) for the pack's general reference list.

## Research basis

This repo is also informed by public B2B marketing strategy, ICP design, positioning, campaign optimization, and ABM resources used by growth and demand generation teams, as general background.

## Public source base

- HubSpot Blog — https://blog.hubspot.com/
- Demandbase Blog — https://www.demandbase.com/blog/
- 6sense Blog — https://6sense.com/blog
- Bombora Insights — https://bombora.com/insights/
- McKinsey Growth & Sales — https://www.mckinsey.com/capabilities/growth-marketing-and-sales
- Gartner Marketing resources — https://www.gartner.com/en
- Forrester research — https://www.forrester.com/
- SaaS product marketing and positioning frameworks from public GTM resources

This repo synthesizes public marketing and demand-generation practice into reusable skill patterns for AI-assisted GTM execution.

## Structure

- `skills/` — marketing-specific agent playbooks

## Focus

This repo is designed for marketing teams that need higher-quality targeting, messaging, and campaign execution insights grounded in public B2B marketing frameworks.
