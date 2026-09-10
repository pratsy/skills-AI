from __future__ import annotations

from typing import Any, Dict, List


# Top-level output keys for all 45 skills, extracted from each skill's own
# "Output schema" section (b2b-agent-skills-*/skills/<slug>/README.md) so this
# stays a direct reflection of what each skill actually documents, not a
# separately-maintained guess.
SKILL_EXPECTED_FIELDS = {
    "abm-account-priority-ranker": ["accounts_ranked", "tier_counts"],
    "account-plan-generator": ["account_name", "owned", "whitespace_ranked"],
    "account-priority-matrix-builder": ["segments_scored", "planning_cycle"],
    "ad-copy-variant-generator": ["variants", "test_design"],
    "attribution-model-reviewer": ["channels_analyzed"],
    "audience-segmentation-optimizer": ["scored_accounts", "tier_summary", "data_quality_flags"],
    "brand-perception-monitor": ["stages", "bottleneck_stage", "diagnosis"],
    "brand-positioning-synthesizer": ["target_market_ranked", "selected_target_market", "unique_attributes", "primary_competitive_alternative", "category", "positioning_statement"],
    "campaign-performance-diagnostician": ["funnel_conversion_rates", "primary_bottleneck", "diagnosis_type", "recommended_action"],
    "champion-advocacy-builder": ["contact_name", "signal_scores", "mobilizer_score", "classification", "next_enablement_need"],
    "competitive-differentiation-coach": ["competitor", "differentiators_ranked", "recommended_lead_claim", "response_framing", "held_in_reserve"],
    "competitor-monitor": ["competitor", "signal_description", "move_type", "overlap_with_icp", "confirmation_level", "related_moves_last_quarter", "materiality_score", "materiality_band", "recommended_action"],
    "competitor-signal-clusterer": ["themes"],
    "content-gap-analysis-agent": ["coverage_matrix", "overall_coverage_pct", "priority_gaps"],
    "crm-data-cleaner": ["record_id", "completeness", "accuracy_pass", "consistency_pass", "timeliness_pass", "record_quality_score", "business_context", "cleanup_priority", "issues"],
    "customer-journey-friction-audit": ["touchpoints_ranked"],
    "deal-committee-readiness-coach": ["deal_id", "readiness_score_pct", "readiness_band", "unanswered_questions"],
    "deal-risk-assessor": ["deal_id", "pillar_scores", "total_score", "risk_band", "single_point_of_failure", "forecast_recommendation", "priority_action"],
    "discovery-question-generator": ["persona", "sequence", "coaching_note"],
    "executive-briefing-builder": ["audience", "governing_thought", "supporting_arguments", "mece_check"],
    "executive-sponsor-identifier": ["candidates_ranked", "primary_eb_target", "rationale"],
    "forecast-bias-detector": ["rep_id", "period_bias_ratios", "trailing_bias_score", "consistency", "classification", "recommended_correction_factor", "coaching_focus"],
    "forecast-confidence-model": ["deal_id", "meddpicc_score", "time_in_stage_ratio", "rep_commit_accuracy", "checks", "forecast_category", "reason"],
    "icp-refinement-agent": ["attribute_lift_ranking", "revised_icp", "contradictions_with_current_icp"],
    "landing-page-copy-optimizer": ["message_match_score", "message_match_status", "on_page_checklist", "on_page_score", "priority_fix"],
    "lead-prioritization-agent": ["lead_id", "fit_score", "intent_score", "quadrant", "routing", "rationale"],
    "lifecycle-email-optimizer": ["lifecycle_stage", "deliverability_layer", "open_layer", "click_layer", "diagnosis", "recommended_action"],
    "market-shift-monitor": ["signal_description", "category", "breadth_score", "velocity_score", "durability_score", "shift_materiality", "shift_band", "recommended_response"],
    "market-sizing-modeler": ["top_down", "bottom_up", "divergence_pct", "divergence_verdict", "recommended_primary_estimate", "som"],
    "market-trend-signal-reporter": ["candidate_trend", "independent_source_count", "corroborating_signal_types", "observed_over_multiple_periods", "signal_to_noise_score", "classification", "reporting_recommendation"],
    "messaging-clarity-auditor": ["claims_scored", "asset_score", "priority_fixes"],
    "multi-threading-plan-builder": ["plan", "sequencing_rationale"],
    "negotiation-readiness-coach": ["our_batna", "buyer_batna", "concessions_ranked"],
    "nurture-sequence-architect": ["sequence_name", "steps", "reengagement_track_trigger"],
    "objection-response-coach": ["objection_text", "classification", "explore_question", "response_if_price", "response_if_value_gap"],
    "persona-insight-extractor": ["persona_role", "source_count", "attributes"],
    "pipeline-health-monitor": ["coverage_ratio", "stage_health", "overall_health", "primary_driver", "recommended_action"],
    "pricing-justification-builder": ["annual_cost_of_status_quo", "expected_improvement_pct", "improvement_source", "expected_annual_value", "annual_price", "roi_ratio", "payback_period_months", "credibility_flag", "interpretation"],
    "renewal-risk-scorer": ["account_id", "usage_decline_score", "engagement_breadth_score", "stakeholder_continuity_score", "sentiment_support_score", "renewal_risk_score", "risk_band", "primary_driver", "recommended_action"],
    "sales-handoff-quality-auditor": ["handoff_type", "fields_scored", "completeness_score", "quality_band", "critical_gaps", "recommended_action"],
    "stakeholder-map-builder": ["deal_id", "contacts_mapped", "coverage_gaps", "single_threading_risk", "blocker_identified", "priority_action"],
    "strategic-account-priority-ranker": ["accounts_ranked", "recommended_list_size", "sponsorship_capacity_basis"],
    "territory-prioritization-agent": ["accounts_ranked", "tiering"],
    "value-proposition-tester": ["customer_profile", "candidates_scored", "recommended_lead_message"],
    "win-loss-theme-clusterer": ["themes_ranked", "top_priority_theme", "sample_size"],
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

    if not isinstance(normalized, dict):
        return {"skill": skill_name, "passed": False, "score": 0, "checks": ["output_not_object"], "missing_fields": expected_fields}

    for field in expected_fields:
        if field in normalized:
            checks.append(f"field_present:{field}")
        else:
            missing.append(field)
            checks.append(f"field_missing:{field}")

    if not missing and expected_fields:
        checks.append("all_required_fields_present")

    passed = len(missing) == 0
    # Score scales with the fraction of expected top-level fields present, so
    # a skill with 2 expected fields and one with 9 are judged on the same basis.
    score = round((len(expected_fields) - len(missing)) / len(expected_fields) * 100) if expected_fields else 0

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
