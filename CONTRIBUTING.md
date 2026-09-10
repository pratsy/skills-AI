# Contributing

Contributions are welcome if they improve the quality, clarity, or usefulness of the public B2B revenue AI skill library.

## Public contribution standards

Please keep contributions aligned to the public-facing purpose of the repo:

- practical B2B sales, marketing, RevOps, and GTM workflows
- structured skill design
- business problem framing
- example outputs
- evaluation criteria
- source references

## What not to contribute

Please do not add:

- private notes
- draft brainstorming content
- internal planning logs
- low-quality experimental prompts
- unfinished or speculative material

## Suggested contribution format

Every skill in this repo follows the same structure — use a pack's `skills/skill-template.md` (e.g. [`b2b-agent-skills-sales/skills/skill-template.md`](b2b-agent-skills-sales/skills/skill-template.md)) as the reference layout:

- when to use it, in concrete situations
- the named, checkable methodology it operationalizes (not a vague "informed by industry practice" claim)
- an explicit scoring model or decision rubric
- an input schema and one fully worked example with real numbers
- common failure patterns specific to that method
- an output JSON schema
- what the skill is grounded in, linking to the pack's `sources-and-frameworks.md`

Before adding a new skill, check the pack's existing skills for overlap — if your idea is a variation on one that already exists, improve that skill instead of adding a near-duplicate.

## Review expectations

Keep the work polished, operationally useful, and grounded in a real, named methodology — not a generic restatement of a business problem.
