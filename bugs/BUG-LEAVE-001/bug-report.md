# BUG-LEAVE-001 — [Leave] [observable failure] [condition] (only if reproduced)

## Severity
High
## Priority
P1
## Environment
- OS: / Browser: / Version: / App: pinned / Viewport: 1920×1080
## Preconditions
ESS user with balance in type X.
## Test Data
type, dates, duration, comment (synthetic).
## Steps to Reproduce
1. Login ESS 2. Leave → Apply 3. Enter data 4. Apply
## Expected Result
Validation blocks invalid range with message.
## Actual Result
(observable only)
## Reproducibility
5/5
## Impact
HR cannot tell why request failed / record lost (justify, no fabrication).
## Evidence
See evidence/BUG-LEAVE-001/ (01-precondition.png, 02-input.png, 03-failure.png, evidence.md)
## Related Test Case
TC-LEAVE-008
## Related Requirement
REQ-LEAVE-003

Severity: Critical unusable/corruption/major unavailable; High major broken/no workaround; Medium workaround/partial; Low cosmetic. Priority P0 immediate P1 pre-release P2 planned P3 backlog.
