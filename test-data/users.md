# Test Users (synthetic — no real persons)

> Passwords are never committed. Set via environment / installer at deploy time.
> Default demo hint observed in recon: `Admin` / `admin123` (public demo only —
> change immediately on any self-hosted install).

| Username | Role | Purpose | Password ref |
|---|---|---|---|
| `qa_admin` | Admin | Full-access flows: PIM create/edit, leave entitlements, approve/reject, reports | Provisioned 2026-10-03 via installer (employee "QA Admin"); login verified, password local-only in `.env` |
| `qa_ess` | ESS | Self-service flows: apply/cancel leave, view personal info, timesheets | Provisioned 2026-10-03 via Admin → Users → Add, linked to employee "Ess Testuser"; login verified, password local-only in `.env` |
| `qa_supervisor` | Supervisor | Approve/reject subordinate leave | Not provisioned: Starter has no separate Supervisor login (supervision is an ESS assignment); approval flows use `qa_admin` unless configured during execution |

## Provisioning notes

- Created 2026-10-03 by installer (qa_admin) and Admin → User Management → Users → Add (qa_ess).
- ESS user is linked to an employee record ("Ess Testuser", empNumber 2).
- Never reuse personal data; all accounts synthetic.
