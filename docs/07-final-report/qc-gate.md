# QC Gate verdict — 2026-10-03 (Phase 14)

> **Decision: APPROVED for portfolio publication as a partial-cycle engagement.**
> This is not a product release approval. The gate remains blocking for
> inaccurate claims, broken traceability, or unreviewed artifacts; the
> incomplete execution and zero-defect outcome are disclosed limitations, not
> criteria silently marked complete.
>
> Re-run the repository checks from the root with
> `python3 -m pip install -r scripts/requirements-qc.txt && python3 scripts/validate_qc.py`.
> The validator checks workbook mappings and status counts, evidence paths,
> expected artifact inventory, ethics disclaimers, and every local Markdown
> link in tracked Markdown files. Human review is still required for screenshot
> meaning/privacy, expected-result defensibility, and the ethics of findings.

## Requirements — PASS

- 20 unique IDs; every requirement maps to at least one case. Assumptions are
  kept separately in `assumptions.md` (4 ASM IDs).

## Cases — PASS

- 54 unique TC IDs; Requirement, Expected Result, Steps, and Test Data are
  populated for every case.
- Type mix matches plan: Positive 20, Negative 14, Boundary 6, State 5,
  UI 4, Compatibility 3, Accessibility 2 (= 54). No duplicate IDs.

## Bugs — PASS (by honest zero)

- `bugs/` holds one clearly-marked unfilled template + a README stating the
  zero count and the filing process. No fabricated defects, no fake severity.
- The 2 Failed cases (TC-AUTH-002, TC-PIM-003) are test-design flags with
  blank Defect IDs and frozen Expected Results — correctly unlinked.

## RTM — PASS

- Every RTM reference resolves to an existing TC; every TC has an execution
  state and appears exactly once in the RTM. Requirement mappings and per-REQ
  status totals reconcile with the case and execution workbooks.

## Metrics — PASS

- 54 = 17 Pass + 2 Fail + 2 Blocked + 33 Not Run. Execution 38.9%,
  pass-of-executed 81.0%, fail 9.5%. Blocked never counted as Passed; N/A absent.
- Counts identical in execution log, case workbook, summary, final report, and
  dashboard SVG. Defect total (0) matches `bugs/`.

## Repository, evidence, and README — PASS

- Inventory: 43 evidence PNGs and 5 QA XLSX workbooks. These are intentional
  portfolio deliverables explicitly required
  by the plan; all PNGs are under `evidence/` and all workbooks under `docs/`.
  No other binary artifact types are allowed by this gate.
- Eight tracked test-data files. `.env` is ignored and untracked; the
  reproducibility instructions identify their localhost database passwords
  as disposable throwaways. This is not represented as an automated secrets
  scan.
- The validator checks every local Markdown link in tracked Markdown (not a
  sample), plus every regression evidence path. README links, embedded images,
  and the demo assets resolve.

## Ethics — PASS (after fix)

- Mandatory disclaimer now on README, final report, and case study. No client
  or employment claims in the reviewed portfolio materials. Penetration
  testing explicitly out of scope.

## Acceptance — PARTIAL-CYCLE WAIVERS

- Satisfied for this portfolio: pinned build and reproducible environment,
  frozen scope, 54 documented/traced cases, execution evidence, reconciled
  metrics, final report, README, eight portfolio images, demo script, and
  disclaimer.
- Not satisfied and explicitly waived only for this partial-cycle portfolio:
  a genuine reproducible defect and the FAIL→BUG→retest/Featured Defect
  differentiators. No defect was verified in the 21 cases with dispositions;
  none was fabricated. This waiver is not a claim that the 54-case suite is
  complete or that the product passed release criteria.
- Carried forward: 33 Not Run cases and the leave-entitlement setup remain
  entry tasks for the next execution cycle.

**Gate: APPROVED for portfolio publication, with the partial-cycle limitations
and waivers above. No product release verdict is given. Re-run the gate after
the next execution cycle; it does not expire this portfolio approval.**
