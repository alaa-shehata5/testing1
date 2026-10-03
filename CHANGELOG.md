# Changelog

## [Unreleased]
### Added
- Phased agent plan + repo skeleton + DRS/test-plan/design/RTM/execution/bug/final-report docs
- Phase 0: project charter frozen on OrangeHRM Starter 5.8.1 self-hosted (+disclaimers, 12 objectives)
- Phase 1: application inventory with demo-drift note (5.8 vs 5.9) and TBD module checklist
- Phase 2: pinned Docker env (5.8.1 digest), verified browsers at 1920x1080, 8-file synthetic test-data set
- Phase 3: frozen scope A-H with conditional-module guards in test-plan.md
- Phase 4: DRS rewritten (16 REQs, Observed/Derived split, planned-TC trace, ASM separated)
- Hardening pass: DRS expanded to 20 REQs (past-date probe-only, candidate workflow, REQ-COMP-001), estimate-free README/RTM/report language, corrected boundary data (50-char name, Sunday date, unique seed IDs), Firefox restored as primary browser
- Phase 5: test plan expanded (6.1-6.11, 11 types, risk table, REG-001..011, decision table, roles); scope honesty rules (no silent redistribution, installer-gated freeze)
- Phase 6: 54-case suite authored in test-cases.xlsx (module 8/4/10/6/12/5/4/3/2 + type 20/14/6/5/4/2/3, TC-COMP-001, all 20 DRS reqs covered, all Not Run)
- Entry gates cleared: installer completed (host networking after bridge TCP drop), qa_admin + qa_ess provisioned with verified logins, 12-module nav verified (Reports partial), RTM conditionals resolved
- Phase 7: RTM gate — REQ→TC aligned across DRS/test-cases/RTM (20×54, 100% planned, script-verified no orphans); TC-DASH-004 cross-module note; REQ-PIM-003 delete wording
- Phase 8/9: TEST-CYCLE-01 smoke + discovery — 21/54 executed with per-TC evidence (17 Pass, 2 Fail on test-design wording, 2 Blocked on leave entitlement); 0 verified SUT defects reported as zero; voided probe error documented (F-02)
- Planned-input dispute resolved by conforming E2001 rerun: TC-PIM-001/002/004/005/007 pass with specified data (Aarav/E2001/ZzzNoMatch); name free-text proven submittable as filter
- Phase 10: retest N/A (no fixes supplied); regression 9/11 Pass 2 Blocked on same build (REG-006 edit persistence, REG-010 full punch cycle); TC-PIM-007 + TC-TIME-001/002 pass folded in
- Phase 11: partial-cycle final QA report issued (38.9% execution, no release verdict, What-I-could-not-verify)
- Phase 12: README sales front door with real numbers and embedded evidence; bugs/ zero-defect statement + filing template guide; evidence PNGs and execution workbooks whitelisted in .gitignore
- Phase 13: case study, three-minute demo script, and eight portfolio slides; corrected requirement/test mappings and screenshot counts; annotated E2001 evidence slide
- Phase 14: QC verdict corrected for intentional evidence/workbook binaries; added rerunnable workbook/link/evidence validator; clarified partial-cycle portfolio approval and release-verdict boundary
