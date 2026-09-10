# Forecast Bias Detector

## Purpose

Identify whether pipeline forecasts are systematically over-optimistic or under-optimistic, and highlight the patterns that distort forecast quality.

## Inputs

- CRM forecast data
- historical win rates
- deal stage progression
- rep-level forecast submissions
- region or segment performance differences

## Outputs

- forecast bias summary
- likely sources of optimism or conservatism
- risky segments or teams
- correction guidance
- next review actions

## Prompt

“You are a senior RevOps and forecasting analyst. Examine the current pipeline and forecast data for bias. Identify whether optimism or conservatism is being introduced by stage behavior, rep tendencies, or segment-specific patterns, and recommend operational controls for better forecast accuracy.”

## What a strong output includes

- bias pattern definition
- segment or rep-level risk assessment
- likely forecast quality issues
- recommended changes to review discipline or stage management
- action plan for next forecast cycle

## Example result

- Bias pattern: late-stage opportunities are consistently overestimated by one segment
- Recommendation: tighten stage entry criteria and require clearer commitment signals
- Risk: forecast confidence is inflated by historical optimism rather than real deal progression

## Source basis

This skill is informed by public sales forecasting, RevOps governance, and pipeline quality frameworks widely used in B2B operating models.

## References

- Salesforce sales operations and forecasting resources
- Gong pipeline review and forecasting patterns
- Gartner and Forrester sales forecasting research
- public SaaS RevOps and pipeline governance practices
