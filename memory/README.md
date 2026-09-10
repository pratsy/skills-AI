# Skill quality model

Every skill in this repo is meant to carry more than a prompt — a business objective, a named methodology, a decision rule, failure patterns, and source grounding, so the output is a decision aid rather than generic text.

Each skill README follows this structure (the reference layout lives in [`skill-template.md`](skill-template.md), shared across all four packs):

1. **Business objective** — the outcome this skill is meant to improve
2. **Methodology** — the named, checkable framework it operationalizes (MEDDPICC, SPIN, TAM/SAM/SOM, and others — see each pack's `sources-and-frameworks.md`)
3. **Scoring model / decision logic** — an explicit formula or rubric, not a narrative
4. **Common failure patterns** — the specific ways this method goes wrong in practice
5. **Worked example** — real inputs and a real computed output
6. **Output schema** — so the skill can be wired into a pipeline, not just pasted as a prompt

Use [`domain-memory-checklist.md`](domain-memory-checklist.md) when writing or reviewing a skill, to check it clears this bar instead of reading as generic.
