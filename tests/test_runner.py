import json
from skills_ai.runner import run_skill
from skills_ai.providers import MockProvider


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
