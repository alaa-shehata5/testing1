# Demo Video Script (3 min)

> Rule: every number on screen is a measured result. Zero defects is stated as
> zero — the 1:40–2:15 slot shows the strongest verification chain and the two
> test-design flags, never an invented bug.

- **0:00–0:15 Hook.** "End-to-end manual QA against an open-source HR app —
  54 cases, full evidence chain, zero fabricated defects."
- **0:15–0:40 App.** Login → Dashboard (12-item admin / 8-item ESS nav) →
  PIM employee list → Leave → Time. Pinned build 5.8.1, Firefox 1920×1080.
- **0:40–1:10 Strategy.** Derived requirements (20 REQs) + 54 cases across
  positive/negative/boundary/state/UI/compat; smoke-first, REG-001–011 frozen.
- **1:10–1:40 Cases zoom.** Suite excerpt: REQ→TC→steps→Expected→Status;
  Expected Results frozen, per-TC evidence naming.
- **1:40–2:15 Deep dive (no bug — by honesty).** E2001: TC-PIM-001 verifies
  creation and retrieval; TC-PIM-007 verifies employee-detail persistence.
  Show regression separately: REG-004/006 use E2091 and REG-005 uses E2094.
  Then cover the two test-design flags and the voided Search-box probe.
- **2:15–2:40 RTM.** REQ-PIM-001→TC-PIM-001 (Pass), REQ-PIM-003→TC-PIM-007
  (Pass), and REQ-LEAVE-002→Blocked (entitlement); defect links are blank
  because no SUT defects were verified.
- **2:40–3:00 Metrics + close.** 54 total · 21 executed (38.9%) · 17 pass
  (81.0%) · 0 defects · regression 9/11 · no release verdict on a partial
  cycle. "Complete plan, suite, RTM, evidence, and report in GitHub."

## Portfolio images

`demo-assets/01-overview.svg` … `08-final.svg` (1200×675): 1 Overview, 2 Test
Plan, 3 Suite excerpt, 4 RTM, 5 Top finding (honest zero), 6 annotated E2001
evidence, 7 Dashboard, 8 Final. Regenerate with
`python3 demo/make_portfolio_svgs.py`; the evidence slide reads its source
screenshot from `evidence/smoke/`.
