# Case Study — Manual QA Testing & Defect Reporting: OrangeHRM Web Application

## Problem (scenario, not a real client)

A small-to-medium organization preparing an HR platform for rollout needs
independent QA over employee records and leave workflows before release. No
commission, no employment relationship — a self-directed portfolio engagement
run against the open-source OrangeHRM application (5.8.1, self-hosted, pinned).

## Objective

Validate critical business flows, verify observed/derived requirements with
positive/negative/boundary/state coverage, produce reproducible evidence for
every verdict, and deliver a client-grade QA report — including honest zeros
where nothing defected.

## Approach

Functional · Negative · Exploratory (charters + session notes) · BVA (30/31
name boundary proven) · EP · State transitions (punch cycle, session guard) ·
Regression (REG-001–011) · UI consistency · Basic manual accessibility
(planned) · Cross-browser smoke. Playwright used for evidence capture only —
no UI automation claimed.

## Deliverables

✓ Test plan (11 techniques, risk matrix, frozen REG subset) · ✓ Derived
requirements (20 REQs, Observed/Derived split) · ✓ 54 cases · ✓ RTM (20×54,
100% planned traceability, script-verified) · ✓ Execution log + summary ·
✓ Evidence (45 per-TC screenshots) · ✓ Regression + retest workbooks ·
✓ Final QA report · ✓ Exploratory log (incl. one voided probe error, documented)

## Results (actual numbers only)

- 54 planned cases; **21 executed (38.9%)**: 17 Pass, 2 Fail, 2 Blocked, 33 Not Run
- **0 verified SUT defects** — reported as zero. The 2 Fails are test-design
  wording flags (TC-AUTH-002, TC-PIM-003); Expected Results left frozen, no
  bugs filed for correct application behavior.
- A planned-input dispute (exploratory vs specified data) was resolved by
  conforming rerun: E2001 seeded, all five cases pass with evidence.
- Regression on the same build: 9/11 Pass, 2 Blocked. Retest: N/A (no fixes).
- Top open risk: the leave submit→approve chain is unverified (entitlement
  setup pending) — stated plainly, no release verdict given.

Full evidence chain (requirement → case → execution → screenshot → regression)
is browsable in this repo, starting at the [README](../README.md).
