# Persona Insight Extractor

Extract structured persona attributes from qualitative source material (win/loss interviews, sales call transcripts, support tickets) using the Jobs-to-be-Done interview framework, instead of writing personas from internal assumption or a template.

## When to use this

- Current personas are demographic templates ("Sarah, 35, VP of Sales") with no evidence trail — nobody can point to the interview or ticket that produced any given trait.
- You have a backlog of call transcripts or win/loss interviews and need to convert them into usable persona attributes.
- Messaging or sales enablement feels off because the persona doesn't match what buyers actually say in calls.

## Methodology

JTBD interview analysis extracts four things from raw qualitative text, and — critically — each must be traceable to a specific quote, not inferred:

- **Job**: what the buyer was actually trying to accomplish (functional job) and what that meant for them personally/socially (emotional/social job).
- **Trigger**: the specific event that made the status quo unacceptable ("push") and what pulled them toward evaluating a new solution ("pull").
- **Anxieties**: what almost stopped them from buying (risk, switching cost, internal politics).
- **Success criteria**: how they'll know, concretely, that the purchase worked.

## Extraction process

1. Tag every source passage with which of the four categories it belongs to (a passage can span more than one).
2. For each tagged passage, extract the attribute as a short phrase plus the verbatim quote it came from.
3. Cluster attributes across sources — an attribute mentioned by only 1 of 10 interviewees is an anecdote; one appearing in 6+ of 10 is a persona-defining pattern.
4. Only promote an attribute to the persona definition if it clears a frequency threshold (recommend: appears in ≥40% of sources for personas built from 8+ interviews; flag as `provisional` below that).

## Inputs

| Field | Type | Example |
|---|---|---|
| `source_transcripts` | list[{source_id, type, persona_role, text}] | raw interview/call/ticket text |
| `persona_role` | string | which role these sources represent, e.g. `"VP Sales"` |
| `minimum_frequency_threshold` | float | default 0.4 |

## Worked example

10 win-loss interviews with VPs of Sales. Passages tagged "trigger":

- 7 of 10 mention some version of: *"I got burned by a forecast miss in front of the board."* → frequency 70% → **persona-defining trigger**: "a public forecast miss that damaged credibility with leadership."
- 2 of 10 mention: *"a new CRO wanted to standardize tooling."* → frequency 20% → **provisional**, not yet persona-defining.

Passages tagged "anxiety": 6 of 10 mention *"worried reps wouldn't actually use another tool."* → 60% → persona-defining anxiety: "adoption risk — reps ignoring yet another tool."

Resulting persona fragment: *Trigger: a public forecast miss that damaged credibility with leadership (70% of sources, evidence: [quote IDs]). Anxiety: fear reps won't adopt another tool on top of existing ones (60% of sources, evidence: [quote IDs]).*

## Common failure patterns

- Writing persona attributes from the analyst's summary impression instead of tagging and counting actual passages — this reintroduces the assumption problem the method is meant to remove.
- Promoting a vivid, memorable quote to persona-defining status because it's a good story, when it only appears once in the source set.
- Merging functional job ("evaluate forecasting tools") with emotional job ("avoid looking unprepared in front of the board") into one line — they drive different messaging and should stay separate.
- Building a persona from a source set that's all closed-won interviews — closed-lost and churn interviews often reveal anxieties a win-only sample never surfaces.

## Output schema

```json
{
  "persona_role": "VP Sales",
  "source_count": 10,
  "attributes": [
    {"category": "trigger", "attribute": "a public forecast miss that damaged credibility with leadership", "frequency": 0.70, "status": "persona-defining", "evidence_quotes": ["...I got burned by a forecast miss in front of the board..."]},
    {"category": "trigger", "attribute": "new CRO standardizing tooling", "frequency": 0.20, "status": "provisional", "evidence_quotes": ["...a new CRO wanted to standardize tooling..."]}
  ]
}
```

## Recommended prompt

> You are a JTBD researcher. Read the interview/call transcripts below, all representing the persona role given. Tag each relevant passage as job (functional or emotional), trigger, anxiety, or success criteria, and extract a short attribute phrase with the supporting verbatim quote. Cluster attributes across sources and compute frequency (% of sources mentioning it). Mark attributes at or above the given threshold as "persona-defining" and those below as "provisional." Do not include any attribute without at least one supporting quote. Return JSON matching the schema above.

## Grounded in

The Jobs-to-be-Done interview method (Clayton Christensen; popularized for B2B by Bob Moesta and Chris Spiek) for extracting evidence-based persona attributes from qualitative source material, applied with a frequency threshold so pattern-level findings are distinguished from single-source anecdotes.

See [sources-and-frameworks.md](../../sources-and-frameworks.md) for the pack's general reference list.
