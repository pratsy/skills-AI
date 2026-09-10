from typing import Dict, Any
from ..template_loader import render_template, load_template_from_file
from pathlib import Path


def run(input_data: Dict, provider) -> Dict[str, Any]:
    base = Path(__file__).resolve().parents[2]
    tpl_path = base / "templates" / "brand_positioning_synthesizer.j2"
    context = {
        "customer_interviews": input_data.get("customer_interviews"),
        "competitor_notes": input_data.get("competitor_notes"),
        "product_value": input_data.get("product_value"),
        "icp": input_data.get("icp"),
    }
    if tpl_path.exists():
        tpl = load_template_from_file(str(tpl_path))
        prompt = render_template(tpl, context)
    else:
        prompt = render_template("""You are a B2B marketing strategist. Synthesize inputs into positioning.""", context)

    raw = provider.generate(prompt)
    if isinstance(raw, dict):
        return {"skill": "brand-positioning-synthesizer", "result": raw}
    return {"skill": "brand-positioning-synthesizer", "raw": raw}
