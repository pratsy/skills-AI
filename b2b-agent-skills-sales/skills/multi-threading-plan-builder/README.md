# Multi-Threading Plan Builder

Turn a stakeholder map (see [`stakeholder-map-builder`](../stakeholder-map-builder/README.md)) into a concrete outreach plan that closes specific coverage gaps, sequenced by dependency — instead of a general reminder to "get more people involved."

## When to use this

- A deal is single-threaded (one primary contact) and the rep needs a specific, sequenced plan to fix it — not just the instruction to "multi-thread more."
- A stakeholder map shows a coverage gap (unconfirmed EB, no identified Blocker) and you need the *next three moves*, not a restated risk.
- Pre-committee-meeting prep: which relationships need to exist before the meeting, in what order.

## Methodology

Multi-threading fails most often not from lack of effort but from **wrong sequencing** — trying to reach the Economic Buyer directly before the Champion has built enough internal credibility to make that introduction land. This skill sequences outreach by dependency, not by role importance alone.

**Dependency rule**: an outreach step targeting Role X is only sequenced before a step targeting Role Y if X does not require Y to already be engaged. In practice: Champion relationship-building has no prerequisite; most other roles benefit from a Champion-brokered introduction rather than cold outreach.

## Plan construction

For each coverage gap identified in the stakeholder map, generate a step with:

- **Target role and person** (or "unidentified — needs to be found" if no candidate exists yet)
- **Method**: champion-brokered introduction > mutual-connection outreach > direct cold outreach > event/committee touch (roughly descending order of expected success rate for the same effort, absent contrary evidence)
- **Prerequisite**: what must be true before this step can execute (e.g., "Champion has met with EB internally at least once")
- **Signal of success**: what confirms the step worked, so the plan can be checked off with evidence, not assumed

## Inputs

| Field | Type | Example |
|---|---|---|
| `coverage_gaps` | list[string] | from stakeholder-map-builder output, e.g. `["economic_buyer not confirmed", "no blocker identified"]` |
| `known_contacts` | list[{name, role, relationship_strength}] | current stakeholder map |
| `champion_internal_credibility` | enum | `unproven \| some evidence \| strong` — has the champion demonstrably moved things internally before |

## Worked example

Gap: "economic_buyer not confirmed" (candidate: J. Alvarez, VP Sales Ops — see executive-sponsor-identifier output). Champion internal credibility: "some evidence" (has scheduled 3 internal meetings).

| Step | Target | Method | Prerequisite | Success signal |
|---|---|---|---|---|
| 1 | Champion (M. Chen) | Direct ask: "Can you get 15 min with J. Alvarez to walk through the business case?" | none | Champion agrees and sets a date |
| 2 | J. Alvarez (EB candidate) | Champion-brokered introduction, framed around the business case Alvarez's function owns | Step 1 complete | Alvarez takes the meeting or responds |
| 3 | J. Alvarez | Rep-led follow-up after the intro, focused on decision process/paper process (MEDDPICC gaps) | Step 2 complete, meeting happened | Alvarez confirms next steps or approval process directly |

No step attempts direct cold outreach to Alvarez before the champion-brokered path, because champion credibility is only "some evidence" — strong enough to ask for a warm intro, not yet strong enough to skip straight to independent rep-to-EB outreach.

## Common failure patterns

- Sequencing a cold outreach to the Economic Buyer as step 1 when the champion has enough credibility to broker a warm introduction — this burns the direct-outreach option before it's needed and can make the EB defensive.
- Building a plan with no success signal per step, so "multi-threading" becomes a checklist of attempted touches rather than confirmed relationship progress.
- Treating all coverage gaps as equally urgent instead of sequencing the plan around the gap most likely to block the deal soonest (usually Economic Buyer or Paper Process ahead of a forecasted close date).
- Assuming champion-brokered introduction always outperforms direct outreach — if champion credibility is "unproven," a well-crafted direct approach (e.g., a specific, relevant insight) may be the higher-probability first move.

## Output schema

```json
{
  "plan": [
    {"step": 1, "target_role": "champion", "target_name": "M. Chen", "action": "ask for warm intro to EB", "method": "direct ask", "prerequisite": "none", "success_signal": "champion agrees and sets a date"},
    {"step": 2, "target_role": "economic_buyer", "target_name": "J. Alvarez", "action": "champion-brokered introduction", "method": "champion-brokered", "prerequisite": "step 1 complete", "success_signal": "EB takes the meeting"}
  ],
  "sequencing_rationale": "champion has some internal credibility (3 scheduled meetings) - warrants brokered intro over cold outreach"
}
```

## Recommended prompt

> You are a sales strategist building a multi-threading plan. For each coverage gap below, generate a sequenced outreach step: target role/person, method (champion-brokered introduction, mutual-connection outreach, direct cold outreach, or event/committee touch — in roughly that order of preference absent contrary evidence), the prerequisite that must be true first, and a concrete success signal. Do not sequence a direct or cold-outreach step ahead of a champion-brokered option unless champion internal credibility is "unproven." Return JSON matching the schema above.

## Grounded in

Dependency-sequenced multi-threading practice within enterprise B2B sales execution — the standard advice to "multi-thread" made operational by sequencing outreach around what the champion's current credibility can actually support, rather than treating all outreach paths as equally viable.

See [sources-and-frameworks.md](../../sources-and-frameworks.md) for the pack's general reference list.
