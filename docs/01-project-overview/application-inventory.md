# Application Inventory — Reconnaissance (Phase 1)

> Freeze statement: **This exact application/version/build is the system under test** for final execution is OrangeHRM Starter **5.8.1 self-hosted** (see charter). The public demo below was used for **reconnaissance only** and is version-volatile — it is not execution evidence.

## 1. SUT identity

| Field | Value |
|---|---|
| Application | OrangeHRM Starter / Open Source (self-hosted, pinned) |
| Pinned version (final execution) | **5.8.1** — `OHRM_VERSION 5.8.1` in `orangehrm/orangehrm:main` Dockerfile (`FROM php:8.3-apache-bookworm`), ZIP `stable/5.8.1`, MD5 `173cbdffe595246d7e54ec2f2330857d` |
| Self-hosted URL | `http://localhost:8080/` (currently redirects to the fresh-install wizard; see `environment.md`) |
| Build/commit pin | Docker image `orangehrm/orangehrm:5.8.1`, digest `sha256:5eb278acc6280c9a3144b2868230abe48b5bc5892fe00d07c7ec3028e86638e7`; source tag `v5.8.1`, commit `d3a50a8` (see `environment.md`) |
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

Starter-documented module set (marketing + Starter Help + API `GET /api/v2/admin/modules`). Presence in the pinned build is not verified until the installer is complete and each module is checked.

| Module | Documented capability | Pinned-build status |
|---|---|---|
| Dashboard | Landing, widgets, nav | Not verified; installer incomplete |
| Admin / HR Administration | Users, roles, org structure, config | Not verified; installer incomplete |
| PIM / Employee Management | Employee DB, add/filter/list, corporate directory | Not verified; installer incomplete |
| Leave / PTO | Apply, assign, leave list, entitlements, balance check, approve/reject, calendar | Not verified; installer incomplete |
| Time | Timesheets, approve/reject, time reports, clock in/out | Not verified; installer incomplete |
| Recruitment (ATS) | Vacancies, candidates, hiring process | Not verified; installer incomplete |
| Performance | 180° reviews, trackers (Starter-limited) | Not verified; installer incomplete |
| Reporting & Analytics | Leave/time/PIM reports, custom/dynamic reports | Not verified; installer incomplete |
| Directory | Corporate directory | Not verified; installer incomplete |
| Maintenance | GDPR/maintenance | Not verified; installer incomplete |
| Claim (+ `mobile`) | API module flags (`claim`, `mobile`) — Starter coverage unclear | Not verified; installer incomplete |

API module enum for reference: `admin, pim, leave, time, recruitment, performance, maintenance, mobile, directory, claim`.

## 4. Visible functionality (documented, not yet interactively executed)

Login → Dashboard → Employee add/filter/list → Leave apply (Full/Half/Specific-time, balance check, comment) → Leave assign/list → Timesheet approve/reject → Vacancy/candidate flow → Reports generation. Leave duration options (Full day / Half-day Morning-Evening / Specify Time) per Leave help article. All require hands-on verification in 5.8.1 build before test-case freeze.

## 5. Unavailable / out-of-recon items (explicit)

- Interactive demo walkthrough: **not performed** — demo is JS-rendered (`"doesn't work properly without JavaScript enabled"` via static fetch), no browser in this container to drive it yet.
- Pinned 5.8.1 behavior: **unverified** — image is running, but the web installer is incomplete.
- Advanced-only premium (full Performance/Compensation/Surveys/Onboarding/Request Desk/advanced Roster), native mobile apps, payments, third-party connectors, prod deployment: **out of scope** per charter.
- Email delivery, LDAP/social auth, cloud trial provisioning: **not available in recon**; treat as limitation unless Phase 2 enables them.

## 6. Environment facts (this recon run)

| Field | Value |
|---|---|
| OS | Ubuntu 24.04.5 LTS (noble), from `/etc/os-release` |
| Browser at recon time | No browsers were installed during the initial recon; Firefox 155.0 and Chrome for Testing 153.0.8010.12 were installed afterward (see `environment.md`) |
| Viewport target | 1920×1080; both browsers later reached the installer, not the configured application |
| Docker at recon time | Docker 29.8.0 available; no images had yet been pulled |
| Python | 3.14.2 (recon tooling only) |
| Disk | 18G avail on /workspaces |

## 7. Env limitations carried into Phase 2

1. Complete the installer, provision test users, and record hands-on module presence/absence with evidence.
2. Re-check demo-vs-pinned behavior for the selected core modules after installation.
3. Static fetch cannot substitute for interactive recon — Phase 2 smoke must be hands-on (or Playwright-driven with screenshots) before scope freeze.

## 8. Verify (Phase 1 gate)

- [x] Exact SUT stated (5.8.1 pinned self-hosted) with recon source separated and dated
- [x] Unavailable items explicit (§5) — a stranger can tell what was *not* seen
- [ ] Phase 2 must verify each module as Present/Absent in the installed pinned build, with evidence

## Sources

- Demo login hint + versions: `opensource-demo.orangehrmlive.com` excerpts (Admin/admin123, OS 5.8 root / OS 5.9 deep link), 2026-10-03
- Pinned build: `orangehrm/orangehrm` `main` Dockerfile (`OHRM_VERSION 5.8.1`, `php:8.3-apache-bookworm`), Docker Hub `orangehrm/orangehrm`
- Modules: orangehrm.com Starter/Advanced pages; Starter Help categories (Admin/PIM/Leave/Time/Recruitment/Performance/Maintenance); API `GET /api/v2/admin/modules`; Leave help article (apply/assign/duration)
- Install prereqs: Starter Installation Guide (Apache 2.2+, PHP 7.4+, MySQL/MariaDB 5.5+; web installer steps 01–09)
