"""
Week 8 visuals — OBJECT-ORIENTED ANALYSIS: BEHAVIOURAL MODELLING.
Use cases · use case diagrams · sequence · communication · activity · documentation.
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


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------
def actor(ax, cx, cy, s=1.0, color=MAROON, label=None, lw=2.2):
    ax.add_patch(Circle((cx, cy + 30 * s), 8 * s, fill=False, edgecolor=color, lw=lw, zorder=7))
    ax.plot([cx, cx], [cy + 22 * s, cy - 6 * s], color=color, lw=lw, zorder=7)
    ax.plot([cx - 14 * s, cx + 14 * s], [cy + 12 * s, cy + 12 * s], color=color, lw=lw, zorder=7)
    ax.plot([cx, cx - 12 * s], [cy - 6 * s, cy - 30 * s], color=color, lw=lw, zorder=7)
    ax.plot([cx, cx + 12 * s], [cy - 6 * s, cy - 30 * s], color=color, lw=lw, zorder=7)
    if label:
        t(ax, cx, cy - 46 * s, label, size=12, color=MAROON, fam=H_SB, z=7)


def usecase(ax, x, y, w, h, label, ec=MAROON, size=10.5):
    ax.add_patch(Ellipse((x + w / 2, y + h / 2), w, h, facecolor=WHITE,
                         edgecolor=ec, lw=1.8, zorder=6))
    t(ax, x + w / 2, y + h / 2, label, size=size, color=MAROON, fam=H_SB, z=7)


def lifeline(ax, x, y_top, y_bot, label=None, box_w=120, ec=MAROON):
    if label is not None:
        box(ax, x - box_w / 2, y_top, box_w, 34, MAROON, r=0, z=7)
        t(ax, x, y_top + 17, label, size=10.5, color=WHITE, fam=H_SB, z=8)
    ax.plot([x, x], [y_top, y_bot], color=MAROON, lw=1.0, ls=(0, (4, 4)), zorder=6)


def activation(ax, x, y1, y2, color=MAROON_TINT, w=12, ec=MAROON):
    box(ax, x - w / 2, y1, w, y2 - y1, color, ec=ec, lw=1.0, r=0, z=7)


def msg(ax, x1, y, x2, label=None, dashed=False, color=MAROON, size=9.5):
    style = "<|-" if dashed else "-|>"
    arrow(ax, x1, y, x2, y, color=color, lw=1.8, style=style, z=8)
    if label is not None:
        t(ax, (x1 + x2) / 2, y + 8, label, size=size, color=MAROON_SOFT, fam=MONO, z=9)


def action(ax, x, y, w, h, name, ec=MAROON, size=10.5, fill=WHITE):
    box(ax, x, y, w, h, fill, ec=ec, lw=1.6, r=16, z=6)
    t(ax, x + w / 2, y + h / 2, name, size=size, color=MAROON_DARK, fam=B_SB, z=7)


def decision(ax, x, y, w, h=44, ec=MAROON):
    ax.add_patch(Polygon([(x + w / 2, y + h), (x + w, y + h / 2),
                          (x + w / 2, y), (x, y + h / 2)],
                         closed=True, facecolor=WHITE, edgecolor=ec, lw=1.8, zorder=6))


def initial_node(ax, x, y, r=7):
    ax.add_patch(Circle((x, y), r, facecolor=MAROON_DARK, edgecolor="none", zorder=8))


def final_node(ax, x, y, r=10):
    ax.add_patch(Circle((x, y), r, fill=False, edgecolor=MAROON_DARK, lw=2.0, zorder=8))
    ax.add_patch(Circle((x, y), r * 0.55, facecolor=MAROON_DARK, edgecolor="none", zorder=8))


def bar(ax, x, y, w, h=10, color=MAROON):
    box(ax, x, y, w, h, color, r=2, z=7)


# --------------------------------------------------------------------------
# 1. The behavioural family
# --------------------------------------------------------------------------
def family():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "The Behavioural Modelling Family", sub="Each diagram answers a slightly different question")

    box(ax, 22, 300, 796, 50, MAROON_DARK, r=12, z=7)
    t(ax, W / 2, 325, "BEHAVIOURAL MODELLING", size=15, color=WHITE, fam=H_B, z=8)

    cols = [
        ("USE CASES", "Use Case Diagram", "What goals do users have?", MAROON),
        ("INTERACTIONS", "Sequence Diagram\nCommunication Diagram", "Who communicates and in what order?", MAROON_SOFT),
        ("ACTIVITIES", "Activity Diagram", "What workflow happens, including decisions and parallelism?", "#8C2B2D"),
    ]
    ax.plot([W / 2, 150], [300, 240], color=MAROON, lw=2.0, zorder=6)
    ax.plot([W / 2, W / 2], [300, 240], color=MAROON, lw=2.0, zorder=6)
    ax.plot([W / 2, 690], [300, 240], color=MAROON, lw=2.0, zorder=6)

    for (cname, dias, q, col), (cx) in zip(cols, [150, W / 2, 690]):
        box(ax, cx - 118, 130, 236, 110, WHITE, ec=col, lw=1.6, r=12, z=6)
        box(ax, cx - 118, 210, 236, 30, col, r=12, z=7)
        t(ax, cx, 225, cname, size=12, color=WHITE, fam=H_B, z=8)
        t(ax, cx, 180, dias, size=10.5, color=MAROON_DARK, fam=B_SB, z=7, ls=1.2)
        t(ax, cx, 148, q, size=9.5, color=GREY, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Use cases = goals · interactions = messages · activities = workflow.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w8_family.png")


# --------------------------------------------------------------------------
# 2. What question each diagram answers
# --------------------------------------------------------------------------
def questions():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "What Question Does Each Diagram Answer?", sub="Very important for examinations")

    rows = [
        ("Use Case", "What does the system provide to its users?"),
        ("Use Case Diagram", "Who interacts with the system and what do they do?"),
        ("Sequence Diagram", "Who sends what message to whom, and in what order?"),
        ("Communication Diagram", "Which objects communicate, and how are their messages organised?"),
        ("Activity Diagram", "What workflow happens, with decisions and parallel activities?"),
    ]
    x0, y0, cw, ch = 60, 70, 320, 54
    for i, (a, b) in enumerate(rows):
        y = y0 + (len(rows) - 1 - i) * (ch + 8)
        box(ax, x0, y, cw, ch, MAROON if i % 2 == 0 else MAROON_DARK, r=9, z=6)
        t(ax, x0 + 160, y + ch / 2, a, size=11.5, color=WHITE, fam=H_SB, z=7)
        box(ax, x0 + 330, y, 340, ch, WHITE, ec=MAROON_SOFT, lw=1.2, r=9, z=6)
        t(ax, x0 + 350, y + ch / 2, b, size=10.5, color=INK, fam=BODY, ha="left", z=7)

    return save(fig, "w8_questions.png")


# --------------------------------------------------------------------------
# 3. Use case vs function
# --------------------------------------------------------------------------
def use_case_goal():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "A Use Case Is a Goal", sub="Ask: what does the actor want to accomplish?")

    box(ax, 22, 130, 380, 250, WHITE, ec=MAROON, lw=1.8, r=14, z=6)
    box(ax, 22, 350, 380, 30, MAROON, r=14, z=7)
    t(ax, 212, 365, "USE CASE", size=13, color=WHITE, fam=H_B, z=8)
    t(ax, 212, 318, "the user's GOAL", size=13, color=MAROON_DARK, fam=B_SB, z=7)
    usecase(ax, 80, 210, 250, 70, "Register for Course", size=12)
    t(ax, 212, 176, "\"I want to register for a course\"", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 438, 130, 380, 250, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=6)
    box(ax, 438, 350, 380, 30, MAROON_DARK, r=14, z=7)
    t(ax, 628, 365, "FUNCTIONS / STEPS", size=13, color=WHITE, fam=H_B, z=8)
    t(ax, 628, 318, "steps to achieve the goal", size=12, color=MAROON_DARK, fam=B_SB, z=7)
    for i, st in enumerate(["Read card", "Validate PIN", "Check balance", "Dispense cash", "Print receipt"]):
        t(ax, 476, 272 - i * 26, st, size=11, color=INK, fam=MONO, ha="left", z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "\"Register for Course\" is the goal — \u201cClick Register Button\u201d is only an interface action.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w8_use_case_goal.png")


# --------------------------------------------------------------------------
# 4. Actor
# --------------------------------------------------------------------------
def actor_human():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Actors — Roles Outside the System", sub="An actor is not necessarily a person")

    box(ax, 22, 130, 380, 250, WHITE, ec=MAROON, lw=1.8, r=14, z=6)
    actor(ax, 130, 200, 1.1, label="Student")
    t(ax, 240, 320, "HUMAN ACTOR", size=12.5, color=MAROON, fam=H_B, z=7)
    t(ax, 240, 290, "a role played by a person", size=11, color=INK, fam=BODY, z=7)
    t(ax, 240, 262, "one person, many roles:", size=10.5, color=GREY, fam=B_IT, z=7)
    t(ax, 240, 238, "Student + Teaching Assistant", size=10.5, color=MAROON_SOFT, fam=MONO, z=7)

    box(ax, 438, 130, 380, 250, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=6)
    t(ax, 628, 320, "NON-HUMAN ACTOR", size=12.5, color=MAROON, fam=H_B, z=7)
    box(ax, 500, 250, 240, 60, MAROON, r=10, z=7)
    t(ax, 620, 280, "Payment Gateway", size=12.5, color=WHITE, fam=H_SB, z=8)
    t(ax, 620, 222, "an external system can be", size=11, color=INK, fam=BODY, z=7)
    t(ax, 620, 202, "an actor too", size=11, color=INK, fam=BODY, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "An actor represents a role played by something EXTERNAL to the system.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w8_actor_human.png")


# --------------------------------------------------------------------------
# 5. Use case diagram
# --------------------------------------------------------------------------
def use_case_diagram():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "A Use Case Diagram", sub="Actors · use cases · system boundary · relationships")

    # system boundary
    box(ax, 150, 60, 540, 360, WHITE, ec=MAROON, lw=2.0, r=12, z=5)
    t(ax, 420, 392, "UNIVERSITY REGISTRATION SYSTEM", size=12, color=MAROON, fam=H_B, z=7)

    usecases = [("Login", 250, 330, 160, 52),
                ("Register Course", 470, 330, 190, 52),
                ("Drop Course", 250, 240, 160, 52),
                ("View Results", 470, 240, 160, 52),
                ("Make Payment", 250, 150, 160, 52),
                ("Enter Marks", 470, 150, 160, 52)]
    for nm, x, y, w, h in usecases:
        usecase(ax, x, y, w, h, nm, size=10)

    # actors
    actor(ax, 70, 350, 1.0, label="Student")
    actor(ax, 70, 150, 1.0, label="Lecturer")
    actor(ax, 770, 350, 1.0, label="Admin")

    # associations
    ax.plot([110, 250], [340, 356], color=MAROON, lw=1.6, zorder=6)
    ax.plot([110, 250], [340, 266], color=MAROON, lw=1.6, zorder=6)
    ax.plot([110, 250], [340, 176], color=MAROON, lw=1.6, zorder=6)
    ax.plot([110, 250], [340, 220], color=MAROON, lw=1.6, zorder=6)
    ax.plot([110, 250], [140, 176], color=MAROON, lw=1.6, zorder=6)
    ax.plot([110, 250], [140, 266], color=MAROON, lw=1.6, zorder=6)
    ax.plot([730, 660], [340, 356], color=MAROON, lw=1.6, zorder=6)

    box(ax, 22, 12, 796, 22, MAROON_DARK, r=10, z=5)
    t(ax, W / 2, 23, "The rectangle is the system boundary — actors sit outside, use cases inside.",
      size=10.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w8_use_case_diagram.png")


# --------------------------------------------------------------------------
# 6. Use case relationships
# --------------------------------------------------------------------------
def relationships():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Use Case Relationships", sub="Association · include · extend · generalisation")

    # association
    box(ax, 22, 250, 380, 180, WHITE, ec=MAROON, lw=1.4, r=10, z=6)
    t(ax, 212, 408, "ASSOCIATION", size=11.5, color=MAROON, fam=H_SB, z=7)
    actor(ax, 110, 330, 0.8, label="Student")
    ax.plot([150, 250], [320, 330], color=MAROON, lw=1.6, zorder=6)
    usecase(ax, 250, 305, 150, 50, "Register Course", size=9.5)

    # include
    box(ax, 438, 250, 380, 180, MAROON_TINT, ec=MAROON, lw=1.4, r=10, z=6)
    t(ax, 628, 408, "include", size=11.5, color=MAROON, fam=H_SB, z=7)
    usecase(ax, 470, 310, 150, 46, "Register Course", size=9.5)
    t(ax, 590, 300, "<<include>>", size=9.5, color=MAROON_SOFT, fam=B_IT, z=7)
    arrow(ax, 570, 300, 660, 300, color=MAROON, lw=1.6, style="-|>", z=8)
    usecase(ax, 660, 300, 150, 46, "Authenticate", size=9.5)
    t(ax, 628, 270, "always needed — required behaviour", size=9.5, color=GREY, fam=B_IT, z=7)

    # extend
    box(ax, 22, 30, 380, 180, WHITE, ec=MAROON, lw=1.4, r=10, z=6)
    t(ax, 212, 188, "extend", size=11.5, color=MAROON, fam=H_SB, z=7)
    usecase(ax, 40, 70, 150, 46, "Withdraw Cash", size=9.5)
    t(ax, 170, 60, "<<extend>>", size=9.5, color=MAROON_SOFT, fam=B_IT, z=7)
    arrow(ax, 200, 62, 290, 62, color=MAROON, lw=1.6, style="-|>", z=8)
    usecase(ax, 290, 55, 170, 60, "Report Suspicious\nTransaction", size=9)
    t(ax, 212, 44, "sometimes added — conditional behaviour", size=9.5, color=GREY, fam=B_IT, z=7)

    # generalisation
    box(ax, 438, 30, 380, 180, MAROON_TINT, ec=MAROON, lw=1.4, r=10, z=6)
    t(ax, 628, 188, "GENERALISATION", size=11.5, color=MAROON, fam=H_SB, z=7)
    usecase(ax, 540, 90, 150, 46, "User", size=9.5)
    ax.add_patch(Polygon([(600, 80), (585, 60), (615, 60)], closed=True, fill=False, edgecolor=MAROON, lw=1.6, zorder=8))
    ax.plot([600, 560], [60, 44], color=MAROON, lw=1.6, zorder=7)
    ax.plot([600, 640], [60, 44], color=MAROON, lw=1.6, zorder=7)
    usecase(ax, 490, 8, 140, 38, "Student", size=9)
    usecase(ax, 570, 8, 140, 38, "Lecturer", size=9)

    box(ax, 22, 8, 796, 22, MAROON_DARK, r=10, z=5)
    t(ax, W / 2, 19, "INCLUDE = I need this as part of the job · EXTEND = I might add this under a condition.",
      size=10.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w8_relationships.png")


# --------------------------------------------------------------------------
# 7. include vs extend
# --------------------------------------------------------------------------
def include_extend():
    W, H = 840, 400
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "include vs extend", sub="An examination favourite")

    rows = [
        ("include", "Reused behaviour", "Part of the base use case", "Always required"),
        ("extend", "Additional / optional behaviour", "Occurs under specified conditions", "Sometimes added"),
    ]
    box(ax, 22, 200, 380, 40, MAROON, r=10, z=7)
    t(ax, 212, 220, "include", size=13, color=WHITE, fam=H_B, z=8)
    box(ax, 438, 200, 380, 40, MAROON_DARK, r=10, z=7)
    t(ax, 628, 220, "extend", size=13, color=WHITE, fam=H_B, z=8)

    for i in range(3):
        y = 160 - i * 46
        t(ax, 60, y, ["reused / factored common behaviour", "part of the base use case", "think: always required"][i],
          size=10.5, color=INK, fam=BODY, ha="left", z=7)
        t(ax, 470, y, ["additional / optional behaviour", "occurs under specified conditions", "think: sometimes added"][i],
          size=10.5, color=INK, fam=BODY, ha="left", z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "include = required, reused · extend = optional, conditional.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w8_include_extend.png")


# --------------------------------------------------------------------------
# 8. Use case specification
# --------------------------------------------------------------------------
def specification():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Use Case Specification", sub="The diagram is not enough — capture what happens inside")

    box(ax, 22, 60, 380, 330, WHITE, ec=MAROON, lw=1.6, r=12, z=6)
    t(ax, 212, 366, "REGISTER FOR COURSE  (UC-01)", size=11.5, color=MAROON, fam=H_B, z=7)
    lines = [
        "Primary actor: Student",
        "Goal: register for a course",
        "",
        "Preconditions:",
        "  - valid account, authenticated",
        "",
        "Main success scenario:",
        "1. Select Register Course",
        "2. Choose a course",
        "3. Check prerequisites",
        "4. Check capacity",
        "5. Confirm registration",
        "6. Confirmation shown",
    ]
    yy = 330
    for ln in lines:
        if ln == "":
            yy -= 10
            continue
        bold = ln.endswith(":") or ln.endswith("(UC-01)") or ln.startswith("Main") or ln.startswith("Preconditions")
        t(ax, 40, yy, ln, size=9.5 if not bold else 10,
          color=MAROON_DARK if bold else INK, fam=B_SB if bold else MONO, ha="left", z=7)
        yy -= 19

    box(ax, 438, 60, 380, 330, MAROON_TINT, ec=MAROON, lw=1.6, r=12, z=6)
    t(ax, 628, 366, "ALTERNATIVE & EXCEPTION FLOWS", size=11.5, color=MAROON, fam=H_B, z=7)
    alt = [
        "Alternative A — Course full:",
        "  inform student, offer waitlist",
        "",
        "Alternative B — Prerequisite missing:",
        "  inform student, registration stops",
        "",
        "Postcondition:",
        "  student is registered for the course",
        "",
        "Why it matters:",
        "  programmers need the details —",
        "  not just \u201cbuild registration\u201d",
    ]
    yy = 330
    for ln in alt:
        if ln == "":
            yy -= 10
            continue
        bold = ln.endswith(":") or ln.startswith("Postcondition") or ln.startswith("Why")
        t(ax, 456, yy, ln, size=9.5 if not bold else 10,
          color=MAROON_DARK if bold else INK, fam=B_SB if bold else MONO, ha="left", z=7)
        yy -= 19

    box(ax, 22, 16, 796, 22, MAROON_DARK, r=10, z=5)
    t(ax, W / 2, 27, "Model the alternative and exception paths — not only the happy path.",
      size=10.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w8_specification.png")


# --------------------------------------------------------------------------
# 9. Sequence components
# --------------------------------------------------------------------------
def sequence_components():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Sequence Diagram Components", sub="Lifelines, activation bars and messages")

    # lifelines
    lifeline(ax, 150, 360, 60, label="Student")
    lifeline(ax, 430, 360, 60, label="System")
    lifeline(ax, 700, 360, 60, label="Database")

    # activation + messages
    activation(ax, 430, 220, 340)
    activation(ax, 700, 180, 300)
    activation(ax, 150, 250, 330)

    msg(ax, 150, 330, 430, "login()")
    msg(ax, 430, 300, 700, "validate()")
    msg(ax, 700, 260, 430, "valid", dashed=True)
    msg(ax, 430, 180, 150, "confirmation", dashed=True)

    t(ax, 150, 40, "lifeline", size=9.5, color=GREY, fam=B_IT, z=7)
    t(ax, 430, 40, "activation bar", size=9.5, color=GREY, fam=B_IT, z=7)

    box(ax, 22, 8, 796, 22, MAROON_DARK, r=10, z=5)
    t(ax, W / 2, 19, "Read top to bottom — time flows downward. Solid arrows = messages; dashed = returns.",
      size=10.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w8_sequence_components.png")


# --------------------------------------------------------------------------
# 10. Login sequence
# --------------------------------------------------------------------------
def sequence_login():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Sequence Diagram — Login", sub="Who communicates with whom, in what order")

    lifeline(ax, 150, 400, 40, label="Student")
    lifeline(ax, 430, 400, 40, label="System")
    lifeline(ax, 700, 400, 40, label="Database")

    activation(ax, 150, 250, 380)
    activation(ax, 430, 180, 380)
    activation(ax, 700, 140, 330)

    msg(ax, 150, 370, 430, "login()")
    msg(ax, 430, 330, 700, "validateCredentials()")
    msg(ax, 700, 290, 430, "valid", dashed=True)
    msg(ax, 430, 250, 150, "login successful", dashed=True)

    box(ax, 22, 8, 796, 22, MAROON_DARK, r=10, z=5)
    t(ax, W / 2, 19, "Order matters — you cannot send \u201clogin successful\u201d before validating the credentials.",
      size=10.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w8_sequence_login.png")


# --------------------------------------------------------------------------
# 11. Fragments
# --------------------------------------------------------------------------
def fragments():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Combined Fragments — alt, loop, opt", sub="Alternatives, repetition and optional behaviour")

    def frag(x, y, w, h, tag, inner, ec):
        box(ax, x, y, w, h, WHITE, ec=ec, lw=1.6, r=8, z=6)
        box(ax, x, y + h - 24, w, 24, ec, r=8, z=7)
        t(ax, x + 14, y + h - 12, tag, size=10.5, color=WHITE, fam=B_SB, ha="left", z=8)
        yy = y + h - 48
        for ln in inner:
            t(ax, x + 12, yy, ln, size=9.5, color=INK, fam=MONO, ha="left", z=7)
            yy -= 18

    frag(22, 160, 380, 250, "alt", ["[course available]", "  Controller -> DB: register()", "",
                                    "[course full]", "  Controller -> UI: showFull()"], MAROON)
    frag(438, 160, 380, 250, "loop", ["[for each student]", "  System -> Student: sendResult()"], MAROON_DARK)

    box(ax, 22, 30, 380, 110, WHITE, ec=MAROON_SOFT, lw=1.6, r=8, z=6)
    box(ax, 22, 116, 380, 24, MAROON_SOFT, r=8, z=7)
    t(ax, 36, 128, "opt", size=10.5, color=WHITE, fam=B_SB, ha="left", z=8)
    t(ax, 34, 88, "[SMS notification enabled]", size=9.5, color=INK, fam=MONO, ha="left", z=7)
    t(ax, 34, 70, "  System -> SMS Service: sendSMS()", size=9.5, color=INK, fam=MONO, ha="left", z=7)

    box(ax, 438, 30, 380, 110, MAROON_TINT, ec=MAROON, lw=1.4, r=8, z=6)
    t(ax, 628, 120, "KEY IDEA", size=11, color=MAROON, fam=H_SB, z=7)
    t(ax, 628, 88, "alt: only the branch whose", size=10.5, color=INK, fam=BODY, z=7)
    t(ax, 628, 68, "guard is true executes", size=10.5, color=INK, fam=BODY, z=7)
    t(ax, 628, 44, "loop repeats · opt runs only if true", size=9.5, color=GREY, fam=B_IT, z=7)

    return save(fig, "w8_fragments.png")


# --------------------------------------------------------------------------
# 12. Communication diagram
# --------------------------------------------------------------------------
def communication():
    W, H = 840, 440
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Communication (Collaboration) Diagram", sub="Which objects communicate, with numbered messages")

    def obj(x, y, name):
        box(ax, x - 80, y, 160, 40, WHITE, ec=MAROON, lw=1.6, r=0, z=6)
        t(ax, x, y + 20, name, size=10.5, color=MAROON_DARK, fam=B_SB, z=7)

    obj(150, 320, ": Student")
    obj(420, 320, ": Registration\nSystem")
    obj(690, 320, ": Course\nDatabase")

    ax.plot([230, 340], [340, 340], color=MAROON, lw=1.8, zorder=7)
    ax.plot([500, 610], [340, 340], color=MAROON, lw=1.8, zorder=7)
    ax.plot([230, 340], [310, 310], color=MAROON, lw=1.8, zorder=7)
    ax.plot([500, 610], [310, 310], color=MAROON, lw=1.8, zorder=7)

    t(ax, 285, 348, "1: register()", size=10, color=MAROON_SOFT, fam=MONO, z=9)
    t(ax, 555, 348, "2: checkCourse()", size=10, color=MAROON_SOFT, fam=MONO, z=9)
    t(ax, 285, 302, "4: confirmation", size=10, color=MAROON_SOFT, fam=MONO, z=9)
    t(ax, 555, 302, "3: availability", size=10, color=MAROON_SOFT, fam=MONO, z=9)

    box(ax, 22, 60, 796, 90, MAROON_TINT, ec=MAROON, lw=1.4, r=10, z=6)
    t(ax, 60, 128, "The numbers 1, 2, 3, 4 show message order.", size=11.5, color=MAROON_DARK, fam=B_SB, ha="left", z=7)
    t(ax, 60, 100, "Objects are arranged around the interaction (not top-to-bottom time).", size=11, color=INK, fam=BODY, ha="left", z=7)
    t(ax, 60, 80, "Older name: collaboration diagram · UML 2.x standard name: communication diagram.", size=10, color=GREY, fam=B_IT, ha="left", z=7)

    box(ax, 22, 20, 796, 22, MAROON_DARK, r=10, z=5)
    t(ax, W / 2, 31, "Emphasis: which objects communicate and how messages are organised.",
      size=10.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w8_communication.png")


# --------------------------------------------------------------------------
# 13. Sequence vs communication
# --------------------------------------------------------------------------
def seq_vs_comm():
    W, H = 840, 400
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Sequence vs Communication Diagram", sub="Same interaction, different emphasis")

    rows = [
        ("Emphasis", "time", "object relationships"),
        ("Arrangement", "messages vertically", "objects around the interaction"),
        ("Best for", "chronological order", "who communicates with whom"),
        ("Prominent", "lifelines", "links between objects"),
    ]
    box(ax, 22, 200, 380, 40, MAROON, r=10, z=7)
    t(ax, 212, 220, "SEQUENCE", size=13, color=WHITE, fam=H_B, z=8)
    box(ax, 438, 200, 380, 40, MAROON_DARK, r=10, z=7)
    t(ax, 628, 220, "COMMUNICATION", size=13, color=WHITE, fam=H_B, z=8)
    yy = 158
    for r, sv, cv in rows:
        t(ax, 60, yy, r, size=10.5, color=GREY, fam=B_SB, ha="left", z=7)
        t(ax, 212, yy, sv, size=10.5, color=INK, fam=BODY, z=7)
        t(ax, 628, yy, cv, size=10.5, color=INK, fam=BODY, z=7)
        yy -= 34

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "The same interaction can be shown either way — each gives a different visual emphasis.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w8_seq_vs_comm.png")


# --------------------------------------------------------------------------
# 14. Activity notation
# --------------------------------------------------------------------------
def activity_notation():
    W, H = 840, 460
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Activity Diagram Notation", sub="Initial node · actions · decision · fork/join · final node")

    box(ax, 22, 130, 796, 210, WHITE, ec=MAROON_SOFT, lw=1.4, r=12, z=6)

    initial_node(ax, 100, 300)
    trans = arrow
    trans(ax, 100, 300, 100, 250)
    action(ax, 55, 205, 130, 44, "Action", size=10.5)
    trans(ax, 185, 227, 300, 227)
    decision(ax, 300, 205, 44)
    trans(ax, 344, 227, 460, 227)
    bar(ax, 460, 218, 16, 62)
    trans(ax, 476, 262, 560, 262)
    trans(ax, 476, 236, 560, 236)
    action(ax, 560, 238, 130, 44, "Action A", size=10)
    action(ax, 560, 170, 130, 44, "Action B", size=10)
    trans(ax, 690, 260, 760, 260)
    trans(ax, 690, 192, 760, 192)
    bar(ax, 760, 188, 16, 62)
    trans(ax, 768, 219, 768, 130)
    final_node(ax, 768, 120)

    # labels
    t(ax, 100, 330, "initial node", size=9, color=GREY, fam=B_IT, z=7)
    t(ax, 120, 180, "action", size=9, color=GREY, fam=B_IT, z=7)
    t(ax, 322, 262, "decision", size=9, color=GREY, fam=B_IT, z=7)
    t(ax, 468, 292, "fork", size=9, color=GREY, fam=B_IT, z=7)
    t(ax, 768, 292, "join", size=9, color=GREY, fam=B_IT, z=7)
    t(ax, 768, 92, "final node", size=9, color=GREY, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "The diamond is a decision; the thick bars are fork (split) and join (synchronise).",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w8_activity_notation.png")


# --------------------------------------------------------------------------
# 15. Activity example
# --------------------------------------------------------------------------
def activity_example():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Activity Diagram — Online Shopping", sub="A workflow with a decision and parallel activities")

    initial_node(ax, 420, 430)
    arrow(ax, 420, 430, 420, 405)
    action(ax, 320, 360, 200, 44, "Select Product", size=11)
    arrow(ax, 420, 360, 420, 316)
    action(ax, 320, 272, 200, 44, "Add to Cart", size=11)
    arrow(ax, 420, 272, 420, 228)
    action(ax, 320, 184, 200, 44, "Make Payment", size=11)
    arrow(ax, 420, 184, 420, 156)
    decision(ax, 398, 112, 44)

    arrow(ax, 398, 134, 220, 134)
    arrow(ax, 442, 134, 620, 134)
    t(ax, 300, 142, "[successful]", size=9.5, color=MAROON_SOFT, fam=B_IT, z=9)
    t(ax, 540, 142, "[failed]", size=9.5, color=MAROON_SOFT, fam=B_IT, z=9)

    action(ax, 120, 88, 200, 44, "Create Order", fill=MAROON_TINT, size=11)
    action(ax, 520, 88, 200, 44, "Show Error", fill=CREAM_2, ec=MAROON_DARK, size=11)

    arrow(ax, 220, 88, 220, 30)
    final_node(ax, 220, 20)

    box(ax, 22, 6, 796, 22, MAROON_DARK, r=10, z=5)
    t(ax, W / 2, 17, "After payment, the diamond branches: successful -> Create Order; failed -> Show Error.",
      size=10.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w8_activity_example.png")


# --------------------------------------------------------------------------
# 16. Swimlanes
# --------------------------------------------------------------------------
def swimlanes():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Swimlanes", sub="Who is responsible for each activity?")

    # two swimlanes
    box(ax, 22, 80, 390, 330, WHITE, ec=MAROON, lw=1.6, r=0, z=5)
    box(ax, 430, 80, 390, 330, MAROON_TINT, ec=MAROON, lw=1.6, r=0, z=5)
    box(ax, 22, 380, 390, 30, MAROON, r=0, z=7)
    t(ax, 217, 395, "Student", size=12, color=WHITE, fam=H_B, z=8)
    box(ax, 430, 380, 390, 30, MAROON_DARK, r=0, z=7)
    t(ax, 625, 395, "System", size=12, color=WHITE, fam=H_B, z=8)

    action(ax, 60, 320, 190, 40, "Select course", size=10.5)
    arrow(ax, 250, 340, 480, 340)
    action(ax, 480, 320, 190, 40, "Check prerequisites", size=10.5)
    arrow(ax, 575, 320, 575, 280)
    action(ax, 480, 240, 190, 40, "Check availability", size=10.5)
    arrow(ax, 480, 240, 250, 240)
    action(ax, 60, 200, 190, 40, "Confirm", size=10.5)
    arrow(ax, 250, 220, 480, 220)
    action(ax, 480, 180, 190, 40, "Create registration", size=10.5)
    arrow(ax, 575, 180, 575, 140)
    action(ax, 480, 100, 190, 40, "Display confirmation", size=10.5)

    box(ax, 22, 16, 796, 22, MAROON_DARK, r=10, z=5)
    t(ax, W / 2, 27, "Without swimlanes we may not know who performs what — responsibilities become clearer with them.",
      size=10.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w8_swimlanes.png")


# --------------------------------------------------------------------------
# 17. Traceability
# --------------------------------------------------------------------------
def traceability():
    W, H = 840, 450
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "How the Models Work Together", sub="From requirement to design, with traceability")

    steps = [
        ("REQUIREMENT", "\u201cStudent must register for courses\u201d", MAROON),
        ("USE CASE", "Register Course (UC-05)", MAROON_DARK),
        ("ACTIVITY DIAGRAM", "Registration workflow", MAROON_SOFT),
        ("SEQUENCE DIAGRAM", "Student -> UI -> Controller -> Database", "#8C2B2D"),
        ("DESIGN", "Registration classes / services", MAROON),
        ("TEST CASES", "Successful / failed registration", MAROON_DARK),
    ]
    y = 360
    for name, ex, col in steps:
        box(ax, 230, y, 380, 46, WHITE, ec=col, lw=1.6, r=10, z=6)
        t(ax, 260, y + 23, name, size=11.5, color=col, fam=H_B, ha="left", z=7)
        t(ax, 560, y + 23, ex, size=9.8, color=INK, fam=MONO, ha="left", z=7)
        if y > 60:
            arrow(ax, 420, y, 420, y - 10, color=col, lw=1.8, z=7)
        y -= 56

    box(ax, 22, 16, 796, 22, MAROON_DARK, r=10, z=5)
    t(ax, W / 2, 27, "Each model elaborates the same requirement at a deeper level — that is traceability.",
      size=10.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w8_traceability.png")


ALL = [
    family, questions, use_case_goal, actor_human, use_case_diagram,
    relationships, include_extend, specification, sequence_components,
    sequence_login, fragments, communication, seq_vs_comm, activity_notation,
    activity_example, swimlanes, traceability,
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
    print("Generated", len(made), "week-8 visuals:")
    for m in made:
        print("  -", m)
