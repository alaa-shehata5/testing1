# RTM — Requirement → Test → Execution → Defect

`rtm.xlsx` is the complete requirement-to-case matrix; it contains one row per
DRS requirement with the mapped case IDs, current execution state, defect
link (blank unless raised), and coverage state.

Before execution, the matrix records planned coverage only. The workbook
currently has 54 planned cases, all `Not Run`; no row should imply a pass or
verified defect before evidence is recorded. Time, Recruitment, and Reports
rows/cases are conditional on confirming those modules in the pinned build.
If a conditional module is absent, update the scope, cases, and RTM together.

## Phase 7 gate (pre-execution, 2026-10-03)

- 20 requirements × 54 planned cases. Every REQ maps to ≥1 TC; every TC maps
  back to exactly one REQ. No orphan TCs, no broken IDs.
- All rows are `Not Run` with blank Defect ID and `Coverage = Planned`.
- TC ID prefixes are suite ordering only, not strict REQ linkage:
  `TC-DASH-004` (unauthenticated dashboard URL) maps to `REQ-AUTH-004`.
- `TC-PIM-002` is a single combined case for both empty-required and
  duplicate-ID attempts under `REQ-PIM-004`; `TC-PIM-003` (50-char boundary)
  maps to `REQ-PIM-001`.
- `REQ-PIM-003` covers view/edit plus conditional delete (`TC-PIM-008`;
  execute only where deletion is available).

Metrics after execution: Coverage = requirements with ≥1 planned TC / total
requirements × 100; Execution = executed / in-scope cases × 100; Pass =
passed / executed × 100; Fail = failed / executed × 100; Blocked = blocked /
in-scope cases × 100. Defect coverage (project metric) = failed cases linked
to defects / failed cases × 100. Report denominators and exclude conditional
cases only after a documented scope decision.
