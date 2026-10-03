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
- A planned-input dispute (exploratory E2091/E2092/9999 probes vs specified
  E2001/Aarav/ZzzNoMatch data) was resolved by conforming reruns with the
  specified data on 2026-10-03 — all five cases pass; exploratory observations
  remain as supporting evidence. The two Fail results are test-design/input
  issues, not product failures.
- Conditional Time, Recruitment, and Reports coverage remains subject to the
  final scope decision; none is silently removed or marked passed.

Metrics (54 planned cases): REQ coverage = requirements with ≥1 planned TC /
total requirements × 100; execution/disposition rate = (Pass + Fail +
Blocked) / in-scope cases × 100; pass rate = Pass / dispositions; fail rate =
Fail / dispositions; blocked rate = Blocked / in-scope cases. Current values:
20/20 requirement mapping (100%); 21/54 dispositions (38.9%); 17/21 Pass
(81.0%); 2/21 Fail (9.5%); 2/54 Blocked (3.7%). The Fail results are
test-design/input-conformance failures, not verified product defects. SUT
defect count is zero.

Defect coverage (project metric) = failed SUT cases linked to defects / failed
SUT cases × 100. It is **N/A** while no SUT defect failures have been verified;
do not report it as 0% or infer a defect from a failed test design.
