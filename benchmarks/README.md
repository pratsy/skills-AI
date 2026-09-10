# Benchmarking and calibration

This folder stores small benchmark datasets used to evaluate skill output quality.

## Scope

The goal is to test if a skill returns the right structure and enough specificity for real operational use.

## Current dataset

- `sample_dataset.json` contains benchmark examples for the renewal risk scorer and executive sponsor identifier.

## How to use

```bash
PYTHONPATH=. python - <<'PY'
from skills_ai.evaluation import evaluate_skill_output
sample = {
    'risk_score': 7,
    'top_drivers': ['usage_decline'],
    'recommended_actions': ['exec_review']
}
print(evaluate_skill_output('renewal-risk-scorer', sample))
PY
```
