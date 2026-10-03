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

- EXP-SEARCH-01: exact/partial/case/ID/no-match/reset all behave correctly
  through the labeled filter fields. Employee Name autocomplete fires
  `/api/v2/pim/employees?nameOrId=…`, suggests, and select+Search returns 1
  card. ID 9999 → "No Records Found". Reset restores full list.
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
- No reproducible SUT defect surfaced in this session. Leave-submit charters
  (EXP-LEAVE-01) remain blocked on entitlement provisioning.
