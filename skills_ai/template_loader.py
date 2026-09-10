from jinja2 import Template
from typing import Dict
from pathlib import Path


def load_template_from_file(path: str) -> str:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Template file not found: {path}")
    return p.read_text(encoding="utf-8")


def render_template(template_str: str, context: Dict) -> str:
    """Render a Jinja2 template string with the provided context."""
    tpl = Template(template_str)
    return tpl.render(**context)
