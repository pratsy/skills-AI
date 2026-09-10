"""Minimal runtime wrapper for the Executive Sponsor Identifier skill."""
from typing import Dict, Any
from ..template_loader import render_template

PROMPT_TEMPLATE = """
You are a sales strategy advisor. Given the opportunity context, return a short JSON with keys: executive_sponsor (name/title), buying_committee (list of names), and engagement_plan (list).

Company: {{ company }}
Deal Size: {{ deal_size }}
Timeline: {{ timeline }}
Primary Contact: {{ primary_contact }}
"""


def run(input_data: Dict, provider) -> Dict[str, Any]:
    context = {
        "company": input_data.get("OPPORTUNITY CONTEXT", {}).get("Company", input_data.get("company", "unknown")),
        "deal_size": input_data.get("OPPORTUNITY CONTEXT", {}).get("Deal size", input_data.get("deal_size", "unknown")),
        "timeline": input_data.get("OPPORTUNITY CONTEXT", {}).get("Timeline", input_data.get("timeline", "unknown")),
        "primary_contact": input_data.get("PRIMARY CONTACT", {}).get("Name", input_data.get("primary_contact", "unknown")),
    }

    prompt = render_template(PROMPT_TEMPLATE, context)
    raw = provider.generate(prompt)

    if isinstance(raw, dict) and raw.get("executive_sponsor"):
        return {"skill": "executive-sponsor-identifier", "result": raw}
    return {"skill": "executive-sponsor-identifier", "raw": raw}
