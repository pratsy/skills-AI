# B2B Agent Skills

[![CI](https://github.com/pratsy/skills-AI/actions/workflows/ci.yml/badge.svg)](https://github.com/pratsy/skills-AI/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Structured AI playbooks for B2B sales, marketing, RevOps, and GTM teams — built for the people who run revenue work, not just for prompting AI.

Most AI prompt libraries hand you a single instruction and stop there. This repo instead packages each skill with the business context an experienced operator would bring to the problem: why it matters, what usually goes wrong, what inputs it needs, and what a good answer looks like — so the output is a decision aid, not just generated text.

## Who this is for

Sales leaders, marketing and lifecycle teams, RevOps and forecasting teams, GTM operators and founders, and anyone building AI workflows around real revenue operations.

## What's in the repo

| Pack | Covers | Skills |
|---|---|---|
| [`b2b-agent-skills-sales/`](b2b-agent-skills-sales/) | Prioritization, qualification, objection handling, deal risk, forecasting, account planning | 17 |
| [`b2b-agent-skills-marketing/`](b2b-agent-skills-marketing/) | ICP, messaging, campaign diagnostics, ABM, lifecycle, content strategy | 15 |
| [`b2b-agent-skills-revops/`](b2b-agent-skills-revops/) | Pipeline health, forecast bias, CRM hygiene, attribution, handoff quality | 5 |
| [`b2b-agent-skills-gtm/`](b2b-agent-skills-gtm/) | Market intelligence, competitor signals, account prioritization | 8 |

Supporting folders:

- [`.claude/skills/`](.claude/skills/) — all 45 skills packaged as real Claude Code Skills you can invoke directly, not just read
- [`sdk/`](sdk/) — a small Python SDK that runs any of the 45 skills programmatically, reading the same `.claude/skills/` definitions as the prompt (provider abstraction, output evaluation). See [`sdk/README.md`](sdk/README.md).
- [`PROMPT_PACKS.md`](PROMPT_PACKS.md) — copy-paste prompts by role, as a faster on-ramp than reading a full skill README
- [`examples/`](examples/) — sample input fixtures and a webhook app example
- [`memory/`](memory/) — the checklist used to keep skills specific and evidence-grounded instead of generic
- [`benchmarks/`](benchmarks/) — a small evaluation dataset and rubric for scoring skill output quality

## Quick start

1. Pick the problem you already have (weak pipeline, unclear messaging, poor account prioritization, forecast risk, competitor noise).
2. Open the matching pack above and find the skill whose title matches the problem.
3. Read its README: business objective, inputs, decision logic, and a recommended prompt.
4. Paste the prompt into your AI tool of choice along with your own data, run it via `sdk`, or — if you're in Claude Code — just ask; the matching skill in `.claude/skills/` is invoked automatically.
5. Turn the output into a decision — who owns the action, and what happens next.

For role-specific prompts you can copy-paste immediately, see [`PROMPT_PACKS.md`](PROMPT_PACKS.md).

## Every skill follows the same structure

- **When to use this** — concrete situations, not an abstract pitch
- **Methodology** — the named, checkable framework it operationalizes (MEDDPICC, SPIN, the Value Proposition Canvas, TAM/SAM/SOM, and others — see each pack's `sources-and-frameworks.md`)
- **Scoring model / decision logic** — an explicit formula or rubric, not a narrative
- **Inputs**, a fully **worked example** with real numbers, and **common failure patterns** specific to that method
- **Output schema** — so the skill can be wired into a pipeline, not just pasted as a prompt
- **Recommended prompt** — ready to paste
- **Grounded in** — what the skill is built on, linking to the pack's `sources-and-frameworks.md` for the full reference list

## Use these directly in Claude Code

All 45 skills are packaged as real [Claude Code Skills](https://code.claude.com/docs/en/skills) in [`.claude/skills/`](.claude/skills/), not just markdown to copy-paste. Clone this repo and open Claude Code anywhere inside it, and Claude can invoke any of them — `deal-risk-assessor`, `pipeline-health-monitor`, `market-sizing-modeler`, and so on — directly against your own data. Copy any folder into your own project's `.claude/skills/` to use it there — no install step. See [`.claude/skills/README.md`](.claude/skills/README.md) for the full list.

## Using skills in code

`sdk` is a thin runtime that reads the same `.claude/skills/<name>/SKILL.md` files used by Claude Code, sends them to a pluggable model provider (mock provider for testing, or Anthropic/OpenAI for real runs) along with your input data, and evaluates the output's structure — one source of truth for both surfaces, so they can't drift apart. Works for any of the 45 skills, not a subset.

```bash
python3 -m pip install -r requirements.txt
python3 -m sdk.runner renewal_risk_scorer --input examples/fixtures/renewal_input.json
```

See [`sdk/README.md`](sdk/README.md) for how the public skill packs relate to the runtime layer, and [`benchmarks/README.md`](benchmarks/README.md) for how output quality is scored.

## Contributing

Contributions that improve a skill's clarity, correctness, or grounding are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). Please avoid submitting near-duplicate skills; if you're extending an existing one, improve it in place instead.

## License

[MIT](LICENSE)
