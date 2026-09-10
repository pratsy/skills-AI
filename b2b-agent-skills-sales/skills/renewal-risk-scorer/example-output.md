# Renewal Risk Scorer — Example Output

## Sample Input

```
Account Name: CloudOps Solutions Inc.
Renewal Date: 2026-11-15
Contract Value: $185,000 ARR
Years as Customer: 2.5
Industry: DevOps / Infrastructure

Product Usage:
- Login frequency: Weekly
- Feature adoption rate: 65%
- Monthly active users: 18 of 25 licensed seats (72%)
- Usage trend (last 90 days): Down 22%
- Core workflows utilized: Infrastructure monitoring, alert management
- Unused modules: Advanced analytics, predictive capacity planning

Stakeholder Health:
- Primary contact engagement: Medium (monthly calls)
- Economic buyer accessibility: Low (delegated to IT manager)
- Executive sponsor change: Yes - CTO left 6 weeks ago, new CTO hired but not yet onboarded to platform
- Support ticket escalation: 3 tickets in last 90 days, 1 critical issue unresolved for 28 days
- NPS or satisfaction score: 6/10 (collected 8 weeks ago)

Commercial Signals:
- Expansion activity: None in 18 months
- Budget cycle alignment: Misaligned - procurement discussing budget freeze for Q4 and Q1
- Competitive pressure observed: Yes - saw competitive tool demo on shared calendar invite
- Pricing sensitivity noted: Yes - asked about volume discounts in last call
- Stakeholder turnover: Yes - CTO departure; 2 infrastructure engineers have left

Support and Success History:
- Support response quality: Average (48-72 hour resolution, no SLA breaches)
- Critical issues unresolved: 1 (API integration issue, 28 days open)
- Customer success engagement: Reactive (only contact on support cases)
- Onboarding completion: Yes - initial onboarding done 2 years ago
- Training and enablement participation: Low (no team members attended recent webinar)

Recent Activity:
- Last business review: 6 months ago
- Last expansion conversation: 18 months ago
- Reported use-case changes: Yes - infrastructure team is consolidating tools, looking at integrated platform vendors
- Mentions of alternative solutions: Yes - competitive platform mentioned, also considering open-source alternative
```

## Example Output

```
RENEWAL RISK ASSESSMENT

Account: CloudOps Solutions Inc.
Renewal Date: 2026-11-15
Contract Value: $185,000 ARR

RISK SCORE: 7.5
Risk Level: HIGH

TOP RISK DRIVERS:

1. Economic Buyer Disengagement & CTO Transition
   - Evidence: Original economic buyer (CTO) departed 6 weeks ago; new CTO in role but not yet familiar with platform capabilities or business case. Primary point of contact is now IT manager without budget authority.
   - Implication: Without a champion at the executive level who understands the value, renewal will likely stall in procurement or be subject to cost-reduction pressure. New CTO will evaluate fit through lens of current tool consolidation initiative rather than historical investment rationale.

2. Usage Decline Coupled with Stakeholder Churn
   - Evidence: Usage down 22% over 90 days; 2 infrastructure engineers have departed; only 72% of licensed seats active. Advanced analytics and predictive planning modules completely unused.
   - Implication: Loss of key users suggests organizational knowledge loss and reduced platform adoption. Team may be consolidating to fewer tools or reducing headcount, both indicating lower utilization of current solution.

3. Unresolved Critical Issue + Reactive Support Model
   - Evidence: API integration issue open for 28 days unresolved; customer success engagement is reactive-only (no proactive touchpoints); no business review in 6 months.
   - Implication: Unresolved technical issue is likely creating daily frustration and feeding the narrative that alternatives (open-source, competitor platform) might be simpler. Lack of proactive support means no one is actively coaching the team on value realization.

4. Active Exploration of Alternatives & Consolidation Initiative
   - Evidence: Infrastructure team is consolidating tools; competitive platform demo observed; open-source alternative being considered; pricing sensitivity raised in last call.
   - Implication: Account is in active evaluation mode for renewal. They are not automatically renewing; they are comparing options. Any delay on our side or continued friction will tip the decision.

5. Budget Misalignment & Procurement Headwind
   - Evidence: Procurement discussing budget freeze for Q4 and Q1; renewal date lands in Q4 when budget is tightest; no executive sponsor to push renewal through budget constraints.
   - Implication: Even if product value is solid, timing and budget climate create friction. Without strong sponsor, renewal will compete against cost reduction initiatives.

PROTECTIVE FACTORS:
- Contract tenure of 2.5 years suggests some installed base and integration history
- Feature adoption rate of 65% is reasonable; core monitoring and alert workflows are still in use
- Support response quality is solid (average 48-72 hours)
- No immediate threats of immediate termination or harsh public feedback

RECOMMENDED INTERVENTIONS:

1. Immediate (within 2 weeks):
   - Action: Schedule executive business review with new CTO + CFO/procurement to reintroduce platform value and renewal timeline; frame as strategic infrastructure decision, not routine renewal.
   - Owner: Account Executive or Account Manager
   - Goal: Build executive awareness of renewal decision; understand new CTO's strategic priorities and tool consolidation criteria.

   - Action: Escalate and resolve the outstanding API integration issue; assign senior support engineer; target resolution within 5 business days.
   - Owner: Support Manager + Customer Success
   - Goal: Demonstrate responsiveness and remove active friction point; rebuild confidence in support quality.

2. Short-term (within 4 weeks):
   - Action: Conduct value realization audit: map current usage to original use cases and contracted SLAs. Identify which features are driving value and which are gaps.
   - Owner: Customer Success Manager
   - Goal: Provide concrete evidence of ROI (even if usage is down, some value is being realized). Identify where training or optimization could unlock additional value.

   - Action: Propose a 30-day tool consolidation evaluation: show how our platform can consolidate 2-3 of their current tools, reducing complexity and cost.
   - Owner: Solutions Architect
   - Goal: Reframe renewal as strategic consolidation vs. renewal-as-usual. Position as alternative to fragmented tool sprawl.

   - Action: Invite entire infrastructure team (including departed colleagues' replacements) to executive training session on advanced analytics and forecasting capabilities.
   - Owner: Customer Success
   - Goal: Expand adoption beyond core monitoring; help new team members see full platform value.

3. Strategic (ongoing):
   - Action: Establish monthly business reviews (vs. reactive support model) with IT manager and new CTO. Include usage insights, competitive landscape, and optimization opportunities.
   - Owner: Account Manager
   - Goal: Maintain visibility and relationship. Be the trusted advisor, not just the vendor.

   - Action: Create a written renewal proposal (4-6 weeks before renewal date) that includes: cost optimization, feature roadmap aligned to consolidation goals, and expanded user training.
   - Owner: Account Executive + Solutions
   - Goal: Make renewal a strategic decision point rather than a cost line item to cut.

METRICS TO MONITOR:
- API integration issue resolution and verification
- New CTO engagement level (meeting attendance, question depth)
- Usage trend in next 30 days (is decline continuing or stabilizing?)
- Procurement stakeholder sentiment on budget freeze timeline
- Competitive platform engagement level (are they still evaluating or have they decided?)

RENEWAL PROBABILITY ESTIMATE:
- Current Risk Level (7.5): 45-60% likely to renew at current terms
- If interventions executed well: 70-80% likely to renew
- If no interventions: 20-30% likely to renew

NEXT CUSTOMER SUCCESS REVIEW: 2026-10-01 (6 weeks before renewal)

RISK NOTES:
This account is at a critical juncture. The CTO transition and tool consolidation initiative have created a window where the renewal is genuinely uncertain. However, the account has 2+ years of history and some baseline usage, which means it's not a complete loss. The next 4 weeks are critical: resolving the support issue and building executive alignment will likely determine the outcome. Delay or inaction will almost certainly lead to churn.
```

## Evaluation of This Output

✅ **Risk score justified:** The 7.5 is backed by at least 5 specific, weighted signals (executive disengagement, usage decline, unresolved issues, active competitive evaluation, budget constraints).

✅ **Top drivers are distinct and actionable:** Each driver is tied to specific account data (not generic). The implications explain business impact, not just symptoms.

✅ **Interventions are assignable:** Each action has a clear owner, timeline, and success criterion. A real CS team could execute these.

✅ **Shows business context:** The output recognizes the CTO transition as a critical inflection point and reframes renewal strategy around that context, not just generic health metrics.

✅ **Renewal probability is consistent:** The 45-60% reflects high risk, but acknowledges that intervention can move the needle, which is more useful than binary churn/no-churn predictions.

✅ **Practical and defensive:** Balances aggressive intervention with acknowledgment of what's within vs. outside our control (budget cycle, competitive pressure).
