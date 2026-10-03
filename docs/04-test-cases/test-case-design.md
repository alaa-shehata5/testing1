# Test-Case Design — OrangeHRM Manual QA

## Status

The workbook contains 54 **planned, unexecuted** cases. Cases for Time,
Recruitment, and Reports are conditional on those modules being present and
usable in the pinned 5.8.1 build. Confirm module availability and freeze the
final allocation before execution; do not silently mark absent-module cases as
passed or redistribute them.

## Workbook

`test-cases.xlsx` is the case source of record. It has one row per case and
these columns: TC ID, Requirement ID, Module, Scenario, Title, Priority, Test
Type, Preconditions, Test Data, Environment, Steps, Expected Result, Actual
Result, Status, Defect ID, Notes.

Each case has a stable ID, a specific requirement mapping, concrete
preconditions/data, reproducible steps, and an observable expected result.
Actual Result and Defect ID remain empty until execution; all planned cases
start as `Not Run`.

## Allocation

| Area | Planned cases |
|---|---:|
| Authentication | 8 |
| Dashboard | 4 |
| PIM / Employee | 10 |
| Profile | 6 |
| Leave | 12 |
| Time (conditional) | 5 |
| Recruitment (conditional) | 4 |
| Reports (conditional) | 3 |
| UI / compatibility | 2 |
| **Total planned** | **54** |

TC ranges: `TC-AUTH-001–008`, `TC-DASH-001–004`, `TC-PIM-001–010`,
`TC-PROF-001–006`, `TC-LEAVE-001–012`, `TC-TIME-001–005`,
`TC-REC-001–004`, `TC-REP-001–003`, `TC-UI-001`, `TC-COMP-001`.

## Test-data and execution rules

- Employee cases use synthetic rows in `test-data/valid_employee.csv`,
  `boundary_employee.csv`, and `invalid_employee.csv`; check employee IDs
  before reusing seed data.
- Leave cases use `test-data/leave_boundary_dates.csv` and role-linked
  synthetic users. Confirm leave type, balance, role, and date configuration
  before execution.
- A past-date input is an exploratory policy probe only. Without an
  authoritative product rule, neither acceptance nor rejection alone is a
  defect.
- Expected results are not rewritten after execution. Record actual behavior
  and evidence separately, then assess any mismatch against the stated
  requirement.
- Conditional cases are executed only after module presence is confirmed.
  Final allocation and RTM must be updated together if a module is absent.

See `docs/02-requirements/derived-requirements.md` for requirement intent and
`docs/05-traceability/rtm.xlsx` for the complete requirement-to-case matrix.
