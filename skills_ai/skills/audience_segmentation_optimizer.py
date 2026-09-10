from typing import Dict, Any
from ..template_loader import render_template, load_template_from_file
from pathlib import Path


def run(input_data: Dict, provider) -> Dict[str, Any]:
    base = Path(__file__).resolve().parents[2]
    tpl_path = base / "templates" / "audience_segmentation_optimizer.j2"
    context = {
        "icp_definition": input_data.get("icp_definition"),
        "accounts": input_data.get("accounts"),
    }
    if tpl_path.exists():
        tpl = load_template_from_file(str(tpl_path))
        prompt = render_template(tpl, context)
    else:
        prompt = render_template(
            """Score accounts on firmographic fit, technographic fit, engagement intensity, and intent signal against the ICP definition.""",
            context,
        )

    raw = provider.generate(prompt)
    if isinstance(raw, dict):
        return {"skill": "audience-segmentation-optimizer", "result": raw}
    return {"skill": "audience-segmentation-optimizer", "raw": raw}
