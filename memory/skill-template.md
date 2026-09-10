# Skill Template

Use this as the reference layout for any new skill in any of the four packs (`b2b-agent-skills-sales/`, `-marketing/`, `-revops/`, `-gtm/`). Every skill should name a real, checkable methodology — not describe itself in the abstract.

A new skill also needs a matching [Claude Code Skill](../.claude/skills/README.md) at `.claude/skills/<slug>/SKILL.md` — CI checks that every skill in the library has one (`tests/test_runner.py::test_all_45_skills_have_a_claude_skill`), so a PR adding a skill without one will fail. Use any existing file under `.claude/skills/` as the format reference; it's a condensed, self-contained version of the sections below, written as instructions to an LLM rather than for a person to read.

## One-line description

What this skill scores/produces, and the named methodology it's built on.

## When to use this

2-4 concrete situations where this skill is the right tool, specific enough that a reader recognizes their own situation.

## Methodology

Name the real framework or method this skill operationalizes (e.g. MEDDPICC, SPIN, a named scoring model). If there isn't an established named framework, say so explicitly and describe the logic being applied instead of inventing a framework name.

## Scoring model / decision logic

An explicit formula, rubric, or decision rule — not a narrative description of "what a strong review considers." If the skill is inherently qualitative, provide a structured scoring rubric (e.g., 1-5 per dimension) rather than a free-text checklist.

## Inputs

A table: field name, type, example value.

## Worked example

One fully worked example with real (illustrative) numbers or content, showing the actual inputs and the actual computed/generated output — not just a narrative "example result."

## Common failure patterns

Failure modes specific to this method (not generic reasoning mistakes like "assuming without evidence").

## Output schema

A JSON schema the skill's output should conform to, so it can be wired into a pipeline.

## Recommended prompt

A prompt that names the methodology and scoring model explicitly, and asks for output matching the schema above.

## Grounded in

Name the real framework/source (author, origin) this skill is built on. Link to your pack's `sources-and-frameworks.md` (from `<pack>/skills/<slug>/README.md` that's `../../sources-and-frameworks.md`) for the pack's general reference list — don't repeat a generic blog list in every skill file.
