# Exploratory Session Notes

## SES-2026-10-03-01 — PIM + Search + Auth edge probes (Phase 9 discovery)

- Date: 2026-10-03. Duration: ~1h across probe batches. Tester: AI agent
  (Playwright-driven Firefox 155.0, 1920×1080, OrangeHRM 5.8.1 pinned).
- Charters: EXP-PIM-01 (forms), EXP-SEARCH-01 (filters), EXP-AUTH-01
  (session/edge). Mission: find genuine reproducible SUT defects; void and
  document any probe error instead of filing it.
- Evidence: `evidence/smoke/TC-PIM-*.png`, `/tmp/probe9/` scratch shots.
  Synthetic records only (E2091, E2092 — disposable).

### Notes

- EXP-SEARCH-01: exploratory queries through the labeled filter fields
  behaved as expected for the values actually entered. Employee Name
  autocomplete fires `/api/v2/pim/employees?nameOrId=…`, suggests, and
  select+Search returns 1 card. ID 9999 → "No Records Found". Reset restores
  full list. These are exploratory observations, not passes for planned cases
  that specify different values (Aarav/E2001 and ZzzNoMatch).
- EXP-PIM-01: empty-required blocked ("Required" x2); duplicate E2091 blocked
  ("Employee Id already exists", still 1 record); true first-name limit is 30
  (30 saved+retrievable, 31 rejected, 50 rejected — all with clear messages).
- EXP-AUTH-01: 500-char username + script/quote password rejected safely (no
  session, stays on login); repeat login + revisit-login redirect correct.
- Probe error (voided, NOT filed): several early batches typed into the
  unlabeled global "Search" box (no group, outside the filter form) instead of
  the Employee Name field, then read "search ignores query" as a finding.
  Control mapping (`input → label → autocomplete membership`) exposed the
  error; correct-field re-probes pass. Lesson recorded in findings.md F-02.
- No reproducible SUT defect surfaced in this session. The two failed
  assertions (TC-AUTH-002 and TC-PIM-003) are test-design issues.
  Leave-submit charters (EXP-LEAVE-01) remain blocked on entitlement
  provisioning.

## SES-2026-10-03-02 — Conforming rerun with specified data (dispute resolution)

- Date: 2026-10-03. Duration: ~30 min. Tester: AI agent (Playwright-driven
  Firefox 155.0, 1920×1080, OrangeHRM 5.8.1 pinned).
- Mission: resolve the planned-input dispute by executing TC-PIM-001/002/004/
  005/007 with their specified data (E2001/Aarav/ZzzNoMatch).
- Procedure: seeded E2001 (Aarav Sharma, DOB 1990-01-15 per valid_employee.csv;
  "Successfully Saved"); verified ID search (1 card); set DOB on personal
  details ("Successfully Updated", persists after refresh); empty-save +
  duplicate-E2001 attempts (both blocked, still 1 record); 'Aarav'
  autocomplete → exactly E2001, Reset → 6 rows; 'ZzzNoMatch' → 0 cards +
  "No Records Found".
- Outcome: all five pass with specified data. Evidence:
  `evidence/smoke/TC-PIM-001-E2001-*.png`, `TC-PIM-002-E2001-duplicate.png`,
  `TC-PIM-004-Aarav-search.png`, `TC-PIM-005-ZzzNoMatch.png`,
  `TC-PIM-007-E2001-detail.png`. Correction: free-text name queries are
  submitted as filters (select-only theory disproven).
