# Test-Case Design (54)

Schema: TC ID, Requirement ID, Module, Scenario, Title, Priority, Test Type, Preconditions, Test Data, Environment, Steps, Expected, Actual, Status, Defect ID, Notes.

Distribution: Auth 8, Dashboard 4, PIM 10, Profile 6, Leave 12, Time 5, Recruitment 4, Reports 3, UI/a11y/compat 2 = 54. Types: Positive 20, Negative 14, Boundary 6, State 5, UI 4, A11y 2, Compat 3.

Example good title: "Verify user can submit full-day leave with valid type/future date/sufficient balance". Steps (8): login ESS → Leave → Apply → type with balance → future working day → Full Day → comment → Apply. Expected: accepted + shown with initial status.

Full 54-row matrix lives in test-cases.xlsx (generated via test-data scripts). Redistribute if Recruitment/Time missing. No dups, no Expected rewrite.
