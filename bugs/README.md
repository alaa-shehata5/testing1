# Bug Reports

> Verified SUT defects filed: **0**. This directory intentionally contains no
> defect reports. `BUG-LEAVE-001/bug-report.md` is the **unfilled filing
> template** (severity/priority scale, environment block, reproduction
> skeleton) — it demonstrates the reporting process, not a found bug. Do not
> cite it as a defect.

## Why zero is the honest count

- 21 of 54 planned cases executed with evidence; every conclusive probe
  matched defensible expected behavior (auth/session, search, creation
  validation, edit persistence, punch cycle).
- Two Failed cases are test-design wording issues (TC-AUTH-002 ESS nav text,
  TC-PIM-003 50-char assumption vs the true 30-char limit) — Expected Results
  left frozen, no BUG filed for correct application behavior.
- One voided probe error (unlabeled global Search box) is documented in
  `exploratory/findings.md` F-02 instead of being filed.
- Per project rule: report 0 if 0 — never fabricate defects to reach a quota.

## If a defect is verified later

File it as `bugs/BUG-<MOD>-<NNN>/bug-report.md` with `evidence/` holding
`01-precondition.png`, `02-input.png`, `03-failure.png`, and `evidence.md`
(each shot answering "What am I looking at?"), link it from
`docs/06-execution/execution-results.xlsx` (Defect ID) and the RTM, and
record retest in `docs/06-execution/retest-results.xlsx`.
