# Security and Secrets Guidance

## Environment variables

Use a local `.env` file for development and GitHub Secrets for CI/CD.

Example:

```bash
cp .env.example .env
```

Example `.env`:

```bash
PROVIDER=openai
OPENAI_API_KEY=your_key_here
OPENAI_MODEL=gpt-4o-mini
```

Never commit real secrets to Git.

## PII and sensitive data handling

Before sending any payload to an LLM provider:

- redact customer names if not required
- remove internal-only identifiers if not required
- strip secrets, API keys, and tokens from text
- avoid sending sensitive financial or legal data unless explicitly approved
- log only sanitized metadata in production systems

Recommended policy:

- keep prompts minimal and scoped to the business task
- send only required fields
- mask or hash identifiers when possible
- document where data is retained and for how long

## GitHub Actions secrets

For GitHub Actions, store secrets in the repository settings:

- `OPENAI_API_KEY`
- `PROVIDER`

Example workflow environment usage:

```yaml
env:
  PROVIDER: openai
  OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
```

## `.gitignore` guidance

Make sure these are ignored:

```gitignore
.env
.env.*
__pycache__/
*.pyc
```

## Production recommendations

- validate and sanitize user input before invoking a skill
- store prompt logs separately from business data
- rate-limit API access
- add retry and timeout controls
- review provider retention and privacy terms before production use
- keep a mapping of which skill requires which data fields


## GitHub Actions workflow policy note

After adjusting repository Actions settings, workflows can run normally for the default branch and pull requests. Keep the repository policy minimal and explicit: disable unnecessary approval gates for forked PRs unless you intentionally want maintainer review before jobs start.
