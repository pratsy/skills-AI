# Changelog

## [Unreleased]

- Renamed `skills_ai/` to `sdk/` — the old name overloaded "skills" for a
  fourth thing in a repo that already has `b2b-agent-skills-*/skills/` and
  `.claude/skills/`, which was a source of confusion. Updated every import,
  CLI reference, and doc link accordingly.
- Rewrote `sdk/providers.py`: fixed `OpenAIProvider`, which was written
  against the pre-1.0 `openai.ChatCompletion` API while `requirements.txt`
  installed the current SDK (v1+) — the old code would have raised an
  `AttributeError` on first real call. Added a native `AnthropicProvider`
  alongside it, since this is fundamentally a Claude Code skills repo and
  didn't have one. `PROVIDER=mock|anthropic|openai` are now equally
  supported, matching `.env.example`.
- Rewrote `SECURITY.md`, which was generic AI-security boilerplate hardcoded
  to OpenAI despite the SDK being provider-agnostic, and ended with an
  unrelated paragraph about GitHub Actions approval-gate policy. Now
  describes what data actually leaves the machine, how to configure any of
  the three providers, and flags that `examples/webhook_app.py` has no auth
  and isn't production-ready.
- `sdk.runner.run_skill()` now accepts `input_data` directly instead of
  requiring a JSON file path; simplified `examples/webhook_app.py`
  accordingly (it previously round-tripped the request payload through a
  temp file, and was hardcoded to `MockProvider` regardless of `.env`
  configuration, so it could never call a real model).
- Packaged all 45 skills as real Claude Code Skills (`.claude/skills/<slug>/SKILL.md`),
  not just markdown to read — clone the repo and Claude Code invokes them directly.
- Rebuilt `skills_ai`'s runner to read those same `SKILL.md` files as its prompt
  source instead of maintaining separate Jinja templates. Removed the 5 bespoke
  `skills_ai/skills/*.py` wrappers, their `.j2` templates, and `template_loader.py`
  (and the now-unused `jinja2` dependency) — every skill now runs through one
  generic path, so all 45 are runnable via the Python SDK, not a hardcoded 5.
- Expanded `skills_ai.evaluation.SKILL_EXPECTED_FIELDS` from 5 to all 45 skills,
  extracted directly from each skill's own "Output schema" section, and fixed the
  scoring formula (previously hardcoded to a 5-field/20-point split).
- Fixed `benchmarks/sample_dataset.json`, which still used a pre-rewrite output
  schema for `renewal-risk-scorer` and `executive-sponsor-identifier`; expanded it
  to one representative skill per domain pack with real worked-example data, and
  removed the now-redundant inline CI "smoke test" in favor of the test suite's
  own full-coverage checks.
- Moved `docs/prompt-packs.md` to root-level `PROMPT_PACKS.md` and removed the
  now-empty `docs/` folder (it held only that one file).
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
