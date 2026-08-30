"""
Week 1 visuals — diagrams, flow charts, comparison panels and charts.
All rendered in the Exploits University maroon / gold brand style.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Polygon, Rectangle
import numpy as np

from common import (BRAND, VISUALS, register_fonts, MAROON, MAROON_DARK,
                    MAROON_DEEP, MAROON_SOFT, MAROON_TINT, MAROON_TINT2, GOLD,
                    GOLD_LIGHT, CREAM, CREAM_2, INK, GREY, GREY_LIGHT, WHITE,
                    CHART_COLORS)

register_fonts()

# font-family shortcuts -> (family, weight, style) tuples
H_XB  = ("Poppins", 800)
H_B   = ("Poppins", 700)
H_SB  = ("Poppins", 600)
H_MD  = ("Poppins", 500)
BODY  = ("Open Sans", 400)
B_SB  = ("Open Sans", 600)
B_B   = ("Open Sans", 700)
B_IT  = ("Open Sans", 400, "italic")
MONO  = ("DejaVu Sans Mono", 400)
SYM   = "DejaVu Sans"

DPI = 150

# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------
def _canvas(w, h, bg=CREAM):
    fig = plt.figure(figsize=(w, h), dpi=DPI)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, w * 100)
    ax.set_ylim(0, h * 100)
    ax.axis("off")
    fig.patch.set_facecolor(bg)
    return fig, ax


def _box(ax, x, y, w, h, fc, ec="none", lw=0, r=10, alpha=1.0, z=5):
    p = FancyBboxPatch((x, y), w, h,
                       boxstyle=f"round,pad=0,rounding_size={r}",
                       mutation_aspect=1, facecolor=fc, edgecolor=ec,
                       linewidth=lw, alpha=alpha, zorder=z)
    ax.add_patch(p)
    return p


def _chev(ax, x, y, w, h, fc, z=5, r=4):
    p = Polygon([(x + r, y), (x + w - r, y), (x + w, y + h / 2),
                 (x + w - r, y + h), (x + r, y + h), (x, y + h / 2)],
                closed=True, facecolor=fc, edgecolor="none", zorder=z)
    ax.add_patch(p)
    return p


def _t(ax, x, y, s, size=13, color=INK, fam=BODY, ha="center", va="center",
       ls=1.3, z=10, style="normal", weight="normal"):
    family, w, st = None, weight, style
    if isinstance(fam, (tuple, list)):
        family = fam[0]
        if len(fam) > 1:
            w = fam[1]
        if len(fam) > 2:
            st = fam[2]
    else:
        family = fam
    ax.text(x, y, s, fontsize=size, color=color, family=family, fontweight=w,
            fontstyle=st, ha=ha, va=va, linespacing=ls, zorder=z)


def _arrow(ax, x1, y1, x2, y2, color=MAROON, lw=2.2, ms=18, style="-|>",
           z=8):
    a = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style,
                        mutation_scale=ms, color=color, lw=lw, zorder=z,
                        shrinkA=0, shrinkB=0)
    ax.add_patch(a)


def _title(ax, W, s, size=21, color=MAROON, y=None, sub=None):
    if y is None:
        y = ax.get_ylim()[1] - 42
    _t(ax, W / 2, y, s, size=size, color=color, fam=H_B)
    ax.plot([W / 2 - 26, W / 2 + 26], [y - 18, y - 18], color=GOLD, lw=2.4,
            zorder=8)
    if sub:
        _t(ax, W / 2, y - 40, sub, size=12.5, color=GREY, fam=B_IT)


def _save(fig, name):
    path = os.path.join(VISUALS, name)
    fig.savefig(path, facecolor=fig.get_facecolor())
    plt.close(fig)
    return path


# --------------------------------------------------------------------------
# 1. The business-to-software journey (8-step snake flow)
# --------------------------------------------------------------------------
def journey():
    W, H = 840, 400
    fig, ax = _canvas(W / 100, H / 100)
    _title(ax, W, "The Business-to-Software Journey", sub="From an organisational goal to working software — the road the whole module follows")

    steps = [
        ("1", "Business Objective", "the result the organisation wants"),
        ("2", "Business Problem / Opportunity", "what is wrong · what could improve"),
        ("3", "Business Need", "what must improve to reach the goal"),
        ("4", "Stakeholder Needs", "who is affected & what they need"),
        ("5", "Software Requirements", "functional & non-functional needs"),
        ("6", "Analysis Models", "domain concepts & UML models"),
        ("7", "Design", "object-oriented design decisions"),
        ("8", "Implementation", "working software (OOP)"),
    ]
    cols = [15, 225, 435, 645]
    bw, bh = 180, 86
    y1, y2 = 230, 30

    shade = [MAROON, MAROON_DARK, MAROON, MAROON_DARK,
             "#8C2B2D", "#8C2B2D", GOLD, GOLD]
    tcol = [WHITE, WHITE, WHITE, WHITE, WHITE, WHITE, MAROON_DARK, MAROON_DARK]

    for i, (num, title, sub) in enumerate(steps):
        row = 0 if i < 4 else 1
        col = i if i < 4 else (7 - i)
        x, y = cols[col], (y1 if row == 0 else y2)
        _box(ax, x, y, bw, bh, shade[i], r=12, z=5)
        # number badge
        _box(ax, x + bw / 2 - 16, y + bh - 12, 32, 24, GOLD, r=12, z=7)
        _t(ax, x + bw / 2, y + bh, num, size=12.5, color=MAROON_DARK, fam=H_B, z=8)
        _t(ax, x + bw / 2, y + bh / 2 + 6, title, size=14.5, color=tcol[i], fam=H_SB, z=8)
        _t(ax, x + bw / 2, y + bh / 2 - 22, sub, size=10.5, color=tcol[i], fam=BODY, z=8, ls=1.2)

    # horizontal arrows row1 (cols 0->3)
    for c in range(3):
        _arrow(ax, cols[c] + bw, y1 + bh / 2, cols[c + 1] - 4, y1 + bh / 2)
    # down arrow from step4 to step5
    _arrow(ax, cols[3] + bw / 2, y1, cols[3] + bw / 2, y2 + bh + 6, color=MAROON, lw=2.6)
    # horizontal arrows row2 (cols 3->0, i.e. step5->6->7->8)
    for c in range(3):
        _arrow(ax, cols[c + 1] - 4, y2 + bh / 2, cols[c] + bw, y2 + bh / 2, color="#8C2B2D")

    return _save(fig, "journey.png")


# --------------------------------------------------------------------------
# 2. Problem vs Need vs Solution
# --------------------------------------------------------------------------
def problem_need_solution():
    W, H = 840, 360
    fig, ax = _canvas(W / 100, H / 100)
    _title(ax, W, "From Problem to Need to Solution", sub="Three ideas that must never be confused")

    cards = [
        ("BUSINESS PROBLEM", "What is wrong today?",
         "“Students wait up to three hours to register for courses.”",
         MAROON_TINT, MAROON, MAROON),
        ("BUSINESS NEED", "What must improve?",
         "“The university needs a faster, more reliable registration process.”",
         MAROON, WHITE, WHITE),
        ("SOFTWARE SOLUTION", "How might we improve it?",
         "“An online student registration system.”",
         CREAM_2, GOLD, INK),
    ]
    cw, ch = 250, 190
    xs = [20, 295, 570]
    for i, (h, sub, body, fc, ec, tc) in enumerate(cards):
        x = xs[i]
        _box(ax, x, 40, cw, ch, fc, ec=ec, lw=2, r=14, z=5)
        _box(ax, x + cw / 2 - 26, 40 + ch - 26, 52, 22, ec, r=11, z=6)
        _t(ax, x + cw / 2, 40 + ch - 15, f"{i+1}", size=12, color=(MAROON if ec != MAROON else MAROON_DARK) if fc != MAROON else WHITE, fam=H_B, z=7)
        _t(ax, x + cw / 2, 40 + ch - 46, h, size=14.5, color=tc, fam=H_SB, z=7)
        _t(ax, x + cw / 2, 40 + ch - 70, sub, size=11, color=(GREY if fc != MAROON else GOLD_LIGHT), fam=B_IT, z=7)
        _t(ax, x + cw / 2, 40 + 52, body, size=12.5, color=tc, fam=BODY, z=7, ls=1.35)

    _arrow(ax, xs[0] + cw + 2, 40 + ch / 2, xs[1] - 2, 40 + ch / 2, color=MAROON, lw=3)
    _arrow(ax, xs[1] + cw + 2, 40 + ch / 2, xs[2] - 2, 40 + ch / 2, color=GOLD, lw=3)

    _box(ax, 20, 8, 800, 26, MAROON_DARK, r=13, z=5)
    _t(ax, W / 2, 21, "Problem = what is wrong?      Need = what must improve?      Solution = how might we improve it?",
       size=12, color=GOLD_LIGHT, fam=B_SB)

    return _save(fig, "problem_need_solution.png")


# --------------------------------------------------------------------------
# 3. Functional vs Non-functional
# --------------------------------------------------------------------------
def functional_nonfunctional():
    W, H = 840, 460
    fig, ax = _canvas(W / 100, H / 100)
    _title(ax, W, "Functional vs Non-Functional Needs", sub="What the system must DO  ·  how WELL it must do it")

    pw, ph = 380, 290
    y = 60
    # left
    _box(ax, 20, y, pw, ph, WHITE, ec=MAROON, lw=2, r=16, z=5)
    _box(ax, 20, y + ph - 56, pw, 56, MAROON, r=14, z=6)
    _t(ax, 20 + pw / 2, y + ph - 28, "FUNCTIONAL", size=17, color=WHITE, fam=H_B, z=7)
    _t(ax, 20 + pw / 2, y + ph - 84, "What must the system DO?", size=12.5, color=MAROON, fam=B_SB, z=7)
    items_l = ["Register students", "Calculate fees", "Generate invoices", "Send notifications", "Transfer money between accounts"]
    for i, it in enumerate(items_l):
        yy = y + ph - 118 - i * 40
        _box(ax, 48, yy, 26, 26, MAROON_TINT, r=8, z=6)
        _t(ax, 61, yy + 13, "✓", size=12, color=MAROON, fam=SYM, z=7)
        _t(ax, 92, yy + 13, it, size=13, color=INK, fam=BODY, ha="left", z=7)

    # right
    _box(ax, 440, y, pw, ph, WHITE, ec=MAROON_DARK, lw=2, r=16, z=5)
    _box(ax, 440, y + ph - 56, pw, 56, MAROON_DARK, r=14, z=6)
    _t(ax, 440 + pw / 2, y + ph - 28, "NON-FUNCTIONAL", size=15.5, color=WHITE, fam=H_B, z=7)
    _t(ax, 440 + pw / 2, y + ph - 84, "How WELL / under what conditions?", size=12.5, color=MAROON_DARK, fam=B_SB, z=7)
    items_r = ["Performance — respond within 2 seconds", "Security — encrypt sensitive data", "Availability — 99.9% uptime", "Usability — easy to learn", "Reliability — no data loss"]
    for i, it in enumerate(items_r):
        yy = y + ph - 118 - i * 40
        _box(ax, 468, yy, 26, 26, MAROON_TINT, r=8, z=6)
        _t(ax, 481, yy + 13, "◆", size=10, color=MAROON, fam=SYM, z=7)
        _t(ax, 512, yy + 13, it, size=13, color=INK, fam=BODY, ha="left", z=7)

    # center VS badge
    _box(ax, 402, y + ph / 2 - 20, 36, 40, GOLD, r=10, z=9)
    _t(ax, 420, y + ph / 2, "VS", size=12, color=MAROON_DARK, fam=H_B, z=10)

    _box(ax, 20, 10, 800, 34, MAROON_DARK, r=14, z=5)
    _t(ax, W / 2, 27, "Easy memory trick:   Functional = behaviour     ·     Non-functional = quality & constraints",
       size=13, color=GOLD_LIGHT, fam=B_SB)

    return _save(fig, "functional_nonfunctional.png")


# --------------------------------------------------------------------------
# 4. Stakeholder map
# --------------------------------------------------------------------------
def stakeholders():
    W, H = 840, 470
    fig, ax = _canvas(W / 100, H / 100)
    _title(ax, W, "Who Has a Stake in the System?", sub="Primary stakeholders interact directly · secondary stakeholders care about the outcomes")

    # centre system box
    cx, cy, cw, ch = 330, 195, 180, 80
    _box(ax, cx, cy, cw, ch, MAROON, r=14, z=7)
    _t(ax, cx + cw / 2, cy + ch / 2 + 10, "Student", size=15, color=WHITE, fam=H_B, z=8)
    _t(ax, cx + cw / 2, cy + ch / 2 - 14, "Registration System", size=12.5, color=GOLD_LIGHT, fam=B_SB, z=8)

    primary = [("Student", 335, 315), ("Finance Officer", 335, 100),
               ("Lecturer", 120, 213), ("Registrar", 555, 213)]
    for label, x, y in primary:
        _box(ax, x, y, 170, 46, MAROON_TINT, ec=MAROON, lw=1.6, r=12, z=6)
        _t(ax, x + 85, y + 23, label, size=12.5, color=MAROON, fam=B_SB, z=7)

    secondary = [("University Management", 60, 360), ("Regulators", 590, 360),
                 ("Auditors", 60, 50), ("ICT Administrators", 590, 50)]
    for label, x, y in secondary:
        _box(ax, x, y, 190, 46, CREAM_2, ec=GOLD, lw=1.8, r=12, z=6)
        _t(ax, x + 95, y + 23, label, size=12.5, color=INK, fam=B_SB, z=7)

    # legend
    _box(ax, 235, 430, 20, 20, MAROON_TINT, ec=MAROON, lw=1.4, r=6, z=7)
    _t(ax, 265, 440, "Primary (direct users)", size=12, color=INK, fam=BODY, ha="left", z=7)
    _box(ax, 430, 430, 20, 20, CREAM_2, ec=GOLD, lw=1.6, r=6, z=7)
    _t(ax, 460, 440, "Secondary (affected by outcomes)", size=12, color=INK, fam=BODY, ha="left", z=7)

    return _save(fig, "stakeholders.png")


# --------------------------------------------------------------------------
# 5. Object anatomy
# --------------------------------------------------------------------------
def object_anatomy():
    W, H = 840, 470
    fig, ax = _canvas(W / 100, H / 100)
    _title(ax, W, "Anatomy of an Object", sub="Every object has identity, state and behaviour")

    # left: concept tree
    ox, oy, ow, oh = 120, 330, 160, 70
    _box(ax, ox, oy, ow, oh, MAROON, r=14, z=6)
    _t(ax, ox + ow / 2, oy + oh / 2, "OBJECT", size=19, color=WHITE, fam=H_B, z=7)

    kids = [("IDENTITY", "what makes it distinct", 30), ("STATE", "its current data", 185), ("BEHAVIOUR", "what it can do", 340)]
    for label, sub, x in kids:
        _box(ax, x, 140, 130, 92, WHITE, ec=MAROON, lw=1.8, r=12, z=6)
        _t(ax, x + 65, 210, label, size=13, color=MAROON, fam=H_SB, z=7)
        _t(ax, x + 65, 182, sub, size=10.5, color=GREY, fam=BODY, z=7, ls=1.2)
        _arrow(ax, ox + ow / 2, oy, x + 65, 240, color=MAROON, lw=2.2)

    # right: student example
    _t(ax, 640, 330, "Example — a Student object", size=14, color=MAROON, fam=B_SB, z=7)
    cards = [
        ("IDENTITY", "ST001", 92),
        ("STATE", "Name = Francis Fweta\nProgramme = BSc ICT\nYear = 3    ·    Status = Active", 150),
        ("BEHAVIOUR", "registerCourse()   dropCourse()\nviewResults()   payFees()", 120),
    ]
    yy = 240
    for title, body, hh in cards:
        _box(ax, 470, yy, 330, hh, WHITE, ec=MAROON, lw=1.6, r=12, z=6)
        _box(ax, 470, yy + hh - 26, 330, 26, MAROON_TINT, r=12, z=6)
        _t(ax, 635, yy + hh - 13, title, size=11, color=MAROON, fam=B_SB, z=7)
        _t(ax, 635, yy + (hh - 26) / 2, body, size=12, color=INK, fam=MONO if "()" in body else BODY, z=7, ls=1.5)
        yy -= hh + 10

    return _save(fig, "object_anatomy.png")


# --------------------------------------------------------------------------
# 6. Class vs Object (blueprint analogy)
# --------------------------------------------------------------------------
def class_vs_object():
    W, H = 840, 470
    fig, ax = _canvas(W / 100, H / 100)
    _title(ax, W, "Class vs Object", sub="A class is the blueprint — an object is one thing built from it")

    # row 1: house blueprint
    _t(ax, 200, 385, "Analogy 1 — houses", size=13, color=MAROON, fam=B_SB, z=7, ha="left")
    _box(ax, 40, 260, 220, 110, WHITE, ec=MAROON, lw=1.8, r=12, z=6)
    _box(ax, 40, 336, 220, 34, MAROON, r=12, z=6)
    _t(ax, 150, 353, "HOUSE BLUEPRINT", size=13, color=WHITE, fam=H_SB, z=7)
    _t(ax, 150, 300, "Bedrooms: 3\nKitchen: 1\nBathroom: 2", size=12.5, color=INK, fam=BODY, z=7, ls=1.45)
    _arrow(ax, 268, 315, 340, 315, color=MAROON, lw=3)
    _t(ax, 300, 340, "builds", size=11, color=GREY, fam=B_IT, z=7)
    for i, label in enumerate(["House 1", "House 2", "House 3"]):
        x = 350 + i * 150
        _box(ax, x, 272, 130, 86, MAROON_TINT, ec=MAROON, lw=1.4, r=10, z=6)
        # tiny house glyph
        hx = x + 65
        ax.plot([hx - 22, hx, hx + 22, hx - 22], [324, 346, 324, 324],
                color=MAROON, lw=2.4, zorder=8)
        ax.plot([hx - 14, hx - 14, hx + 14, hx + 14], [310, 324, 324, 310],
                color=MAROON, lw=2.0, zorder=8)
        _t(ax, x + 65, 292, label, size=12, color=MAROON, fam=B_SB, z=7)

    # row 2: student class
    _t(ax, 200, 205, "Analogy 2 — the module", size=13, color=MAROON, fam=B_SB, z=7, ha="left")
    _box(ax, 40, 60, 220, 130, WHITE, ec=MAROON, lw=1.8, r=12, z=6)
    _box(ax, 40, 156, 220, 34, MAROON, r=12, z=6)
    _t(ax, 150, 173, "STUDENT  (class)", size=13, color=WHITE, fam=H_SB, z=7)
    _t(ax, 150, 120, "studentID, name, programme\nregisterCourse()\nviewResults()", size=11, color=INK, fam=MONO, z=7, ls=1.4)
    _arrow(ax, 268, 125, 340, 125, color=MAROON, lw=3)
    _t(ax, 300, 150, "instantiates", size=11, color=GREY, fam=B_IT, z=7)
    objs = [("student1", "Francis"), ("student2", "Grace"), ("student3", "John")]
    for i, (v, name) in enumerate(objs):
        x = 350 + i * 150
        _box(ax, x, 72, 130, 92, MAROON_TINT, ec=MAROON, lw=1.4, r=10, z=6)
        _t(ax, x + 65, 140, v, size=12.5, color=MAROON, fam=H_SB, z=7)
        _t(ax, x + 65, 108, "= " + name, size=12, color=INK, fam=BODY, z=7)
        _t(ax, x + 65, 84, "an object", size=10.5, color=GREY, fam=B_IT, z=7)

    _box(ax, 20, 12, 800, 32, MAROON_DARK, r=13, z=5)
    _t(ax, W / 2, 28, "Student is a class  ·  Francis is an object of the Student class",
       size=13, color=GOLD_LIGHT, fam=B_SB)

    return _save(fig, "class_vs_object.png")


# --------------------------------------------------------------------------
# 7. Real-world to software (bank objects)
# --------------------------------------------------------------------------
def bank_objects():
    W, H = 840, 440
    fig, ax = _canvas(W / 100, H / 100)
    _title(ax, W, "Business Concepts Become Software Objects", sub="The bank's real-world entities modelled as classes")

    _box(ax, 20, 320, 800, 60, MAROON_TINT, r=14, z=5)
    _t(ax, W / 2, 365, "REAL WORLD", size=13, color=MAROON, fam=B_B, z=6)
    _t(ax, W / 2, 338, "Customer   ───────▶   Bank Account   ───────▶   Transaction",
       size=15, color=MAROON_DARK, fam=MONO, z=6)

    specs = [
        ("Customer", ["customerID", "name", "phone"], ["openAccount()", "updateDetails()"]),
        ("Account", ["accountNumber", "balance", "accountType"], ["deposit()", "withdraw()", "transfer()"]),
        ("Transaction", ["transactionID", "amount", "date", "type"], ["process()", "reverse()"]),
    ]
    xs = [30, 315, 600]
    for (name, attrs, meths), x in zip(specs, xs):
        _box(ax, x, 40, 210, 250, WHITE, ec=MAROON, lw=1.6, r=12, z=6)
        _box(ax, x, 256, 210, 34, MAROON, r=12, z=6)
        _t(ax, x + 105, 273, name, size=14.5, color=WHITE, fam=H_SB, z=7)
        yy = 236
        for a in attrs:
            _t(ax, x + 16, yy, a, size=11.5, color=INK, fam=MONO, ha="left", z=7)
            yy -= 22
        ax.plot([x + 8, x + 202], [yy + 12, yy + 12], color=GOLD, lw=1.2, zorder=7)
        yy -= 18
        for m in meths:
            _t(ax, x + 16, yy, m, size=11.5, color=MAROON, fam=MONO, ha="left", z=7)
            yy -= 22

    _arrow(ax, 245, 165, 306, 165, color=GOLD, lw=2.4)
    _arrow(ax, 530, 165, 591, 165, color=GOLD, lw=2.4)
    _t(ax, 276, 186, "interacts", size=10.5, color=GREY, fam=B_IT, z=7)
    _t(ax, 561, 186, "interacts", size=10.5, color=GREY, fam=B_IT, z=7)

    return _save(fig, "bank_objects.png")


# --------------------------------------------------------------------------
# 8. Inheritance
# --------------------------------------------------------------------------
def inheritance():
    W, H = 840, 330
    fig, ax = _canvas(W / 100, H / 100)
    _title(ax, W, "Inheritance — a First Look", sub="Specialised classes reuse the common state & behaviour of a general class")

    ux, uy, uw, uh = 300, 150, 240, 90
    _box(ax, ux, uy, uw, uh, MAROON, r=14, z=6)
    _t(ax, ux + uw / 2, uy + uh - 24, "User", size=15, color=WHITE, fam=H_B, z=7)
    _t(ax, ux + uw / 2, uy + uh / 2 - 4, "userID · name · email", size=11, color=GOLD_LIGHT, fam=MONO, z=7)
    _t(ax, ux + uw / 2, uy + 22, "login() · logout()", size=11, color=CREAM, fam=MONO, z=7)

    kids = [("Student", 60), ("Lecturer", 340), ("Administrator", 620)]
    for label, x in kids:
        _box(ax, x, 30, 160, 60, WHITE, ec=MAROON, lw=1.8, r=12, z=6)
        _t(ax, x + 80, 60, label, size=13.5, color=MAROON, fam=H_SB, z=7)
        _arrow(ax, ux + uw / 2, uy, x + 80, 96, color=MAROON, lw=2.2)

    return _save(fig, "inheritance.png")


# --------------------------------------------------------------------------
# 9. Polymorphism
# --------------------------------------------------------------------------
def polymorphism():
    W, H = 840, 370
    fig, ax = _canvas(W / 100, H / 100)
    _title(ax, W, "Polymorphism — One Operation, Different Behaviour", sub="The same call means different things to different objects")

    _box(ax, 285, 250, 270, 56, MAROON, r=13, z=6)
    _t(ax, W / 2, 278, "displayDashboard()", size=15, color=WHITE, fam=MONO, z=7)

    panels = [
        ("Student", ["Courses", "Fees", "Results"]),
        ("Lecturer", ["Courses taught", "Students", "Marks", "Attendance"]),
        ("Administrator", ["User accounts", "Reports", "System settings"]),
    ]
    xs = [20, 300, 580]
    for (name, items), x in zip(panels, xs):
        _box(ax, x, 40, 240, 180, WHITE, ec=MAROON, lw=1.6, r=14, z=6)
        _box(ax, x, 186, 240, 34, MAROON, r=12, z=6)
        _t(ax, x + 120, 203, name, size=13.5, color=WHITE, fam=H_SB, z=7)
        for i, it in enumerate(items):
            yy = 168 - i * 32
            _t(ax, x + 30, yy, "• " + it, size=12, color=INK, fam=BODY, ha="left", z=7)
        _arrow(ax, W / 2, 250, x + 120, 226, color=MAROON, lw=2.0)

    _box(ax, 20, 8, 800, 26, MAROON_DARK, r=13, z=5)
    _t(ax, W / 2, 21, "One name, many appropriate behaviours — decided by the object that receives the call",
       size=12, color=GOLD_LIGHT, fam=B_SB)

    return _save(fig, "polymorphism.png")


# --------------------------------------------------------------------------
# 10. Encapsulation
# --------------------------------------------------------------------------
def encapsulation():
    W, H = 840, 380
    fig, ax = _canvas(W / 100, H / 100)
    _title(ax, W, "Encapsulation — Protecting the Object's Data", sub="Data and its operations live together; the outside goes through controlled methods")

    # class box
    _box(ax, 30, 50, 300, 220, WHITE, ec=MAROON, lw=2, r=14, z=6)
    _box(ax, 30, 232, 300, 38, MAROON, r=12, z=6)
    _t(ax, 180, 251, "BankAccount", size=14.5, color=WHITE, fam=H_B, z=7)
    _t(ax, 60, 196, "- balance   (private)", size=12.5, color=MAROON_DARK, fam=MONO, ha="left", z=7)
    ax.plot([44, 316], [180, 180], color=GOLD, lw=1.2, zorder=7)
    _t(ax, 60, 160, "+ deposit()", size=12.5, color=INK, fam=MONO, ha="left", z=7)
    _t(ax, 60, 132, "+ withdraw()", size=12.5, color=INK, fam=MONO, ha="left", z=7)
    _t(ax, 60, 104, "+ getBalance()", size=12.5, color=INK, fam=MONO, ha="left", z=7)
    _t(ax, 60, 66, "state hidden, rules enforced here", size=10.5, color=GREY, fam=B_IT, ha="left", z=7)

    # wrong vs right
    _arrow(ax, 336, 160, 400, 160, color=MAROON, lw=2.6)
    _box(ax, 410, 150, 400, 110, MAROON_TINT, ec=MAROON, lw=1.6, r=14, z=6)
    _t(ax, 435, 232, "✗", size=15, color=MAROON, fam=SYM, ha="left", z=7)
    _t(ax, 462, 232, "Direct tampering (avoid)", size=13, color=MAROON, fam=B_B, ha="left", z=7)
    _t(ax, 435, 200, "balance = -500000", size=12.5, color=INK, fam=MONO, ha="left", z=7)
    _t(ax, 435, 172, "any part of the app can change the data", size=11, color=GREY, fam=B_IT, ha="left", z=7)

    _box(ax, 410, 40, 400, 100, CREAM_2, ec=GOLD, lw=1.8, r=14, z=6)
    _t(ax, 435, 118, "✓", size=15, color=MAROON_DARK, fam=SYM, ha="left", z=7)
    _t(ax, 462, 118, "Controlled interaction", size=13, color=MAROON_DARK, fam=B_B, ha="left", z=7)
    _t(ax, 435, 88, "withdraw(50000)", size=12.5, color=INK, fam=MONO, ha="left", z=7)
    _t(ax, 435, 58, "account active? amount valid? funds enough? recorded?", size=10.5, color=GREY, fam=B_IT, ha="left", z=7)

    return _save(fig, "encapsulation.png")


# --------------------------------------------------------------------------
# 11. Four OO principles
# --------------------------------------------------------------------------
def four_principles():
    W, H = 840, 430
    fig, ax = _canvas(W / 100, H / 100)
    _title(ax, W, "The Four Principles of Object Orientation", sub="You will meet these again and again through the module")

    cards = [
        ("A", "Abstraction", "Focus on the important characteristics; hide unnecessary detail.", MAROON),
        ("E", "Encapsulation", "Bind data with its behaviour and protect internal state.", MAROON_DARK),
        ("I", "Inheritance", "Create specialised classes from an existing general class.", "#8C2B2D"),
        ("P", "Polymorphism", "Related objects can respond differently to the same call.", GOLD),
    ]
    pos = [(20, 170), (440, 170), (20, 20), (440, 20)]
    for (glyph, title, desc, col), (x, y) in zip(cards, pos):
        _box(ax, x, y, 380, 120, WHITE, ec=col, lw=2, r=16, z=6)
        _box(ax, x + 20, y + 62, 54, 54, col, r=14, z=7)
        _t(ax, x + 47, y + 89, glyph, size=24, color=(MAROON_DARK if col == GOLD else WHITE), fam=H_B, z=8)
        _t(ax, x + 92, y + 96, title, size=16, color=col if col != GOLD else MAROON_DARK, fam=H_B, ha="left", z=7)
        _t(ax, x + 92, y + 66, desc, size=12, color=INK, fam=BODY, ha="left", va="top", z=7, ls=1.3)
        _t(ax, x + 20, y + 38, "one line to remember", size=9.5, color=GREY, fam=B_IT, ha="left", z=7)

    return _save(fig, "four_principles.png")


# --------------------------------------------------------------------------
# 12. Aspects overview (4 cards)
# --------------------------------------------------------------------------
def aspects_overview():
    W, H = 840, 330
    fig, ax = _canvas(W / 100, H / 100)
    _title(ax, W, "Four Aspects of a Complete Software Need", sub="Businesses rarely need just “software” — they need all four captured")

    cards = [
        ("Functional", "What it must DO", "Register students, calculate fees, transfer money", MAROON),
        ("Non-functional", "How WELL it must work", "2-second response, 99.9% availability, security", MAROON_DARK),
        ("Business rules", "Policies to enforce", "“Pass BICT 2101 before BICT 3202”", "#8C2B2D"),
        ("Constraints", "Limits on the solution", "Budget, existing database, platform, law", GOLD),
    ]
    xs = [20, 225, 430, 635]
    for (title, sub, ex, col), x in zip(cards, xs):
        _box(ax, x, 30, 185, 230, WHITE, ec=col, lw=1.8, r=14, z=6)
        _box(ax, x, 214, 185, 46, col, r=12, z=6)
        _t(ax, x + 92, 237, title, size=13, color=(MAROON_DARK if col == GOLD else WHITE), fam=H_SB, z=7)
        _t(ax, x + 92, 186, sub, size=11, color=(MAROON_DARK if col == GOLD else col), fam=B_B, z=7)
        _t(ax, x + 92, 110, ex, size=10.5, color=INK, fam=BODY, z=7, ls=1.3)
        _t(ax, x + 92, 48, "an example…", size=9.5, color=GREY, fam=B_IT, z=7)

    return _save(fig, "aspects_overview.png")


# --------------------------------------------------------------------------
# 13. Elicitation techniques
# --------------------------------------------------------------------------
def elicitation():
    W, H = 840, 380
    fig, ax = _canvas(W / 100, H / 100)
    _title(ax, W, "How Do We Discover Requirements?", sub="Six common requirements-elicitation techniques")

    cards = [
        ("1", "Interviews", "Talk one-to-one with stakeholders"),
        ("2", "Questionnaires", "Collect answers from many users at once"),
        ("3", "Observation", "Watch users perform their real work"),
        ("4", "Document analysis", "Study forms, reports, policies, spreadsheets"),
        ("5", "Workshops", "Bring stakeholders together to discuss needs"),
        ("6", "Prototyping", "Show a draft system and collect feedback"),
    ]
    pos = [(20, 180), (300, 180), (580, 180), (20, 20), (300, 20), (580, 20)]
    for (num, title, desc), (x, y) in zip(cards, pos):
        _box(ax, x, y, 240, 130, WHITE, ec=MAROON, lw=1.6, r=14, z=6)
        _box(ax, x + 16, y + 90, 34, 30, MAROON, r=10, z=7)
        _t(ax, x + 33, y + 105, num, size=14, color=WHITE, fam=H_B, z=8)
        _t(ax, x + 64, y + 104, title, size=13.5, color=MAROON, fam=H_SB, ha="left", z=7)
        _t(ax, x + 16, y + 52, desc, size=11, color=INK, fam=BODY, ha="left", va="center", z=7, ls=1.25)

    return _save(fig, "elicitation.png")


# --------------------------------------------------------------------------
# 14. Bar chart — project failure contributors (illustrative)
# --------------------------------------------------------------------------
def chart_failure_reasons():
    W, H = 840, 420
    fig, ax = _canvas(W / 100, H / 100)
    _title(ax, W, "Why Analysis Matters", sub="Illustrative survey pattern — factors cited in troubled software projects")

    labels = ["Incomplete requirements", "Changing requirements", "Lack of user involvement",
              "Unrealistic expectations", "Poor planning", "Lack of skilled resources"]
    values = [13, 12, 12, 10, 9, 8]
    colors = [MAROON, MAROON_SOFT, GOLD, "#8C2B2D", "#B3797A", GREY]

    y = np.arange(len(labels))[::-1]
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.axis("off")

    plot = fig.add_axes([0.16, 0.22, 0.60, 0.55])
    plot.barh(y, values, color=colors, height=0.55, zorder=3)
    plot.set_yticks(y)
    plot.set_yticklabels(labels, fontsize=12.5, family="Open Sans", color=INK)
    plot.set_xlim(0, 15)
    plot.set_xticks([])
    for s in ("top", "right", "left"):
        plot.spines[s].set_visible(False)
    plot.spines["bottom"].set_color(GREY_LIGHT)
    for yi, v in zip(y, values):
        plot.text(v + 0.25, yi, f"{v}%", va="center", fontsize=11.5,
                  family="Open Sans", fontweight="semibold", color=MAROON)

    fig.text(0.5, 0.085, "Illustrative only — typical of published industry surveys on project outcomes.",
             ha="center", va="center", fontsize=11, family="Open Sans",
             fontstyle="italic", color=GREY)

    return _save(fig, "chart_failure_reasons.png")


# --------------------------------------------------------------------------
# 15. Donut — a complete software need
# --------------------------------------------------------------------------
def chart_needs_mix():
    W, H = 840, 420
    fig, ax = _canvas(W / 100, H / 100)
    _title(ax, W, "A Complete Software Need", sub="Functional, non-functional and rules/constraints all belong in the requirement set")

    plot = fig.add_axes([0.30, 0.18, 0.40, 0.62])
    sizes = [50, 30, 20]
    labels = ["Functional\nrequirements", "Non-functional\nrequirements", "Business rules\n& constraints"]
    cols = [MAROON, GOLD, MAROON_SOFT]
    wedges, _ = plot.pie(sizes, colors=cols, startangle=90, counterclock=False,
                         wedgeprops=dict(width=0.34, edgecolor=CREAM, linewidth=3))
    plot.text(0, 0.06, "Software", ha="center", va="center", fontsize=17,
              family="Poppins", fontweight="bold", color=MAROON)
    plot.text(0, -0.22, "Needs", ha="center", va="center", fontsize=17,
              family="Poppins", fontweight="bold", color=MAROON)

    for w, lab, col in zip(wedges, labels, cols):
        ang = (w.theta2 + w.theta1) / 2
        x = np.cos(np.deg2rad(ang)) * 0.82
        y = np.sin(np.deg2rad(ang)) * 0.82
        plot.text(x, y, lab, ha="center", va="center", fontsize=11,
                  family="Open Sans", fontweight="semibold", color=col)

    fig.text(0.5, 0.05, "Conceptual emphasis — all three must be captured during analysis.",
             ha="center", va="center", fontsize=11, family="Open Sans",
             fontstyle="italic", color=GREY)

    return _save(fig, "chart_needs_mix.png")


# --------------------------------------------------------------------------
# 16. ATM worked example flow
# --------------------------------------------------------------------------
def atm_flow():
    W, H = 840, 300
    fig, ax = _canvas(W / 100, H / 100)
    _title(ax, W, "Worked Example — the ATM", sub="Moving from a business problem to candidate objects")

    steps = [
        ("Business\nproblem", "customers must visit\nbranches for basic tasks", MAROON),
        ("Business\nneed", "convenient\nself-service banking", MAROON_DARK),
        ("Objective", "24/7 access · reduce\nbranch workload", "#8C2B2D"),
        ("Software\nsolution", "an ATM\nsystem", GOLD),
        ("Candidate\nobjects", "Customer · Card · Account\nTransaction · ATM · Receipt", MAROON_SOFT),
    ]
    cw, ch = 152, 150
    x = 12
    for i, (title, body, col) in enumerate(steps):
        _chev(ax, x, 40, cw, ch, col, r=6, z=6)
        _t(ax, x + cw / 2 + 8, 40 + ch - 34, title, size=13, color=WHITE if col != GOLD else MAROON_DARK, fam=H_B, z=8, ls=1.15)
        _t(ax, x + cw / 2 + 8, 40 + ch / 2 - 6, body, size=10, color=WHITE if col != GOLD else MAROON_DARK, fam=BODY, z=8, ls=1.25)
        x += cw - 4

    _box(ax, 20, 8, 800, 26, MAROON_DARK, r=13, z=5)
    _t(ax, W / 2, 21, "business problem  →  business need  →  requirements  →  objects  —  the Week 1 mindset",
       size=12, color=GOLD_LIGHT, fam=MONO)

    return _save(fig, "atm_flow.png")


ALL = [
    journey, problem_need_solution, functional_nonfunctional, stakeholders,
    object_anatomy, class_vs_object, bank_objects, inheritance, polymorphism,
    encapsulation, four_principles, aspects_overview, elicitation,
    chart_failure_reasons, chart_needs_mix, atm_flow,
]


if __name__ == "__main__":
    made = []
    for fn in ALL:
        try:
            p = fn()
            made.append(os.path.basename(p))
        except Exception as e:
            print(f"[FAIL] {fn.__name__}: {e}")
    print("Generated", len(made), "visuals:")
    for m in made:
        print("  -", m)
