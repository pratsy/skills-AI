from typing import Dict, Any
from ..template_loader import render_template, load_template_from_file
from pathlib import Path


def run(input_data: Dict, provider) -> Dict[str, Any]:
    base = Path(__file__).resolve().parents[2]
    tpl_path = base / "templates" / "nurture_sequence_architect.j2"
    context = {
        "stage": input_data.get("stage"),
        "engagement_events": input_data.get("engagement_events"),
        "content_inventory": input_data.get("content_inventory"),
    }
    if tpl_path.exists():
        tpl = load_template_from_file(str(tpl_path))
        prompt = render_template(tpl, context)
    else:
        prompt = render_template("""Create a nurture sequence based on engagement and content.""", context)

    raw = provider.generate(prompt)
    if isinstance(raw, dict):
        return {"skill": "nurture-sequence-architect", "result": raw}
    return {"skill": "nurture-sequence-architect", "raw": raw}
