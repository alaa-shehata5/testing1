# Environment (Phase 2) — reproducible self-hosted build

Date: 2026-10-03. All values below were observed on this machine unless marked TBD.

## 1. Host + browsers

| Field | Value |
|---|---|
| OS | Ubuntu 24.04.5 LTS (noble), `/etc/os-release` |
| Primary browser | **Mozilla Firefox 155.0** (Playwright `firefox-1543`, `firefox --version`) |
| Secondary browser | **Chrome for Testing 153.0.8010.12** (Playwright `chromium-1243`, `chrome-linux64/chrome --version`) |
| Browser source | `npx -y playwright@latest install chromium firefox --with-deps` (v1.63.0); no system Firefox/Chromium installed (apt offers snap stubs only, snap unavailable) |
| Viewport | 1920×1080 — authenticated qa_admin + qa_ess sessions verified in Firefox at this viewport (dashboard + nav); Chrome verified to login page |
| Docker | 29.8.0 |
| Date | 2026-10-03; installer completed ~14:00 UTC, logins + nav verified ~14:10 UTC |

## 2. SUT containers (pinned — matches charter §1)

| Item | Value |
|---|---|
| App image | `orangehrm/orangehrm:5.8.1` — digest `sha256:5eb278acc6280c9a3144b2868230abe48b5bc5892fe00d07c7ec3028e86638e7`, image ID `5eb278acc628`, 832MB |
| App env inside image | `OHRM_VERSION=5.8.1`, `OHRM_MD5=173cbdffe595246d7e54ec2f2330857d` (matches charter) |
| DB image | `mariadb:10.11` (`10.11.19-MariaDB-ubu2204`), ready for connections |
| Container network | Host network mode; Apache listens on port 80 and MariaDB on port 3306 |
| SUT URL | `http://localhost/` → redirects to `/web/index.php/auth/login` |
| Install proof | Installer log records migrations through 5.8.1, instance creation, DB-user creation, and config write. The database contains 168 tables and one `qa_admin` account linked to the Admin role. |
| Login-page proof | Firefox 155.0 and Chrome for Testing 153.0.8010.12 both loaded the login page at HTTP 200/title `OrangeHRM`, viewport 1920×1080; username/password/Login controls were present |
| Authenticated-session proof | qa_admin login lands on `/web/index.php/dashboard/index` with 12-item nav; qa_ess login lands with 8-item restricted nav (both Firefox, 1920×1080, 2026-10-03) |
| Module flags | 18 `ohrm_module` rows are enabled, including admin, PIM, Leave, Time, Attendance, Recruitment, Dashboard, Performance, Directory, Maintenance, Claim, and Mobile. This is DB configuration evidence only, not proof of role-visible UI functionality. |
| Git tag (source pin) | `orangehrm/orangehrm` tag `v5.8.1`, commit `d3a50a8` (PR #1934, 2026-04-06) |
| Drift warning | `orangehrm/orangehrm:latest` (= `5.9`, digest `sha256:d692780e…`, `OHRM_VERSION=5.9`) is **not** the SUT — always use the `:5.8.1` tag + digest above |

## 3. Reproduce (copy-paste)

```bash
# NOTE: passwords below are disposable local-only throwaways for `localhost`
# reproduction. Never reuse for shared/staging/prod systems.
docker run -d --name orangehrm-db --network host \
  -e MARIADB_ROOT_PASSWORD=rootpass -e MARIADB_DATABASE=orangehrm \
  -e MARIADB_USER=orangehrm -e MARIADB_PASSWORD=orangehrmpass mariadb:10.11
docker run -d --name orangehrm-581 --network host \
  orangehrm/orangehrm:5.8.1@sha256:5eb278acc6280c9a3144b2868230abe48b5bc5892fe00d07c7ec3028e86638e7
curl -s -o /dev/null -w "%{http_code} %{url_effective}\n" -L http://localhost/
```

Host networking is Linux-specific (bridge mode dropped inter-container TCP
with timeout 110; host mode verified working). Keep these disposable
credentials local; do not use them on shared or production systems. The web
installer was completed 2026-10-03 (Welcome → License → DB host `127.0.0.1`,
existing database `orangehrm` → System Check → Instance "QAPortfolio Ltd",
US/English/UTC → Admin user `qa_admin` → Install; 168 tables, root serves the
login page). Test users provisioned per `test-data/users.md`.

## 4. Test data (all synthetic)

| File | Rows | Purpose |
|---|---|---|
| `test-data/valid_employee.csv` | 3 | Happy-path PIM creation |
| `test-data/boundary_employee.csv` | 4 | Name min/max length, age 18y/100y on 2026-10-03 |
| `test-data/invalid_employee.csv` | 4 | Empty, numeric names, duplicate ID `E2001`, future DOB |
| `test-data/leave_boundary_dates.csv` | 8 | Past/today/future, half-day, End<Start, long range, weekend |
| `test-data/search_test_data.csv` | 6 | Exact/case/partial/space/no-result/id queries |
| `test-data/users.md` | 2 provisioned | qa_admin (installer admin) + qa_ess (linked to "Ess Testuser"); supervisor deferred to qa_admin (see users.md) |
| `test-data/employees.csv` | 2 | Legacy seed with IDs unique from `valid_employee.csv` |
| `test-data/leave-data.csv` | 2 | Legacy seed (kept) |

## 5. Entry-gate status (all clear for TEST-CYCLE-01)

- [x] Web installer completed; pinned application login page is live.
- [x] qa_admin + qa_ess logins verified; role nav recorded in inventory.
- [x] Runtime module presence/access verified (inventory §3); Reports partial-flag documented.
- [ ] Containers currently running (`orangehrm-581`, `orangehrm-db`); stop with `docker stop` / remove with `docker rm` — data is disposable, test data re-seeds from CSVs.

## Verify (Phase 2 gate)

- [x] Official source only (Docker Hub `orangehrm/*`, GitHub tag `v5.8.1`) — no third-party copy
- [x] OS / browsers / app / viewport / date recorded with versions
- [x] Both browsers load the installed login page and expose username/password/Login controls (200 + title, both engines, 1920×1080)
- [x] All 8 required test-data files present
- [x] Another person can reproduce and authenticate in the environment via §3 + `test-data/users.md` (credentials stay local in `.env`)
