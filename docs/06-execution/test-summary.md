# TEST-CYCLE-01 — Execution Summary

> Status: **In progress — Day-1 Smoke partial (2026-10-03).** Figures below are
> recorded results with evidence, not plan counts. Nothing was rewritten:
> Expected Results in `test-cases.xlsx` are frozen; mismatches are recorded as
> Fail/Blocked with notes, never edited to force a pass.

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
| Failed | 2 (both test-design wording, NOT SUT defects — no BUG filed) |
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
- TC-AUTH-002 Fail (recorded, not rewritten): ESS lands correctly with
  restricted 8-item nav, but Expected text says "PIM/Leave visible" while PIM
  is correctly hidden for ESS. Test-design correction needed; no SUT bug.
- Dashboard/nav: TC-DASH-001,002,004 Pass (12-item admin nav, 8-item ESS nav,
  module routing PIM/Leave/Time/Recruitment, post-logout redirect).
- Leave: TC-LEAVE-001,002 Blocked — ESS Apply Leave renders "No Leave Types
  with Leave Balance". Entitlement provisioning is the entry task before any
  leave-submit assertion.
- PIM list page loads (table + 3 rows, evidence
  `TC-PIM-004-employee-list.png`) but exact-search assertion not yet executed —
  TC-PIM-004 stays Not Run.
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

- PIM: TC-PIM-001 Pass (E2091 created+retrievable), TC-PIM-002 Pass
  (empty-required + duplicate E2091 both blocked, still 1 record),
  TC-PIM-003 Fail-recorded (50-char assumption wrong; true limit 30 —
  30 saved+retrievable as E2092, 31 rejected; app correct, test-design fix
  needed), TC-PIM-004 Pass (autocomplete → exactly 1 card),
  TC-PIM-005 Pass (ID 9999 → "No Records Found", no stale rows).
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
- New executions folded into the totals above: TC-PIM-007 Pass (E2091 edit
  persists after reload), TC-TIME-001/002 Pass (ESS punch-in → visible record
  → punch-out, all "Successfully Saved"). Synthetic records only
  (E2094 created; attendance punched in+out same day leaving a completed pair).

## Next entry tasks (not results)

1. Provision leave type + entitlement/balance for qa_ess, then execute
   TC-LEAVE-001–012.
2. Correct TC-AUTH-002 Expected wording (My Info/Leave visible; Admin/PIM
   absent) through the test-design change process — Expected stays frozen
   until then.
3. Functional days: PIM search/create/edit, Profile, Time punch, Recruitment,
   Reports, UI/keyboard, compat matrix.
