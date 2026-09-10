from typing import Dict, Any
from ..template_loader import render_template, load_template_from_file
from pathlib import Path


def run(input_data: Dict, provider) -> Dict[str, Any]:
    base = Path(__file__).resolve().parents[2]
    tpl_path = base / "templates" / "nurture_sequence_architect.j2"
    context = {
        "entry_segment": input_data.get("entry_segment"),
        "lead_score_at_entry": input_data.get("lead_score_at_entry"),
        "available_content": input_data.get("available_content"),
        "engagement_history": input_data.get("engagement_history"),
    }
    if tpl_path.exists():
        tpl = load_template_from_file(str(tpl_path))
        prompt = render_template(tpl, context)
    else:
        prompt = render_template(
            """Create an engagement-branched nurture sequence with graduate/suppress conditions per step.""",
            context,
        )

    raw = provider.generate(prompt)
    if isinstance(raw, dict):
        return {"skill": "nurture-sequence-architect", "result": raw}
    return {"skill": "nurture-sequence-architect", "raw": raw}
