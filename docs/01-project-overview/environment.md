# Environment (Phase 2) — reproducible self-hosted build

Date: 2026-10-03. All values below were observed on this machine unless marked TBD.

## 1. Host + browsers

| Field | Value |
|---|---|
| OS | Ubuntu 24.04.5 LTS (noble), `/etc/os-release` |
| Primary browser | **Google Chrome for Testing 153.0.8010.12** (Playwright `chromium-1243`, `chrome-linux64/chrome --version`) |
| Secondary browser | **Mozilla Firefox 155.0** (Playwright `firefox-1543`, `firefox --version`) |
| Browser source | `npx -y playwright@latest install chromium firefox --with-deps` (v1.63.0); no system Firefox/Chromium installed (apt offers snap stubs only, snap unavailable) |
| Viewport | 1920×1080 — verified: both browsers loaded SUT at this viewport, HTTP 200, title `OrangeHRM` |
| Docker | 29.8.0 |
| Date | 2026-10-03 12:5x UTC |

## 2. SUT containers (pinned — matches charter §1)

| Item | Value |
|---|---|
| App image | `orangehrm/orangehrm:5.8.1` — digest `sha256:5eb278acc6280c9a3144b2868230abe48b5bc5892fe00d07c7ec3028e86638e7`, image ID `5eb278acc628`, 832MB |
| App env inside image | `OHRM_VERSION=5.8.1`, `OHRM_MD5=173cbdffe595246d7e54ec2f2330857d` (matches charter) |
| DB image | `mariadb:10.11` (`10.11.19-MariaDB-ubu2204`), ready for connections |
| SUT URL | `http://localhost:8080/` → redirects to `/installer/index.php/welcome` (fresh-install wizard) |
| Installer proof | `curl` shows footer `OrangeHRM OS 5.8.1`; both browsers HTTP 200 title `OrangeHRM` at 1920×1080 |
| Git tag (source pin) | `orangehrm/orangehrm` tag `v5.8.1`, commit `d3a50a8` (PR #1934, 2026-04-06) |
| Drift warning | `orangehrm/orangehrm:latest` (= `5.9`, digest `sha256:d692780e…`, `OHRM_VERSION=5.9`) is **not** the SUT — always use the `:5.8.1` tag + digest above |

## 3. Reproduce (copy-paste)

```bash
# NOTE: passwords below are disposable local-only throwaways for `localhost`
# reproduction. Never reuse for shared/staging/prod systems.
docker network create orangehrm-net
docker run -d --name orangehrm-db --network orangehrm-net \
  -e MARIADB_ROOT_PASSWORD=rootpass -e MARIADB_DATABASE=orangehrm \
  -e MARIADB_USER=orangehrm -e MARIADB_PASSWORD=orangehrmpass mariadb:10.11
docker run -d --name orangehrm-581 --network orangehrm-net \
  -p 8080:80 orangehrm/orangehrm:5.8.1@sha256:5eb278acc6280c9a3144b2868230abe48b5bc5892fe00d07c7ec3028e86638e7
curl -s -o /dev/null -w "%{http_code}\n" -L http://localhost:8080/
```

Then complete the web installer (Welcome → License → DB host `orangehrm-db`,
database `orangehrm` → System Check → Instance → Admin user → Install) and
create the users in `test-data/users.md`.

## 4. Test data (all synthetic)

| File | Rows | Purpose |
|---|---|---|
| `test-data/valid_employee.csv` | 3 | Happy-path PIM creation |
| `test-data/boundary_employee.csv` | 4 | Name min/max, age 18y/100y on 2026-10-03 |
| `test-data/invalid_employee.csv` | 4 | Empty, numeric names, duplicate ID `E2001`, future DOB |
| `test-data/leave_boundary_dates.csv` | 8 | Past/today/future, half-day, End<Start, long range, weekend |
| `test-data/search_test_data.csv` | 6 | Exact/case/partial/space/no-result/id queries |
| `test-data/users.md` | 3 users | Admin / ESS / Supervisor provisioning (passwords via env) |
| `test-data/employees.csv` | 2 | Legacy seed (kept) |
| `test-data/leave-data.csv` | 2 | Legacy seed (kept) |

## 5. Outstanding (blocks execution entry gate)

- [ ] Web installer not yet completed — instance creation + admin user pending.
- [ ] No test users provisioned yet (needs installed instance).
- [ ] Module presence (`TBD Phase 2` in application-inventory.md) flips to Present/Absent only after install.
- [ ] Containers currently running (`orangehrm-581`, `orangehrm-db`); stop with `docker stop` / remove with `docker rm` — data is disposable, test data re-seeds from CSVs.

## Verify (Phase 2 gate)

- [x] Official source only (Docker Hub `orangehrm/*`, GitHub tag `v5.8.1`) — no third-party copy
- [x] OS / browsers / app / viewport / date recorded with versions
- [x] Browsers verified against live SUT (200 + title, both engines, 1920×1080)
- [x] All 8 required test-data files present
- [ ] Another person can reproduce env — commands in §3; installer completion still required before TEST-CYCLE-01
