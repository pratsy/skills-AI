from skills_ai.evaluation import evaluate_skill_output, evaluate_skill_from_result


def test_evaluation_renewal_skill():
    output = {
        "risk_score": 7,
        "top_drivers": ["usage_decline", "exec_change"],
        "recommended_actions": ["schedule_exec_review", "resolve_integration_issue"],
    }
    res = evaluate_skill_output("renewal-risk-scorer", output)
    assert res["passed"] is True
    assert res["score"] >= 80


def test_evaluation_shape_works_on_result_object():
    result = {
        "skill": "brand-positioning-synthesizer",
        "result": {
            "positioning_summary": "Faster time-to-insight",
            "key_differentiators": ["speed", "reduced engineering overhead"],
            "message_pillars": ["speed", "operational clarity"],
        },
    }
    res = evaluate_skill_from_result(result)
    assert res["passed"] is True
    assert res["skill"] == "brand-positioning-synthesizer"
