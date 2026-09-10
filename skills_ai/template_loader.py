from jinja2 import Template
from typing import Dict


def render_template(template_str: str, context: Dict) -> str:
    """Render a Jinja2 template string with the provided context."""
    tpl = Template(template_str)
    return tpl.render(**context)
