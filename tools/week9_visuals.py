"""
Week 9 visuals — THE UNIFIED SOFTWARE DEVELOPMENT PROCESS (USDP / UP).
Iterative & incremental · four phases · workflows · artefacts · reuse · risks.
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (FancyBboxPatch, FancyArrowPatch, Circle,
                                Polygon, Ellipse)

from common import (MAROON, MAROON_DARK, MAROON_DEEP, MAROON_SOFT, MAROON_TINT,
                    GOLD, GOLD_LIGHT, CREAM, CREAM_2, INK, GREY, GREY_LIGHT,
                    WHITE, CHART_COLORS)
from draw import (canvas, box, chev, t, arrow, title, save, H_XB, H_B, H_SB,
                  H_MD, BODY, B_SB, B_B, B_IT, MONO, SYM)


def gtri(ax, x, y, w, h, ec=MAROON, lw=2.0, z=8):
    ax.add_patch(Polygon([(x, y + h), (x - w / 2, y), (x + w / 2, y)],
                         closed=True, fill=False, edgecolor=ec, lw=lw, zorder=z))


def uc(ax, x, y, w, name, attrs=None, ops=None, name_color=WHITE, fill=WHITE,
       ec=MAROON, line_h=17, pad=8, name_size=11.5):
    attrs = attrs or []
    ops = ops or []
    h_name = 27
    h_attrs = pad + line_h * len(attrs) + (pad if attrs else 0)
    h_ops = pad + line_h * len(ops) + (pad if ops else 0)
    h = h_name + h_attrs + h_ops
    box(ax, x, y, w, h, fill, ec=ec, lw=1.8, r=0, z=6)
    box(ax, x, y + h - h_name, w, h_name, ec, r=0, z=6)
    t(ax, x + w / 2, y + h - h_name / 2, name, size=name_size, color=name_color, fam=H_SB, z=7)
    ax.plot([x, x + w], [y + h_attrs + h_ops, y + h_attrs + h_ops], color=ec, lw=1.0, zorder=7)
    ax.plot([x, x + w], [y + h_ops, y + h_ops], color=ec, lw=1.0, zorder=7)
    yy = y + h_attrs + h_ops - pad
    for a in attrs:
        t(ax, x + 9, yy, a, size=10, color=INK, fam=MONO, ha="left", z=7)
        yy -= line_h
    yy = y + h_ops - pad
    for o in ops:
        t(ax, x + 9, yy, o, size=10, color=MAROON_SOFT, fam=MONO, ha="left", z=7)
        yy -= line_h
    return (x, y, w, h)


# --------------------------------------------------------------------------
# 1. Where Week 9 fits
# --------------------------------------------------------------------------
def progression():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Where Week 9 Fits", sub="UML tells us how to model · UP tells us how to organise the work")

    box(ax, 22, 150, 380, 200, WHITE, ec=MAROON, lw=1.8, r=14, z=6)
    t(ax, 212, 326, "UML", size=16, color=MAROON, fam=H_B, z=7)
    t(ax, 212, 288, "how to MODEL a system", size=12, color=INK, fam=BODY, z=7)
    t(ax, 212, 258, "class, sequence, activity diagrams…", size=10.5, color=GREY, fam=B_IT, z=7)
    t(ax, 212, 200, "Weeks 3–8", size=11, color=MAROON_SOFT, fam=B_SB, z=7)

    box(ax, 438, 150, 380, 200, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=6)
    t(ax, 628, 326, "UNIFIED PROCESS", size=16, color=MAROON_DARK, fam=H_B, z=7)
    t(ax, 628, 288, "how to ORGANISE the work", size=12, color=INK, fam=BODY, z=7)
    t(ax, 628, 258, "phases, iterations, workflows…", size=10.5, color=GREY, fam=B_IT, z=7)
    t(ax, 628, 200, "Week 9", size=11, color=MAROON_SOFT, fam=B_SB, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "UP is an iterative and incremental process for object-oriented development using UML.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w9_progression.png")


# --------------------------------------------------------------------------
# 2. Why a process
# --------------------------------------------------------------------------
def why_process():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Why Software Needs a Process", sub="Without it, everyone builds something different")

    quotes = [
        ("Analyst", "\u201cI thought the system should do X.\u201d", MAROON),
        ("Programmer", "\u201cI thought it should do Y.\u201d", MAROON_DARK),
        ("Tester", "\u201cI don't know what requirements I'm testing.\u201d", MAROON_SOFT),
        ("Client", "\u201cThis isn't what we requested.\u201d", "#8C2B2D"),
        ("Manager", "\u201cWhy are we six months late?\u201d", MAROON),
    ]
    xx = 22
    for role, quote, col in quotes:
        box(ax, xx, 120, 150, 180, WHITE, ec=col, lw=1.4, r=10, z=6)
        box(ax, xx, 270, 150, 30, col, r=10, z=7)
        t(ax, xx + 75, 285, role, size=10.5, color=WHITE, fam=H_SB, z=8)
        t(ax, xx + 75, 210, quote, size=10, color=INK, fam=B_IT, z=7)
        xx += 162

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "A process tells the team WHAT work to do, WHEN, WHO does it, and WHAT to produce.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w9_why_process.png")


# --------------------------------------------------------------------------
# 3. UP vs RUP
# --------------------------------------------------------------------------
def up_vs_rup():
    W, H = 840, 400
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "UP vs RUP", sub="A general framework vs a specific implementation")

    box(ax, 22, 100, 380, 220, WHITE, ec=MAROON, lw=1.8, r=14, z=6)
    t(ax, 212, 296, "UNIFIED PROCESS (UP)", size=14, color=MAROON, fam=H_B, z=7)
    t(ax, 212, 258, "a general software-development", size=11.5, color=INK, fam=BODY, z=7)
    t(ax, 212, 236, "process framework", size=11.5, color=INK, fam=BODY, z=7)
    t(ax, 212, 180, "general process concept", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 438, 100, 380, 220, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=6)
    t(ax, 628, 296, "RATIONAL UNIFIED PROCESS", size=14, color=MAROON_DARK, fam=H_B, z=7)
    t(ax, 628, 258, "a specific commercial implementation", size=11.5, color=INK, fam=BODY, z=7)
    t(ax, 628, 236, "of UP (Rational, later IBM)", size=11.5, color=INK, fam=BODY, z=7)
    t(ax, 628, 180, "one of several implementations", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "UP = general framework · RUP = a specific commercial implementation of UP.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w9_up_vs_rup.png")


# --------------------------------------------------------------------------
# 4. Waterfall vs UP
# --------------------------------------------------------------------------
def waterfall_vs_up():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Waterfall vs UP", sub="Separate stages vs repeated cycles with feedback")

    box(ax, 22, 120, 380, 250, WHITE, ec=MAROON, lw=1.8, r=14, z=6)
    box(ax, 22, 340, 380, 30, MAROON, r=14, z=7)
    t(ax, 212, 355, "WATERFALL", size=12.5, color=WHITE, fam=H_B, z=8)
    wf = ["Requirements", "Analysis", "Design", "Coding", "Testing", "Deployment"]
    yy = 300
    for i, nm in enumerate(wf):
        box(ax, 110, yy, 200, 30, CREAM_2, ec=MAROON_SOFT, lw=1.0, r=7, z=6)
        t(ax, 210, yy + 15, nm, size=10, color=INK, fam=BODY, z=7)
        if i < len(wf) - 1:
            arrow(ax, 210, yy, 210, yy - 10, color=MAROON_SOFT, lw=1.4, z=7)
        yy -= 40

    box(ax, 438, 120, 380, 250, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=6)
    box(ax, 438, 340, 380, 30, MAROON_DARK, r=14, z=7)
    t(ax, 628, 355, "UNIFIED PROCESS", size=12.5, color=WHITE, fam=H_B, z=8)
    cyc = ["Requirements", "Analysis", "Design", "Implementation", "Testing", "Feedback", "Improve"]
    cx, cy, r = 628, 220, 66
    ax.add_patch(Circle((cx, cy), r, fill=False, edgecolor=MAROON, lw=2.0, zorder=7))
    for i, nm in enumerate(cyc):
        ang = np.deg2rad(90 - i * (360 / len(cyc)))
        px, py = cx + r * np.cos(ang), cy + r * np.sin(ang)
        t(ax, px, py, nm, size=8.5, color=MAROON_DARK, fam=B_SB, z=8)
    t(ax, 628, 176, "repeatedly", size=10, color=GREY, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "UP repeats the cycle — each iteration improves the system.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w9_waterfall_vs_up.png")


# --------------------------------------------------------------------------
# 5. Iterative vs incremental
# --------------------------------------------------------------------------
def iterative_incremental():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Iterative vs Incremental", sub="Refine and improve vs add new functionality")

    box(ax, 22, 120, 380, 250, WHITE, ec=MAROON, lw=1.8, r=14, z=6)
    box(ax, 22, 340, 380, 30, MAROON, r=14, z=7)
    t(ax, 212, 355, "ITERATIVE", size=12.5, color=WHITE, fam=H_B, z=8)
    t(ax, 212, 308, "repeat cycles, improve each time", size=11.5, color=INK, fam=BODY, z=7)
    t(ax, 212, 260, "Draft -> Review -> Improve", size=12, color=MAROON_SOFT, fam=MONO, z=7)
    t(ax, 212, 232, "-> Review -> Improve -> Final", size=12, color=MAROON_SOFT, fam=MONO, z=7)
    t(ax, 212, 180, "like redrafting an essay", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 438, 120, 380, 250, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=6)
    box(ax, 438, 340, 380, 30, MAROON_DARK, r=14, z=7)
    t(ax, 628, 355, "INCREMENTAL", size=12.5, color=WHITE, fam=H_B, z=8)
    t(ax, 628, 308, "grow usable functionality", size=11.5, color=INK, fam=BODY, z=7)
    for i, nm in enumerate(["Login", "+ registration", "+ assignment", "+ results"]):
        t(ax, 476, 262 - i * 26, nm, size=11, color=MAROON_DARK, fam=MONO, ha="left", z=7)
    t(ax, 628, 130, "each increment adds value", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "UP is BOTH iterative AND incremental.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w9_iterative_incremental.png")


# --------------------------------------------------------------------------
# 6. Increments
# --------------------------------------------------------------------------
def increments():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Incremental Growth of an E-Learning System", sub="Each increment adds usable capability")

    data = [("Inc 1", "Login", 1), ("Inc 2", "Login\n+ registration", 2),
            ("Inc 3", "Login\n+ registration\n+ assignment", 3),
            ("Inc 4", "Login\n+ registration\n+ assignment\n+ results", 4)]
    xx = 30
    for name, cap, n in data:
        h = 40 + n * 46
        y = 40
        box(ax, xx, y, 180, h, MAROON if n < 4 else MAROON_DARK, r=10, z=6)
        t(ax, xx + 90, y + h + 18, name, size=11, color=MAROON, fam=H_B, z=7)
        t(ax, xx + 90, y + h - 22, cap, size=9.5, color=WHITE, fam=B_SB, z=8, ls=1.25)
        xx += 196

    box(ax, 22, 16, 796, 22, MAROON_DARK, r=10, z=5)
    t(ax, W / 2, 27, "We are not waiting until the end to discover whether the system works.",
      size=10.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w9_increments.png")


# --------------------------------------------------------------------------
# 7. Four characteristics
# --------------------------------------------------------------------------
def characteristics():
    W, H = 840, 460
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Four Characteristics of UP", sub="Use-case driven · architecture-centred · iterative & incremental · risk-driven")

    cards = [
        ("USE-CASE DRIVEN", "development organised around use cases", "UC-01 Register Course drives requirements -> analysis -> design -> code -> test", MAROON),
        ("ARCHITECTURE-CENTRED", "establish a sound architecture early", "UI -> Business Logic -> Data Access -> Database", MAROON_DARK),
        ("ITERATIVE & INCREMENTAL", "develop through repeated cycles", "Iteration 1 -> feedback -> Iteration 2 -> feedback…", MAROON_SOFT),
        ("RISK-DRIVEN", "address significant risks early", "test 5,000 transactions/sec before the end", "#8C2B2D"),
    ]
    pos = [(22, 250), (438, 250), (22, 40), (438, 40)]
    for (cname, sub, ex, col), (x, y) in zip(cards, pos):
        box(ax, x, y, 380, 180, WHITE, ec=col, lw=1.8, r=12, z=6)
        box(ax, x, y + 148, 380, 32, col, r=12, z=7)
        t(ax, x + 190, y + 164, cname, size=11.5, color=WHITE, fam=H_B, z=8)
        t(ax, x + 190, y + 120, sub, size=11, color=INK, fam=B_SB, z=7)
        t(ax, x + 190, y + 74, ex, size=9.5, color=GREY, fam=MONO, z=7, ls=1.2)

    box(ax, 22, 10, 796, 22, MAROON_DARK, r=10, z=5)
    t(ax, W / 2, 21, "Use-case driven + architecture-centred + iterative & incremental + risk-driven.",
      size=10.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w9_characteristics.png")


# --------------------------------------------------------------------------
# 8. Four phases
# --------------------------------------------------------------------------
def phases():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "The Four UP Phases", sub="Inception -> Elaboration -> Construction -> Transition")

    steps = [
        ("INCEPTION", "Should we build it?\nScope · business case"),
        ("ELABORATION", "Can we build it?\nArchitecture · risks"),
        ("CONSTRUCTION", "Build the complete system\nImplement · test"),
        ("TRANSITION", "Can users use it?\nDeploy · train"),
    ]
    cw, ch, gap = 176, 150, 24
    x = 28
    for i, (nm, desc) in enumerate(steps):
        col = [MAROON, MAROON_DARK, MAROON_SOFT, "#8C2B2D"][i]
        chev(ax, x, 160, cw, ch, col, z=6)
        t(ax, x + cw / 2 + 8, 260, nm, size=12, color=WHITE, fam=H_B, z=7)
        t(ax, x + cw / 2 + 8, 200, desc, size=9.5, color=WHITE, fam=B_SB, z=7, ls=1.3)
        x += cw + gap

    t(ax, W / 2, 90, "then a new development cycle begins for future releases", size=11, color=MAROON_SOFT, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "A phase is NOT a waterfall stage — each phase contains iterations.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w9_phases.png")


# --------------------------------------------------------------------------
# 9. Phases compared
# --------------------------------------------------------------------------
def phase_questions():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "The Four Phases Compared", sub="Each phase has its own question and focus")

    rows = [
        ("Inception", "Should we build it?", "Scope, business case, major requirements & risks"),
        ("Elaboration", "Can we build it?", "Architecture, detailed requirements, major risks"),
        ("Construction", "Can we build the complete product?", "Implementation, integration, testing"),
        ("Transition", "Can users successfully use it?", "Deployment, training, acceptance, fixes"),
    ]
    x0, y0, cw, ch = 60, 70, 200, 64
    for i, (ph, q, f) in enumerate(rows):
        y = y0 + (len(rows) - 1 - i) * (ch + 10)
        box(ax, x0, y, cw, ch, MAROON if i % 2 == 0 else MAROON_DARK, r=9, z=6)
        t(ax, x0 + 100, y + ch / 2, ph, size=11.5, color=WHITE, fam=H_B, z=7)
        box(ax, x0 + 210, y, 270, ch, WHITE, ec=MAROON_SOFT, lw=1.2, r=9, z=6)
        t(ax, x0 + 230, y + ch / 2, q, size=10.5, color=MAROON_DARK, fam=B_SB, ha="left", z=7)
        box(ax, x0 + 490, y, 300, ch, CREAM_2, ec=GREY, lw=1.2, r=9, z=6)
        t(ax, x0 + 510, y + ch / 2, f, size=9.5, color=INK, fam=BODY, ha="left", z=7)

    return save(fig, "w9_phase_questions.png")


# --------------------------------------------------------------------------
# 10. Architecture layers
# --------------------------------------------------------------------------
def architecture():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Software Architecture", sub="The high-level organisation of a system")

    layers = [("User Interface", MAROON), ("Business Logic", MAROON_DARK),
              ("Data Access", MAROON_SOFT), ("Database", "#8C2B2D")]
    y = 60
    for i, (nm, col) in enumerate(layers):
        box(ax, 180, y, 480, 60, col, r=10, z=6)
        t(ax, 420, y + 30, nm, size=13, color=WHITE, fam=H_B, z=7)
        if i < len(layers) - 1:
            arrow(ax, 420, y, 420, y - 14, color=MAROON, lw=2.0, z=7)
        y += 74

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "A system built for 100 students may collapse with 100,000 — architecture is validated early.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w9_architecture.png")


# --------------------------------------------------------------------------
# 11. Workflows
# --------------------------------------------------------------------------
def workflows():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Process Workflows / Disciplines", sub="Core technical disciplines + supporting disciplines")

    box(ax, 22, 250, 796, 130, WHITE, ec=MAROON, lw=1.6, r=12, z=6)
    t(ax, 60, 352, "CORE TECHNICAL DISCIPLINES", size=11.5, color=MAROON, fam=H_B, ha="left", z=7)
    core = ["Business Modeling", "Requirements", "Analysis & Design", "Implementation", "Test", "Deployment"]
    xx = 60
    for nm in core:
        box(ax, xx, 268, 118, 40, MAROON, r=8, z=7)
        t(ax, xx + 59, 288, nm, size=9.5, color=WHITE, fam=B_SB, z=8, ls=1.1)
        xx += 124

    box(ax, 22, 100, 796, 130, MAROON_TINT, ec=MAROON, lw=1.6, r=12, z=6)
    t(ax, 60, 202, "SUPPORTING DISCIPLINES", size=11.5, color=MAROON, fam=H_B, ha="left", z=7)
    sup = ["Configuration & Change Management", "Project Management", "Environment"]
    xx = 60
    for nm in sup:
        box(ax, xx, 118, 230, 40, MAROON_DARK, r=8, z=7)
        t(ax, xx + 115, 138, nm, size=9.5, color=WHITE, fam=B_SB, z=8, ls=1.1)
        xx += 240

    box(ax, 22, 16, 796, 22, MAROON_DARK, r=10, z=5)
    t(ax, W / 2, 27, "A workflow = related activities aimed at one development objective (e.g. Requirements).",
      size=10.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w9_workflows.png")


# --------------------------------------------------------------------------
# 12. Workflow intensity
# --------------------------------------------------------------------------
def workflow_intensity():
    W, H = 840, 440
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Workflow Intensity Across Phases", sub="Disciplines overlap — they do not happen only once")

    phases = ["Inception", "Elaboration", "Construction", "Transition"]
    dis = ["Requirements", "Analysis & Design", "Implementation", "Test"]
    intensity = {"Requirements": [10, 7, 3, 2], "Analysis & Design": [2, 10, 5, 2],
                 "Implementation": [1, 4, 10, 3], "Test": [1, 4, 9, 9]}
    colors = {"Requirements": MAROON, "Analysis & Design": MAROON_DARK,
              "Implementation": MAROON_SOFT, "Test": "#8C2B2D"}

    # simple grouped bars per discipline row
    x0, y0 = 180, 60
    bar_w, gap = 36, 16
    for di, dname in enumerate(dis):
        y = y0 + (len(dis) - 1 - di) * 78
        t(ax, 60, y + 30, dname, size=10.5, color=INK, fam=B_SB, ha="left", z=7)
        for pi, ph in enumerate(phases):
            v = intensity[dname][pi]
            bw = 40 + v * 22
            box(ax, x0 + pi * (bar_w + gap) - 40, y, bar_w, 60, colors[dname], r=6, z=6)
            box(ax, x0 + pi * (bar_w + gap) - 40, y, bar_w, v * 8, colors[dname], r=6, z=7)
        if di == len(dis) - 1:
            for pi, ph in enumerate(phases):
                t(ax, x0 + pi * (bar_w + gap) - 40 + bar_w / 2, y - 16, ph, size=9.5, color=GREY, fam=B_IT, z=7)

    box(ax, 22, 16, 796, 22, MAROON_DARK, r=10, z=5)
    t(ax, W / 2, 27, "Coding is heavy in Construction, but small amounts (prototypes) appear in Elaboration too.",
      size=10.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w9_workflow_intensity.png")


# --------------------------------------------------------------------------
# 13. Artefacts
# --------------------------------------------------------------------------
def artefacts():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Artefacts Across the Phases", sub="Work products the team produces or uses")

    data = [
        ("INCEPTION", ["Vision", "Business Case", "Initial Use-Case Model", "Risk Assessment", "Project Plan"], MAROON),
        ("ELABORATION", ["Detailed Requirements", "Architecture Document", "Domain Model", "Architectural Prototype"], MAROON_DARK),
        ("CONSTRUCTION", ["Source Code", "Components", "Test Cases", "Working Builds"], MAROON_SOFT),
        ("TRANSITION", ["Deployment Package", "User Documentation", "Training Materials", "Release Notes"], "#8C2B2D"),
    ]
    pos = [(22, 240), (438, 240), (22, 40), (438, 40)]
    for (ph, items, col), (x, y) in zip(data, pos):
        box(ax, x, y, 380, 180, WHITE, ec=col, lw=1.6, r=12, z=6)
        box(ax, x, y + 148, 380, 32, col, r=12, z=7)
        t(ax, x + 190, y + 164, ph, size=12, color=WHITE, fam=H_B, z=8)
        yy = y + 120
        for it in items:
            t(ax, x + 26, yy, "- " + it, size=10.5, color=INK, fam=BODY, ha="left", z=7)
            yy -= 24

    box(ax, 22, 10, 796, 22, MAROON_DARK, r=10, z=5)
    t(ax, W / 2, 21, "An artefact is evidence of the team's work — e.g. the use-case model or the source code.",
      size=10.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w9_artefacts.png")


# --------------------------------------------------------------------------
# 14. Reuse
# --------------------------------------------------------------------------
def reuse():
    W, H = 840, 440
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Software Reuse", sub="Use existing assets — but evaluate before adopting")

    box(ax, 22, 140, 380, 240, WHITE, ec=MAROON, lw=1.8, r=14, z=6)
    t(ax, 212, 356, "REUSABLE ASSETS", size=12.5, color=MAROON, fam=H_B, z=7)
    assets = ["classes", "components", "libraries", "frameworks", "services / APIs", "design patterns"]
    xx, yy = 46, 300
    for i, a in enumerate(assets):
        col = MAROON if i % 2 == 0 else MAROON_DARK
        box(ax, xx + (i % 2) * 182, yy - (i // 2) * 40, 172, 32, col, r=8, z=7)
        t(ax, xx + (i % 2) * 182 + 86, yy - (i // 2) * 40 + 16, a, size=10, color=WHITE, fam=B_SB, z=8)

    box(ax, 438, 140, 380, 240, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=6)
    t(ax, 628, 356, "EVALUATE BEFORE ADOPTING", size=12.5, color=MAROON, fam=H_B, z=7)
    qs = ["Is it secure?", "Is it maintained?", "Does it fit our requirements?", "Is it compatible?",
          "Is its licence acceptable?", "Is performance adequate?"]
    yy = 322
    for q in qs:
        t(ax, 464, yy, "-", size=11, color=MAROON, fam=B_B, ha="left", z=7)
        t(ax, 480, yy, q, size=10.5, color=INK, fam=BODY, ha="left", z=7)
        yy -= 24

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Reuse is not automatically good — evaluate quality, compatibility, security and licence.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w9_reuse.png")


# --------------------------------------------------------------------------
# 15. Generalisation vs inheritance
# --------------------------------------------------------------------------
def gen_vs_inheritance():
    W, H = 840, 420
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Generalisation vs Inheritance", sub="Closely related — but not identical")

    box(ax, 22, 110, 380, 250, WHITE, ec=MAROON, lw=1.8, r=14, z=6)
    box(ax, 22, 330, 380, 30, MAROON, r=14, z=7)
    t(ax, 212, 345, "GENERALISATION", size=13, color=WHITE, fam=H_B, z=8)
    t(ax, 212, 300, "a modelling / design relationship", size=11.5, color=INK, fam=BODY, z=7)
    uc(ax, 130, 210, 170, "Vehicle", line_h=13, pad=6, name_size=11)
    gtri(ax, 215, 184, 36, 22, ec=MAROON, lw=2.0, z=8)
    ax.plot([215, 215], [208, 160], color=MAROON, lw=2.0, zorder=7)
    uc(ax, 130, 120, 170, "Car", line_h=13, pad=6, name_size=11)
    t(ax, 212, 108, "Student IS-A User", size=10.5, color=MAROON_SOFT, fam=MONO, z=7)

    box(ax, 438, 110, 380, 250, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=6)
    box(ax, 438, 330, 380, 30, MAROON_DARK, r=14, z=7)
    t(ax, 628, 345, "INHERITANCE", size=13, color=WHITE, fam=H_B, z=8)
    t(ax, 628, 300, "a programming-language mechanism", size=11.5, color=INK, fam=BODY, z=7)
    t(ax, 628, 256, "class Student extends User", size=12, color=MAROON_SOFT, fam=MONO, z=7)
    t(ax, 628, 216, "acquires attributes and", size=11, color=INK, fam=BODY, z=7)
    t(ax, 628, 196, "operations from User", size=11, color=INK, fam=BODY, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Generalisation = conceptual relationship · Inheritance = the programming mechanism that implements it.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w9_gen_vs_inheritance.png")


# --------------------------------------------------------------------------
# 16. Concurrency problem
# --------------------------------------------------------------------------
def concurrency():
    W, H = 840, 460
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Concurrency — a Real Problem", sub="Two students, one remaining seat")

    box(ax, 22, 150, 796, 200, WHITE, ec=MAROON, lw=1.6, r=12, z=6)
    t(ax, W / 2, 326, "Course capacity = 1  (the last seat)", size=13, color=MAROON_DARK, fam=H_B, z=7)
    t(ax, 60, 288, "Student A -> Register", size=12, color=INK, fam=MONO, ha="left", z=7)
    t(ax, 60, 262, "Student B -> Register", size=12, color=INK, fam=MONO, ha="left", z=7)
    t(ax, 60, 232, "Both systems check: Available seats = 1", size=12, color=MAROON_SOFT, fam=MONO, ha="left", z=7)
    box(ax, 60, 180, 330, 40, MAROON, r=8, z=7)
    t(ax, 225, 200, "Student A -> SUCCESS", size=11.5, color=WHITE, fam=B_SB, z=8)
    box(ax, 460, 180, 330, 40, MAROON_DARK, r=8, z=7)
    t(ax, 625, 200, "Student B -> SUCCESS", size=11.5, color=WHITE, fam=B_SB, z=8)

    box(ax, 22, 70, 796, 60, MAROON_TINT, ec=MAROON, lw=1.4, r=10, z=6)
    t(ax, 60, 100, "Registered = 2 · Capacity = 1", size=12.5, color=MAROON_DARK, fam=B_B, ha="left", z=7)

    box(ax, 22, 16, 796, 22, MAROON_DARK, r=10, z=5)
    t(ax, W / 2, 27, "Without synchronisation this is a serious system error — concurrency matters at analysis/design level.",
      size=10.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w9_concurrency.png")


# --------------------------------------------------------------------------
# 17. Phases contain iterations
# --------------------------------------------------------------------------
def phases_iterations():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Phases Contain Iterations", sub="This is what makes UP different from waterfall")

    phases = [
        ("INCEPTION", ["Iteration 1", "Iteration 2"], MAROON),
        ("ELABORATION", ["Iteration 1", "Iteration 2", "Iteration 3"], MAROON_DARK),
        ("CONSTRUCTION", ["Iteration 1", "Iteration 2", "Iteration 3", "…"], MAROON_SOFT),
        ("TRANSITION", ["Iteration 1", "Iteration 2"], "#8C2B2D"),
    ]
    y = 340
    for i, (ph, its, col) in enumerate(phases):
        box(ax, 150, y, 540, 82, WHITE, ec=col, lw=1.8, r=10, z=6)
        box(ax, 150, y + 50, 190, 32, col, r=10, z=7)
        t(ax, 245, y + 66, ph, size=11, color=WHITE, fam=H_B, z=8)
        xx = 360
        for it in its:
            box(ax, xx, y + 14, 96, 34, MAROON_TINT, ec=col, lw=1.2, r=7, z=7)
            t(ax, xx + 48, y + 31, it, size=8.5, color=INK, fam=B_SB, z=8)
            xx += 104
        if i < len(phases) - 1:
            arrow(ax, 420, y, 420, y - 12, color=col, lw=1.8, z=7)
        y -= 94

    box(ax, 22, 12, 796, 22, MAROON_DARK, r=10, z=5)
    t(ax, W / 2, 23, "Iterations provide planned intervals that deliver incremental value within each phase.",
      size=10.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w9_phases_iterations.png")


ALL = [
    progression, why_process, up_vs_rup, waterfall_vs_up, iterative_incremental,
    increments, characteristics, phases, phase_questions, architecture,
    workflows, workflow_intensity, artefacts, reuse, gen_vs_inheritance,
    concurrency, phases_iterations,
]


if __name__ == "__main__":
    made = []
    for fn in ALL:
        try:
            p = fn()
            made.append(p.split(os.sep)[-1])
        except Exception as e:
            import traceback
            print(f"[FAIL] {fn.__name__}: {e}")
            traceback.print_exc()
    print("Generated", len(made), "week-9 visuals:")
    for m in made:
        print("  -", m)
