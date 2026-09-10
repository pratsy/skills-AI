# Changelog

## [Unreleased]

- Removed the legacy pre-split `b2b-agent-skills/` folder and merged near-duplicate
  skills (`content-gap-identifier`, `pipeline-health-audit-agent`) into their
  stronger counterparts, bringing the library to 45 skills with no overlap.
- Replaced the repeated, unlinked reference list at the bottom of every skill
  README with a pointer to each pack's `sources-and-frameworks.md`.
- Rewrote the root README for clarity and cut duplicated sections; corrected
  stale skill counts and featured-skill lists that referenced renamed/removed
  skills.
- Added launch-ready CLI and Python SDK wrapper.
- Added OpenAI provider abstraction and template loading.
- Added sales and marketing skill library templates.
- Added evaluation harness and GitHub Actions CI.
- Added security guidance and API example.

## [0.1.0] - 2026-09-10

- Initial public skill library release for B2B sales and marketing workflows.
- Added initial sales skill packs and marketing skill packs.
- Added prompt, example-output, and rubric documentation.
- Added test suite and example fixtures.
