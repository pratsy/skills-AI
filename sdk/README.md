# sdk

This folder is not a public skill pack. It is the runtime implementation layer for the repo.

Think of the architecture like this:

- `b2b-agent-skills-sales/`, `b2b-agent-skills-marketing/`, etc. = the public-facing playbooks — full methodology, worked examples, source references, written for a human to read.
- `.claude/skills/<name>/SKILL.md` = a condensed, self-contained version of each skill's operating logic, written for an LLM to execute directly.
- `sdk/` = the Python SDK that reads those same `SKILL.md` files, sends them to a model provider along with your input data, and evaluates the output's structure.

All three point at the same 45 skills. `SKILL.md` is the single source of prompt content — the SDK doesn't maintain a separate copy, so it can't drift out of sync with what Claude Code uses.

## How a skill runs

`sdk.runner.run_skill(skill_name, input_path)`:

1. Looks for a bespoke `sdk/skills/<skill_name>.py` module (an escape hatch for a skill that needs custom input handling — none currently exist; all 45 skills run generically).
2. Otherwise, falls back to `run_generic_skill()`: reads `.claude/skills/<slug>/SKILL.md`, strips the YAML frontmatter, appends your input data as JSON, and sends the result to the configured provider.
3. Normalizes the provider's response into `{"skill": ..., "result": ...}`.

## Quickstart

1. Install dependencies:

```bash
python3 -m pip install -r requirements.txt --user
```

2. Run any of the 45 skills with the included mock provider:

```bash
# using the package runner
python3 -m sdk.runner renewal_risk_scorer --input examples/fixtures/renewal_input.json

# or using the CLI script (dashes or underscores both work)
./bin/skills-ai deal-risk-assessor
```

Skills without a fixture file still run — pass any JSON matching the inputs described in that skill's `SKILL.md` or README, or call with no `--input` to see the skill run against an empty input (useful for checking the plumbing works).

Set `PROVIDER=anthropic` or `PROVIDER=openai` in your `.env` (see `.env.example`) to use a real model instead of the mock provider, or add a new one by implementing the `Provider` interface in `sdk.providers`.

## Evaluating output quality

`sdk.evaluation.SKILL_EXPECTED_FIELDS` defines the expected top-level output keys for all 45 skills, pulled directly from each skill's own "Output schema" section. `evaluate_skill_output(skill_name, output)` checks a result against that shape without needing a model call — see [`benchmarks/README.md`](../benchmarks/README.md) for the sample dataset built on top of it.
