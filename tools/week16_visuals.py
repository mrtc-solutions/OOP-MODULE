"""
Week 16 visuals — COMPREHENSIVE REVISION, INTEGRATED CASE STUDY AND EXAMINATION PREPARATION.
Module map · analysis vs design · OO principles · UML families · use cases ·
class notation · relationships · multiplicity · state · sequence vs activity ·
integration · consistency · USDP · iteration · mobile money · exam approach.
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


def diamond(ax, x, y, w, h, fc=WHITE, ec=MAROON, lw=1.8, z=6):
    ax.add_patch(Polygon([(x, y + h / 2), (x + w / 2, y + h), (x + w, y + h / 2),
                          (x + w / 2, y)], closed=True, facecolor=fc,
                         edgecolor=ec, lw=lw, zorder=z))


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


def state(ax, x, y, w, h, label, sub=None, fill=WHITE, ec=MAROON, lw=2.0,
          lab_size=12, sub_size=9.5, z=6):
    box(ax, x, y, w, h, fill, ec=ec, lw=lw, r=12, z=z)
    cy = y + h / 2 + (7 if sub else 0)
    t(ax, x + w / 2, cy, label, size=lab_size, color=MAROON_DARK, fam=B_SB, z=z + 1)
    if sub:
        t(ax, x + w / 2, y + h / 2 - 10, sub, size=sub_size, color=GREY, fam=B_IT, z=z + 1)


def inode(ax, x, y, r=9, z=8):
    ax.add_patch(Circle((x, y), r, facecolor=MAROON, edgecolor=MAROON_DARK, lw=1.0, zorder=z))


def fnode(ax, x, y, r=10, z=8):
    ax.add_patch(Circle((x, y), r, facecolor=WHITE, edgecolor=MAROON, lw=2.0, zorder=z))
    ax.add_patch(Circle((x, y), r - 4, facecolor=MAROON, edgecolor="none", zorder=z))


def actor(ax, x, y, label, scale=1.0, z=8):
    ax.add_patch(Circle((x, y + 46 * scale), 10 * scale, facecolor=WHITE,
                        edgecolor=MAROON, lw=1.8, zorder=z))
    ax.plot([x, x], [y + 36 * scale, y + 14 * scale], color=MAROON, lw=1.8, zorder=z)
    ax.plot([x - 16 * scale, x + 16 * scale], [y + 28 * scale, y + 28 * scale],
            color=MAROON, lw=1.8, zorder=z)
    ax.plot([x, x - 12 * scale], [y + 14 * scale, y], color=MAROON, lw=1.8, zorder=z)
    ax.plot([x, x + 12 * scale], [y + 14 * scale, y], color=MAROON, lw=1.8, zorder=z)
    t(ax, x, y - 16, label, size=11, color=INK, fam=B_SB, z=z)


# --------------------------------------------------------------------------
# 1. Progression Week 15 -> 16
# --------------------------------------------------------------------------
def progression():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Week 15 -> Week 16", sub="The student becomes the analyst / designer")

    box(ax, 22, 110, 380, 216, WHITE, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 212, 300, "WEEK 15", size=13, color=MAROON, fam=H_B, z=6)
    for i, s in enumerate(["Complete case study", "Model integration", "CASE tool implementation"]):
        box(ax, 80, 238 - i * 38, 264, 30, MAROON_TINT, r=8, z=6)
        t(ax, 212, 253 - i * 38, s, size=11, color=INK, fam=BODY, z=7)
    t(ax, 212, 126, "\u201capply everything to a complete system\u201d", size=10, color=GREY, fam=B_IT, z=7)

    box(ax, 438, 110, 380, 216, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 300, "WEEK 16", size=13, color=MAROON_DARK, fam=H_B, z=6)
    for i, s in enumerate(["Comprehensive revision", "Integrated case study", "Examination preparation"]):
        box(ax, 496, 238 - i * 38, 264, 30, WHITE, ec=MAROON, lw=1.3, r=8, z=6)
        t(ax, 628, 253 - i * 38, s, size=10.5, color=MAROON_SOFT, fam=BODY, z=7)
    t(ax, 628, 126, "\u201csolve a new problem independently\u201d", size=10, color=GREY, fam=B_IT, z=7)

    arrow(ax, 406, 220, 434, 220, lw=2.4, ms=16, z=8)
    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Here is a real-world problem. Analyse it and design the system.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w16_progression.png")


# --------------------------------------------------------------------------
# 2. The entire module in one picture
# --------------------------------------------------------------------------
def module_picture():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "The Entire Module in One Picture", sub="Connected stages, not unrelated exam topics")

    box(ax, 260, 400, 320, 34, MAROON, r=10, z=6)
    t(ax, 420, 417, "UNDERSTAND THE PROBLEM -> BUSINESS NEEDS", size=10, color=WHITE, fam=H_SB, z=7)
    arrow(ax, 420, 398, 420, 388, lw=1.6, ms=11, z=8)
    box(ax, 260, 354, 320, 34, MAROON, r=10, z=6)
    t(ax, 420, 371, "REQUIREMENTS -> USE CASES -> OBJECTS", size=10, color=WHITE, fam=H_SB, z=7)
    arrow(ax, 300, 352, 220, 300, lw=1.6, ms=11, z=8)
    arrow(ax, 420, 352, 420, 300, lw=1.6, ms=11, z=8)
    arrow(ax, 540, 352, 620, 300, lw=1.6, ms=11, z=8)
    box(ax, 130, 268, 180, 32, MAROON_TINT, ec=MAROON, lw=1.3, r=10, z=6)
    t(ax, 220, 284, "OBJECT MODEL", size=9.5, color=MAROON_DARK, fam=B_SB, z=7)
    t(ax, 220, 258, "Classes · Relationships", size=8.5, color=GREY, fam=B_IT, z=7)
    box(ax, 330, 268, 180, 32, MAROON_TINT, ec=MAROON, lw=1.3, r=10, z=6)
    t(ax, 420, 284, "DYNAMIC MODEL", size=9.5, color=MAROON_DARK, fam=B_SB, z=7)
    t(ax, 420, 258, "States · Events", size=8.5, color=GREY, fam=B_IT, z=7)
    box(ax, 530, 268, 180, 32, MAROON_TINT, ec=MAROON, lw=1.3, r=10, z=6)
    t(ax, 620, 284, "BEHAVIOUR MODEL", size=9.5, color=MAROON_DARK, fam=B_SB, z=7)
    t(ax, 620, 258, "Interactions · Activities", size=8.5, color=GREY, fam=B_IT, z=7)
    arrow(ax, 420, 266, 420, 256, lw=1.6, ms=11, z=8)
    box(ax, 260, 224, 320, 32, MAROON_SOFT, r=10, z=6)
    t(ax, 420, 240, "ANALYSIS MODEL", size=10, color=WHITE, fam=H_SB, z=7)
    arrow(ax, 420, 222, 420, 212, lw=1.6, ms=11, z=8)
    box(ax, 260, 180, 320, 32, MAROON, r=10, z=6)
    t(ax, 420, 196, "OBJECT-ORIENTED DESIGN", size=10, color=WHITE, fam=H_SB, z=7)
    arrow(ax, 420, 178, 420, 168, lw=1.6, ms=11, z=8)
    box(ax, 260, 136, 320, 32, MAROON_SOFT, r=10, z=6)
    t(ax, 420, 152, "ARCHITECTURE / COMPONENTS", size=10, color=WHITE, fam=H_SB, z=7)
    arrow(ax, 420, 134, 420, 124, lw=1.6, ms=11, z=8)
    box(ax, 260, 92, 320, 32, MAROON, r=10, z=6)
    t(ax, 420, 108, "IMPLEMENTATION", size=10, color=WHITE, fam=H_SB, z=7)

    box(ax, 22, 14, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 27, "Students must be able to reproduce this journey from memory.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w16_module_picture.png")


# --------------------------------------------------------------------------
# 3. Analysis vs design
# --------------------------------------------------------------------------
def analysis_design():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Analysis vs Design", sub="Understand the problem vs construct the solution")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "ANALYSIS  (What?)", size=13, color=MAROON, fam=H_B, z=6)
    for i, s in enumerate(["Understands the problem", "Identifies domain concepts", "\u201cStudents should borrow books\u201d", "Student · Book · Loan"]):
        y = 268 - i * 34
        box(ax, 60, y - 15, 304, 30, MAROON_TINT, r=8, z=6)
        t(ax, 212, y, s, size=10.5, color=INK, fam=BODY, z=7)

    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "DESIGN  (How?)", size=13, color=MAROON_DARK, fam=H_B, z=6)
    for i, s in enumerate(["Defines the software solution", "Refines concepts into structures", "LoanController · LoanService", "BookRepository · NotificationService"]):
        y = 268 - i * 34
        box(ax, 476, y - 15, 304, 30, WHITE, ec=MAROON, lw=1.3, r=8, z=6)
        t(ax, 628, y, s, size=10.5, color=MAROON_SOFT, fam=BODY, z=7)

    arrow(ax, 406, 220, 434, 220, lw=2.6, ms=18, z=8)
    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "That distinction is extremely important in examinations.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w16_analysis_design.png")


# --------------------------------------------------------------------------
# 4. OO principles — object, class, encapsulation, abstraction
# --------------------------------------------------------------------------
def oo_principles():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Core OO Concepts", sub="Object · Class · Encapsulation · Abstraction")

    cards = [
        (22, "OBJECT", "identity + state + behaviour", ["Student #ST1001", "name = John · year = 3", "registerCourse()"]),
        (300, "CLASS", "blueprint / definition", ["Student", "-studentId · -name", "+registerCourse()", "+dropCourse()"]),
        (578, "ENCAPSULATION", "data + operations, controlled access", ["BankAccount", "-balance", "+deposit() · +withdraw()", "+getBalance()"]),
    ]
    for x, hd, sub, items in cards:
        box(ax, x, 96, 240, 246, WHITE, ec=MAROON, lw=1.8, r=14, z=5)
        box(ax, x, 306, 240, 36, MAROON, r=12, z=6)
        t(ax, x + 120, 324, hd, size=11.5, color=WHITE, fam=H_SB, z=7)
        t(ax, x + 120, 274, sub, size=9.5, color=GREY, fam=B_IT, z=7)
        for i, s in enumerate(items):
            y = 232 - i * 34
            box(ax, x + 24, y - 13, 192, 26, MAROON_TINT, r=8, z=6)
            t(ax, x + 120, y, s, size=9.5, color=INK, fam=BODY, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Abstraction: focus on important characteristics; hide unnecessary details.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w16_oo_principles.png")


# --------------------------------------------------------------------------
# 5. Inheritance & polymorphism
# --------------------------------------------------------------------------
def inheritance_polymorphism():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Inheritance & Polymorphism", sub="Is-a relationships and one operation, many behaviours")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "INHERITANCE", size=13, color=MAROON, fam=H_B, z=6)
    uc(ax, 130, 200, 150, "Person", attrs=["-name", "-email"], ops=["+login()"], name_size=10.5)
    gtri(ax, 205, 192, 34, 24, z=8)
    ax.plot([186, 140], [192, 150], color=MAROON, lw=1.8, zorder=7)
    ax.plot([225, 270], [192, 150], color=MAROON, lw=1.8, zorder=7)
    uc(ax, 70, 96, 140, "Student", name_size=10)
    uc(ax, 200, 96, 140, "Lecturer", name_size=10)
    t(ax, 212, 76, "subclasses inherit name, email, login()", size=10, color=GREY, fam=B_IT, z=7)

    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "POLYMORPHISM", size=13, color=MAROON_DARK, fam=H_B, z=6)
    uc(ax, 546, 200, 160, "Employee", ops=["+calculateSalary()"], name_size=10.5)
    gtri(ax, 626, 192, 34, 24, z=8)
    ax.plot([607, 566], [192, 150], color=MAROON, lw=1.8, zorder=7)
    ax.plot([646, 700], [192, 150], color=MAROON, lw=1.8, zorder=7)
    uc(ax, 486, 96, 160, "PermanentEmployee", ops=["+calculateSalary()"], name_size=9.5)
    uc(ax, 630, 96, 160, "ContractEmployee", ops=["+calculateSalary()"], name_size=9.5)
    t(ax, 628, 76, "employee.calculateSalary() behaves differently", size=10, color=GREY, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Generalisation is the UML relationship; inheritance is the implementation mechanism.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w16_inheritance_polymorphism.png")


# --------------------------------------------------------------------------
# 6. UML diagram families
# --------------------------------------------------------------------------
def uml_families():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "UML Diagram Families", sub="Structural · Behavioural · Interaction")

    cards = [
        (22, "STRUCTURAL", "what the system is made of", ["class diagram", "component diagram", "deployment diagram", "package diagram"], MAROON),
        (300, "BEHAVIOURAL", "what the system does", ["use-case diagram", "activity diagram", "state-machine diagram"], MAROON_SOFT),
        (578, "INTERACTION", "communication between parts", ["sequence diagram", "communication / collaboration"], MAROON_DARK),
    ]
    for x, hd, sub, items, colr in cards:
        box(ax, x, 96, 240, 246, WHITE, ec=colr, lw=1.8, r=14, z=5)
        box(ax, x, 306, 240, 36, colr, r=12, z=6)
        t(ax, x + 120, 324, hd, size=11.5, color=WHITE, fam=H_SB, z=7)
        t(ax, x + 120, 276, sub, size=10, color=GREY, fam=B_IT, z=7)
        for i, s in enumerate(items):
            y = 232 - i * 38
            box(ax, x + 24, y - 14, 192, 28, MAROON_TINT, r=8, z=6)
            t(ax, x + 120, y, s, size=9.5, color=INK, fam=BODY, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "UML is a modelling language, not a programming language.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w16_uml_families.png")


# --------------------------------------------------------------------------
# 7. Use-case relations (actor-use case, include, extend)
# --------------------------------------------------------------------------
def use_case_relations():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Actors, Use Cases, Include and Extend", sub="The goal an actor accomplishes")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "ACTOR vs USE CASE", size=12.5, color=MAROON, fam=H_B, z=6)
    actor(ax, 120, 150, "Student", scale=1.0)
    box(ax, 220, 176, 150, 26, MAROON_TINT, ec=MAROON, lw=1.2, r=14, z=6)
    t(ax, 295, 189, "Register Course", size=9.5, color=INK, fam=BODY, z=7)
    arrow(ax, 166, 186, 218, 186, lw=1.6, ms=11, z=8)
    t(ax, 212, 120, "actor = external role · use case = system goal", size=10, color=GREY, fam=B_IT, z=7)

    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "INCLUDE vs EXTEND", size=12.5, color=MAROON_DARK, fam=H_B, z=6)
    box(ax, 486, 230, 140, 30, WHITE, ec=MAROON, lw=1.2, r=14, z=6)
    t(ax, 556, 245, "Register Course", size=9, color=INK, fam=BODY, z=7)
    box(ax, 486, 160, 140, 30, WHITE, ec=MAROON, lw=1.2, r=14, z=6)
    t(ax, 556, 175, "Check Eligibility", size=9, color=INK, fam=BODY, z=7)
    arrow(ax, 556, 228, 556, 194, lw=1.6, ms=11, z=8)
    t(ax, 566, 208, "<<include>> required", size=9, color=MAROON_SOFT, fam=B_IT, z=8, ha="left")
    box(ax, 706, 160, 120, 30, WHITE, ec=MAROON_SOFT, lw=1.2, r=14, z=6)
    t(ax, 766, 175, "Apply Discount", size=8.5, color=MAROON_SOFT, fam=BODY, z=7)
    arrow(ax, 626, 172, 704, 172, lw=1.6, ms=11, z=8)
    t(ax, 668, 188, "<<extend>>", size=9, color=MAROON_SOFT, fam=B_IT, z=8)
    t(ax, 628, 120, "do not use include and extend randomly", size=10, color=GREY, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Include = required behaviour · Extend = optional additional behaviour.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w16_use_case_relations.png")


# --------------------------------------------------------------------------
# 8. Class notation
# --------------------------------------------------------------------------
def class_notation():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Class Diagram Notation", sub="Attributes, operations and visibility")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "A CLASS", size=12.5, color=MAROON, fam=H_B, z=6)
    uc(ax, 120, 128, 184, "Student",
       attrs=["-studentId : String", "-name : String", "-email : String"],
       ops=["+registerCourse()", "+dropCourse()", "+getName() : String"], name_size=11)
    t(ax, 212, 112, "attributes = data · operations = behaviour", size=10, color=GREY, fam=B_IT, z=7)

    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "VISIBILITY", size=12.5, color=MAROON_DARK, fam=H_B, z=6)
    rows = [("+", "public"), ("-", "private"), ("#", "protected"), ("~", "package")]
    for i, (sy, m) in enumerate(rows):
        y = 268 - i * 40
        box(ax, 500, y - 14, 56, 28, MAROON, r=8, z=6)
        t(ax, 528, y, sy, size=13, color=WHITE, fam=MONO, z=7)
        t(ax, 590, y, m, size=11, color=INK, fam=BODY, ha="left", z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "The class diagram describes the static structure of the system.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w16_class_notation.png")


# --------------------------------------------------------------------------
# 9. Relationships
# --------------------------------------------------------------------------
def relationships():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Class Relationships", sub="Association · Aggregation · Composition · Generalisation")

    # association
    box(ax, 60, 300, 120, 34, WHITE, ec=MAROON, lw=1.4, r=8, z=6)
    t(ax, 120, 317, "Student", size=10, color=INK, fam=B_SB, z=7)
    box(ax, 240, 300, 120, 34, WHITE, ec=MAROON, lw=1.4, r=8, z=6)
    t(ax, 300, 317, "Course", size=10, color=INK, fam=B_SB, z=7)
    arrow(ax, 182, 317, 238, 317, lw=1.8, ms=12, z=8)
    t(ax, 60, 288, "ASSOCIATION — a general relationship", size=9, color=GREY, fam=B_IT, ha="left", z=7)

    # aggregation
    box(ax, 60, 200, 120, 34, WHITE, ec=MAROON, lw=1.4, r=8, z=6)
    t(ax, 120, 217, "Department", size=10, color=INK, fam=B_SB, z=7)
    diamond(ax, 206, 206, 26, 22, fc=WHITE, z=8)
    box(ax, 240, 200, 120, 34, WHITE, ec=MAROON, lw=1.4, r=8, z=6)
    t(ax, 300, 217, "Lecturer", size=10, color=INK, fam=B_SB, z=7)
    ax.plot([182, 206], [217, 217], color=MAROON, lw=1.8, zorder=8)
    ax.plot([232, 238], [217, 217], color=MAROON, lw=1.8, zorder=8)
    t(ax, 60, 188, "AGGREGATION — weaker whole-part", size=9, color=GREY, fam=B_IT, ha="left", z=7)

    # composition
    box(ax, 500, 300, 120, 34, WHITE, ec=MAROON, lw=1.4, r=8, z=6)
    t(ax, 560, 317, "House", size=10, color=INK, fam=B_SB, z=7)
    diamond(ax, 646, 306, 26, 22, fc=MAROON, z=8)
    box(ax, 680, 300, 120, 34, WHITE, ec=MAROON, lw=1.4, r=8, z=6)
    t(ax, 740, 317, "Room", size=10, color=INK, fam=B_SB, z=7)
    ax.plot([622, 646], [317, 317], color=MAROON, lw=1.8, zorder=8)
    ax.plot([672, 678], [317, 317], color=MAROON, lw=1.8, zorder=8)
    t(ax, 500, 288, "COMPOSITION — strong ownership", size=9, color=GREY, fam=B_IT, ha="left", z=7)

    # generalisation
    box(ax, 500, 200, 120, 34, WHITE, ec=MAROON, lw=1.4, r=8, z=6)
    t(ax, 560, 217, "Vehicle", size=10, color=INK, fam=B_SB, z=7)
    gtri(ax, 646, 210, 30, 22, z=8)
    ax.plot([630, 600], [210, 160], color=MAROON, lw=1.8, zorder=7)
    ax.plot([662, 690], [210, 160], color=MAROON, lw=1.8, zorder=7)
    box(ax, 540, 126, 100, 30, WHITE, ec=MAROON, lw=1.4, r=8, z=6)
    t(ax, 590, 141, "Car", size=10, color=INK, fam=B_SB, z=7)
    box(ax, 640, 126, 120, 30, WHITE, ec=MAROON, lw=1.4, r=8, z=6)
    t(ax, 700, 141, "Motorcycle", size=10, color=INK, fam=B_SB, z=7)
    t(ax, 500, 112, "GENERALISATION — is-a", size=9, color=GREY, fam=B_IT, ha="left", z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Choose the diamond from the ownership / lifecycle, not because it looks nice.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w16_relationships.png")


# --------------------------------------------------------------------------
# 10. Multiplicity
# --------------------------------------------------------------------------
def multiplicity():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Multiplicity", sub="How many objects can participate")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "EXAMPLE", size=12.5, color=MAROON, fam=H_B, z=6)
    uc(ax, 60, 176, 150, "Student", name_size=10.5)
    uc(ax, 200, 176, 150, "Registration", name_size=10.5)
    arrow(ax, 212, 190, 198, 190, lw=1.8, ms=12, z=8)
    t(ax, 205, 204, "1", size=11, color=MAROON, fam=B_SB, z=8)
    t(ax, 205, 176, "0..*", size=11, color=MAROON_SOFT, fam=B_SB, z=8)
    t(ax, 205, 130, "one student -> zero or many registrations", size=10, color=GREY, fam=B_IT, z=7)

    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "COMMON MULTIPLICITIES", size=12.5, color=MAROON_DARK, fam=H_B, z=6)
    rows = [("1", "exactly one"), ("0..1", "zero or one"), ("*", "many"), ("0..*", "zero or many"), ("1..*", "one or many")]
    for i, (sy, m) in enumerate(rows):
        y = 268 - i * 34
        box(ax, 496, y - 13, 70, 26, MAROON, r=8, z=6)
        t(ax, 531, y, sy, size=11, color=WHITE, fam=MONO, z=7)
        t(ax, 610, y, m, size=11, color=INK, fam=BODY, ha="left", z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Multiplicity is far more meaningful than simply drawing lines between classes.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w16_multiplicity.png")


# --------------------------------------------------------------------------
# 11. State diagram (Course lifecycle)
# --------------------------------------------------------------------------
def state_diagram():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "State Diagram: Course Lifecycle", sub="Events cause transitions between states")

    fnode(ax, 130, 416, r=10)
    state(ax, 90, 360, 120, 40, "Created")
    arrow(ax, 150, 414, 150, 404, lw=1.8, ms=12, z=8)
    state(ax, 90, 250, 120, 40, "Available")
    state(ax, 340, 250, 120, 40, "Full")
    state(ax, 590, 250, 120, 40, "Closed")
    arrow(ax, 150, 358, 150, 294, lw=1.8, ms=12, z=8)
    t(ax, 166, 330, "open registration", size=9, color=GREY, fam=B_IT, z=8, ha="left")
    arrow(ax, 212, 270, 336, 270, lw=1.8, ms=12, z=8)
    t(ax, 274, 286, "last seat taken", size=9, color=GREY, fam=B_IT, z=8)
    arrow(ax, 462, 270, 586, 270, lw=1.8, ms=12, z=8)
    t(ax, 524, 286, "registration closes", size=9, color=GREY, fam=B_IT, z=8)

    box(ax, 22, 130, 796, 44, MAROON_TINT, r=12, z=5)
    t(ax, W / 2, 152, "Event = something that causes change · State = condition at a point · Transition = movement between states.",
      size=11, color=MAROON_DARK, fam=B_SB, z=7)

    box(ax, 22, 18, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 31, "Dynamic modelling asks \u201cwhat happens?\u201d rather than \u201cwhat exists?\u201d",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w16_state_diagram.png")


# --------------------------------------------------------------------------
# 12. Sequence vs activity
# --------------------------------------------------------------------------
def sequence_vs_activity():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Sequence Diagram vs Activity Diagram", sub="A classic examination comparison")

    rows = [
        ("Sequence", "Activity"),
        ("Focuses on interactions", "Focuses on workflow"),
        ("Shows participants / lifelines", "Shows activities and decisions"),
        ("Shows message ordering", "Shows process flow"),
    ]
    x0, w1, w2 = 90, 330, 330
    y_top, rh = 330, 48
    box(ax, x0, y_top - rh - len(rows) * rh - 14, w1 + w2, 14 + rh + len(rows) * rh, WHITE, ec=MAROON, lw=1.6, r=12, z=4)
    for i, (a, b) in enumerate(rows):
        yy = y_top - rh * i - rh / 2
        fc = MAROON if i == 0 else (WHITE if i % 2 else MAROON_TINT)
        box(ax, x0, y_top - rh * i - rh, w1 + w2, rh, fc, r=0, z=5)
        col = WHITE if i == 0 else INK
        t(ax, x0 + w1 / 2, yy, a, size=11.5, color=col, fam=B_SB if i == 0 else BODY, z=6)
        t(ax, x0 + w1 + w2 / 2, yy, b, size=11.5, color=col, fam=B_SB if i == 0 else BODY, z=6)
        if i:
            ax.plot([x0, x0 + w1 + w2], [y_top - rh * i, y_top - rh * i], color=GREY_LIGHT, lw=1.0, zorder=6)
    ax.plot([x0 + w1, x0 + w1], [y_top - rh - len(rows) * rh, y_top - rh], color=GREY_LIGHT, lw=1.0, zorder=6)

    box(ax, 22, 18, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 31, "Sequence = who talks to whom? · Activity = what happens next?",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w16_sequence_vs_activity.png")


# --------------------------------------------------------------------------
# 13. Full model integration chain
# --------------------------------------------------------------------------
def integration_chain():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Full Model Integration", sub="One requirement traced through every model")

    steps = [
        ("REQUIREMENT", "\u201cStudents must be able to register for courses\u201d"),
        ("USE CASE", "Register Course"),
        ("CLASSES", "Student · Course · Registration · RegistrationService"),
        ("SEQUENCE", "Student -> RegistrationService -> Course -> Registration"),
        ("STATE", "Course: Available -> Full"),
        ("ACTIVITY", "Select Course -> Check Eligibility -> Check Capacity -> Register"),
        ("DESIGN", "Presentation -> Application -> Domain -> Persistence"),
    ]
    y = 372
    for i, (hd, sub) in enumerate(steps):
        box(ax, 250, y, 340, 52, MAROON if i % 2 == 0 else MAROON_SOFT, r=12, z=6)
        t(ax, 420, y + 34, hd, size=10.5, color=GOLD_LIGHT, fam=H_SB, z=7)
        t(ax, 420, y + 14, sub, size=9, color=WHITE, fam=BODY, z=7)
        if i < len(steps) - 1:
            arrow(ax, 420, y - 1, 420, y - 9, lw=1.8, ms=12, z=8)
        y -= 60

    box(ax, 22, 14, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 27, "That is integrated OOAD.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w16_integration_chain.png")


# --------------------------------------------------------------------------
# 14. Consistency checks
# --------------------------------------------------------------------------
def consistency():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "UML Model Consistency", sub="Six checks to keep the models agreeing")

    checks = [
        ("1", "Use Cases <-> Requirements", "does every important requirement have a use case?"),
        ("2", "Use Cases <-> Classes", "are there classes that can support the use cases?"),
        ("3", "Sequence <-> Class", "do messages correspond to valid operations?"),
        ("4", "Activity <-> Sequence", "do workflow and interactions tell compatible stories?"),
        ("5", "State <-> Behaviour", "are transitions caused by meaningful events/operations?"),
        ("6", "Design <-> Requirements", "does the final design solve the original problem?"),
    ]
    x0, w = 40, 760
    y_top, rh = 380, 52
    for i, (num, hd, q) in enumerate(checks):
        y = y_top - i * rh - rh
        box(ax, x0, y, w, rh - 6, WHITE if i % 2 == 0 else MAROON_TINT, ec=MAROON, lw=1.3, r=10, z=5)
        box(ax, x0, y + (rh - 6) / 2 - 16, 32, 32, MAROON, r=16, z=6)
        t(ax, x0 + 16, y + (rh - 6) / 2, num, size=12, color=WHITE, fam=H_SB, z=7)
        t(ax, x0 + 52, y + (rh - 6) / 2 + 8, hd, size=11, color=MAROON_DARK, fam=B_SB, ha="left", z=7)
        t(ax, x0 + 52, y + (rh - 6) / 2 - 13, q, size=10, color=GREY, fam=B_IT, ha="left", z=7)

    box(ax, 22, 12, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 25, "checkCapacity() vs checkAvailableSeats() \\u2014 are they the same operation?",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w16_consistency.png")


# --------------------------------------------------------------------------
# 15. USDP phases
# --------------------------------------------------------------------------
def usdp():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "The Unified Process — Four Phases", sub="Iterative and incremental development")

    phases = [
        ("INCEPTION", "\u201cShould we build it?\u201d", ["business problem", "scope", "stakeholders", "feasibility", "business case"]),
        ("ELABORATION", "\u201cHow will we build it?\u201d", ["requirements", "architecture", "risk analysis", "key use cases", "initial design"]),
        ("CONSTRUCTION", "\u201cLet's build it.\u201d", ["implementation", "integration", "testing", "refinement"]),
        ("TRANSITION", "\u201cLet's deliver it.\u201d", ["deployment", "user acceptance", "training", "fixes", "operational use"]),
    ]
    for i, (hd, q, items) in enumerate(phases):
        x = 22 + i * 202
        box(ax, x, 96, 188, 246, WHITE if i % 2 == 0 else MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
        box(ax, x, 306, 188, 36, MAROON, r=12, z=6)
        t(ax, x + 94, 324, hd, size=10.5, color=WHITE, fam=H_SB, z=7)
        t(ax, x + 94, 274, q, size=10, color=MAROON_SOFT, fam=B_IT, z=7)
        for j, it in enumerate(items):
            y = 232 - j * 30
            t(ax, x + 94, y, it, size=9.5, color=INK, fam=BODY, z=7)
        if i < 3:
            arrow(ax, x + 190, 220, x + 200, 220, lw=2.0, ms=14, z=8)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Iterations are planned, measured intervals within the phases.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w16_usdp.png")


# --------------------------------------------------------------------------
# 16. Iterative development
# --------------------------------------------------------------------------
def iterative():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Iterative Development", sub="Build, evaluate, learn, repeat")

    its = [
        ("ITERATION 1", "Requirements + basic design"),
        ("ITERATION 2", "More functionality"),
        ("ITERATION 3", "More functionality"),
        ("ITERATION 4", "Refinement + testing"),
    ]
    for i, (hd, sub) in enumerate(its):
        x = 22 + i * 202
        box(ax, x, 190, 188, 90, MAROON if i % 2 == 0 else MAROON_SOFT, r=12, z=6)
        t(ax, x + 94, 252, hd, size=10.5, color=WHITE, fam=H_SB, z=7)
        t(ax, x + 94, 226, sub, size=9.5, color=GOLD_LIGHT if i % 2 == 0 else WHITE, fam=BODY, z=7)
        arrow(ax, x + 94, 188, x + 94, 168, lw=1.6, ms=11, z=8)
        box(ax, x, 128, 188, 40, MAROON_TINT, ec=MAROON, lw=1.2, r=10, z=6)
        t(ax, x + 94, 148, "FEEDBACK", size=10, color=MAROON_DARK, fam=B_SB, z=7)
        if i < 3:
            arrow(ax, x + 190, 168, x + 200, 236, lw=1.6, ms=11, z=8)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Not \u201cplan everything -> build everything -> test everything\u201d.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w16_iterative.png")


# --------------------------------------------------------------------------
# 17. Mobile money case study
# --------------------------------------------------------------------------
def mobile_money():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Case Study: Mobile Money System", sub="Actors · inheritance · associations · send-money flow")

    actor(ax, 100, 96, "Customer", scale=0.8)
    actor(ax, 250, 96, "Agent", scale=0.8)
    actor(ax, 400, 96, "Administrator", scale=0.8)
    t(ax, 250, 70, "+ Banking System · Notification Service", size=9, color=GREY, fam=B_IT, z=7)

    box(ax, 60, 200, 260, 40, WHITE, ec=MAROON, lw=1.4, r=8, z=6)
    t(ax, 190, 220, "User", size=10.5, color=INK, fam=B_SB, z=7)
    gtri(ax, 190, 192, 30, 22, z=8)
    ax.plot([176, 120], [192, 150], color=MAROON, lw=1.6, zorder=7)
    ax.plot([190, 190], [192, 150], color=MAROON, lw=1.6, zorder=7)
    ax.plot([204, 260], [192, 150], color=MAROON, lw=1.6, zorder=7)
    box(ax, 60, 118, 110, 30, WHITE, ec=MAROON, lw=1.2, r=8, z=6)
    t(ax, 115, 133, "Customer", size=9.5, color=INK, fam=B_SB, z=7)
    box(ax, 140, 118, 110, 30, WHITE, ec=MAROON, lw=1.2, r=8, z=6)
    t(ax, 195, 133, "Agent", size=9.5, color=INK, fam=B_SB, z=7)
    box(ax, 220, 118, 110, 30, WHITE, ec=MAROON, lw=1.2, r=8, z=6)
    t(ax, 275, 133, "Administrator", size=9.5, color=INK, fam=B_SB, z=7)

    box(ax, 460, 236, 130, 34, WHITE, ec=MAROON, lw=1.4, r=8, z=6)
    t(ax, 525, 253, "Customer", size=10, color=INK, fam=B_SB, z=7)
    box(ax, 660, 236, 130, 34, WHITE, ec=MAROON, lw=1.4, r=8, z=6)
    t(ax, 725, 253, "Wallet", size=10, color=INK, fam=B_SB, z=7)
    arrow(ax, 592, 253, 658, 253, lw=1.8, ms=12, z=8)
    t(ax, 625, 266, "1", size=10, color=MAROON, fam=B_SB, z=8)
    t(ax, 625, 240, "1", size=10, color=MAROON_SOFT, fam=B_SB, z=8)
    box(ax, 660, 150, 130, 34, WHITE, ec=MAROON, lw=1.4, r=8, z=6)
    t(ax, 725, 167, "Transaction", size=10, color=INK, fam=B_SB, z=7)
    arrow(ax, 725, 234, 725, 188, lw=1.8, ms=12, z=8)
    t(ax, 738, 210, "0..*", size=10, color=MAROON_SOFT, fam=B_SB, z=8)

    box(ax, 460, 100, 300, 30, MAROON, r=10, z=6)
    t(ax, 610, 115, "SEND MONEY: sendMoney() -> validateSender() -> checkBalance() -> creditReceiver() -> createTransaction() -> sendNotification()", size=8, color=WHITE, fam=MONO, z=7)

    box(ax, 22, 14, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 27, "User <- Customer / Agent / Administrator · Customer 1 -- 1 Wallet · Wallet 1 -- 0..* Transaction.",
      size=10.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w16_mobile_money.png")


# --------------------------------------------------------------------------
# 18. Exam approach (12 steps / noun technique)
# --------------------------------------------------------------------------
def exam_approach():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "How to Approach an Exam Scenario", sub="Never start drawing immediately")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "THE 12 STEPS", size=12.5, color=MAROON, fam=H_B, z=6)
    steps = ["1. Read the problem twice", "2. Underline the nouns", "3. Identify objects/classes", "4. Identify actors",
             "5. Identify actions/goals", "6. Goals -> use cases", "7. Use-case diagram", "8. Class model",
             "9. Choose a scenario", "10. Sequence diagram", "11. Activity/state", "12. Check consistency"]
    for i, st in enumerate(steps):
        r, c = divmod(i, 6)
        y = 268 - r * 26
        x = 48 + c * 175
        t(ax, x, y, st, size=8.8, color=INK, fam=BODY, ha="left", z=7)

    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "NOUN TECHNIQUE", size=12.5, color=MAROON_DARK, fam=H_B, z=6)
    t(ax, 628, 274, "\u201cA patient books an appointment with a doctor.\u201d", size=10, color=GREY, fam=B_IT, z=7)
    t(ax, 628, 236, "NOUNS -> candidates", size=10.5, color=MAROON, fam=B_SB, z=7)
    for i, s in enumerate(["Patient", "Appointment", "Doctor", "Receptionist", "Schedule"]):
        r, c = divmod(i, 3)
        x = 486 + c * 106
        y = 210 - r * 30
        box(ax, x, y - 11, 96, 22, WHITE, ec=MAROON, lw=1.2, r=8, z=6)
        t(ax, x + 48, y, s, size=8.5, color=INK, fam=BODY, z=7)
    t(ax, 628, 138, "VERBS -> use cases", size=10.5, color=MAROON, fam=B_SB, z=7)
    t(ax, 628, 118, "book · manage · access", size=10, color=INK, fam=BODY, z=7)

    box(ax, 22, 16, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 29, "Not every noun becomes a class \\u2014 use judgement, not a mechanical rule.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w16_exam_approach.png")


ALL = [
    progression, module_picture, analysis_design, oo_principles, inheritance_polymorphism,
    uml_families, use_case_relations, class_notation, relationships, multiplicity,
    state_diagram, sequence_vs_activity, integration_chain, consistency, usdp,
    iterative, mobile_money, exam_approach,
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
    print("Generated", len(made), "week-16 visuals:")
    for m in made:
        print("  -", m)
