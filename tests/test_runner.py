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
        "OPPORTUNITY CONTEXT": {"Company": "Acme Corp", "Deal size": "$600K", "Timeline": "8 weeks"},
        "PRIMARY CONTACT": {"Name": "Sarah Chen"}
    }
    # write a temp file
    with open("tests/_tmp_input.json", "w", encoding="utf-8") as f:
        json.dump(input_data, f)

    res = run_skill("executive_sponsor_identifier", "tests/_tmp_input.json", provider=MockProvider())
    assert res["skill"] == "executive-sponsor-identifier"
    assert "result" in res or "raw" in res
