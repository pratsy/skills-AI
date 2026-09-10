import json
from sdk.evaluation import evaluate_skill_output, evaluate_skill_from_result, SKILL_EXPECTED_FIELDS


def test_evaluation_renewal_skill():
    output = {
        "account_id": "acct_7734",
        "usage_decline_score": 100,
        "engagement_breadth_score": 85,
        "stakeholder_continuity_score": 100,
        "sentiment_support_score": 15,
        "renewal_risk_score": 79.25,
        "risk_band": "critical",
        "primary_driver": "champion departed with no replacement",
        "recommended_action": "executive-level proactive outreach this week",
    }
    res = evaluate_skill_output("renewal-risk-scorer", output)
    assert res["passed"] is True
    assert res["score"] == 100


def test_evaluation_shape_works_on_result_object():
    result = {
        "skill": "brand-positioning-synthesizer",
        "result": {
            "target_market_ranked": [{"segment": "mid-market", "total": 14}],
            "selected_target_market": "mid-market sales orgs",
            "unique_attributes": ["explainable scoring"],
            "primary_competitive_alternative": "black-box forecasting tools",
            "category": "AI deal risk scoring",
            "positioning_statement": "For mid-market sales teams...",
        },
    }
    res = evaluate_skill_from_result(result)
    assert res["passed"] is True
    assert res["skill"] == "brand-positioning-synthesizer"


def test_evaluation_scores_partial_completeness():
    # deal-risk-assessor expects 7 fields; give it 4 of them.
    output = {
        "deal_id": "opp_1",
        "pillar_scores": {},
        "total_score": 14,
        "risk_band": "moderate",
    }
    res = evaluate_skill_output("deal-risk-assessor", output)
    assert res["passed"] is False
    assert 0 < res["score"] < 100
    assert set(res["missing_fields"]) == {"single_point_of_failure", "forecast_recommendation", "priority_action"}


def test_evaluation_covers_all_45_skills():
    assert len(SKILL_EXPECTED_FIELDS) == 45
    for skill_name, fields in SKILL_EXPECTED_FIELDS.items():
        assert len(fields) >= 1, f"{skill_name} has no expected fields"
        res = evaluate_skill_output(skill_name, {f: "x" for f in fields})
        assert res["passed"] is True, f"{skill_name} should pass when every expected field is present"
        assert res["score"] == 100


def test_benchmark_sample_dataset_matches_current_schema():
    dataset = json.load(open("benchmarks/sample_dataset.json"))
    assert len(dataset) >= 1
    for case in dataset:
        res = evaluate_skill_output(case["skill"], case["expected_output"])
        assert res["passed"] is True, f"{case['skill']}: benchmark expected_output is out of sync with SKILL_EXPECTED_FIELDS ({res['missing_fields']})"
