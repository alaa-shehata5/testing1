# RTM — Requirement → Test → Execution → Defect

`rtm.xlsx` is the current requirement-to-case-to-execution matrix. It contains
one row per DRS requirement, the exact case IDs from the test-case workbook,
reconciled status counts, any linked defect ID, and coverage progress.

## Phase 7 status

- 20 requirements map to the 54 stable case IDs; every case maps to one DRS
  requirement and every RTM reference resolves to an existing case.
- RTM execution counts are synchronized from `execution-results.xlsx`:
  17 Pass, 2 Fail, 2 Blocked, and 33 Not Run across the suite.
- No SUT defect is currently filed, so defect links remain blank.
- Conforming reruns used the planned E2001/Aarav/ZzzNoMatch data for the
  affected PIM cases; their final results and evidence are recorded in the
  execution workbook. Exploratory E2091/E2092/9999 observations remain
  supporting evidence, not substitutes for planned-case results.
- The two Fail results are invalid test expectations, not product failures.
- Conditional Time, Recruitment, and Reports coverage remains subject to the
  final scope decision; none is silently removed or marked passed.

Metrics (54 planned cases): planned requirement coverage = requirements with
≥1 planned TC / total requirements × 100; disposition rate = (Pass + Fail +
Blocked) / in-scope cases × 100; pass rate = Pass / dispositions; fail rate =
Fail / dispositions; blocked rate = Blocked / in-scope cases. Current values:
20/20 planned requirement mapping (100%); 12/20 requirements have at least
one recorded execution disposition (60%); 9/20 have at least one passing case
(45%); 21/54 case dispositions (38.9%); 17/21 Pass (81.0%); 2/21 Fail
(9.5%); 2/54 Blocked (3.7%). The Fail results are test-design failures, not
verified product defects. SUT defect count is zero.

Defect coverage (project metric) = failed SUT cases linked to defects / failed
SUT cases × 100. It is **N/A** while no SUT defect failures have been verified;
do not report it as 0% or infer a defect from a failed test design.
