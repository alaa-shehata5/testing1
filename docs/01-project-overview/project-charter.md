# Project Charter — OrangeHRM Manual QA

> Project: `orangehrm-manual-qa` | Headline: **End-to-End Manual QA Testing of an Open-Source HR Management Platform**

## 1. System Under Test (frozen for this engagement)

| Field | Frozen value |
|---|---|
| Application | OrangeHRM Starter / Open Source (self-hosted, pinned) |
| Pinned version | **5.8.1** (`OHRM_VERSION 5.8.1` in `orangehrm/orangehrm` `main` Dockerfile, `FROM php:8.3-apache-bookworm`) |
| Image / source | Official `orangehrm/orangehrm` Docker Hub image + official GitHub repo `orangehrm/orangehrm` (GPL-3.0); ZIP sourced from SourceForge `stable/5.8.1` with MD5 `173cbdffe595246d7e54ec2f2330857d` per Dockerfile |
| Deployment for final execution | Self-hosted Docker, pinned to 5.8.1 build above for reproducibility |
| Reconnaissance only | Public demo `https://opensource-demo.orangehrmlive.com` — used for module discovery only, never as final execution evidence |
| Roles | Admin / ESS (to be confirmed during recon, Phase 1) |
| Reference date | 2026-10-03 (charter freeze date) |

Statement: **This exact application/version/build is the system under test.** Any version drift requires a new charter revision + changelog entry.

## 2. Why OrangeHRM (retain in charter)

Business-process depth vs "clicked Login 12 times". Covers authentication, employee records, forms, tables, search/filtering, role behavior, leave workflows, time tracking, reports, state transitions. OrangeHRM Starter/Open Source includes employee management, leave/PTO, reporting/analytics, recruitment, time tracking [1]. Public repo GPL-licensed + Docker envs + live demo [2]. Use demo for recon, final execution self-hosted/pinned for reproducibility.

## 3. Comparison (retain verbatim)

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

## 4. Business scenario + responsibility chain

Stakeholder: small-to-medium org implementing HR platform requesting independent manual QA before release. You are QA engineer.
Understand → Derive requirements → Define scope → Design cases → Execute → Investigate → Document defects → Retest → Regress → Report.

## 5. Primary objectives (12)

1. Validate critical business workflows.
2. Verify observed/derived requirements.
3. Test positive/negative.
4. Boundary conditions.
5. State transitions.
6. Forms/validation.
7. Navigation/session.
8. UI consistency.
9. Basic accessibility checks.
10. Genuine reproducible defects.
11. Professional evidence.
12. Client-facing QA report.

## 6. Scope intent (freeze detail in Phase 3)

Intended in-scope: Auth, Dashboard, Employee Management (PIM), Profile/forms, Leave (major), Time (only if present in 5.8.1 build), Recruitment (only if available), Reports (where available). Out of scope: performance/load, penetration/exploitation, source/DB modification, API/UI automation, prod deployment, payments, third-party integrations, mobile, unavailable premium. Full freeze in `docs/03-test-plan/test-plan.md`.

## 7. Engagement principles (binding)

- Core principle: Don't optimize for "54 test cases" or "15 bugs". Optimize for evidence chain: requirement → test case → execution → failure → screenshot → bug report → retest/regression.
- ID stability: REQ-xxx-001, TC-xxx-001, BUG-xxx-001, REG-xxx, EXP-xxx-01, TEST-CYCLE-01. Never renumber halfway.
- No fabricated defects/metrics. No Expected-Result rewriting after seeing Actual Result. Synthetic test data only.

## 8. Disclaimers (mandatory, do not edit wording without ADR)

> "This is an independently executed portfolio QA engagement against an open-source application. It was not commissioned by OrangeHRM. It does not represent client work or employment by the application owner."

> "Security penetration testing was outside the project scope. Basic security-related functional observations such as session behavior and authorization boundaries were considered where observable through the UI."

## 9. Done When (Phase 0 gate)

- [x] Exact app/build identified (5.8.1, pinned Docker/source above), environment reproducible intent recorded, scope intent frozen
- [ ] Recon (Phase 1) confirms modules actually present in 5.8.1 build
- [ ] Disclaimer present in charter + README + Final Report

Verify: charter states exact SUT + disclaimer + objectives — yes, sections 1, 5, 8.

## References

- [1] https://orangehrm.com/open-source/open-source-on-demand "Free Open-Source Software | Starter | HRMS | OrangeHRM"
- [2] https://github.com/orangehrm/orangehrm "GitHub - orangehrm/orangehrm"
- [3] https://www.nopcommerce.com/en/demo "Store Demo - nopCommerce"
- [4] https://github.com/nopsolutions/nopcommerce "nopCommerce GitHub, .NET 9 for 4.90 + Docker"
- [5] https://help.orangehrm.com/hc/en-us/articles/360037755534-How-to-use-Leave-Module "How to use Leave Module – OrangeHRM"
