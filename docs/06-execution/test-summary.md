# TEST-CYCLE-01 — Execution Summary

> Status: **In progress — Smoke, exploratory probes, and partial regression
> completed (2026-10-03).** Figures below are reconciled against
> `execution-results.xlsx`; `test-cases.xlsx` and `rtm.xlsx` are synchronized
> to that log. Frozen expected results were not changed after execution.

Env: Ubuntu 24.04.5 LTS, Firefox 155.0 primary (Playwright `firefox-1543`) /
Chrome for Testing 153.0.8010.12 secondary, OrangeHRM 5.8.1 pinned
(`orangehrm/orangehrm:5.8.1@sha256:5eb278ac…`), 1920×1080.
SUT `http://localhost/` → `/web/index.php/auth/login` (HTTP 200, verified this cycle).
Order: Day1 Smoke (this file), Day2–4 Functional, Day4–5 Exploratory, Day5
Consolidation, Day6 Retest, Day7 Regression, Day8 Docs.
Statuses: Pass/Fail/Blocked/N/A/Not Run. Detail in execution-results.xlsx.

## Totals (54 planned)

| Status | Count |
|---|---:|
| Passed | 17 |
| Failed | 2 (test-design wording, NOT SUT defects — no BUG filed) |
| Blocked | 2 (leave entitlement precondition missing) |
| Not Run | 33 (functional + exploratory days pending) |
| N/A | 0 |
| Executed (Pass+Fail+Blocked) | 21 |
| Execution % (Executed / 54) | 38.9% |
| Pass % (Passed / Executed) | 81.0% |
| Fail % (Failed / Executed) | 9.5% |


Blocked is never counted as Passed.

## Day-1 Smoke outcomes

- Auth/session: TC-AUTH-001,003,004,005,006,007,008 Pass (login controls,
  invalid/unknown/empty/whitespace rejection with generic "Invalid
  credentials" or inline "Required", logout, back-button + direct-URL guard).
- TC-AUTH-002 Fail (recorded, expected not rewritten): ESS lands correctly
  with restricted 8-item nav, but the case expected PIM to be visible. PIM is
  correctly hidden for this ESS role. This is an invalid test expectation,
  not an SUT defect.
- Dashboard/nav: TC-DASH-001,002,004 Pass (12-item admin nav, 8-item ESS nav,
  module routing PIM/Leave/Time/Recruitment, post-logout redirect).
- Leave: TC-LEAVE-001,002 Blocked — ESS Apply Leave renders "No Leave Types
  with Leave Balance". Entitlement provisioning is the entry task before any
  leave-submit assertion.
- PIM conforming rerun (2026-10-03, specified data): E2001 (Aarav Sharma, DOB
  1990-01-15) created+retrievable with persisting DOB (TC-PIM-001/007 Pass);
  empty-required + duplicate E2001 blocked with still exactly 1 record
  (TC-PIM-002 Pass); 'Aarav' autocomplete → exactly E2001, Reset → 6 rows
  (TC-PIM-004 Pass); 'ZzzNoMatch' → 0 cards + "No Records Found"
  (TC-PIM-005 Pass). Exploratory E2091/E2092/9999 probes retained as supporting
  evidence.
- Chrome: login + dashboard URL reached (evidence
  `TC-DASH-003-chrome-dashboard.png`); widget-by-widget parity comparison
  pending — TC-DASH-003 stays Not Run.

## Evidence (this cycle, `evidence/smoke/`)

TC-AUTH-001-login-page.png, TC-AUTH-002-admin-dashboard.png,
TC-AUTH-002-ess-dashboard.png, TC-AUTH-003-invalid-password.png,
TC-AUTH-004-unknown-user.png, TC-AUTH-005-empty-credentials.png,
TC-AUTH-006-whitespace-credentials.png, TC-AUTH-007-after-logout.png,
TC-AUTH-008-back-button.png, TC-DASH-001-dashboard-load.png,
TC-DASH-002-nav-recruitment.png, TC-DASH-003-chrome-dashboard.png,
TC-DASH-004-direct-url-after-logout.png, TC-LEAVE-002-ess-apply-form.png,
TC-PIM-001-add-employee-form.png, TC-PIM-004-employee-list.png,
TC-TIME-001-ess-timesheet.png.

## Phase 9 discovery (2026-10-03, SES-2026-10-03-01)

- PIM conforming rerun resolved the planned-input dispute by execution:
  all five cases rerun with specified data (see Day-1 update above). All pass;
  free-text name queries ARE submitted as filters (select-only theory
  disproven by the ZzzNoMatch rerun).
- TC-PIM-003 Fail-recorded (50-char assumption wrong; true limit 30 —
  30 saved+retrievable as E2092, 31 rejected; app validation is consistent,
  test expectation was unsupported). This is a test-design failure, not an
  SUT defect. Expected remains unchanged in the execution record; update the
  case through change control before a future run.
- The E2091 edit evidence from REG-006 is retained as supporting evidence;
  the TC-PIM-007 Pass above comes from the conforming E2001 run.
- Auth edge: 500-char + script/quote input rejected safely (no session);
  repeat-login redirect correct (exploratory note, no defect).
- Verified SUT defects filed: **0**. `bugs/BUG-AUTH-001` / `bugs/BUG-LEAVE-001`
  remain unfilled templates. One voided probe error documented (unlabeled
  global Search box mistaken for the Name field; correct-field re-probes
  pass). Full log: `exploratory/session-notes.md`, `exploratory/findings.md`.
  Per plan, zero is reported as zero — never fabricated to a quota.

## Phase 10 retest/regression (2026-10-03)

- Retest: **N/A — no fix/build was supplied.** Phase 9 verified 0 SUT defects,
  so there is nothing to retest. No fixes were pretended:
  `docs/06-execution/retest-results.xlsx` records the N/A disposition.
- Regression (same pinned build, fresh evidence in `evidence/regression/`):
  REG-001/002/003/004/005/006/008/010/011 Pass; REG-007/009 Blocked
  (leave-entitlement precondition still unmet — nothing submittable, nothing
  cancellable). Detail: `docs/06-execution/regression-results.xlsx`.
- New results reflected in the totals above: TC-PIM-007 Pass (conforming
  E2001 run; E2091 evidence retained as supporting). TC-TIME-001/002 Pass (ESS punch-in → visible record →
  punch-out, both "Successfully Saved"). Synthetic records only
  (E2094 created; attendance punched in+out same day leaving a completed pair).

## Next entry tasks (not results)

1. Provision leave type + entitlement/balance for qa_ess, then execute
   TC-LEAVE-001–012.
2. Revise case expectations for TC-AUTH-002 and TC-PIM-003 through documented
   change control before any repeat execution. Keep prior outcomes immutable.
3. Continue unrun Profile, remaining PIM, Time, Recruitment, Reports,
   UI/keyboard, and compatibility cases.
