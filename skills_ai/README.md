# skills_ai SDK

This folder is not a public skill pack. It is the runtime implementation layer for the repo.

Think of the architecture like this:

- `b2b-agent-skills-sales/`, `b2b-agent-skills-marketing/`, etc. = the public-facing playbooks, prompts, source references, and examples
- `skills_ai/` = the Python SDK and engine that loads those templates, runs providers, evaluates outputs, and lets you execute skills in code

This separation is intentional. The public repo should stay readable and credible for people browsing the library, while the runtime layer handles execution logic and automation.

Quickstart

1. Install dependencies:

```bash
python3 -m pip install -r requirements.txt --user
```

2. Run a skill with the included mock provider:

```bash
# using the package runner
python3 -m skills_ai.runner renewal_risk_scorer --input examples/fixtures/renewal_input.json

# or using the CLI script
./bin/skills-ai renewal_risk_scorer --input examples/fixtures/renewal_input.json
```

Replace the mock provider by implementing a real `Provider` in `skills_ai.providers`.
