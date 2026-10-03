# OrangeHRM Manual QA — Phased Plan for AI Agents

> Project: `orangehrm-manual-qa` | Headline: **End-to-End Manual QA Testing of an Open-Source HR Management Platform**
> SUT: OrangeHRM Starter / Open Source (self-hosted pinned version/commit preferred; public demo for reconnaissance only)
> Mandatory disclaimer (README + Final Report + portfolio): "This is an independently executed portfolio QA engagement against an open-source application. It was not commissioned by OrangeHRM. It does not represent client work or employment by the application owner."
> Security wording (never claim "Security testing was completed"): "Security penetration testing was outside the project scope. Basic security-related functional observations such as session behavior and authorization boundaries were considered where observable through the UI."
> Core principle: Don't optimize for "54 test cases" or "15 bugs". Optimize for evidence chain: requirement → test case → execution → failure → screenshot → bug report → retest/regression.
> ID stability: REQ-xxx-001, TC-xxx-001, BUG-xxx-001, REG-xxx, EXP-xxx-01, TEST-CYCLE-01. Never renumber halfway.
> No fabricated defects/metrics. No Expected-Result rewriting after seeing Actual Result. Synthetic test data only.

Skills applied: `plan-writing` (small verifiable tasks, Done When), `documentation-templates` (README/ADR/Changelog/AI-friendly structure), `testing-strategy` (behavior target + risk + cheapest honest level + failure signal), `readme` (local/architecture/env/deployment/troubleshooting depth adapted for QA portfolio).

References: [1] https://orangehrm.com/open-source/open-source-on-demand "Free Open-Source Software | Starter | HRMS | OrangeHRM" | [2] https://github.com/orangehrm/orangehrm "GitHub - orangehrm/orangehrm" | [3] https://www.nopcommerce.com/en/demo "Store Demo - nopCommerce" | [4] https://github.com/nopsolutions/nopcommerce "nopCommerce GitHub, .NET 9 for 4.90 + Docker" | [5] https://help.orangehrm.com/hc/en-us/articles/360037755534-How-to-use-Leave-Module "How to use Leave Module – OrangeHRM"

---

## Goal

Build `orangehrm-manual-qa/` as a client-grade manual QA portfolio: charter → reconnaissance → derived requirements → test plan → 54-case suite → RTM → execution → verified defects + evidence → retest/regression → metrics → final QA report → GitHub → freelancing assets (case study, 8 images, 3-min demo).

## Agent Roster

- Orchestrator: owns phase gates, DoD, traceability.
- Recon Agent: application-inventory.
- Env Agent: self-hosted build, test users/data, environment.md.
- Requirements Agent: DRS (OBS/DER/ASM).
- Plan Agent: test-plan.md, scope freeze, risk matrix.
- Case Author: 54 cases.
- RTM Agent: REQ→TC before execution, then results/defects linkage.
- Execution Agent: TEST-CYCLE-01 smoke→functional→exploratory→consolidation→retest→regression.
- Exploratory Agent: charters + session notes + EP/BVA/decision-table/state-transition.
- Defect Agent: reproducible bug reports + severity/priority justification.
- Evidence Agent: screenshots/recordings naming + annotation.
- Report Agent: metrics + final-qa-report.md.
- Publisher Agent: repo cleanup, README, CHANGELOG, .gitignore, links.
- Portfolio Agent: case study, 8 images, video-script.

## Done When

- [ ] Exact app/build identified, environment reproducible, scope frozen
- [ ] 40–60 quality cases, fully traced, executed with actual results
- [ ] Genuine reproducible defects with evidence, justified severity/priority
- [ ] Metrics mathematically correct, defect counts match bugs/
- [ ] Final QA report + polished README + portfolio assets + disclaimer

---

# PHASE 0 — Application Selection & Charter

## Why OrangeHRM (retain in charter)

Business-process depth vs "clicked Login 12 times". Covers authentication, employee records, forms, tables, search/filtering, role behavior, leave workflows, time tracking, reports, state transitions. OrangeHRM Starter/Open Source includes employee management, leave/PTO, reporting/analytics, recruitment, time tracking [1]. Public repo GPL-licensed + Docker envs + live demo [2]. Use demo for recon, final execution self-hosted/pinned for reproducibility.

## Comparison (retain verbatim)

| Criterion | OrangeHRM | nopCommerce | DemoQA | SauceDemo |
|---|---|---:|---:|---:|
| Business realism | 5/5 | 5/5 | 2/5 | 3/5 |
| Authentication | 5 | 5 | 2 | 5 |
| CRUD | 5 | 5 | 4 | 1 |
| Forms/validation | 5 | 5 | 5 | 2 |
| Search/filtering | 5 | 5 | 3 | 3 |
| Workflow/state testing | 5 | 5 | 2 | 3 |
| Role/permission testing | 5 | 5 | 1 | 2 |
| Reporting | 5 | 5 | 1 | 1 |
| UI testing | 5 | 5 | 4 | 4 |
| Exploratory testing | 5 | 5 | 4 | 4 |
| Local/self-hosting | 5 | 5 | 3 | 5 |
| Reproducibility | 5 | 5 | 3 | 4 |
| Portfolio differentiation | **5** | 5 | 2 | 2 |
| Setup complexity | Medium | Medium/High | Low | Very Low |
| Overall portfolio potential | **Excellent** | Excellent | Moderate | Moderate |

Candidate A OrangeHRM: genuine HR domain; docs cover leave apply/cancel/approve/reject/calendars/reports [1][5]; repo + Docker [2]; advantage workflow/business-rule testing; disadvantage must establish modules in exact build. Candidate B nopCommerce: storefront, catalog, search/filter/sort, accounts, cart, wishlist, checkout, orders, inventory, admin [3]; open source .NET 9 4.90 + Docker [4]; disadvantage scope enormous; excellent second project later. Candidate C DemoQA: forms, tables, alerts, browser, widgets, Book Store, drag/drop, dynamic properties, validation — practice site not client system — learning not flagship. Candidate D SauceDemo: auth/inventory/sort/cart/checkout — easy but no differentiation — secondary only. Selection: Use OrangeHRM Starter/Open Source pinned version/commit, self-hosted.

## Business scenario + responsibility chain

Stakeholder: small-to-medium org implementing HR platform requesting independent manual QA before release. You are QA engineer.
Understand → Derive requirements → Define scope → Design cases → Execute → Investigate → Document defects → Retest → Regress → Report.

## Primary objectives (12)

1. Validate critical business workflows. 2. Verify observed/derived requirements. 3. Test positive/negative. 4. Boundary conditions. 5. State transitions. 6. Forms/validation. 7. Navigation/session. 8. UI consistency. 9. Basic accessibility checks. 10. Genuine reproducible defects. 11. Professional evidence. 12. Client-facing QA report.

Tasks: Review demo + Starter functionality → Inspect modules → Decide version/build → Decide self-host/hosted → Freeze + disclaimer. Output: docs/01-project-overview/project-charter.md. Effort 1–2h. Verify: charter states exact SUT + disclaimer + objectives.

---

# PHASE 1 — Reconnaissance (30–60 min, BEFORE scope freeze)

Output: docs/01-project-overview/application-inventory.md. Record: App version, URL, Build/commit, Roles, Modules, Browser, OS, Date/time, Visible functionality, Unavailable functionality, Env limitations. Verify: another person can tell exact SUT + unavailable items.

---

# PHASE 2 — Environment Setup (2–5h)

Use official source/repos not third-party copy [2]. Record OS Ubuntu/Linux, Browser Firefox X, Secondary Chromium, App OrangeHRM X, Viewport 1920×1080, Date YYYY-MM-DD. Tasks: obtain source → local/Docker → test users → synthetic employees → test data → verify browser. Output: environment.md + test-data/. Verify: another person can reproduce env. Test-data files required: valid_employee.csv, boundary_employee.csv, invalid_employee.csv, leave_boundary_dates.csv, search_test_data.csv, test-data/users.md, employees.csv, leave-data.csv.

---

# PHASE 3 — Scope Freeze

In-scope A. Auth: login, invalid user/pass, empty, messages, logout, session, protected pages. B. Dashboard: loading, nav, widgets, links, consistency, responsive. C. Employee Management: listing, search, filtering, creation, required, editing, viewing, deletion where avail, IDs, personal info. D. Profile: personal/contact/job, dates, dropdowns, required, edit/save/reset. E. Leave (major): type, balance, dates, full/half, invalid dates, comments, submission, pending, cancel, approve/reject, list, calendar [5]. F. Time (only if present): in/out, records, filtering, timesheets, invalid seq, duplicates, persistence. G. Recruitment (only if avail): creation, search, details, required, transitions, app info, delete/edit. H. Reports (where avail): generation, filters, ranges, empty, consistency, export.

Out of scope: performance/load, penetration/exploitation, source/DB modification, API/UI automation, prod deployment, payments, third-party integrations, mobile, unavailable premium. Verify: test-plan scope lists in/out/assumptions/limitations.

---

# PHASE 4 — Derived Requirements (DRS) (3–5h)

Outputs: docs/02-requirements/derived-requirements.md + assumptions.md. Not official BRD. Types: OBS observed (OBS-AUTH-001 login page provides user/pass + action), DER derived (DER-AUTH-001 shall authenticate on valid creds), ASM assumption (ASM-AUTH-001 valid user assumed access to role modules).

Template columns: Requirement ID (REQ-LEAVE-001), Type (Derived), Module (Leave), Requirement (submit with valid data), Priority (High), Source (Observable behavior), Acceptance Criteria (accepted + appears in history), Notes (subject to balance). IDs: REQ-AUTH-001, REQ-DASH-001, REQ-PIM-001, REQ-LEAVE-001, REQ-TIME-001, REQ-REC-001, REQ-REPORT-001, REQ-UI-001. Stable. Verify: every REQ has ≥1 TC planned, no contradiction, ASM separated.

---

# PHASE 5 — Test Planning (2–3h)

Output: docs/03-test-plan/test-plan.md with Objective, Scope, Risks, Strategy, Environment, Entry/Exit, Types, Roles, Deliverables.

## 6.1 Functional: Input→Processing→Output→State. Ex Apply→Validate→Submit→Accepted→My Leave→Pending.
## 6.2 Smoke first: Login→Dashboard→Employee→Leave→Create/view→Logout. Fail badly → stop, report env.
## 6.3 Sanity after fix: Ex leave fix → Create/View/Cancel/List then regression.
## 6.4 Regression subset REG-001 Login, REG-002 Logout, REG-003 Dashboard, REG-004 Employee search, REG-005 Create employee, REG-006 Edit employee, REG-007 Apply leave, REG-008 View leave, REG-009 Cancel leave, REG-010 Time action, REG-011 Logout/session.
## 6.5 Exploratory charters: EXP-LEAVE-01 leave-date validation (today/past/future/same/end<start/long/boundary/zero/partial/repeat/refresh). Outputs exploratory/charters.md, session-notes.md, findings.md.
## 6.6 EP: Leave <0 invalid, 1+ valid, 0/1/max boundary; age/date before/min/normal/max/after.
## 6.7 BVA: Min, Min-1, Min+1, Max, Max-1, Max+1 from validation/UI/config/docs/behavior, not invented.
## 6.8 Decision table:
| Balance | Dates | Data | Expected |
| Available | Valid | Complete | Submit |
| Zero | Valid | Complete | Reject/validation |
| Available | Invalid | Complete | Reject |
| Available | Valid | Missing | Validation |
| Insufficient | Valid | Complete | Reject/configured |
## 6.9 State: Not Created→Submitted→Pending→Approved/Rejected→Scheduled→Taken. Test invalid: rejected→cancel? cancelled→approve? approved→modify? Test don't assume.
## 6.10 UI: alignment, labels, consistency, error placement, button states, affordances, tables, pagination, empty/loading, dialogs. Not every preference = bug.
## 6.11 Accessibility basic pass only: keyboard, focus, labels, tab order, button names, error ID, color-only, 200% zoom, clipping, modal keyboard.

Risk matrix:
| Module | Impact | Complexity | Risk |
| Authentication | High | Medium | High |
| Employee Data | High | High | High |
| Leave | High | High | High |
| Dashboard | Medium | Medium | Medium |
| UI | Low | Medium | Low |
Explain priority follows risk, not "tested equally". Verify: strategy lists all 11 types.

---

# PHASE 6 — Test Cases (54) (5–8h)

Outputs: docs/04-test-cases/test-cases.xlsx + test-case-design.md. Order Auth→Employee→Leave→Time→Reports→UI then dedup.

Distribution: Auth/session 8, Dashboard/nav 4, Employee mgmt 10, Profile/forms 6, Leave 12, Time 5, Recruitment 4, Reports 3, UI/a11y/compat 2 = 54. If Recruitment/Time missing redistribute. Type: Positive 20, Negative 14, Boundary 6, State 5, UI 4, Accessibility 2, Compatibility 3 = 54.

Schema: TC ID, Requirement ID, Module, Scenario, Title, Priority, Test Type, Preconditions, Test Data, Environment, Steps, Expected, Actual, Status, Defect ID, Notes. Bad: Test leave. Good: Verify user can submit full-day leave with valid type/future date/sufficient balance. Bad steps "Go to leave. Enter data. Submit." Good 8 steps: login ESS → Leave → Apply → type with balance → future working day → Full Day → comment → Apply. Expected: accepted + shown with initial status. Verify: unique IDs, reproducible, specific expected, data documented, all types present.

---

# PHASE 7 — RTM (1–2h, BEFORE execution)

Output: docs/05-traceability/rtm.xlsx. Columns Requirement|Description|Test Cases|Execution|Defect|Coverage. Ex REQ-AUTH-001 Valid login TC-AUTH-001,002 Pass — Covered; REQ-LEAVE-001 Submit TC-LEAVE-001–004 Fail BUG-LEAVE-001 Covered; REQ-PIM-002 Search TC-PIM-003–005 Pass — Covered. Metrics: Coverage=REQ with ≥1TC/Total×100; Execution=Executed/Total×100; Pass=Passed/Executed×100; Fail=Failed/Executed×100; Blocked=Blocked/Executed×100; Defect coverage [project metric]=TC linked to defects/Failed×100. Verify: REQ→TC mapped pre-execution.

---

# PHASE 8 — Execution TEST-CYCLE-01 (5–8h)

Outputs: docs/06-execution/execution-results.xlsx + test-summary.md + evidence/smoke|exploratory|regression/. Env table OS/Browser/Version/App/Viewport. Order Day1 Smoke (auth/dash/nav/employee/leave/logout), Day2–4 Functional, Day4–5 Exploratory, Day5 Consolidation, Day6 Retest, Day7 Regression, Day8 Docs. Statuses Pass/Fail/Blocked/N/A/Not Run. Verify: no Expected rewritten.

---

# PHASE 9 — Bug Discovery (4–8h) + Documentation (3–6h)

Goal not "need 15 bugs" but disciplined process. Report 13 if 13, 7 if 7. Never fake. Flow Observe→Repeat→Isolate→Reproduce→Compare→Capture.

Auth: empty user/pass/both, wrong user/pass, whitespace, very long, special, repeat login, logout, back-button, direct URL after logout, session expiry. Employee forms: required, empty, max length, special, numbers in text, duplicate IDs/names, invalid/boundary dates, cancel/reset, save twice, refresh. Search/filter: exact/partial/case/spaces/no-result/multi/clear/pagination/filter+pagination/filter+sort/search after edit. Leave: past/today/tomorrow/weekend/holiday/Start=End/End<Start/long/zero/insufficient/full/half/specific-time/empty-long comment/repeat/refresh/back/cancel/approve/reject. Tables: wrong count, dup/missing rows, sorting, filters not clearing, empty state, shifting, truncation, broken actions, wrong record.

Bug ID BUG-LEAVE-001. Title: [Module] [observable failure] [condition]. Ex Leave — End date earlier than start can be submitted without validation (only if reproduced). Template: Title, Severity High, Priority P1, Env OS/Browser/Version/App/Viewport, Preconditions, Test Data, Steps 1-4, Expected, Actual, Repro 5/5, Impact, Evidence evidence/BUG-LEAVE-001/, Related TC-LEAVE-008, Related REQ-LEAVE-003, Notes.

Severity: Critical unusable/corruption/major workflow unavailable/severe in-scope security; High major broken/significant unavailable/important incorrect/no workaround; Medium important non-blocking/workaround/partial; Low cosmetic/wording/alignment/low usability. Priority P0 immediate, P1 before release, P2 planned, P3 backlog. Ex login typo Low/P3; misleading leave error Medium/P2; disappearing leave High/P1 with justification. Taxonomy: Functional, Validation, UI, Usability, Navigation, State, Data Integrity, Compatibility. Verify: reproduced, steps work, defensible expected, observable actual, screenshot supports, justified.

Evidence: BUG-LEAVE-001/01-precondition.png,02-input.png,03-failure.png,evidence.md. Capture area+failure+input+URL+browser; avoid personal data; synthetic only. Annotate subtle circles/arrows/boxes/labels. Naming BUG-LEAVE-001-invalid-date-validation.png not Screenshot1.png. Every shot answers What am I looking at?

---

# PHASE 10 — Retest/Regression (2–4h)

Original→Retest→Pass/Fail→Regression subset. If no fix: "Retesting was not possible because no fix/build was supplied; regression impact was assessed through related scenarios." Don't pretend fixes. Outputs retest-results.xlsx, regression-results.xlsx. Verify: linked to BUG IDs.

---

# PHASE 11 — Metrics + Final Report (2–4h)

Dashboard: Total 54, Executed XX, Passed XX, Failed XX, Blocked XX, Not Run XX, N/A XX; Defects Total XX Critical X High X Medium X Low X; Requirements XX Covered XX Coverage XX% Execution XX% Pass XX% Fail XX%. Show 42/8/4 exactly if that is result.

Report docs/07-final-report/final-qa-report.md: 1 Executive Summary 1-page (tested/covered/found/risky), 2 App Under Test (app/version/URL/deploy/build/purpose), 3 Scope (in/out/assumptions/limitations), 4 Env table, 5 Strategy (11 types), 6 Execution chart/table, 7 Coverage REQ→TC, 8 Defects Module|Crit|High|Med|Low, 9 Major Findings ("highest-impact issue affected leave-submission under [condition]" not "terrible"), 10 Risks separated Confirmed vs Limitations vs Untested, 11 Recommendations evidence-based (add validation preventing invalid ranges). + Limitations (payments/email/load/server security out of manual UI scope) + decision framework (strengths/defects/risks/untested/env/next actions, no fake release verdict) + What I could not verify. Verify: numbers add up, % correct, Blocked≠Passed.

---

# PHASE 12 — GitHub Publication (2–4h)

Tree:
orangehrm-manual-qa/README.md, LICENSE, CHANGELOG.md, docs/01-project-overview/project-charter.md+application-inventory.md, docs/02-requirements/derived-requirements.md+assumptions.md, docs/03-test-plan/test-plan.md, docs/04-test-cases/test-cases.xlsx+test-case-design.md, docs/05-traceability/rtm.xlsx, docs/06-execution/execution-results.xlsx+test-summary.md, docs/07-final-report/final-qa-report.md, bugs/BUG-AUTH-001/bug-report.md+evidence/, bugs/BUG-LEAVE-001/bug-report.md+evidence/, evidence/smoke|exploratory|regression/, test-data/users.md+employees.csv+leave-data.csv, reports/dashboards+screenshots/, demo/video-script.md+demo-assets/, .gitignore. No giant Excel dumps elsewhere, no binaries, no secrets.

README sales: Title + one-liner + [View Test Plan][View Test Cases][View RTM][View Bug Reports][View Final Report]; Snapshot App OrangeHRM Type Manual Cases 54 Modules 6+ Defects XX Env Firefox/Chromium/Linux; What Tested; Techniques; Coverage; Defect Summary; Featured Bug (Condition→Repro→Failure→Expected→Impact→Evidence→Sev/Pri); Evidence 2–3 shots; Deliverables links; Tools; Limitations; Disclaimer. Tools: Firefox DevTools/Network/Responsive/Console/Storage, Chromium secondary, Markdown, LibreOffice Calc/Google Sheets, Flameshot/GNOME/Firefox shots, OBS Studio, git/GitHub. Commits as listed in rules. Use official source/Docker [2], pinned commit. Verify: links work, naming consistent, understandable alone.

---

# PHASE 13 — Freelancing Assets (2–4h)

Title: Manual QA Testing & Defect Reporting — OrangeHRM Web Application. Problem (scenario not real client): org preparing HR app needs independent QA on employee/leave. Objective: validate flows, find defects, traceability, actionable findings. Approach: Functional Negative Exploratory BVA EP State Regression UI Basic A11y Cross-Browser. Deliverables ✓ Plan ✓ DRS ✓ 54 Cases ✓ RTM ✓ Execution ✓ Bugs ✓ Evidence ✓ Regression ✓ Final. Results actual numbers only.

8 images: 1 Overview (App/Scope/Cases/Defects/Coverage/Tools), 2 Test Plan (Objective/Scope/Strategy/Env/Entry-Exit/Risks), 3 Suite 8–12 rows (ID/REQ/Scenario/Priority/Type/Expected/Status), 4 RTM REQ→TC→RESULT→BUG, 5 Bug best (Title/Env/Steps/Expected/Actual/Sev/Pri/Evidence), 6 Evidence annotated 2-sec obvious, 7 Dashboard 54 Total Passed/Failed/Blocked Execution%/Pass%/Defects, 8 Final (Summary/Findings/Risk/Recs).

Video 3min: 0:00–0:15 Hook "end-to-end manual QA against open-source HR app." 0:15–0:40 App Login/Dash/Modules/Employee/Leave. 0:40–1:10 Strategy "derived requirements + 54 cases positive/negative/boundary/state/UI/a11y/compat." 1:10–1:40 Cases zoom REQ/TC/Steps/Expected/Status. 1:40–2:15 Bug App→Steps→Unexpected→Shot→Expected vs Actual. 2:15–2:40 RTM REQ-LEAVE-001→TC-001/002→FAIL→BUG-001. 2:40–3:00 Metrics + "complete plan/suite/RTM/defects/evidence/report in GitHub." Don't spend 90s explaining testing.

---

# PHASE 14 — QC Gate (blocking)

Requirements: IDs, ≥1 test, no contradiction, ASM separated. Cases: unique ID, reproducible, specific expected, data documented, pos+neg, boundary, state, no dups. Bugs: reproduced, steps work, defensible expected, observable actual, shot supports, sev/pri justified, no fake impact/bugs. RTM: REQ→TC, TC→Exec, Fail→defects, no broken IDs. Metrics: totals add, % correct, Blocked≠Passed, N/A not hidden, counts match bugs/. GitHub: README/links, no secrets/PII/binaries, consistent, self-explanatory. Ethics: self-initiated, no client/employment claim, no fake metrics/defects.

Acceptance: exact build, reproducible env, frozen scope, documented REQ, 40–60 cases, traced, executed, actuals, genuine reproducible defects + shots + justified sev/pri, correct metrics, final report, organized repo, polished README, 8 shots, demo, disclaimer.

Differentiators present: real engagement flow; chain REQ-LEAVE-003→TC-009→FAIL→BUG-002→Shot→Retest; exploratory charters/notes/findings; state diagram + invalid transitions; test-data design; risk matrix driving priority; "Basic manual accessibility checks" not audit; compat matrix Firefox vs Chromium actual only; taxonomy; What I could not verify; no fake verdict; Featured Defect.

Final architecture: 01 Charter, 02 Recon, 03 DRS, 04 Plan, 05 54-suite, 06 RTM, 07 Exploratory, 08 Execution, 09 Defects, 10 Evidence, 11 Retesting, 12 Regression, 13 Metrics, 14 Final Report, 15 Case Study, 16 Demo.
