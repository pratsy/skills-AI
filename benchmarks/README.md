# Benchmarking and calibration

This folder stores small benchmark datasets used to evaluate skill output quality — whether a skill's output has the structure and specificity expected for real operational use, checked deterministically (no model call required) via `sdk.evaluation`.

## Scope: 4 skills here, all 45 covered elsewhere

`sample_dataset.json` holds realistic, human-readable input/expected-output pairs for 4 skills — one per domain pack (`renewal-risk-scorer`, `audience-segmentation-optimizer`, `pipeline-health-monitor`, `market-sizing-modeler`) — so someone skimming the repo can see what a passing output actually looks like without reading a full README.

This is deliberately not expanded to all 45. Doing that would mean copy-pasting each skill's "Output schema" example from its README into a second file, which creates exactly the failure mode this repo has been cleaned up from elsewhere: two places holding the same information that can silently drift apart when only one gets updated.

**Schema-shape correctness for all 45 skills is already fully covered**, without that duplication risk: `tests/test_evaluation.py::test_evaluation_covers_all_45_skills` builds a synthetic example for every skill directly from `sdk.evaluation.SKILL_EXPECTED_FIELDS` (itself extracted from each skill's own README) and asserts it passes. It runs in CI on every push and can't drift out of sync, because there's no second copy of the schema to forget to update — it reads the same dict the evaluator uses. If you want to check a specific skill's full expected shape, that dict (or the skill's own README) is the source of truth, not this file.

## How to use

```bash
PYTHONPATH=. python3 - <<'PY'
import json
from sdk.evaluation import evaluate_skill_output

dataset = json.load(open("benchmarks/sample_dataset.json"))
for case in dataset:
    result = evaluate_skill_output(case["skill"], case["expected_output"])
    print(case["skill"], "->", result["passed"], result["score"])
PY
```

To evaluate a real skill run instead of a benchmark fixture, use `evaluate_skill_from_result()` on the output of `sdk.runner.run_skill(...)`.
