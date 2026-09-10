# Pipeline Health Monitor

## Why this skill exists

Most pipeline problems are not random. They are predictable.

A sales team can look busy and still have weak revenue quality because the pipeline is overloaded with low-conviction deals, stage imbalance, poor conversion behavior, and weak signal quality. This skill helps detect that early before forecasting and leadership reviews become unreliable.

It is designed to assess whether the pipeline is truly healthy, balanced, and actionable.

## Expert memory layer

Experienced RevOps teams know that pipeline health is not just about volume.

The patterns that matter most include:

- which stages are weak or inconsistent
- where deals sit too long with no clear momentum
- which segments create false confidence because the pipeline is full but low quality
- which source or motion is producing poor conversion patterns
- whether the pipeline reflects actual buying readiness or just activity

This skill encodes those patterns into a structured health review and operational recommendation.

## Business objective

This skill helps the team answer:

> Is the pipeline healthy enough to support revenue commitments, or is it masking weak quality behind a high number of deals?

## Inputs

- stage-by-stage pipeline data
- conversion metrics by segment or motion
- time-to-close trends
- source mix and acquisition quality
- deal quality signals, age, and progression patterns
- forecast confidence or risk flags

## Decision logic

A healthy pipeline should show:

1. balanced flow across stages
2. realistic conversion rates by segment and source
3. healthy speed of progression
4. early visibility into risk or stalled deals
5. enough quality signal to support forecasting confidence

When the pipeline is full but weak, the issue is usually not volume. It is quality management and stage control.

## Common failure patterns

This skill should guard against weak reasoning such as:

- mistaking pipeline volume for pipeline quality
- ignoring stage-specific bottlenecks
- treating all sources as equally reliable
- failing to see stall patterns before forecast review
- accepting weak qualification because the number of deals looks healthy

## Outputs

A useful output should include:

- pipeline health assessment
- weak stage summary
- stage-to-stage conversion issues
- source or segment risk patterns
- operational recommendations to improve quality and forecast confidence

## Example result

### Pipeline health: moderate risk
- Weak stage: qualification to proposal conversion is underperforming
- Pattern: too many deals remain in early stages without strong buying progression
- Source issue: lower-quality inbound leads are inflating volume without improving conversion quality
- Recommendation: tighten qualification criteria, improve SDR-to-AE handoff quality, and review stage-entry standards

### Pipeline health: strong but fragile
- Volume is healthy, but deal progression is concentrated in a few segments
- Risk: forecast confidence is inflated because a small share of deals carries most of the upside
- Recommendation: rebalance acquisition mix and review stage aging across segments

## Recommended prompt

> You are a senior RevOps analyst. Evaluate the pipeline health using the provided stage conversion, deal age, source mix, and quality signals. Identify weak stages, conversion bottlenecks, risks to forecast confidence, and the operational actions needed to improve quality. Focus on realistic revenue execution issues rather than just activity volume.

## Source basis

This skill is informed by public pipeline quality, forecasting, and revenue operations practices, including:

- stage-to-stage conversion review methods
- forecasting discipline and bias awareness
- pipeline hygiene and qualification quality frameworks
- sales ops governance practices for revenue reliability

## References

See [sources-and-frameworks.md](../../sources-and-frameworks.md) for the full source list used across this skill pack.

## Why this is different from a generic prompt

This is not just a “review my pipeline” prompt.

It is designed to detect the real operational issues that hurt revenue quality:

- weak stage progression
- excess volume with poor quality
- false confidence from inflated pipeline coverage
- uneven source performance
- forecast risk hidden behind healthy-looking numbers

That is the expert memory that makes the skill genuinely useful for revenue teams.
