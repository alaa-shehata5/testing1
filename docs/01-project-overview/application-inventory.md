# Application Inventory — Reconnaissance (Phase 1)

> Freeze statement: **This exact application/version/build is the system under test** for final execution is OrangeHRM Starter **5.8.1 self-hosted** (see charter). The public demo below was used for **reconnaissance only** and is version-volatile — it is not execution evidence.

## 1. SUT identity

| Field | Value |
|---|---|
| Application | OrangeHRM Starter / Open Source (self-hosted, pinned) |
| Pinned version (final execution) | **5.8.1** — `OHRM_VERSION 5.8.1` in `orangehrm/orangehrm:main` Dockerfile (`FROM php:8.3-apache-bookworm`), ZIP `stable/5.8.1`, MD5 `173cbdffe595246d7e54ec2f2330857d` |
| Self-hosted URL | `http://localhost/` (`/` redirects to `/web/index.php/auth/login`) |
| Build/commit pin | Docker image `orangehrm/orangehrm:5.8.1`, digest `sha256:5eb278acc6280c9a3144b2868230abe48b5bc5892fe00d07c7ec3028e86638e7`; source tag `v5.8.1`, commit `d3a50a8` (see `environment.md`) |
| Recon source (not SUT) | `https://opensource-demo.orangehrmlive.com` and `https://opensource-demo.orangehrmlive.com/web/index.php/auth/login` |
| Demo version observed 2026-10-03 | Root page footer: **OrangeHRM OS 5.8**; deep login path footer: **OrangeHRM OS 5.9**. Demo is drifting — confirms demo cannot serve as reproducible SUT |
| License | GPL-3.0 (`orangehrm/orangehrm` repo) |
| Recon date/time | 2026-10-03 12:51 UTC |

## 2. Roles (verified in pinned build 2026-10-03)

| Role | Source | Status |
|---|---|---|
| Admin (`qa_admin`) | Created during local install (employee "QA Admin") | Verified: logs in, lands on dashboard, full 12-item nav |
| ESS (`qa_ess`) | Created 2026-10-03, linked to employee "Ess Testuser" | Verified: logs in; sees Leave/Time/My Info/Performance/Dashboard/Directory/Claim/Buzz (no Admin/PIM/Recruitment/Maintenance) |
| Supervisor | No separate Supervisor login in Starter; supervision is an ESS assignment | Deferred: approval flows use qa_admin unless a supervisor assignment is configured during execution |
| Custom ESS / Custom Supervisor | User-role docs | Not provisioned; out of execution scope |

Credentials remain local in gitignored `.env` and are not recorded here.

## 3. Modules

Starter-documented module set (marketing + Starter Help + API `GET /api/v2/admin/modules`). Database flags (`ohrm_module`) plus hands-on nav verification 2026-10-03 via authenticated qa_admin (full nav) and qa_ess (restricted nav) sessions at `http://localhost/`.

| Module | DB flag | Admin nav | ESS nav | Status |
|---|---|---|---|---|
| Dashboard | enabled | ✓ | ✓ | Present (UI-verified) |
| Admin / HR Administration | enabled | ✓ | — | Present (UI-verified) |
| PIM / Employee Management | enabled | ✓ | — | Present (UI-verified) |
| Leave / PTO | enabled | ✓ | ✓ | Present (UI-verified) |
| Time / Attendance | `time` + `attendance` enabled | ✓ | ✓ | Present (UI-verified) |
| Recruitment (ATS) | enabled | ✓ | — | Present, admin-side (UI-verified) |
| Performance | enabled | ✓ | ✓ | Present (UI-verified; Starter limits apply) |
| Reporting & Analytics | no standalone flag | (sub-views) | (sub-views) | Partial: report views live under PIM/Leave/Time; confirm per-case in execution |
| Directory | enabled | ✓ | ✓ | Present (UI-verified) |
| Maintenance | enabled | ✓ | — | Present (UI-verified) |
| Claim / Mobile | both enabled | ✓ Claim | ✓ Claim | Claim present (UI-verified); mobile-app coverage out of scope |
| Buzz | — | ✓ | ✓ | Present (UI-verified; social feed, no cases planned) |
| My Info (ESS profile) | — | — | ✓ | Present (UI-verified) |

API module enum for reference: `admin, pim, leave, time, recruitment, performance, maintenance, mobile, directory, claim`.

## 4. Visible functionality (interactively verified 2026-10-03)

Authenticated sessions verified end to end in Firefox: qa_admin login lands
on `/web/index.php/dashboard/index` with the full 12-item nav; qa_ess login
lands on the same dashboard with the 8-item restricted nav. Test employee
"Ess Testuser" created via PIM and linked to the qa_ess system account.
Functional workflows (create/search/apply/approve) are NOT yet executed —
that is TEST-CYCLE-01.

## 5. Unavailable / out-of-recon items (explicit)

- Interactive demo walkthrough: **not performed** — demo is JS-rendered (`"doesn't work properly without JavaScript enabled"` via static fetch); pinned build verified instead.
- Pinned 5.8.1 authenticated behavior: **login + nav verified**; functional workflows await TEST-CYCLE-01.
- Advanced-only premium (full Performance/Compensation/Surveys/Onboarding/Request Desk/advanced Roster), native mobile apps, payments, third-party connectors, prod deployment: **out of scope** per charter.
- Email delivery, LDAP/social auth, cloud trial provisioning: **not available in recon**; treat as limitation unless Phase 2 enables them.

## 6. Environment facts (this recon run)

| Field | Value |
|---|---|
| OS | Ubuntu 24.04.5 LTS (noble), from `/etc/os-release` |
| Browser at recon time | No browsers were installed during initial recon; Firefox 155.0 and Chrome for Testing 153.0.8010.12 were installed afterward |
| Viewport target | 1920×1080; both browsers later loaded the installed login page |
| Docker at recon time | Docker 29.8.0 available; no images had yet been pulled |
| Python | 3.14.2 (recon tooling only) |
| Disk | 18G avail on /workspaces |

## 7. Remaining verification (execution-gated)

1. [x] Sign in with `qa_admin`, provision ESS user, record runtime module visibility — done 2026-10-03 (this file §2–§4).
2. Re-check demo-vs-pinned behavior for selected core modules during TEST-CYCLE-01 functional days.
3. Static fetch cannot substitute for interactive recon — execution stays hands-on (Playwright-driven with screenshots).

## 8. Verify (Phase 1 gate)

- [x] Exact SUT stated (5.8.1 pinned self-hosted) with recon source separated and dated
- [x] Unavailable items explicit (§5) — a stranger can tell what was *not* seen
- [x] Runtime module visibility and role access verified in the installed pinned build (DB flags + authenticated admin/ESS nav, 2026-10-03)

## Sources

- Demo login hint + versions: `opensource-demo.orangehrmlive.com` excerpts (Admin/admin123, OS 5.8 root / OS 5.9 deep link), 2026-10-03
- Pinned build: `orangehrm/orangehrm` `main` Dockerfile (`OHRM_VERSION 5.8.1`, `php:8.3-apache-bookworm`), Docker Hub `orangehrm/orangehrm`
- Modules: orangehrm.com Starter/Advanced pages; Starter Help categories (Admin/PIM/Leave/Time/Recruitment/Performance/Maintenance); API `GET /api/v2/admin/modules`; Leave help article (apply/assign/duration)
- Install prereqs: Starter Installation Guide (Apache 2.2+, PHP 7.4+, MySQL/MariaDB 5.5+; web installer steps 01–09)
