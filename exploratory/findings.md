# Exploratory Findings

## F-01 (2026-10-03, SES-2026-10-03-01): No SUT defect verified — discovery negative

- Charters exercised: EXP-PIM-01, EXP-SEARCH-01, EXP-AUTH-01 (partial).
- Areas probed with evidence: login invalid/unknown/empty/whitespace/long/
  special/repeat, dashboard + nav routing, logout/back/direct-URL, employee
  exact/partial/case/ID/no-match/reset search, employee
  valid/empty/duplicate/30/31/50-char create, detail view load.
- Outcome: among exploratory probes with a defensible expected result, no
  SUT defect was verified. The two failed test assertions below are test
  design issues, not product failures. Verified SUT defect count from this
  session: **0**. No `bugs/BUG-*/` report filed; bug-report files remain
  templates by design.
- Test-design issues (not SUT defects; original expected results remain
  unchanged in the execution record): TC-AUTH-002 expected PIM in the ESS
  navigation although the role correctly hides it; TC-PIM-003 assumed a
  50-character name limit although the observed limit is 30.
- Update 2026-10-03 (conforming rerun SES-2026-10-03-02): the five PIM cases
  were rerun with their specified data (E2001/Aarav/ZzzNoMatch) and all pass.
  The exploratory E2091/E2092/9999 observations stand as supporting evidence.
  Correction: free-text name queries ARE submitted as filters — the ZzzNoMatch
  rerun returned 0 cards with "No Records Found", disproving the earlier
  select-only theory. TC-PIM-005 has no test-design issue.

## F-02 (2026-10-03): Voided probe error — unlabeled global Search box

- Early probes filled the header "Search" input (no form group, outside the
  labeled filter form) and misread unfiltered results as a search defect.
- Control mapping proved the error: real Employee Name field is the
  "Type for hints..." autocomplete in its labeled group; correct-field
  re-probes (SES-2026-10-03-01) all pass with API + suggestion evidence.
- The global box's purpose is unconfirmed (no label, content ignored by filter
  submit); without a defensible expected result, nothing is filed from it.
