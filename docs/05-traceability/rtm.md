# RTM — Requirement → Test → Execution → Defect

`rtm.xlsx` is the complete requirement-to-case matrix; it contains one row per
DRS requirement with the mapped case IDs, current execution state, defect
link (blank unless raised), and coverage state.

Before execution, the matrix records planned coverage only. The workbook
currently has 54 planned cases, all `Not Run`; no row should imply a pass or
verified defect before evidence is recorded. Time, Recruitment, and Reports
rows/cases are conditional on confirming those modules in the pinned build.
If a conditional module is absent, update the scope, cases, and RTM together.

Metrics after execution: Coverage = requirements with ≥1 planned TC / total
requirements × 100; Execution = executed / in-scope cases × 100; Pass =
passed / executed × 100; Fail = failed / executed × 100; Blocked = blocked /
in-scope cases × 100. Defect coverage (project metric) = failed cases linked
to defects / failed cases × 100. Report denominators and exclude conditional
cases only after a documented scope decision.
