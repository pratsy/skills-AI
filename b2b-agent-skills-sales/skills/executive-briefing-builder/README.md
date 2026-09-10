# Executive Briefing Builder

Structure an executive briefing using the Pyramid Principle (Barbara Minto) — answer first, then supporting arguments, then evidence — instead of a chronological narrative that makes a time-pressed executive dig for the point.

## When to use this

- Preparing a one-page or verbal briefing for an economic buyer or exec sponsor ahead of a meeting.
- Past exec conversations have gone long because the story was told chronologically instead of leading with the conclusion.
- You need to brief an internal exec (your own leadership) on deal status before they join a customer call.

## Methodology

The Pyramid Principle inverts how most people naturally write: state the governing conclusion first, then the (usually 3) supporting arguments that justify it, each backed by evidence — instead of building up to the conclusion through narrative or chronology. Executives read top-down and stop as soon as they have what they need; a pyramid structure means they get the answer even if they only read the first line.

```
Level 1 — Governing Thought: the single conclusion/ask, one sentence.
Level 2 — Supporting Arguments (usually 3): each a complete, standalone reason for the Level 1 conclusion — the MECE test (mutually exclusive, collectively exhaustive) applies: no overlap, no major gap.
Level 3 — Evidence: the specific data/facts backing each Level 2 argument, only as much as needed to be credible, not exhaustive.
```

## Construction rule

Write the Governing Thought last, but place it first — draft the supporting arguments and evidence, then distill the single sentence they collectively prove, and put that at the top. If the Governing Thought can't be stated as a single clear sentence, the underlying arguments likely aren't focused enough yet.

## Inputs

| Field | Type | Example |
|---|---|---|
| `audience` | string | `"buyer's CFO"` or `"our VP Sales"` |
| `purpose` | string | e.g. `"secure approval to proceed to contract"` |
| `key_facts` | list[string] | raw facts/evidence available |
| `desired_ask` | string | the specific action wanted from this audience |

## Worked example

Audience: buyer's CFO, ahead of a budget approval conversation. Purpose: secure sign-off. Key facts: forecast misses cost ~$180K/year in re-planning per the VP Sales' own estimate; 3 reference customers of similar size report 20-25% variance reduction; implementation is 15 minutes, no IT involvement required; price is $60K/year.

**Governing Thought**: "Approving this investment addresses a $180K/year cost at roughly a third of that price, with no IT burden."

**Supporting Arguments** (MECE — cost, proof, implementation risk, each independent):
1. The cost of the status quo is quantified and material ($180K/year, per your own VP Sales' estimate).
2. The expected improvement is evidenced by comparable customers (20-25% variance reduction, 3 references), not a vendor claim alone.
3. Implementation risk is minimal (15-minute setup, no IT resourcing required) — this is not a project that competes with other IT priorities.

**Evidence** under each: the specific $45K x 4 breakdown; the named reference accounts and their reported results; the setup process detail.

## Common failure patterns

- Leading with company background or product overview before the ask — burns the first (and sometimes only) attention window an executive gives the document.
- Supporting arguments that overlap (e.g., two of three arguments both really being about cost) instead of covering genuinely distinct angles — fails the MECE test and reads as padded.
- Including all available evidence under each argument instead of the minimum credible set — executives want enough to trust the claim, not the full analysis.
- Writing the Governing Thought as a topic ("update on the deal") instead of an actual conclusion/ask ("approving this addresses X at Y cost") — a topic doesn't tell the reader what to do with the information.

## Output schema

```json
{
  "audience": "buyer's CFO",
  "governing_thought": "Approving this investment addresses a $180K/year cost at roughly a third of that price, with no IT burden.",
  "supporting_arguments": [
    {"argument": "The cost of the status quo is quantified and material.", "evidence": ["$45K x 4 occurrences/year, per VP Sales estimate"]},
    {"argument": "Expected improvement is evidenced by comparable customers, not a vendor claim.", "evidence": ["3 reference accounts, 20-25% variance reduction"]},
    {"argument": "Implementation risk is minimal.", "evidence": ["15-minute setup, no IT resourcing required"]}
  ],
  "mece_check": "pass - cost, proof, and risk are independent angles with no overlap"
}
```

## Recommended prompt

> You are an executive communications strategist using the Pyramid Principle. Given the audience, purpose, and key facts below, draft a single-sentence Governing Thought that states the conclusion/ask directly. Then generate 2-4 supporting arguments that are mutually exclusive and collectively exhaustive (MECE) — check explicitly for overlap between arguments. Under each argument, list only the minimum evidence needed for credibility. Return JSON matching the schema above.

## Grounded in

Barbara Minto's Pyramid Principle, the standard structure for executive communication in management consulting, used here so the executive gets the conclusion and reasoning even if they only read the first sentence.

See [sources-and-frameworks.md](../../sources-and-frameworks.md) for the pack's general reference list.
