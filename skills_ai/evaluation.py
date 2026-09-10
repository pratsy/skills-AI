from __future__ import annotations

from typing import Any, Dict, List


SKILL_EXPECTED_FIELDS = {
    "renewal-risk-scorer": ["risk_score", "top_drivers", "recommended_actions"],
    "executive-sponsor-identifier": ["executive_sponsor", "buying_committee", "engagement_plan"],
    "brand-positioning-synthesizer": ["positioning_summary", "key_differentiators", "message_pillars"],
    "audience-segmentation-optimizer": ["prioritized_segments", "channel_recommendations"],
    "nurture-sequence-architect": ["sequence_steps", "trigger_logic"],
}


def _normalize_result(value: Any) -> Dict[str, Any]:
    if isinstance(value, dict):
        return value
    if isinstance(value, str):
        try:
            import json

            return json.loads(value)
        except Exception:
            return {"raw": value}
    return {"raw": value}


def evaluate_skill_output(skill_name: str, output: Any) -> Dict[str, Any]:
    """Check whether an LLM output contains the minimum expected structure.

    This is intentionally lightweight and deterministic, so it works in CI without
    external model calls.
    """
    normalized = _normalize_result(output)
    expected_fields = SKILL_EXPECTED_FIELDS.get(skill_name, [])

    checks: List[str] = []
    missing: List[str] = []
    score = 0

    if not isinstance(normalized, dict):
        return {"skill": skill_name, "passed": False, "score": 0, "checks": ["output_not_object"], "missing_fields": expected_fields}

    for field in expected_fields:
        if field in normalized:
            checks.append(f"field_present:{field}")
            score += 20
        else:
            missing.append(field)
            checks.append(f"field_missing:{field}")

    if not missing:
        score += 20
        checks.append("all_required_fields_present")

    passed = len(missing) == 0
    score = min(score, 100)

    return {
        "skill": skill_name,
        "passed": passed,
        "score": score,
        "checks": checks,
        "missing_fields": missing,
    }


def evaluate_skill_from_result(skill_result: Dict[str, Any]) -> Dict[str, Any]:
    """Given a run_skill result object, select the correct output payload and score it."""
    skill_name = skill_result.get("skill", "unknown")
    result = skill_result.get("result", skill_result.get("raw", {}))
    return evaluate_skill_output(skill_name, result)
