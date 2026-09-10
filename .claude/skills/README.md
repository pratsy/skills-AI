# Claude Code skills

This directory packages 15 of this repo's strongest skills as real [Claude Code Skills](https://code.claude.com/docs/en/skills) — `SKILL.md` files Claude discovers and can invoke directly, not just markdown you read and copy-paste.

## How to use these

**In this repo**, they're already active — clone it and open Claude Code anywhere inside it, and these 15 skills are available automatically (ask Claude to score a deal's risk, build a discovery sequence, size a market, etc., and it will use the matching skill).

**In your own project**, copy the folder(s) you want into your own repo's `.claude/skills/`:

```bash
cp -r .claude/skills/deal-risk-assessor /path/to/your-project/.claude/skills/
```

Restart your Claude Code session and it's available there too — no install step, no dependency, no API key. Each `SKILL.md` is self-contained (the scoring model, required inputs, and output format are all inline) and links back to its full README in the matching pack for the worked example and rationale.

## What's here vs. what isn't

These 15 are a curated subset — the ones most useful to invoke directly in a live session (scoring/diagnostic skills that take data you already have and return a structured read). The other 30 skills in this repo are still fully documented in their pack READMEs; they work as copy-paste prompts and can be packaged the same way on request. See each pack's `skill-template.md` for the format if you want to add more here yourself.

| Domain | Skills |
|---|---|
| Sales | `deal-risk-assessor`, `discovery-question-generator`, `objection-response-coach`, `renewal-risk-scorer`, `forecast-confidence-model`, `lead-prioritization-agent` |
| Marketing | `audience-segmentation-optimizer`, `brand-positioning-synthesizer`, `value-proposition-tester`, `messaging-clarity-auditor` |
| RevOps | `pipeline-health-monitor`, `forecast-bias-detector` |
| GTM | `market-sizing-modeler`, `win-loss-theme-clusterer`, `competitor-monitor` |
