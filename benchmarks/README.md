# Benchmarking and calibration

This folder stores small benchmark datasets used to evaluate skill output quality — whether a skill's output has the structure and specificity expected for real operational use, checked deterministically (no model call required) via `skills_ai.evaluation`.

## Scope

`sample_dataset.json` currently covers **4 of the 45 skills**, one per domain pack (`renewal-risk-scorer`, `audience-segmentation-optimizer`, `pipeline-health-monitor`, `market-sizing-modeler`), each with a real input/expected-output pair matching that skill's documented worked example. This is a starting evaluation set, not full coverage — `skills_ai.evaluation.SKILL_EXPECTED_FIELDS` already defines the expected output shape for all 45 skills (pulled directly from each skill's own "Output schema" section), so extending this dataset to more skills is mostly a matter of adding entries, not new infrastructure.

## How to use

```bash
PYTHONPATH=. python3 - <<'PY'
import json
from skills_ai.evaluation import evaluate_skill_output

dataset = json.load(open("benchmarks/sample_dataset.json"))
for case in dataset:
    result = evaluate_skill_output(case["skill"], case["expected_output"])
    print(case["skill"], "->", result["passed"], result["score"])
PY
```

To evaluate a real skill run instead of a benchmark fixture, use `evaluate_skill_from_result()` on the output of `skills_ai.runner.run_skill(...)`.
