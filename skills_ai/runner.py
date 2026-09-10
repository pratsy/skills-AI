import argparse
import json
import importlib
import re
from pathlib import Path
from .providers import MockProvider, get_provider_from_env

REPO_ROOT = Path(__file__).resolve().parents[1]


def _strip_frontmatter(skill_md_text: str) -> str:
    """Remove the YAML frontmatter block from a SKILL.md file, returning the body."""
    match = re.match(r"^---\n.*?\n---\n(.*)$", skill_md_text, re.S)
    return match.group(1).strip() if match else skill_md_text.strip()


def _slugify(skill_name: str) -> str:
    return skill_name.replace("_", "-")


def run_generic_skill(skill_name: str, input_data: dict, provider) -> dict:
    """Run any of the 45 skills using its .claude/skills/<slug>/SKILL.md as the prompt.

    This is the default execution path for every skill that doesn't have a bespoke
    skills_ai.skills.<name> module. Keeping SKILL.md as the single source of prompt
    content means the Claude Code skill and the Python SDK can never drift apart.
    """
    slug = _slugify(skill_name)
    skill_md_path = REPO_ROOT / ".claude" / "skills" / slug / "SKILL.md"
    if not skill_md_path.exists():
        raise FileNotFoundError(
            f"No skill found for '{skill_name}': expected {skill_md_path} "
            f"(or a custom module at skills_ai/skills/{skill_name}.py)"
        )

    instructions = _strip_frontmatter(skill_md_path.read_text(encoding="utf-8"))
    prompt = (
        f"{instructions}\n\n"
        "## Input data\n\n"
        f"```json\n{json.dumps(input_data, indent=2)}\n```\n\n"
        "Apply the instructions above to this input data and return the output in the "
        "format specified."
    )

    raw = provider.generate(prompt)

    if isinstance(raw, dict) and raw.get("assessment"):
        return {"skill": slug, "result": raw["assessment"]}
    if isinstance(raw, dict):
        return {"skill": slug, "result": raw}
    return {"skill": slug, "raw": raw}


def run_skill(skill_name: str, input_path: str = None, provider=None):
    if provider is None:
        provider = get_provider_from_env()

    input_data = {}
    if input_path:
        with open(input_path, "r", encoding="utf-8") as f:
            input_data = json.load(f)

    # A skill may have a bespoke skills_ai.skills.<name> module for custom input
    # handling; otherwise it runs generically off its SKILL.md.
    module_name = f"skills_ai.skills.{skill_name}"
    try:
        mod = importlib.import_module(module_name)
    except ModuleNotFoundError:
        return run_generic_skill(skill_name, input_data, provider)

    return mod.run(input_data, provider)


def _cli():
    parser = argparse.ArgumentParser(description="Run a Skill locally")
    parser.add_argument("skill", help="skill slug, dashes or underscores (e.g. deal-risk-assessor)")
    parser.add_argument("--input", help="path to JSON input file", dest="input", default=None)
    args = parser.parse_args()

    out = run_skill(args.skill.replace("-", "_"), args.input)
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    _cli()
