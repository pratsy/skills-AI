# Forecast Confidence Model

## Purpose

Estimate the confidence level of a sales forecast based on deal health, stakeholder alignment, urgency, and buying process maturity.

## Business problem

Forecasts often overstate certainty when the deal is actually unstable or poorly qualified. This skill helps revenue teams evaluate the reliability of the forecast.

## Inputs

- deal stage
- stakeholder map
- stage progression history
- close probability factors
- product fit and commitment signals
- deal risk notes

## Outputs

- forecast confidence score
- main reasons for confidence or uncertainty
- recommended action to improve forecast quality
- flags for risk or stochastic timing

## Use cases

- weekly forecast review
- revenue operations analysis
- leadership pipeline checks
- deal review meetings

## Prompt

“You are a senior sales operations strategist. Assess the confidence of this forecast using the provided deal details. Consider deal health, stakeholder alignment, urgency, process clarity, and commercial risk. Return a confidence rating, explain key drivers, and suggest actions that would increase forecast reliability.”

## Example output

- Forecast confidence: Moderate
- Main reasons: deal has clear buying process but stakeholder alignment is still incomplete
- Risk factor: no explicit budget alignment yet
- Action: clarify sponsor, procurement path, and decision timeline before committing to a strong close date

## Evaluation

- Confidence rating reflects actual deal quality
- Risks are grounded in process and stakeholder evidence
- Recommendations support better forecasting discipline
- Output is useful in executive and RevOps review settings
