# skills_ai SDK

Minimal Python SDK to run skills locally.

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
