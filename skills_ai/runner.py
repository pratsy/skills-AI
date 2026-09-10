import argparse
import json
import importlib
from pathlib import Path
from .providers import MockProvider, get_provider_from_env


def run_skill(skill_name: str, input_path: str = None, provider=None):
    if provider is None:
        provider = get_provider_from_env()

    # import skill module from skills_ai.skills
    module_name = f"skills_ai.skills.{skill_name}"
    try:
        mod = importlib.import_module(module_name)
    except Exception as e:
        raise ImportError(f"Could not import skill module {module_name}: {e}")

    input_data = {}
    if input_path:
        with open(input_path, "r", encoding="utf-8") as f:
            input_data = json.load(f)

    result = mod.run(input_data, provider)
    return result


def _cli():
    parser = argparse.ArgumentParser(description="Run a Skill locally")
    parser.add_argument("skill", help="skill module name (e.g. renewal_risk_scorer)")
    parser.add_argument("--input", help="path to JSON input file", dest="input", default=None)
    args = parser.parse_args()

    out = run_skill(args.skill, args.input)
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    _cli()
