# Security and secrets guidance

## What actually leaves your machine

Running a skill through `sdk` sends two things to whichever provider you've configured: the skill's `SKILL.md` instructions (public — it's committed to this repo) and the input data you pass in. **The input data is the only part that can contain anything sensitive**, and it goes to the provider verbatim — nothing in this repo redacts or filters it for you. Treat every skill invocation as "this JSON payload leaves my machine and goes to a third-party API," and decide what belongs in it accordingly.

Using `PROVIDER=mock` (the default) sends nothing anywhere — useful for testing the plumbing without exposing data or needing an API key.

## Provider configuration

`sdk/providers.py` supports three providers, selected via the `PROVIDER` environment variable. Copy `.env.example` to `.env` and set only the block for the provider you're using:

| `PROVIDER` | Required variables | Notes |
|---|---|---|
| `mock` (default) | none | deterministic fixture response, no network call, safe for CI |
| `anthropic` | `ANTHROPIC_API_KEY` | optional `ANTHROPIC_MODEL` (defaults to `claude-sonnet-5`) |
| `openai` | `OPENAI_API_KEY` | optional `OPENAI_MODEL` (defaults to `gpt-4o-mini`) |

Never commit a real `.env` file or hardcode a key into a skill file — `.env` is already in `.gitignore`. If you add a new provider, follow the same pattern: read the key from an environment variable in `__init__`, fail loudly with a clear error if it's missing, never accept a key as a function argument or default value.

## Handling sensitive input data

Before passing real account/customer data into a skill:

- Strip anything not needed for the specific question you're asking — a deal-risk score doesn't need a customer's full contract text, just the fields the skill's README documents as inputs.
- Don't include secrets, credentials, or internal system identifiers in the input payload — they add no value to the skill's output and every field you include is sent to the provider.
- If you're running skills against real customer data at any volume, review your provider's data retention and training-use policy before doing so — this varies by provider and by API tier, and this repo doesn't set any provider-side retention configuration for you.

## If you deploy `examples/webhook_app.py`

It's a minimal example of exposing a skill over HTTP, not a production service: it has no authentication, no rate limiting, and no input validation beyond what FastAPI's type checking gives you for free. Before running it anywhere reachable outside your own machine, at minimum add authentication, rate limiting, and request size limits, and confirm which provider it's configured to call — don't assume it's still pointed at the mock provider.

## Reporting a vulnerability

This is a skill-content and reference-implementation repository, not a hosted service — most "vulnerabilities" in practice will be in how you deploy `examples/webhook_app.py` or a skill of your own, not in this repo's code. If you find an issue in the code itself (the SDK, the CI workflow, or a skill's instructions producing an unsafe recommendation), please open a GitHub issue.
