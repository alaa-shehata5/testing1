# Test Users (synthetic — no real persons)

> Passwords are never committed. Set via environment / installer at deploy time.
> Default demo hint observed in recon: `Admin` / `admin123` (public demo only —
> change immediately on any self-hosted install).

| Username | Role | Purpose | Password ref |
|---|---|---|---|
| `qa_admin` | Admin | Full-access flows: PIM create/edit, leave entitlements, approve/reject, reports | `SET_VIA_ENV_QA_ADMIN` |
| `qa_ess` | ESS | Self-service flows: apply/cancel leave, view personal info, timesheets | `SET_VIA_ENV_QA_ESS` |
| `qa_supervisor` | Supervisor (if present in build) | Approve/reject subordinate leave | `SET_VIA_ENV_QA_SUP` |

## Provisioning notes

- Create after completing the web installer (Phase 2 follow-up): Admin → Admin → User Management → Users → Add.
- ESS user must be linked to an employee record from `valid_employee.csv`.
- Record creation date + creator in execution log; never reuse personal data.
