# Derived Requirements Specification (DRS)

> Not an official BRD. Every row below is either **Observed** (directly seen in
> demo/docs/installer on 2026-10-03) or **Derived** (inferred rule to be proven
> by testing — a derived rule that fails in the pinned build is a finding, not
> a rewrite). Assumptions live only in `assumptions.md` (ASM-xxx), never here.
> IDs are stable: `REQ-xxx-001`. Never renumber.

| Requirement ID | Type | Module | Requirement | Priority | Source | Acceptance Criteria | Planned TCs (Phase 6) | Notes |
|---|---|---|---|---|---|---|---|---|
| REQ-AUTH-001 | Observed | Auth | Login page provides username + password + Login action | High | Demo login hint (`Admin`/`admin123`), 2026-10-03 | Fields + action present and operable | TC-AUTH-001–002 | Fact, not a rule |
| REQ-AUTH-002 | Derived | Auth | Valid credentials authenticate and open role landing | High | Observable login behavior | Dashboard shown, session created | TC-AUTH-001–002 | — |
| REQ-AUTH-003 | Derived | Auth | Invalid/empty credentials are rejected with a message, no session | High | Observable validation | Stays on login + message, no session | TC-AUTH-003–006 | — |
| REQ-AUTH-004 | Derived | Auth | Logout terminates session; protected pages redirect to login | High | Session behavior | Back-button/direct URL after logout → login | TC-AUTH-007–008 | REG-001/002/011 |
| REQ-DASH-001 | Derived | Dashboard | Dashboard loads nav/widgets/links consistently | Medium | Observed dashboard (docs) | All widgets load, links navigate | TC-DASH-001–004 | REG-003 |
| REQ-PIM-001 | Derived | PIM | Create employee with valid required fields | High | Employee form (help: Add an Employee) | Record appears in list with ID | TC-PIM-001–003 | Synthetic data only; REG-005 |
| REQ-PIM-002 | Derived | PIM | Search/filter employees (exact/partial/case/empty) | High | Listing + Filter Employee List help | Correct subset; empty state if none | TC-PIM-004–006 | REG-004 |
| REQ-PIM-003 | Derived | PIM/Profile | Edit/view employee details; save/reset persist correctly | High | Profile form | Persisted after save + refresh | TC-PIM-007–010 | REG-006 |
| REQ-LEAVE-001 | Observed | Leave | Apply screen offers leave type + balance check + Full/Half/Specific-time duration + comment + Apply | High | Leave help article [5] | All controls present per type | TC-LEAVE-001 | Fact, not a rule |
| REQ-LEAVE-002 | Derived | Leave | Valid full/half-day request with balance is submitted as Pending | High | Leave Apply flow [5] | Appears in history with initial status | TC-LEAVE-001–004 | Subject to balance; REG-007/008 |
| REQ-LEAVE-003 | Derived | Leave | Invalid dates (past, End<Start) or insufficient balance are rejected with a message | High | Validation (to be proven) | Not submitted + message | TC-LEAVE-005–008 | Do not invent rules — verify by testing |
| REQ-LEAVE-004 | Derived | Leave | Cancel pending request; approve/reject transitions respected; invalid transitions blocked | High | Workflow (to be proven) | Status updates; rejected→cancel etc. blocked | TC-LEAVE-009–012 | Verify by testing; REG-009 |
| REQ-TIME-001 | Derived | Time | Clock in/out creates a persistent, filterable attendance record | Medium | Time docs, **only if present** | Record + filtering works | TC-TIME-001–005 | Drop + redistribute if absent; REG-010 |
| REQ-REC-001 | Derived | Recruitment | Create/search requisition with required fields + status flow | Medium | Recruitment docs, **only if present** | Appears in list; transitions tracked | TC-REC-001–004 | Drop + redistribute if absent |
| REQ-REPORT-001 | Derived | Reports | Generate/filter reports; empty behavior; export if present | Medium | Reports docs, **where available** | Correct data / empty state | TC-REP-001–003 | Drop + redistribute if absent |
| REQ-UI-001 | Derived | UI | Consistent labels, error placement, tables, pagination, dialogs | Low | UI observation | No blocking inconsistency | TC-UI-001–002 | Preference ≠ bug |

## Trace check (Phase 4 gate)

- Every REQ above maps to ≥1 planned TC range — no orphan requirements.
- No contradictions: REQ-LEAVE-001 states what the screen *offers*;
  REQ-LEAVE-002/003 state what submission *must do* — a REQ-LEAVE-003 failure
  is a defect candidate, never a reason to soften the requirement.
- ASM separated: `assumptions.md` holds ASM-AUTH-001, ASM-LEAVE-001,
  ASM-DATA-001, ASM-ENV-001 + the security-scope note. No ASM rows in this table.
- Conditional REQs (TIME/REC/REPORT) carry redistribute-not-fabricate guards
  per the frozen scope (`docs/03-test-plan/test-plan.md`).
