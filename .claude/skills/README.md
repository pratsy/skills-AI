# Claude Code skills

All 45 skills in this repo are packaged here as real [Claude Code Skills](https://code.claude.com/docs/en/skills) — `SKILL.md` files Claude discovers and can invoke directly, not just markdown you read and copy-paste.

## How to use these

**In this repo**, they're already active — clone it and open Claude Code anywhere inside it, and all 45 skills are available automatically (ask Claude to score a deal's risk, build a discovery sequence, size a market, etc., and it will use the matching skill).

**In your own project**, copy the folder(s) you want into your own repo's `.claude/skills/`:

```bash
cp -r .claude/skills/deal-risk-assessor /path/to/your-project/.claude/skills/
```

Restart your Claude Code session and it's available there too — no install step, no dependency, no API key. Each `SKILL.md` is self-contained (the scoring model, required inputs, and output format are all inline) and links back to its full README in the matching pack for the worked example and rationale.

## The other integration surface

`sdk/`, the Python SDK, reads these exact same `SKILL.md` files as its prompt source (see [`sdk/runner.py`](../../sdk/runner.py)) — so a skill's logic lives in exactly one place regardless of whether you invoke it through Claude Code or through code. If you add or edit a skill here, both surfaces pick it up automatically.

## Directory

45 skills, matching the four packs exactly:

| Domain | Skills |
|---|---|
| Sales (17) | `account-plan-generator`, `champion-advocacy-builder`, `competitive-differentiation-coach`, `deal-committee-readiness-coach`, `deal-risk-assessor`, `discovery-question-generator`, `executive-briefing-builder`, `executive-sponsor-identifier`, `forecast-confidence-model`, `lead-prioritization-agent`, `multi-threading-plan-builder`, `negotiation-readiness-coach`, `objection-response-coach`, `pricing-justification-builder`, `renewal-risk-scorer`, `stakeholder-map-builder`, `territory-prioritization-agent` |
| Marketing (15) | `abm-account-priority-ranker`, `ad-copy-variant-generator`, `audience-segmentation-optimizer`, `brand-perception-monitor`, `brand-positioning-synthesizer`, `campaign-performance-diagnostician`, `content-gap-analysis-agent`, `customer-journey-friction-audit`, `icp-refinement-agent`, `landing-page-copy-optimizer`, `lifecycle-email-optimizer`, `messaging-clarity-auditor`, `nurture-sequence-architect`, `persona-insight-extractor`, `value-proposition-tester` |
| RevOps (5) | `attribution-model-reviewer`, `crm-data-cleaner`, `forecast-bias-detector`, `pipeline-health-monitor`, `sales-handoff-quality-auditor` |
| GTM (8) | `account-priority-matrix-builder`, `competitor-monitor`, `competitor-signal-clusterer`, `market-shift-monitor`, `market-sizing-modeler`, `market-trend-signal-reporter`, `strategic-account-priority-ranker`, `win-loss-theme-clusterer` |

## Adding or editing a skill

Use any existing `SKILL.md` as the template: `name` and `description` frontmatter (plus `license: MIT`), then Role / Method / If information is missing / Output / Common failure patterns / Reference sections. Keep it under ~50 lines — the full depth belongs in the pack README it links back to, not duplicated here.
