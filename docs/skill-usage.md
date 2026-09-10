# Skill usage guide

This guide explains how to run the skills in this project with the local SDK and with API integrations.

## Local usage

Run a skill with a JSON input file:

```bash
PYTHONPATH=. python -m skills_ai.runner renewal_risk_scorer --input examples/fixtures/renewal_input.json
```

Run from the CLI wrapper:

```bash
./bin/skills-ai renewal_risk_scorer --input examples/fixtures/renewal_input.json
```

## Example output shape

### Renewal Risk Scorer

```json
{
  "skill": "renewal-risk-scorer",
  "result": {
    "risk_score": 7,
    "top_drivers": ["usage_decline", "exec_change"],
    "recommended_actions": ["exec_review", "resolve_issue"]
  }
}
```

### Executive Sponsor Identifier

```json
{
  "skill": "executive-sponsor-identifier",
  "result": {
    "executive_sponsor": "Thomas O'Brien",
    "buying_committee": ["CFO", "CTO", "VP Analytics"],
    "engagement_plan": ["Executive briefing", "Technical proof"]
  }
}
```

## API integration

Use the FastAPI example:

```bash
uvicorn examples.webhook_app:app --reload
```

Request body:

```json
{
  "skill": "renewal_risk_scorer",
  "payload": {
    "Account Name": "CloudOps",
    "Renewal Date": "2026-11-15"
  }
}
```

## Quality bar

Successful outputs should satisfy the expected schema for the chosen skill and be specific to the client context. The evaluation harness can score the output before using it in production.

## Important notes

- Add `OPENAI_API_KEY` to `.env` or GitHub Secrets before using the OpenAI provider.
- Use the mock provider for tests and local validation.
- Remove or redact sensitive identifiers before sending data to LLM providers.
