# Application Inventory — Reconnaissance (Phase 1)

> Freeze statement: **This exact application/version/build is the system under test** for final execution is OrangeHRM Starter **5.8.1 self-hosted** (see charter). The public demo below was used for **reconnaissance only** and is version-volatile — it is not execution evidence.

## 1. SUT identity

| Field | Value |
|---|---|
| Application | OrangeHRM Starter / Open Source (self-hosted, pinned) |
| Pinned version (final execution) | **5.8.1** — `OHRM_VERSION 5.8.1` in `orangehrm/orangehrm:main` Dockerfile (`FROM php:8.3-apache-bookworm`), ZIP `stable/5.8.1`, MD5 `173cbdffe595246d7e54ec2f2330857d` |
| Self-hosted URL | TBD in Phase 2 (Docker deploy pending; record `http://<host>:<port>` + image digest here) |
| Build/commit pin | TBD in Phase 2 — record `git rev-parse HEAD` of `orangehrm/orangehrm` and/or Docker image digest (`docker images --digests`). Dockerfile `latest` digest prefix observed via Hub metadata `sha256:d692780ef…` is **not** a full pin — replace with full digest on pull |
| Recon source (not SUT) | `https://opensource-demo.orangehrmlive.com` and `https://opensource-demo.orangehrmlive.com/web/index.php/auth/login` |
| Demo version observed 2026-10-03 | Root page footer: **OrangeHRM OS 5.8**; deep login path footer: **OrangeHRM OS 5.9**. Demo is drifting — confirms demo cannot serve as reproducible SUT |
| License | GPL-3.0 (`orangehrm/orangehrm` repo) |
| Recon date/time | 2026-10-03 12:51 UTC |

## 2. Roles (demo hint + docs; confirm in pinned build Phase 2)

| Role | Source | Status |
|---|---|---|
| Admin (`Admin` / `admin123` hint on demo login page) | Observed login-page hint via search excerpt, 2026-10-03 | Documented, needs interactive confirm in 5.8.1 build |
| ESS (Employee Self Service, incl. Default ESS) | Starter HR Administration docs + usability-enhancement notes | Documented, needs confirm |
| Supervisor (incl. Default Supervisor) | Same as above | Documented, needs confirm |
| Custom ESS / Custom Supervisor | User-role docs | Documented, needs confirm |

No test users created yet — Phase 2.

## 3. Modules

Starter-documented module set (marketing + Starter Help + API `GET /api/v2/admin/modules`). Mark `Pinned-build present?` as TBD until Phase 2 interactive check.

| Module | Documented capability | Pinned-build present? |
|---|---|---|
| Dashboard | Landing, widgets, nav | TBD Phase 2 |
| Admin / HR Administration | Users, roles, org structure, config | TBD Phase 2 |
| PIM / Employee Management | Employee DB, add/filter/list, corporate directory | TBD Phase 2 |
| Leave / PTO | Apply, assign, leave list, entitlements, balance check, approve/reject, calendar | TBD Phase 2 |
| Time | Timesheets, approve/reject, time reports, clock in/out | TBD Phase 2 |
| Recruitment (ATS) | Vacancies, candidates, hiring process | TBD Phase 2 |
| Performance | 180° reviews, trackers (Starter-limited) | TBD Phase 2 |
| Reporting & Analytics | Leave/time/PIM reports, custom/dynamic reports | TBD Phase 2 |
| Directory | Corporate directory | TBD Phase 2 |
| Maintenance | GDPR/maintenance | TBD Phase 2 |
| Claim (+ `mobile`) | API module flags (`claim`, `mobile`) — Starter coverage unclear | TBD Phase 2 |

API module enum for reference: `admin, pim, leave, time, recruitment, performance, maintenance, mobile, directory, claim`.

## 4. Visible functionality (documented, not yet interactively executed)

Login → Dashboard → Employee add/filter/list → Leave apply (Full/Half/Specific-time, balance check, comment) → Leave assign/list → Timesheet approve/reject → Vacancy/candidate flow → Reports generation. Leave duration options (Full day / Half-day Morning-Evening / Specify Time) per Leave help article. All require hands-on verification in 5.8.1 build before test-case freeze.

## 5. Unavailable / out-of-recon items (explicit)

- Interactive demo walkthrough: **not performed** — demo is JS-rendered (`"doesn't work properly without JavaScript enabled"` via static fetch), no browser in this container to drive it yet.
- Pinned 5.8.1 behavior: **unverified** — no self-hosted instance deployed yet.
- Advanced-only premium (full Performance/Compensation/Surveys/Onboarding/Request Desk/advanced Roster), native mobile apps, payments, third-party connectors, prod deployment: **out of scope** per charter.
- Email delivery, LDAP/social auth, cloud trial provisioning: **not available in recon**; treat as limitation unless Phase 2 enables them.

## 6. Environment facts (this recon run)

| Field | Value |
|---|---|
| OS | Ubuntu 24.04.5 LTS (noble), from `/etc/os-release` |
| Browser | **None installed** — `firefox`, `chromium`, `google-chrome` all not found. Phase 2 must install Firefox (primary) + Chromium (secondary) and record versions |
| Viewport target | 1920×1080 (not yet verified — no browser) |
| Docker | 29.8.0 available, **zero images pulled** |
| Python | 3.14.2 (recon tooling only) |
| Disk | 18G avail on /workspaces |

## 7. Env limitations carried into Phase 2

1. Must `docker pull orangehrm/orangehrm` pinned digest + deploy with MySQL/MariaDB, then record URL + commit + digest here.
2. Must install browsers and re-check demo-vs-pinned parity for the 7 core modules above.
3. Static fetch cannot substitute for interactive recon — Phase 2 smoke must be hands-on (or Playwright-driven with screenshots) before scope freeze.

## 8. Verify (Phase 1 gate)

- [x] Exact SUT stated (5.8.1 pinned self-hosted) with recon source separated and dated
- [x] Unavailable items explicit (§5) — a stranger can tell what was *not* seen
- [ ] Phase 2 must flip every `TBD Phase 2` above to Present/Absent with build evidence

## Sources

- Demo login hint + versions: `opensource-demo.orangehrmlive.com` excerpts (Admin/admin123, OS 5.8 root / OS 5.9 deep link), 2026-10-03
- Pinned build: `orangehrm/orangehrm` `main` Dockerfile (`OHRM_VERSION 5.8.1`, `php:8.3-apache-bookworm`), Docker Hub `orangehrm/orangehrm`
- Modules: orangehrm.com Starter/Advanced pages; Starter Help categories (Admin/PIM/Leave/Time/Recruitment/Performance/Maintenance); API `GET /api/v2/admin/modules`; Leave help article (apply/assign/duration)
- Install prereqs: Starter Installation Guide (Apache 2.2+, PHP 7.4+, MySQL/MariaDB 5.5+; web installer steps 01–09)
