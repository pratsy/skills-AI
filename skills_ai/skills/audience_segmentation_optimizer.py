from typing import Dict, Any
from ..template_loader import render_template, load_template_from_file
from pathlib import Path


def run(input_data: Dict, provider) -> Dict[str, Any]:
    base = Path(__file__).resolve().parents[2]
    tpl_path = base / "templates" / "audience_segmentation_optimizer.j2"
    context = {
        "buyer_data": input_data.get("buyer_data"),
        "campaign_performance": input_data.get("campaign_performance"),
        "intent_signals": input_data.get("intent_signals"),
    }
    if tpl_path.exists():
        tpl = load_template_from_file(str(tpl_path))
        prompt = render_template(tpl, context)
    else:
        prompt = render_template("""Segment audiences based on buyer data and intent.""", context)

    raw = provider.generate(prompt)
    if isinstance(raw, dict):
        return {"skill": "audience-segmentation-optimizer", "result": raw}
    return {"skill": "audience-segmentation-optimizer", "raw": raw}
