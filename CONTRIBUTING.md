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

Every skill in this repo follows the same structure — use [`memory/skill-template.md`](memory/skill-template.md) as the reference layout:

- when to use it, in concrete situations
- the named, checkable methodology it operationalizes (not a vague "informed by industry practice" claim)
- an explicit scoring model or decision rubric
- an input schema and one fully worked example with real numbers
- common failure patterns specific to that method
- an output JSON schema
- what the skill is grounded in, linking to the pack's `sources-and-frameworks.md`

Before adding a new skill, check the pack's existing skills for overlap — if your idea is a variation on one that already exists, improve that skill instead of adding a near-duplicate.

## A new skill needs two files, not one

1. `b2b-agent-skills-<domain>/skills/<slug>/README.md` — the full version, per the template above.
2. `.claude/skills/<slug>/SKILL.md` — a condensed, self-contained version of the same skill, written as instructions for an LLM to execute rather than for a person to read. Use any existing file under `.claude/skills/` as the format reference; keep it under ~50 lines and link back to the README for the worked example instead of duplicating it.

CI checks that every skill has both (`tests/test_runner.py::test_all_45_skills_are_documented` and `test_all_45_skills_have_a_claude_skill`) — a PR adding only the README will fail that check, not silently pass with reduced functionality.

## Before submitting

Run the test suite locally (`PYTHONPATH=. pytest -q`) — it's fast (well under a second) and will catch a missing `SKILL.md`, a broken cross-reference, or an output schema that doesn't match what `sdk.evaluation` expects.

## Review expectations

Keep the work polished, operationally useful, and grounded in a real, named methodology — not a generic restatement of a business problem.
