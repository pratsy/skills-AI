import json
import pathlib
import pytest
from sdk.runner import run_skill, run_generic_skill, _strip_frontmatter
from sdk.providers import MockProvider


def test_run_renewal_risk_scorer():
    path = "examples/fixtures/renewal_input.json"
    res = run_skill("renewal_risk_scorer", path, provider=MockProvider())
    assert res["skill"] == "renewal-risk-scorer"
    assert "result" in res
    assert isinstance(res["result"].get("risk_score"), int) or isinstance(res["result"].get("risk_score"), int)


def test_run_executive_sponsor_identifier():
    # Use minimal input for executive sponsor skill
    input_data = {
        "deal_size": "$600K",
        "champion_notes": "Sarah Chen has named a VP as the likely approver",
        "candidates": [
            {"name": "Sarah Chen", "title": "RevOps Manager", "engagement_evidence": "scheduled 3 internal meetings"}
        ],
    }
    # write a temp file
    with open("tests/_tmp_input.json", "w", encoding="utf-8") as f:
        json.dump(input_data, f)

    res = run_skill("executive_sponsor_identifier", "tests/_tmp_input.json", provider=MockProvider())
    assert res["skill"] == "executive-sponsor-identifier"
    assert "result" in res or "raw" in res


def test_run_marketing_skills():
    # brand positioning
    res1 = run_skill("brand_positioning_synthesizer", "examples/fixtures/brand_positioning_input.json", provider=MockProvider())
    assert res1["skill"] == "brand-positioning-synthesizer"

    # audience segmentation
    res2 = run_skill("audience_segmentation_optimizer", "examples/fixtures/audience_segmentation_input.json", provider=MockProvider())
    assert res2["skill"] == "audience-segmentation-optimizer"

    # nurture sequence
    res3 = run_skill("nurture_sequence_architect", "examples/fixtures/nurture_sequence_input.json", provider=MockProvider())
    assert res3["skill"] == "nurture-sequence-architect"


def _all_skill_slugs():
    packs = [
        "b2b-agent-skills-gtm",
        "b2b-agent-skills-marketing",
        "b2b-agent-skills-revops",
        "b2b-agent-skills-sales",
    ]
    slugs = []
    for pack in packs:
        for readme in pathlib.Path(pack, "skills").glob("*/README.md"):
            slugs.append(readme.parent.name)
    return sorted(slugs)


def test_all_45_skills_are_documented():
    assert len(_all_skill_slugs()) == 45


def test_all_45_skills_have_a_claude_skill():
    for slug in _all_skill_slugs():
        skill_md = pathlib.Path(".claude", "skills", slug, "SKILL.md")
        assert skill_md.exists(), f"missing .claude/skills/{slug}/SKILL.md"


def test_all_45_skills_run_through_the_generic_runner():
    for slug in _all_skill_slugs():
        skill_name = slug.replace("-", "_")
        res = run_skill(skill_name, input_path=None, provider=MockProvider())
        assert res["skill"] == slug
        assert "result" in res or "raw" in res


def test_generic_skill_raises_a_clear_error_for_an_unknown_skill():
    with pytest.raises(FileNotFoundError):
        run_generic_skill("not_a_real_skill", {}, MockProvider())


def test_strip_frontmatter_removes_yaml_block():
    text = "---\nname: x\ndescription: y\n---\nBody content here.\n"
    assert _strip_frontmatter(text) == "Body content here."
