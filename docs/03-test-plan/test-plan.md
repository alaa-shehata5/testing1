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

## Strategy (testing-strategy skill: risk → cheapest honest level)

Functional Input→Processing→Output→State; Smoke Login→Dash→Employee→Leave→Create/view→Logout (stop if badly failed); Sanity after fix (Create/View/Cancel/List); Regression REG-001..011; Exploratory charters EXP-xxx; EP (<0 invalid, 1+ valid); BVA Min±1/Max±1 from observed rules; Decision table balance×dates×data; State NotCreated→Submitted→Pending→Approved/Rejected→Scheduled→Taken + invalid transitions; UI consistency; Basic a11y (keyboard/focus/labels/tab/names/errors/color-only/200%/clipping/modal).

Risk matrix: Auth High, Employee High, Leave High, Dashboard Medium, UI Low — priority follows risk.

## Environment

Ubuntu 24.04.5 LTS, Chrome for Testing 153.0.8010.12 (primary, Playwright),
Firefox 155.0 (secondary), OrangeHRM 5.8.1 pinned
(`orangehrm/orangehrm:5.8.1@sha256:5eb278ac…`), 1920×1080, 2026-10-03.
Full record: `docs/01-project-overview/environment.md`.

## Entry/Exit

Entry: build deployed, inventory frozen, test users/data ready. Exit: 54 executed (or redistributed if module missing), defects reproduced + evidenced, metrics + report done, QC gate passed.

## Deliverables

Plan, DRS, 54 cases, RTM, execution-results, bugs+evidence, retest/regression, metrics, final report, README, 8 images, 3-min demo.
