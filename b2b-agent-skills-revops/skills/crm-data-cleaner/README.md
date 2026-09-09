# CRM Data Cleaner

## Purpose

Detect inconsistencies and quality issues in CRM data and recommend fixes that improve operational quality and reporting reliability.

## Business problem

CRM data is often incomplete, duplicated, or inconsistent. That weakens qualification, reporting, forecasting, and handoff quality.

## Inputs

- CRM data set
- field mappings
- contact and account records
- owner assignments
- historical activity data

## Outputs

- data quality summary
- common issue types
- recommended fixes
- priority clean-up actions

## Use cases

- CRM hygiene reviews
- system cleanup before reporting cycles
- sales process standardization
- data migration quality checks

## Prompt

“You are a RevOps data quality analyst. Review the provided CRM records and flag data quality issues that reduce sales effectiveness or forecast reliability. Identify duplicates, missing information, inconsistent fields, and risky ownership patterns. Return a prioritized remediation list with rationale.”

## Example output

- Duplicate account records on enterprise clients
- Missing stage and close dates for active opportunities
- Inconsistent owner assignment across multiple business units
- Priority action: standardize field definitions and fix owner assignments before the next forecast cycle

## Evaluation

- Issues are prioritized by operational impact
- Recommendations align with reporting and sales process quality
- Output supports both sales and RevOps goals
- It helps prevent bad data from compromising decisions
