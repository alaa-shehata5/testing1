# Exploratory Findings

## F-01 (2026-10-03, SES-2026-10-03-01): No SUT defect verified — discovery negative

- Charters exercised: EXP-PIM-01, EXP-SEARCH-01, EXP-AUTH-01 (partial).
- Areas probed with evidence: login invalid/unknown/empty/whitespace/long/
  special/repeat, dashboard + nav routing, logout/back/direct-URL, employee
  exact/partial/case/ID/no-match/reset search, employee
  valid/empty/duplicate/30/31/50-char create, detail view load.
- Outcome: every conclusive probe matched defensible expected behavior.
  Verified SUT defect count from this session: **0**. No `bugs/BUG-*/`
  report filed: `BUG-AUTH-001` and `BUG-LEAVE-001` remain unfilled templates
  by design. Reporting zero is the honest result; no metrics were fabricated
  to reach a quota.
- Test-design flags (NOT SUT defects, no BUG filed, Expected frozen):
  TC-AUTH-002 (ESS wording claims PIM visible; PIM correctly hidden) and
  TC-PIM-003 (assumes 50-char max; true limit is 30 with clear messaging).

## F-02 (2026-10-03): Voided probe error — unlabeled global Search box

- Early probes filled the header "Search" input (no form group, outside the
  labeled filter form) and misread unfiltered results as a search defect.
- Control mapping proved the error: real Employee Name field is the
  "Type for hints..." autocomplete in its labeled group; correct-field
  re-probes (SES-2026-10-03-01) all pass with API + suggestion evidence.
- The global box's purpose is unconfirmed (no label, content ignored by filter
  submit); without a defensible expected result, nothing is filed from it.
