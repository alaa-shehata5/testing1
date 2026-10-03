# Test Plan — OrangeHRM Manual QA

## Objective

Independent manual QA of OrangeHRM pinned build: validate employee + leave workflows, verify OBS/DER requirements, cover positive/negative/boundary/state/UI/a11y/compat, produce traceable evidence + final report.

## Scope (frozen 2026-10-03 — changes require changelog entry)

### In scope

A. Auth: login, invalid user/pass, empty fields, messages, logout, session,
protected pages.
B. Dashboard: loading, nav, widgets, links, consistency, responsive 1920×1080.
C. Employee Management: listing, search, filtering, creation, required fields,
editing, viewing, deletion where available, IDs, personal info.
D. Profile: personal/contact/job, dates, dropdowns, required fields,
edit/save/reset.
E. Leave (major): type, balance, dates, full/half, invalid dates, comments,
submission, pending, cancel, approve/reject, list, calendar.
F. Time (**only if present** in 5.8.1 build): in/out, records, filtering,
timesheets, invalid sequences, duplicates, persistence.
G. Recruitment (**only if available**): creation, search, details, required
fields, transitions, applicant info, delete/edit.
H. Reports (**where available**): generation, filters, ranges, empty results,
consistency, export.

Conditional modules (F/G/H): if absent from the pinned build, their cases are
redistributed to A–E per the Phase 6 distribution rule — never fabricated.

### Out of scope

Performance/load, penetration/exploitation, source/DB modification, API/UI
automation, prod deployment, payments, third-party integrations, mobile,
unavailable premium/Advanced-only features.

### Assumptions

ASM-AUTH-001 valid credentials grant role-assigned modules; ASM-LEAVE-001
leave balance/governing rules follow the configured type; ASM-DATA-001
synthetic employees/users only (see `test-data/`). Full list:
`docs/02-requirements/assumptions.md`.

### Limitations

Web installer not yet completed at freeze time (env §5) — module presence
unconfirmed; email delivery, load, server-side security, payments,
integrations, mobile, and premium features unavailable in this setup.
Security note: penetration testing is out of scope; only UI-observable
session/authorization boundaries are noted.

## Strategy (testing-strategy: risk → cheapest honest level)

### 6.1 Functional

Input→Processing→Output→State. Ex: Apply→Validate→Submit→Accepted→
My Leave→Pending. Every functional case asserts the output *and* the resulting
state — a submit that reports success but leaves no record is a fail.

### 6.2 Smoke (first, TEST-CYCLE-01 Day 1)

Login→Dashboard→Employee→Leave→Create/view→Logout. If smoke fails badly,
stop, report environment — do not burn the functional suite on a broken build.

### 6.3 Sanity (after any fix)

Narrow re-check of the touched area. Ex: leave fix →
Create/View/Cancel/List, then decide on regression.

### 6.4 Regression subset (frozen IDs)

REG-001 Login, REG-002 Logout, REG-003 Dashboard, REG-004 Employee search,
REG-005 Create employee, REG-006 Edit employee, REG-007 Apply leave,
REG-008 View leave, REG-009 Cancel leave, REG-010 Time action,
REG-011 Logout/session. Never renumber; drop with a logged reason if the
module is absent (never silently).

### 6.5 Exploratory charters

EXP-LEAVE-01 leave-date validation
(today/past/future/same/End<Start/long/boundary/zero/partial/repeat/refresh).
Outputs: `exploratory/charters.md`, session notes, findings. Time-boxed,
mission-driven, evidence-kept.

### 6.6 Equivalence partitioning (EP)

Leave days: <0 invalid, 1+ valid; age/date: before/min/normal/max/after.
One representative per partition in the suite; partition breaks found in
exploratory become new cases, not silent edits.

### 6.7 Boundary value analysis (BVA)

Min, Min-1, Min+1, Max, Max-1, Max+1 — taken from observed validation, UI
messages, config, docs, or behavior. Never invented. Data:
`test-data/boundary_employee.csv`, `test-data/leave_boundary_dates.csv`.

### 6.8 Decision table (leave submission)

| Balance | Dates | Data | Expected |
|---|---|---|---|
| Available | Valid | Complete | Submit |
| Zero | Valid | Complete | Reject/validation |
| Available | Invalid | Complete | Reject |
| Available | Valid | Missing | Validation |
| Insufficient | Valid | Complete | Reject/configured |

### 6.9 State transitions

Not Created→Submitted→Pending→Approved/Rejected→Scheduled→Taken. Invalid
transitions are tested, not assumed: rejected→cancel? cancelled→approve?
approved→modify? Each gets an explicit case with the observed outcome.

### 6.10 UI consistency

Alignment, labels, consistency, error placement, button states, affordances,
tables, pagination, empty/loading states, dialogs. Rule: not every preference
is a bug — UI findings need an observable inconsistency or a violated
convention, severity Low unless blocking.

### 6.11 Accessibility (basic pass only — never call it an audit)

Keyboard reachability, visible focus, form labels, logical tab order,
accessible button names, error association, no color-only meaning, 200% zoom
reflow, no clipped content, modal keyboard containment.

## Test types (11 — all used)

Functional, Smoke, Sanity, Regression, Exploratory, Positive, Negative,
Boundary (EP/BVA/decision-table), State-transition, UI, Accessibility &
Compatibility (cross-browser Chrome vs Firefox at 1920×1080, actual results
only).

## Risks

| Module | Impact | Complexity | Risk | Consequence for priority |
|---|---|---|---|---|
| Authentication | High | Medium | High | Full 8-case coverage first; session findings are release-blockers |
| Employee Data | High | High | High | 10 PIM + 6 Profile cases; data-integrity findings outrank cosmetics |
| Leave | High | High | High | 12 cases incl. decision table + state; workflow breaks are P1 minimum |
| Dashboard | Medium | Medium | Medium | 4 smoke-weighted cases |
| Time / Recruitment / Reports | Medium | Medium | Medium | Covered only if present; otherwise redistributed |
| UI / Accessibility / Compat | Low | Medium | Low | 2 cases + cross-browser pass; Low severity unless blocking |

Priority follows risk, not "tested equally". If time is cut, Low-risk UI cases
defer first; High-risk Auth/Employee/Leave never defer.

## Roles

Single-QA engagement: one engineer owns Understand→Report end to end
(charter §4). No handoffs; traceability (REQ→TC→result→BUG) in the RTM
substitutes for cross-role review. Final-report review is a self-QC pass
against the Phase 14 gate.

## Environment

Ubuntu 24.04.5 LTS, Chrome for Testing 153.0.8010.12 (primary, Playwright),
Firefox 155.0 (secondary), OrangeHRM 5.8.1 pinned
(`orangehrm/orangehrm:5.8.1@sha256:5eb278ac…`), 1920×1080, 2026-10-03.
Full record: `docs/01-project-overview/environment.md`.

## Entry/Exit

Entry: build deployed, inventory frozen, test users/data ready. Exit: 54 executed (or redistributed if module missing), defects reproduced + evidenced, metrics + report done, QC gate passed.

## Deliverables

Plan, DRS, 54 cases, RTM, execution-results, bugs+evidence, retest/regression, metrics, final report, README, 8 images, 3-min demo.
