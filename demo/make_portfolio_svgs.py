#!/usr/bin/env python3
"""Generate the 8 Phase-13 portfolio images as self-contained SVGs (1200x675)."""
import base64
import os
from xml.sax.saxutils import escape

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "demo-assets")
os.makedirs(OUT, exist_ok=True)

BG, CARD, ACC, TXT, MUT, GRN, RED, YLW = (
    "#161616", "#232323", "#FF7B1D", "#F5F5F5", "#B0B0B0",
    "#76BC21", "#E5484D", "#F5A524")

def head(title, sub):
    return f"""<rect x="0" y="0" width="1200" height="675" rx="16" fill="{BG}"/>
<rect x="0" y="0" width="1200" height="130" rx="16" fill="#1E1E1E"/>
<rect x="48" y="34" width="64" height="64" rx="12" fill="{ACC}"/>
<text x="80" y="80" font-family="Arial,sans-serif" font-size="36" font-weight="bold" fill="#fff" text-anchor="middle">Q</text>
<text x="130" y="62" font-family="Arial,sans-serif" font-size="30" font-weight="bold" fill="{TXT}">{escape(title)}</text>
<text x="130" y="94" font-family="Arial,sans-serif" font-size="19" fill="{MUT}">{escape(sub)}</text>"""

def foot(n):
    return f"""<text x="1152" y="640" font-family="Arial,sans-serif" font-size="18" fill="{MUT}" text-anchor="end">{n} / 8 · orangehrm-manual-qa</text>"""

def svg(body, n):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="675" viewBox="0 0 1200 675">
{body}
</svg>"""

def stat(x, y, big, label, color=TXT):
    return (f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="52" '
            f'font-weight="bold" fill="{color}">{escape(big)}</text>'
            f'<text x="{x}" y="{y+30}" font-family="Arial,sans-serif" font-size="20" fill="{MUT}">{escape(label)}</text>')

def card(x, y, w, h, lines):
    t = "".join(
        f'<text x="{x+24}" y="{y+38+i*30}" font-family="Arial,sans-serif" font-size="21" fill="{TXT if i==0 else MUT}">{escape(l)}</text>'
        for i, l in enumerate(lines))
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{CARD}"/>{t}'

P = {}
P["01-overview"] = svg(head("Manual QA — OrangeHRM 5.8.1", "End-to-end portfolio engagement · pinned self-hosted build") + "\n" +
    stat(60, 240, "54", "planned cases") + stat(280, 240, "21", "executed (38.9%)", ACC) +
    stat(560, 240, "17", "passed", GRN) + stat(760, 240, "0", "SUT defects", GRN) + stat(980, 240, "100%", "REQ traceability") + "\n" +
    card(48, 300, 540, 200, ["Scope", "Auth · Dashboard · PIM / Employee", "Leave · Time · Recruitment · Reports", "Out: perf/load, pen-test, prod, mobile"]) +
    card(612, 300, 540, 200, ["Toolbox", "Firefox 155 + Chromium · 1920×1080", "Playwright evidence capture · Calc", "Synthetic data only · git/GitHub"]) + "\n" +
    card(48, 520, 1104, 80, ["Evidence chain:  requirement → test case → execution → screenshot → regression — every verdict traceable"]) + "\n" + foot(1), 1)

P["02-test-plan"] = svg(head("Test Plan", "Objective · scope · 11-technique strategy · env · entry/exit · risks") + "\n" +
    card(48, 160, 540, 160, ["Objective", "Validate employee + leave workflows", "Verify 20 derived requirements"]) +
    card(612, 160, 540, 160, ["Environment", "OrangeHRM 5.8.1 pinned (digest)", "Firefox 155 / Chromium · 1920×1080"]) + "\n" +
    card(48, 340, 540, 160, ["Strategy (excerpt)", "Smoke-first · REG-001–011 frozen", "EP · BVA 30/31 · state transitions"]) +
    card(612, 340, 540, 160, ["Risk → priority", "Auth / Employee / Leave: HIGH", "Dashboard: MEDIUM · UI: LOW"]) + "\n" +
    card(48, 520, 1104, 80, ["Entry gate: installer + logins + nav verified  ·  Exit: metrics reconcile, zero fabricated"]) + "\n" + foot(2), 2)

rows3 = [("TC-AUTH-003", "REQ-AUTH-003", "Invalid login", "High", "Negative", "Rejected + feedback", "Pass"),
         ("TC-PIM-001", "REQ-PIM-001", "Create E2001", "High", "Positive", "Saved + retrievable", "Pass"),
         ("TC-PIM-003", "REQ-PIM-001", "50-char name", "Med", "Boundary", "True limit is 30", "Fail*"),
         ("TC-PIM-004", "REQ-PIM-002", "Exact search", "High", "Positive", "Exactly 1 card", "Pass"),
         ("TC-PIM-005", "REQ-PIM-002", "No-match", "High", "Negative", "Empty state", "Pass"),
         ("TC-LEAVE-001", "REQ-LEAVE-001", "Apply leave", "High", "Positive", "Pending + history", "Blocked"),
         ("TC-TIME-001", "REQ-TIME-001", "Punch in", "Med", "Positive", "Timestamped record", "Pass"),
         ("TC-AUTH-008", "REQ-AUTH-004", "Back-button", "High", "Negative", "Login redirect", "Pass")]
y = 170
t3 = ""
for r in rows3:
    c = GRN if r[6] == "Pass" else (RED if r[6] == "Fail*" else YLW)
    t3 += (f'<text x="60" y="{y}" font-family="monospace" font-size="19" fill="{TXT}">{r[0]:<12} {r[1]:<13} {r[2]:<14} {r[3]:<5} {r[4]:<9}</text>'
           f'<text x="1010" y="{y}" font-family="Arial,sans-serif" font-size="19" font-weight="bold" fill="{c}">{r[6]}</text>')
    y += 46
P["03-suite"] = svg(head("Test Suite — 54 cases (excerpt)", "ID · REQ · scenario · priority · type · expected · status   (*Fail = test-design flag)") + "\n" + t3 + "\n" +
    f'<text x="60" y="600" font-family="Arial,sans-serif" font-size="19" fill="{MUT}">Full suite: docs/04-test-cases/test-cases.xlsx · Expected Results frozen after execution</text>' + "\n" + foot(3), 3)

rows4 = [("REQ-AUTH-003", "TC-AUTH-003–006", "4/4 Pass", "—"),
         ("REQ-PIM-001", "TC-PIM-001, 003", "1 Pass · 1 Fail*", "—"),
         ("REQ-PIM-002", "TC-PIM-004–006, 009–010", "2 Pass · 3 Not Run", "—"),
         ("REQ-LEAVE-002", "TC-LEAVE-002–004", "Blocked (entitlement)", "—"),
         ("REQ-TIME-001", "TC-TIME-001–005", "2 Pass · 3 Not Run", "—"),
         ("REQ-PROF-001", "TC-PROF-001–006", "Not Run", "—")]
y = 190
t4 = (f'<text x="60" y="{150}" font-family="Arial,sans-serif" font-size="20" font-weight="bold" fill="{MUT}">REQUIREMENT → TEST CASES → RESULT → DEFECT</text>')
for r in rows4:
    t4 += (f'<text x="60" y="{y}" font-family="monospace" font-size="21" fill="{TXT}">{r[0]:<14} → {r[1]:<24}</text>'
           f'<text x="640" y="{y}" font-family="Arial,sans-serif" font-size="21" fill="{TXT}">{escape(r[2])}</text>'
           f'<text x="1000" y="{y}" font-family="Arial,sans-serif" font-size="21" fill="{MUT}">{r[3]}</text>')
    y += 56
P["04-rtm"] = svg(head("Traceability — REQ → TC → Result → Defect", "20 requirements · 100% planned mapping · defect links blank (0 defects)") + "\n" + t4 + "\n" +
    f'<text x="60" y="600" font-family="Arial,sans-serif" font-size="19" fill="{MUT}">Matrix: docs/05-traceability/rtm.xlsx · every TC maps back to exactly one REQ</text>' + "\n" + foot(4), 4)

P["05-finding"] = svg(head("Top Finding — honest zero, strongest chain", "No bug invented: the exhibit is verification depth, not a defect") + "\n" +
    card(48, 160, 1104, 130, ["E2001 end-to-end chain (all green)",
         "REQ-PIM-001 → TC-PIM-001 (Pass); REQ-PIM-003 → TC-PIM-007 (Pass)",
         "REG-004/006 use E2091; REG-005 uses E2094 (separate regression evidence)"]) +
    card(48, 310, 540, 170, ["Test-design flags (no bugs filed)", "TC-AUTH-002: ESS wording vs correct RBAC", "TC-PIM-003: 50-char guess vs true limit 30"]) +
    card(612, 310, 540, 170, ["Process catch (documented, not filed)", "Voided probe: wrong Search box filled", "Caught by control mapping → F-02"]) + "\n" +
    card(48, 500, 1104, 80, ["Position:  0 verified SUT defects in 21 executed cases — reported as zero, never quota-filled"]) + "\n" + foot(5), 5)

evidence_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                             "evidence", "smoke", "TC-PIM-001-E2001-in-list.png")
with open(evidence_path, "rb") as image_file:
    evidence_data = base64.b64encode(image_file.read()).decode("ascii")
evidence_slide = (
    '<rect x="0" y="0" width="1200" height="675" fill="#161616"/>'
    + head("Evidence — E2001 retrieved by ID", "Actual execution screenshot · TC-PIM-001 · Pass")
    + f'<image x="48" y="155" width="800" height="450" href="data:image/png;base64,{evidence_data}" preserveAspectRatio="none"/>'
    + '<rect x="346" y="256" width="151" height="22" fill="none" stroke="#FF7B1D" stroke-width="4"/>'
    + '<rect x="192" y="442" width="642" height="23" fill="none" stroke="#76BC21" stroke-width="4"/>'
    + card(872, 175, 280, 180, ["Filter", "Employee ID: E2001", "Outcome", "(1) Record Found"])
    + card(872, 375, 280, 155, ["Matched record", "E2001 · Aarav Sharma", "Source screenshot", "TC-PIM-001-E2001-in-list.png"])
    + '<text x="48" y="632" font-family="Arial,sans-serif" font-size="17" fill="#B0B0B0">Orange: applied employee-ID filter · Green: single matching result</text>'
    + foot(6)
)
P["06-evidence"] = svg(evidence_slide, 6)

P["07-dashboard"] = svg(head("Dashboard — TEST-CYCLE-01 (partial, 2026-10-03)", "Measured counts only · Blocked ≠ Passed") + "\n" +
    stat(60, 240, "54", "total planned") + stat(300, 240, "21", "executed", ACC) + stat(520, 240, "38.9%", "execution") +
    stat(760, 240, "81.0%", "pass of executed", GRN) + stat(1010, 240, "0", "defects", GRN) + "\n" +
    card(48, 300, 340, 170, ["Passed: 17", "Auth 7 · Dash 3 · PIM 5", "Time 2"]) +
    card(420, 300, 340, 170, ["Failed: 2 · Blocked: 2", "Both test-design flags", "Leave entitlement ×2"]) +
    card(792, 300, 360, 170, ["Regression 9/11", "Retest N/A (no fixes)", "Not Run: 33"]) + "\n" +
    card(48, 490, 1104, 90, ["54-case check:  17 + 2 + 2 + 33 = 54  ·  defect total matches bugs/ (templates only)"]) + "\n" + foot(7), 7)

P["08-final"] = svg(head("Final report — verdict: none given", "Partial cycle · risks separated · next actions ordered") + "\n" +
    card(48, 160, 540, 150, ["Summary", "Auth/session + search + validation", "green with evidence; punch cycle green"]) +
    card(612, 160, 540, 150, ["Top risk (confirmed)", "Leave submit→approve chain: 0% verified", "Entitlement setup is the entry task"]) + "\n" +
    card(48, 330, 540, 150, ["Untested (explicit)", "Profile · Recruitment · Reports", "Keyboard path · Chrome parity"]) +
    card(612, 330, 540, 150, ["Recommendations", "1. Provision entitlements  2. Fix 2", "wordings  3. Run 33 remaining"]) + "\n" +
    card(48, 500, 1104, 80, ["A verdict on 38.9% execution with the core leave flow unverified would be fabrication — so none is given"]) + "\n" + foot(8), 8)

for name, content in P.items():
    with open(os.path.join(OUT, f"{name}.svg"), "w") as f:
        f.write(content)
print("wrote", len(P), "SVGs to", OUT)
