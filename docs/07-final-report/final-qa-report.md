# Final QA Report — OrangeHRM Manual QA (TEST-CYCLE-01, partial)

> Report status: **Issued 2026-10-03 as a partial-cycle report.** 21 of 54
> planned cases executed (38.9%) with evidence; 33 remain Not Run and 2 are
> Blocked on leave-entitlement preconditions. Zero SUT defects were verified —
> reported as zero, never filled to a quota. No release verdict is given (see
> §12 decision framework).

## 1. Executive Summary

Independent manual QA of OrangeHRM 5.8.1 (self-hosted, pinned) covering
authentication/session, dashboard/navigation, employee search/creation, and
time-attendance punch flows. Of 54 planned cases, 21 were executed: 17 passed,
2 failed on test-design wording (not SUT behavior — no bugs filed), and 2 are
blocked awaiting leave-entitlement configuration. Exploratory discovery across
auth edge cases, PIM forms, and search filters surfaced no reproducible SUT
defect. The riskiest untested area is the leave workflow (submit/cancel/
approve/reject), which cannot be exercised until entitlements are provisioned.

## 2. Application Under Test

| Field | Value |
|---|---|
| Application | OrangeHRM Starter / Open Source 5.8.1, self-hosted |
| Build pin | `orangehrm/orangehrm:5.8.1@sha256:5eb278ac…`, source tag `v5.8.1` (commit `d3a50a8`) |
| SUT URL | `http://localhost/` → `/web/index.php/auth/login` |
| Deployment | Docker (host network): app `orangehrm-581` + DB `mariadb:10.11`, 168 tables |
| Purpose | Small-to-medium-org HR platform: employee records, leave/PTO, time tracking |
| Test users | `qa_admin` (Admin, 12-item nav), `qa_ess` (ESS, 8-item nav) — synthetic, local-only |

## 3. Scope

In scope (executed): auth/session, dashboard/nav, employee listing/search/
creation/boundary/duplicate handling, edit persistence, time punch in/out.
In scope (not yet executed): profile forms, leave submit/cancel/approve/reject,
recruitment, reports, UI/keyboard, cross-browser parity.
Out of scope: performance/load, penetration/exploitation, source/DB
modification, API/UI automation, prod deployment, payments, third-party
integrations, mobile, premium/Advanced-only features.
Assumptions: `docs/02-requirements/assumptions.md` (ASM-AUTH-001, ASM-LEAVE-001,
ASM-DATA-001, ASM-ENV-001). All test data synthetic (`test-data/`).

## 4. Environment

| Field | Value |
|---|---|
| OS | Ubuntu 24.04.5 LTS |
| Primary browser | Firefox 155.0 (Playwright `firefox-1543`) |
| Secondary browser | Chrome for Testing 153.0.8010.12 (login verified; full parity pending) |
| App | OrangeHRM 5.8.1 pinned (image ID `5eb278acc628`, 832MB) |
| Viewport | 1920×1080 |
| Date | 2026-10-03 |
| Reproduce | `docs/01-project-overview/environment.md` §3 + `test-data/users.md` (credentials local-only in gitignored `.env`) |

## 5. Strategy (11 techniques, as planned in test-plan.md)

Functional (input→processing→output→state), smoke-first (Day-1 gate passed —
build was testable), sanity/regression subset (REG-001–011 frozen; 9 pass,
2 blocked), exploratory charters (EXP-PIM-01, EXP-SEARCH-01, EXP-AUTH-01
exercised; EXP-LEAVE-01 blocked), equivalence partitioning (valid/invalid
credentials, matching/no-match search), boundary analysis (name length 30/31,
empty/whitespace), decision-table thinking (leave submit blocked before the
table could be exercised), state-transition checks (punch in→out cycle,
logout→session guard), UI consistency (nav/module headers), basic manual
accessibility (keyboard path planned, not yet executed), cross-browser
(Chrome smoke login only so far). No technique was claimed without evidence.

## 6. Execution

| Status | Count | Share |
|---|---|---:|
| Total planned | 54 | 100% |
| Executed (Pass+Fail+Blocked) | 21 | 38.9% |
| Passed | 17 | 81.0% of executed |
| Failed | 2 | 9.5% of executed — both test-design wording, not SUT defects |
| Blocked | 2 | 3.7% of total — leave entitlement precondition |
| Not Run | 33 | 61.1% of total |
| N/A | 0 | — |

Blocked is never counted as Passed. By module: Auth 7P/1F, Dashboard 3P/1NR,
PIM 5P/1F/4NR, Time 2P/3NR, Leave 2B/10NR, Profile 6NR, Recruitment 4NR,
Reports 3NR, UI 1NR, Compat 1NR. Regression on the same build: 9 Pass /
2 Blocked. Retest: N/A (no fixes supplied — nothing to retest, honestly stated).
Detail: `docs/06-execution/execution-results.xlsx`,
`regression-results.xlsx`, `retest-results.xlsx`, `test-summary.md`.

## 7. Coverage (REQ→TC)

20 derived requirements, each with ≥1 planned case (100% planned coverage);
every one of the 54 cases maps back to exactly one requirement (no orphans,
verified by script). Executed coverage concentrates on REQ-AUTH-001–004,
REQ-DASH-001, REQ-PIM-001–004, and REQ-TIME-001. Uncovered-as-executed:
REQ-PROF-001, REQ-LEAVE-002–004 (blocked/pending), REQ-REC-001,
REQ-REPORT-001, REQ-UI-001, REQ-COMP-001. Matrix:
`docs/05-traceability/rtm.xlsx` (all rows `Planned` pre-execution baseline;
execution state lives in the execution workbooks).

## 8. Defects

| Module | Critical | High | Medium | Low | Total |
|---|---|---|---|---|---|
| — (none verified) | 0 | 0 | 0 | 0 | **0** |

Defect total (0) matches `bugs/` (two unfilled templates, intact by design).
The 2 Failed cases are test-design corrections in queue, not product defects:
TC-AUTH-002 (ESS wording claims PIM visible; PIM correctly hidden) and
TC-PIM-003 (assumed 50-char max; true limit is 30 with clear messaging —
30-char saved+retrievable as E2092, 31-char rejected). Expected Results were
left frozen per process; no BUG was filed for correct application behavior.

## 9. Major Findings

1. Authentication and session boundaries behave correctly under all 8 probes:
   generic "Invalid credentials" (no account enumeration), inline "Required"
   for empty/whitespace, safe rejection of 500-char and script/quote input,
   logout + back-button + direct-URL guard all redirect to login.
2. Employee workflows are sound where exercised: autocomplete search returns
   exactly the matching record, ID no-match yields "No Records Found" (no
   stale rows), duplicates blocked with "Employee Id already exists", and the
   30-character name limit is enforced with a clear message on both sides of
   the boundary.
3. Time attendance completes a full punch-in → visible record → punch-out
   cycle with confirmations.
4. The highest-impact open item is leave submission: ESS Apply Leave renders
   "No Leave Types with Leave Balance", so the entire submit/cancel/approve/
   reject chain (12 cases) awaits entitlement provisioning — a setup task,
   not a product failure.
5. Process integrity held: one voided probe error (unlabeled global Search box
   mistaken for the Name field) was caught by control mapping and documented
   in `exploratory/findings.md` F-02 instead of being filed.

## 10. Risks (separated)

- Confirmed (observed): leave-workflow coverage is zero — the business-critical
  submit→approve chain is unverified on this build.
- Limitations (environment): email delivery, load, server-side security,
  payments, integrations, mobile, and premium features unavailable in this setup.
- Untested (explicit): 33 Not Run cases — profile forms, leave state
  transitions, recruitment, reports incl. export, keyboard-only path, and full
  Chrome parity. Any statement about those areas would be speculation.

## 11. Recommendations (evidence-based)

1. Provision a leave type + entitlement/balance for `qa_ess` (admin setup),
   then execute TC-LEAVE-001–012 including the End<Start rejection probe and
   the past-date policy probe.
2. Correct the two test-design wordings through the change process
   (TC-AUTH-002 → "My Info/Leave visible; Admin/PIM absent"; TC-PIM-003 →
   30/31 boundary with E2092 evidence) — Expectations stay frozen until then.
3. Execute the remaining functional days (Profile → Recruitment → Reports →
   UI/keyboard → compat matrix) before any release discussion.
4. Keep the evidence convention (per-TC named screenshots answering "What am
   I looking at?") — it is what made the voided-probe catch possible.

## 12. Decision framework (no fake verdict)

- Strengths: auth/session, search, creation validation, and punch flows all
  green with evidence; environment reproducible and pinned.
- Defects: zero verified product defects; two test-design fixes queued.
- Risks: leave chain unverified; 61.1% of the suite not run.
- Untested/env: see §10; single-build, localhost-only evidence.
- Next actions: §11 items 1–3 in order.
- Release statement: **none given** — a verdict on 38.9% execution with the
  core leave workflow unverified would be fabrication.

## 13. What I could not verify

Leave submission/cancellation/approval/rejection under any balance condition;
past-date and weekend/holiday policy; profile edit/reset behavior; candidate
creation and vacancy flows beyond page-load; report generation, filtering, and
export bytes; keyboard-only operability and focus visibility; Firefox-vs-Chrome
widget parity; and anything requiring email, load, or server-side inspection.
Security penetration testing was outside the project scope. Basic
security-related functional observations such as session behavior and
authorization boundaries were considered where observable through the UI.

## Disclaimer

This is an independently executed portfolio QA engagement against an
open-source application. It was not commissioned by OrangeHRM. It does not
represent client work or employment by the application owner.
