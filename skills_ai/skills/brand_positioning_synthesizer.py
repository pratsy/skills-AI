from typing import Dict, Any
from ..template_loader import render_template, load_template_from_file
from pathlib import Path


def run(input_data: Dict, provider) -> Dict[str, Any]:
    base = Path(__file__).resolve().parents[2]
    tpl_path = base / "templates" / "brand_positioning_synthesizer.j2"
    context = {
        "competitive_alternatives": input_data.get("competitive_alternatives"),
        "product_attributes": input_data.get("product_attributes"),
        "win_loss_notes": input_data.get("win_loss_notes"),
        "customer_segments": input_data.get("customer_segments"),
        "category_candidates": input_data.get("category_candidates"),
    }
    if tpl_path.exists():
        tpl = load_template_from_file(str(tpl_path))
        prompt = render_template(tpl, context)
    else:
        prompt = render_template(
            """Synthesize competitive alternatives, unique attributes, and target market evidence into a positioning statement.""",
            context,
        )

    raw = provider.generate(prompt)
    if isinstance(raw, dict):
        return {"skill": "brand-positioning-synthesizer", "result": raw}
    return {"skill": "brand-positioning-synthesizer", "raw": raw}
