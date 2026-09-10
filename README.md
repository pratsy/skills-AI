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

- [`skills_ai/`](skills_ai/) — a small Python SDK that runs a subset of skills programmatically (template rendering, provider abstraction, output evaluation). Most skills in this repo are designed to be used as prompts directly; `skills_ai` currently wires up five of them end-to-end as a reference implementation for anyone who wants to run skills in code rather than copy-paste them. See [`skills_ai/README.md`](skills_ai/README.md).
- [`docs/`](docs/) — quick start, prompt packs, and business use cases in plain English
- [`examples/`](examples/) — sample input fixtures and a webhook app example
- [`memory/`](memory/) — the schema and checklist used to keep skills specific instead of generic
- [`benchmarks/`](benchmarks/) — a small evaluation dataset and rubric for scoring skill output quality

## Quick start

1. Pick the problem you already have (weak pipeline, unclear messaging, poor account prioritization, forecast risk, competitor noise).
2. Open the matching pack above and find the skill whose title matches the problem.
3. Read its README: business objective, inputs, decision logic, and a recommended prompt.
4. Paste the prompt into your AI tool of choice along with your own data, or run it through `skills_ai` if it's one of the five wired-up skills.
5. Turn the output into a decision — who owns the action, and what happens next.

For role-specific prompts you can copy-paste immediately, see [`docs/prompt-packs.md`](docs/prompt-packs.md) and [`docs/business-use-cases.md`](docs/business-use-cases.md).

## Every skill follows the same structure

- **Why this skill exists** — the business problem, in plain language
- **Business objective** — the single question the skill answers
- **Expert memory layer** — the patterns an experienced operator would recognize
- **Inputs / Decision logic / Common failure patterns**
- **Outputs** and an **example result**
- **Recommended prompt** — ready to paste
- **Source basis** — the practice area it's grounded in, linking to the pack's [sources-and-frameworks.md](b2b-agent-skills-sales/sources-and-frameworks.md) for the full reference list

## Using skills in code

`skills_ai` is a thin runtime over the same skill definitions — Jinja2 prompt templates, a pluggable model provider (mock provider included, OpenAI provider available), and an output evaluator.

```bash
python3 -m pip install -r requirements.txt
python3 -m skills_ai.runner renewal_risk_scorer --input examples/fixtures/renewal_input.json
```

See [`skills_ai/README.md`](skills_ai/README.md) for how the public skill packs relate to the runtime layer, and [`benchmarks/README.md`](benchmarks/README.md) for how output quality is scored.

## Contributing

Contributions that improve a skill's clarity, correctness, or grounding are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). Please avoid submitting near-duplicate skills; if you're extending an existing one, improve it in place instead.

## License

[MIT](LICENSE)
