# Expert Memory Architecture

This repo is not just a collection of prompts. It is structured around an operating memory model for B2B revenue work.

## Core idea

A useful business AI system needs more than a model prompt. It needs memory.

The memory layer captures the practical patterns that experienced operators learn over time:

- which accounts deserve attention and why
- which buying motions carry more risk than they appear
- which pipeline patterns are healthy versus noisy
- which marketing signals actually indicate conversion issues
- which competitor signals deserve action and which are just background noise
- which objections, blockers, and stakeholder patterns appear repeatedly

This turns the repo from a generic assistant library into a structured decision-support system.

## The memory model

Each skill should carry a compact memory pack with these parts:

1. Business objective
   - what outcome is this skill meant to improve?

2. Decision context
   - what role is using it?
   - what signals matter most?
   - what business motion is being evaluated?

3. Failure patterns
   - what does a bad outcome look like?
   - what mistakes usually lead to weak conclusions?

4. Domain rules
   - what framework or operating logic should the model respect?
   - examples: MEDDIC, BANT, ICP fit, pipeline health review, content gap diagnosis

5. Source grounding
   - why should the model trust this conclusion?
   - what public or practitioner references support it?

6. Action orientation
   - what should the user do with the output?
   - what next step should follow from the result?

7. Feedback loop
   - what should humans correct over time?
   - how does the memory improve as more experience is added?

## Domain examples

### Sales memory
- stakeholder coverage quality
- champion and economic buyer patterns
- deal risk themes by stage and segment
- objection patterns that repeat across similar accounts

### Marketing memory
- message-to-buyers alignment signals
- funnel drop-off patterns
- content gaps by customer stage
- positioning drift and perception changes

### RevOps memory
- health of pipeline by stage
- forecast bias patterns
- data quality and stage consistency issues
- handoff quality across teams

### GTM memory
- market shifts and strategic relevance
- competitor signals that matter to buying decisions
- account prioritization patterns by segment and opportunity type

## Why this matters

Generic AI fails because it has no memory of the real business context.

This repo adds the missing layer:

- operational memory
- domain expertise
- evidence-based logic
- action-driven outputs

That is what makes it useful for sales, marketing, RevOps, and GTM operators.

## Standard memory template

Use the schema in `memory/skill-memory-template.yaml` for each skill.

This keeps the repo consistent and makes the logic more defensible to actual business users.

## Public references that inform this structure

This repo deliberately uses public, practitioner-aligned sources rather than vague or fabricated expertise. Good references include:

- ICP and segmentation frameworks
- MEDDIC / sales qualification patterns
- BANT-style qualification and prioritization logic
- funnel diagnostics and lifecycle analysis patterns
- pipeline health and forecasting quality concepts
- competitor intelligence and market signal monitoring practices

These are not meant to be rigid formulas. They are operational heuristics to make the AI outputs more grounded and useful.

## Final design principle

The repo should feel like a business operating system, not a generic prompt library.

If a skill can explain:
- the business problem,
- the decision logic,
- the relevant signals,
- the likely failure modes,
- and the right next action,

then it has real value.
