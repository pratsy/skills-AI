"""Minimal runtime wrapper for the Executive Sponsor Identifier skill."""
from typing import Dict, Any
from ..template_loader import render_template, load_template_from_file
from pathlib import Path

PROMPT_TEMPLATE = """
You are a sales strategist identifying the likely Economic Buyer. Score each candidate on
Authority (0-5) and Engagement (0-5), compute Sponsor Likelihood = Authority x Engagement,
and recommend the primary target. Return JSON with keys: candidates_ranked, primary_eb_target, rationale.

Deal Size: {{ deal_size }}
Champion Notes: {{ champion_notes }}
Candidates: {{ candidates }}
"""


def run(input_data: Dict, provider) -> Dict[str, Any]:
    context = {
        "deal_size": input_data.get("deal_size", "unknown"),
        "champion_notes": input_data.get("champion_notes", "n/a"),
        "candidates": input_data.get("candidates", []),
    }

    base = Path(__file__).resolve().parents[2]
    tpl_path = base / "templates" / "executive_sponsor_identifier.j2"
    if tpl_path.exists():
        tpl = load_template_from_file(str(tpl_path))
        prompt = render_template(tpl, context)
    else:
        prompt = render_template(PROMPT_TEMPLATE, context)
    raw = provider.generate(prompt)

    if isinstance(raw, dict) and raw.get("candidates_ranked"):
        return {"skill": "executive-sponsor-identifier", "result": raw}
    if isinstance(raw, dict) and raw.get("assessment"):
        return {"skill": "executive-sponsor-identifier", "result": raw["assessment"]}
    return {"skill": "executive-sponsor-identifier", "raw": raw}
