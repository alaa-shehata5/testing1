# Derived Requirements Specification (DRS)

> Not an official BRD. **Observed** rows record behavior or controls documented
> in the cited recon source; this does not imply interactive verification in
> the pinned build. **Derived** rows are portfolio test expectations to prove
> against OrangeHRM 5.8.1; a failure is a finding candidate, not a reason to
> rewrite the expected result. Assumptions live only in `assumptions.md`
> (ASM-xxx), never here.
> IDs are stable: `REQ-xxx-001`. Never renumber.

| Requirement ID | Type | Module | Requirement | Priority | Source | Acceptance Criteria | Planned TCs (Phase 6) | Notes |
|---|---|---|---|---|---|---|---|---|
| REQ-AUTH-001 | Observed | Auth | Login page provides username, password, and Login action | High | Public demo login page hint/search excerpt, 2026-10-03; not pinned-build evidence | Controls are visible and operable in the pinned build | TC-AUTH-001 | Observation to confirm on SUT |
| REQ-AUTH-002 | Derived | Auth | Valid credentials authenticate and open the assigned landing page | High | Login behavior; test account setup in `test-data/users.md` | Dashboard/role landing appears and authenticated navigation is available | TC-AUTH-002 | REG-001 |
| REQ-AUTH-003 | Derived | Auth | Invalid or empty credentials do not authenticate and provide user feedback | High | Authentication validation expectation | Login remains unauthenticated; feedback is displayed | TC-AUTH-003–006 | Do not assert exact wording |
| REQ-AUTH-004 | Derived | Auth | Logout ends access to the authenticated session | High | Session behavior | Protected URL after logout requires authentication; back navigation does not restore usable access | TC-AUTH-007, TC-AUTH-008, TC-DASH-004 | REG-002/011; TC-DASH-004 retains DASH prefix for suite ordering but maps to this session requirement |
| REQ-DASH-001 | Derived | Dashboard | Dashboard and available navigation/widgets load and respond to interaction | Medium | Starter documentation; pinned build not yet observed | Dashboard renders; selected visible navigation/widget actions reach the corresponding page | TC-DASH-001–003 | REG-003 |
| REQ-PIM-001 | Derived | PIM | A valid employee can be created and found by its employee ID | High | OrangeHRM help: Add an Employee | Save confirmation or equivalent is shown; created employee is retrievable by ID | TC-PIM-001, TC-PIM-003 | Synthetic data only; REG-005; TC-PIM-003 is the max-boundary creation probe |
| REQ-PIM-002 | Derived | PIM | Employee search returns matching records and an understandable empty result for a no-match query | High | OrangeHRM help: Filter Employee List | Matching seeded employee appears; no-match query does not show unrelated rows | TC-PIM-004–006, TC-PIM-009–010 | REG-004 |
| REQ-PIM-003 | Derived | PIM | Employee details can be viewed and an allowed edit persists after refresh; where deletion is available, an allowed delete with confirmation removes the record | High | Employee/profile form behavior | Saved synthetic change remains after reopening the record; confirmed delete is absent from subsequent search | TC-PIM-007–008 | REG-006; TC-PIM-008 is conditional on delete being available |
| REQ-PIM-004 | Derived | PIM | Required employee data and duplicate employee IDs are handled without creating an invalid duplicate record | High | Add Employee form expectation; verify in pinned build | Missing required data or duplicate ID is not silently saved as a second employee; actionable validation is shown | TC-PIM-002 | Exact validation text is not prescribed; single case covers both empty-required and duplicate-ID attempts |
| REQ-PROF-001 | Derived | Profile | User profile fields can be viewed and supported edits persist; cancelling an edit does not save it | Medium | Employee profile form behavior | Saved change persists after refresh; cancelled unsaved change is absent | TC-PROF-001–006 | Use synthetic test account data |
| REQ-LEAVE-001 | Observed | Leave | Leave Apply documentation describes leave type, balance check, duration options, comment, and Apply action | High | OrangeHRM Leave help article [5]; documentation only | Corresponding available controls are present in pinned build | TC-LEAVE-001 | Full/Half/Specific-time availability may depend on configuration |
| REQ-LEAVE-002 | Derived | Leave | A valid request for an available leave type, date, and balance is submitted and appears in leave history | High | Leave Apply flow [5] | Request appears in history with its initial workflow status | TC-LEAVE-002–004 | Do not assume a particular balance/configuration; REG-007/008 |
| REQ-LEAVE-003 | Derived | Leave | A date range with end earlier than start is not submitted as a valid leave request | High | Basic date-range integrity expectation | Submission is blocked or remains absent from history, with feedback | TC-LEAVE-005–006 (006 = past-date policy probe) | Past-date policy is not specified here and is only probed, not asserted |
| REQ-LEAVE-004 | Derived | Leave | Pending requests can be cancelled by the requester; an authorized reviewer can approve or reject a pending request | High | Leave workflow documentation [5] | The selected action changes the displayed request status and is reflected in history | TC-LEAVE-009–012 | Preconditions: role-linked users and a pending request; REG-009; TC-LEAVE-012 is the invalid-transition probe |
| REQ-LEAVE-005 | Derived | Leave | A leave request that lacks required form data or sufficient configured balance is not silently accepted | High | Leave form and balance-check behavior [5] | Request is not added as accepted/pending without satisfying required data and configured balance; feedback is visible | TC-LEAVE-007–008 | Confirm leave balance/configuration before execution |
| REQ-TIME-001 | Derived | Time | If Time is present, supported attendance actions create a visible record that remains available in its history | Medium | Starter Time documentation; conditional on pinned build | Action outcome and associated record are visible; record remains after navigation/refresh | TC-TIME-001–005 | Conditional; do not execute if absent |
| REQ-REC-001 | Derived | Recruitment | If Recruitment is present, a candidate can be created, found, and opened using supported required fields | Medium | Starter Recruitment documentation; conditional on pinned build | Candidate appears in results and its details can be opened | TC-REC-001–004 | Candidate workflow, not requisition; conditional |
| REQ-REPORT-001 | Derived | Reports | If the report feature is present, selected filters are reflected in generated results | Medium | Starter reporting documentation; conditional on pinned build | Results match the chosen filter/data set, or a clear empty result is shown | TC-REP-001–003 | Export only if available; conditional |
| REQ-UI-001 | Derived | UI/A11y | Primary UI controls are keyboard reachable, have understandable labels/names, and show visible focus | Low | Basic manual accessibility expectation | Keyboard can reach primary login/navigation controls and focus is visible | TC-UI-001 | Basic check only; not an accessibility audit |
| REQ-COMP-001 | Derived | Compatibility | Core login and landing-page flows render and remain operable in the declared primary and secondary browsers at the target viewport | Medium | Project compatibility objective | Firefox and Chrome for Testing each load the same core flow without browser-specific blocking behavior | TC-COMP-001 | Record actual outcomes per browser |

## Trace check (Phase 4 gate)

- Every REQ above maps to ≥1 specific case in `docs/04-test-cases/test-cases.xlsx`
  and an RTM row in `docs/05-traceability/rtm.xlsx`.
- No contradictions: REQ-LEAVE-001 states what the screen *offers*;
  REQ-LEAVE-002–005 specify test expectations. Past-date acceptance is not
  asserted without an authoritative business rule.
- ASM separated: `assumptions.md` holds ASM-AUTH-001, ASM-LEAVE-001,
  ASM-DATA-001, ASM-ENV-001 + the security-scope note. No ASM rows in this table.
- Conditional REQs (TIME/REC/REPORT) remain planned only until presence is
  checked; if absent, record an explicit scope decision and update the cases
  and RTM together before execution.
