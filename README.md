# OrangeHRM Manual QA Testing

> End-to-end manual QA assessment of an open-source HR management platform.

[View Test Plan](docs/03-test-plan/test-plan.md) | [View Test Cases](docs/04-test-cases/test-case-design.md) | [View RTM](docs/05-traceability/rtm.md) | [View Bug Reports](bugs/BUG-LEAVE-001/bug-report.md) | [View Final Report](docs/07-final-report/final-qa-report.md) | [Phased Agent Plan](orangehrm-manual-qa-phased-plan.md)

## Project Snapshot

```text
Application: OrangeHRM Starter / Open Source (pinned self-hosted build)
Testing Type: Manual QA (functional, smoke, sanity, regression, exploratory, BVA/EP, state, UI, basic a11y, compat)
Test Cases: 54 planned (Auth 8, Dashboard 4, PIM 10, Profile 6, Leave 12, Time 5, Recruitment 4, Reports 3, UI 2)
Modules: 6+ | Defects: XX verified (fill actual) | Environment: Firefox / Chromium / Linux 1920×1080
```

## What I Tested

Auth, Dashboard, Employee Management, Profile/forms, Leave (major), Time (if present), Recruitment (if present), Reports (if present).

## Testing Techniques

Functional, Smoke, Sanity, Regression REG-001..011, Exploratory charters EXP-xxx, EP, BVA Min±1/Max±1, Decision tables, State-transition (Pending→Approved/Rejected + invalid), UI, Basic accessibility, Cross-browser.

## Coverage / Defect Summary / Featured Bug

See [RTM](docs/05-traceability/rtm.md), [Execution](docs/06-execution/test-summary.md), [BUG-LEAVE-001](bugs/BUG-LEAVE-001/bug-report.md). Featured defect chain: REQ-LEAVE-003 → TC-LEAVE-008 → FAIL → BUG-LEAVE-001 + evidence.

## Deliverables

- Test Plan, DRS, 54 cases (`docs/04-test-cases/test-cases.xlsx`), RTM (`docs/05-traceability/rtm.xlsx`), Execution (`docs/06-execution/execution-results.xlsx`), Bugs+evidence, Final Report.

## Tools

Firefox DevTools/Network/Responsive/Console/Storage, Chromium, Markdown, LibreOffice Calc/Sheets, Flameshot/GNOME/Firefox shots, OBS Studio, git/GitHub.

## Limitations

Perf/load, pen-test, source/DB mods, automation, prod deploy, payments, integrations, mobile, premium unavailable out of scope.

## Disclaimer

This is a self-initiated QA portfolio project performed against an open-source application. It does not represent commissioned client work or employment by the application owner.
