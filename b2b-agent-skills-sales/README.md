# B2B Agent Skills — Sales

Open-source AI playbooks for sales execution, qualification, pipeline strategy, and deal progression.

## Coverage

- lead prioritization
- discovery
- qualification
- objection handling
- deal risk assessment
- forecast confidence
- account planning
- expansion signals

## Featured skills

- lead-prioritization-agent
- discovery-question-generator
- objection-response-coach
- deal-risk-assessor
- forecast-confidence-model
- renewal-risk-scorer
- executive-sponsor-identifier
- competitive-differentiation-coach
- multi-threading-plan-builder
- champion-advocacy-builder
- deal-committee-readiness-coach
- account-plan-generator
- negotiation-readiness-coach
- pricing-justification-builder
- stakeholder-map-builder
- territory-prioritization-agent
- executive-briefing-builder

## Standard skill format

Every skill in this library follows the same operational structure — see [`memory/skill-template.md`](../memory/skill-template.md):

- when to use it, in concrete situations
- the named methodology it operationalizes (MEDDPICC, SPIN, the Challenger Sale's Mobilizer test, BATNA, the Pyramid Principle, and others — see below)
- an explicit scoring model or decision rubric, not a narrative description
- an input schema and a fully worked example with real numbers
- an output JSON schema so the skill can be wired into a pipeline, not just pasted as a prompt

## Named methodologies used in this pack

Rather than one generic "informed by industry practice" claim per skill, each skill names the specific method it's built on:

- **MEDDPICC** — deal qualification and risk scoring (`deal-risk-assessor`, `forecast-confidence-model`, `deal-committee-readiness-coach`, `stakeholder-map-builder`, `executive-sponsor-identifier`)
- **SPIN Selling** (Neil Rackham) — discovery sequencing (`discovery-question-generator`)
- **LAER** objection handling — (`objection-response-coach`)
- **The Challenger Sale's Mobilizer test** (Dixon & Adamson) — champion strength (`champion-advocacy-builder`)
- **BATNA / principled negotiation** (Fisher & Ury, *Getting to Yes*) — (`negotiation-readiness-coach`)
- **The Pyramid Principle** (Barbara Minto) — executive communication structure (`executive-briefing-builder`)
- **Whitespace analysis** — account and territory planning (`account-plan-generator`, `territory-prioritization-agent`)
- **Fit/intent two-axis lead scoring** — (`lead-prioritization-agent`)
- **Usage-trend weighted customer health scoring** — (`renewal-risk-scorer`)

See [sources-and-frameworks.md](sources-and-frameworks.md) for the pack's general reference list.

## Structure

- `skills/` — sales-specific agent playbooks

## Focus

This repo is built to help sales teams use AI agents that act like experienced operators across the funnel, grounded in public B2B sales practice and enablement frameworks.
