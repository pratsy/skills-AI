# Domain Memory Checklist

Use this checklist when building or improving a skill so it does not become generic.

## 1. Business clarity
- Is the business problem clear?
- Is the target decision obvious?
- Is the output actually useful to an operator?

## 2. Context quality
- Does the skill include the right signals for the domain?
- Does it account for role-specific context?
- Does it distinguish noise from signal?

## 3. Failure awareness
- Does it identify the most common failure modes?
- Does it warn about false positives and false negatives?
- Does it show uncertainty when evidence is weak?

## 4. Source grounding
- Are the recommendations connected to public frameworks or research?
- Is the skill based on practitioner logic rather than empty prompts?
- Are the sources named and documented?

## 5. Action orientation
- Does the output tell the user what to do next?
- Is the recommendation practical and operationally realistic?
- Does it tell the user what to validate before taking action?

## 6. Update path
- If the named methodology turns out to be wrong for a case, is it clear which section to fix (the scoring model, the failure patterns, or the worked example)?
- Does the skill cite a specific enough source (`sources-and-frameworks.md`) that a contributor could check whether it's still accurate?

## 7. Distinctiveness
- Is this skill more than a generic summary prompt?
- Does it encode domain-specific expertise?
- Does it look like something a real expert would actually use?

## 8. Trust and defensibility
- Would a revenue leader trust the output in a review meeting?
- Would a marketer or RevOps leader feel it reflects real business logic?
- Would a technical builder understand why the skill is valuable?

If a skill cannot answer these questions clearly, it is too generic.
