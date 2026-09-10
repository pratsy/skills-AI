"""Minimal runtime wrapper for the Renewal Risk Scorer skill."""
from typing import Dict, Any
from ..template_loader import render_template

PROMPT_TEMPLATE = """
You are a customer retention strategist. Given the account data below, provide a short JSON with keys: risk_score (1-10), top_drivers (list), recommended_actions (list).

Account: {{ account_name }}
Renewal Date: {{ renewal_date }}
Product Usage Trend: {{ product_usage_trend }}
Support Issues Open: {{ support_issues_open }}
Executive Sponsor Change: {{ executive_sponsor_change }}
"""


def run(input_data: Dict, provider) -> Dict[str, Any]:
    context = {
        "account_name": input_data.get("Account Name") or input_data.get("account_name", "unknown"),
        "renewal_date": input_data.get("Renewal Date") or input_data.get("renewal_date", "unknown"),
        "product_usage_trend": input_data.get("Product Usage", {}).get("Usage trend (last 90 days)", "unknown"),
        "support_issues_open": input_data.get("Support and Success History", {}).get("Critical issues unresolved", 0),
        "executive_sponsor_change": input_data.get("Stakeholder Health", {}).get("Executive sponsor change", "no"),
    }

    prompt = render_template(PROMPT_TEMPLATE, context)
    raw = provider.generate(prompt)

    # If provider returns structured dict (mock), normalize; otherwise return raw text
    if isinstance(raw, dict) and raw.get("assessment"):
        return {"skill": "renewal-risk-scorer", "result": raw["assessment"]}
    return {"skill": "renewal-risk-scorer", "raw": raw}
