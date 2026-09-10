"""Minimal runtime wrapper for the Renewal Risk Scorer skill."""
from typing import Dict, Any
from ..template_loader import render_template, load_template_from_file
from pathlib import Path


def run(input_data: Dict, provider) -> Dict[str, Any]:
    context = {
        "account_id": input_data.get("account_id", "unknown"),
        "usage_trend_90d": input_data.get("usage_trend_90d", "unknown"),
        "active_users": input_data.get("active_users", "unknown"),
        "champion_status": input_data.get("champion_status", "unknown"),
        "support_signals": input_data.get("support_signals", "unknown"),
    }

    base = Path(__file__).resolve().parents[2]
    tpl_path = base / "templates" / "renewal_risk_scorer.j2"
    if tpl_path.exists():
        tpl = load_template_from_file(str(tpl_path))
        prompt = render_template(tpl, context)
    else:
        prompt = render_template("""
You are a customer success analyst scoring renewal risk using a weighted usage/engagement/
continuity/sentiment model. Return JSON with keys: renewal_risk_score, risk_band, primary_driver.

Account: {{ account_id }}
Usage Trend: {{ usage_trend_90d }}
Active Users: {{ active_users }}
Champion Status: {{ champion_status }}
Support Signals: {{ support_signals }}
""", context)
    raw = provider.generate(prompt)

    # MockProvider returns a fixed {"assessment": {"risk_score": ...}} shape for local testing;
    # a real provider returns the renewal_risk_score/risk_band/primary_driver schema directly.
    if isinstance(raw, dict) and raw.get("assessment"):
        return {"skill": "renewal-risk-scorer", "result": raw["assessment"]}
    if isinstance(raw, dict) and raw.get("renewal_risk_score") is not None:
        return {"skill": "renewal-risk-scorer", "result": raw}
    return {"skill": "renewal-risk-scorer", "raw": raw}
