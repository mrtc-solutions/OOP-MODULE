"""
Week 11 visuals — REFINING THE OBJECT-ORIENTED DESIGN.
Refinement · design classes · attributes/operations · responsibilities ·
cohesion/coupling · interfaces · abstract classes · layering · traceability.
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


# --------------------------------------------------------------------------
# 1. Progression Week 10 -> 11 -> 12
# --------------------------------------------------------------------------
def progression():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Week 10 -> 11 -> 12", sub="From \u201cwhat is design?\u201d to a complete, integrated design")

    cols = [
        ("WEEK 10", "OBJECT-ORIENTED DESIGN", "\u201cWhat is design?\u201d", MAROON),
        ("WEEK 11", "DESIGN REFINEMENT", "\u201cHow do we turn the models into a\ndetailed, implementable design?\u201d", MAROON_SOFT),
        ("WEEK 12", "INTEGRATED OO DESIGN", "\u201cHow do we put everything\ntogether into a complete system?\u201d", MAROON_DARK),
    ]
    for i, (wk, hd, sub, colr) in enumerate(cols):
        x = 30 + i * 268
        box(ax, x, 110, 244, 216, WHITE, ec=colr, lw=1.8, r=14, z=5)
        box(ax, x, 288, 244, 38, colr, r=12, z=6)
        t(ax, x + 122, 307, wk, size=12.5, color=WHITE, fam=H_SB, z=7)
        t(ax, x + 122, 254, hd, size=13, color=MAROON_DARK, fam=H_B, z=7)
        t(ax, x + 122, 190, sub, size=11, color=GREY, fam=B_IT, z=7)
        if i < 2:
            arrow(ax, x + 248, 220, x + 264, 220, lw=2.4, ms=16, z=8)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Week 11 refines the Week 10 models into a design developers can implement, maintain, test and extend.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w11_progression.png")


# --------------------------------------------------------------------------
# 2. Refinement — general to detailed
# --------------------------------------------------------------------------
def refinement():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Design Refinement", sub="Taking something general and making it more detailed and precise")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 212, 312, "GENERAL (analysis)", size=13, color=MAROON, fam=H_B, z=6)
    for i, s in enumerate(["Student", "Course", "Registration"]):
        box(ax, 100, 218 - i * 38, 224, 30, MAROON_TINT, r=8, z=6)
        t(ax, 212, 233 - i * 38, s, size=12, color=INK, fam=BODY, z=7)
    t(ax, 212, 106, "\u201cthere is a Student concept\u201d", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 438, 96, 380, 246, WHITE, ec=MAROON_SOFT, lw=1.8, r=14, z=5)
    t(ax, 628, 312, "DETAILED (design)", size=13, color=MAROON_SOFT, fam=H_B, z=6)
    uc(ax, 546, 124, 164, "Student",
       attrs=["studentId : String", "name : String", "email : String"],
       ops=["registerCourse()", "dropCourse()"], name_size=11)
    t(ax, 628, 112, "how the software represents Student", size=10.5, color=GREY, fam=B_IT, z=7)

    arrow(ax, 406, 220, 434, 220, lw=2.6, ms=18, z=8)
    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "The design model becomes increasingly precise as it moves toward implementation.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w11_refinement.png")


# --------------------------------------------------------------------------
# 3. Analysis class vs design class
# --------------------------------------------------------------------------
def analysis_vs_design_class():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Analysis Class vs Design Class", sub="A key examination distinction")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 212, 312, "ANALYSIS CLASS", size=13.5, color=MAROON, fam=H_B, z=6)
    uc(ax, 130, 150, 164, "Student", name_size=11)
    t(ax, 212, 130, "important domain concept", size=10.5, color=GREY, fam=B_IT, z=7)
    t(ax, 212, 110, "little implementation detail", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 312, "DESIGN CLASS", size=13.5, color=MAROON_DARK, fam=H_B, z=6)
    uc(ax, 536, 106, 184, "Student",
       attrs=["-studentId : String", "-name : String", "-email : String", "-status : StudentStatus"],
       ops=["+registerCourse(c: Course)", "+dropCourse(c: Course)"],
       name_size=11)
    t(ax, 628, 94, "visibility · types · parameters · operations", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "From \u201cthere is a concept\u201d to \u201chere is how the software represents and manipulates it.\u201d",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w11_analysis_vs_design_class.png")


# --------------------------------------------------------------------------
# 4. Entity / Boundary / Control
# --------------------------------------------------------------------------
def entity_boundary_control():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Entity, Boundary & Control Classes", sub="Three roles for thinking about classes")

    cards = [
        (22, "ENTITY", "information important to the domain", ["Student", "Course", "Registration", "Payment"], MAROON),
        (300, "BOUNDARY", "interaction with external actors", ["LoginPage", "RegistrationForm", "StudentDashboard", "PaymentScreen"], MAROON_SOFT),
        (578, "CONTROL", "coordinates use-case logic", ["RegistrationController", "PaymentController", "LoginController"], MAROON_DARK),
    ]
    for x, hd, sub, items, colr in cards:
        box(ax, x, 96, 240, 246, WHITE, ec=colr, lw=1.8, r=14, z=5)
        box(ax, x, 306, 240, 36, colr, r=12, z=6)
        t(ax, x + 120, 324, hd, size=13, color=WHITE, fam=H_SB, z=7)
        t(ax, x + 120, 278, sub, size=10, color=GREY, fam=B_IT, z=7)
        for i, s in enumerate(items):
            y = 224 - i * 30
            box(ax, x + 30, y - 12, 180, 24, MAROON_TINT, r=8, z=6)
            t(ax, x + 120, y, s, size=10.5, color=INK, fam=BODY, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Student -> RegistrationPage -> RegistrationController -> Registration -> Course.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w11_entity_boundary_control.png")


# --------------------------------------------------------------------------
# 5. Refining attributes
# --------------------------------------------------------------------------
def attributes():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Refining Attributes", sub="From plain names to typed data")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 212, 312, "ANALYSIS", size=13, color=MAROON, fam=H_B, z=6)
    uc(ax, 130, 150, 164, "Student", attrs=["studentId", "name", "email", "programme"], name_size=11)

    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 312, "DESIGN", size=13, color=MAROON_DARK, fam=H_B, z=6)
    uc(ax, 536, 150, 184, "Student",
       attrs=["studentId : String", "name : String", "email : String", "programme : String"],
       name_size=11)
    t(ax, 628, 128, "ask: what does the object", size=10.5, color=GREY, fam=B_IT, z=7)
    t(ax, 628, 110, "need to fulfil its responsibilities?", size=10.5, color=GREY, fam=B_IT, z=7)

    arrow(ax, 406, 220, 434, 220, lw=2.6, ms=18, z=8)
    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "An attribute is information maintained by an object — design specifies its type.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w11_attributes.png")


# --------------------------------------------------------------------------
# 6. Refining operations
# --------------------------------------------------------------------------
def operations():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Refining Operations", sub="Operation signatures communicate much more")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 212, 312, "GENERAL", size=13, color=MAROON, fam=H_B, z=6)
    uc(ax, 130, 170, 164, "Student", ops=["registerCourse()", "dropCourse()"], name_size=11)

    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 312, "PRECISE", size=13, color=MAROON_DARK, fam=H_B, z=6)
    uc(ax, 536, 150, 184, "Student", ops=["registerCourse(course: Course): Registration"], name_size=11)
    t(ax, 628, 130, "name = registerCourse", size=10.5, color=INK, fam=BODY, z=7)
    t(ax, 628, 112, "input = Course · return = Registration", size=10.5, color=INK, fam=BODY, z=7)

    arrow(ax, 406, 220, 434, 220, lw=2.6, ms=18, z=8)
    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "registerCourse(course: Course): Registration tells the developer exactly what to build.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w11_operations.png")


# --------------------------------------------------------------------------
# 7. Responsibility assignment
# --------------------------------------------------------------------------
def responsibility():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Responsibility-Driven Design", sub="Which object should perform this operation?")

    box(ax, 22, 110, 360, 230, WHITE, ec=MAROON_SOFT, lw=1.8, r=14, z=5)
    t(ax, 202, 312, "LESS LOGICAL", size=12.5, color=MAROON_SOFT, fam=H_B, z=6)
    uc(ax, 100, 150, 204, "Student", ops=["checkCourseAvailability()"], ec=MAROON_SOFT, name_size=11)
    t(ax, 202, 130, "availability is not the student's concern", size=10, color=GREY, fam=B_IT, z=7)

    box(ax, 458, 110, 360, 230, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 638, 312, "MORE LOGICAL", size=12.5, color=MAROON, fam=H_B, z=6)
    uc(ax, 526, 150, 224, "Course",
       attrs=["capacity", "currentEnrollment"],
       ops=["hasAvailableSpace()"], name_size=11)
    t(ax, 638, 130, "availability is a property of the course", size=10, color=GREY, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Assign each responsibility to the object that naturally owns the relevant information.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w11_responsibility.png")


# --------------------------------------------------------------------------
# 8. Cohesion
# --------------------------------------------------------------------------
def cohesion():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Cohesion", sub="How closely related are the responsibilities inside a class?")

    box(ax, 22, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "HIGH COHESION  (good)", size=13.5, color=MAROON, fam=H_B, z=6)
    uc(ax, 120, 118, 184, "Course", attrs=["courseCode", "title", "capacity", "credits"], ops=["hasSpace()", "addStudent()", "removeStudent()"], name_size=11)
    t(ax, 212, 106, "everything is about the course", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 438, 96, 380, 246, WHITE, ec=MAROON_SOFT, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "LOW COHESION  (bad)", size=13.5, color=MAROON_SOFT, fam=H_B, z=6)
    uc(ax, 536, 118, 184, "Course", attrs=["courseCode", "title"], ops=["registerStudent()", "sendEmail()", "calculateSalary()", "generatePDF()", "compressImage()"], ec=MAROON_SOFT, name_size=11)
    t(ax, 628, 106, "salary in a Course? unrelated", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Good design generally aims for high cohesion.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w11_cohesion.png")


# --------------------------------------------------------------------------
# 9. Coupling — high vs low (interfaces)
# --------------------------------------------------------------------------
def coupling():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Coupling", sub="Reduce dependency with abstractions")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON_SOFT, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "HIGH COUPLING  (bad)", size=13, color=MAROON_SOFT, fam=H_B, z=6)
    chain = ["Student", "Payment", "Database", "Email", "SMS", "Reports"]
    for i, n in enumerate(chain):
        x = 70 + i * 60
        box(ax, x, 150, 52, 34, MAROON_SOFT, r=7, z=6)
        t(ax, x + 26, 167, n, size=8.5, color=WHITE, fam=B_SB, z=7)
        if i < len(chain) - 1:
            arrow(ax, x + 53, 167, x + 69, 167, color=MAROON_SOFT, lw=1.8, ms=12, z=8)
    t(ax, 212, 118, "changing the database breaks everything", size=10, color=GREY, fam=B_IT, z=7)

    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "LOW COUPLING  (good)", size=13, color=MAROON, fam=H_B, z=6)
    box(ax, 500, 210, 110, 40, MAROON, r=8, z=6)
    t(ax, 555, 230, "PaymentService", size=10, color=WHITE, fam=B_SB, z=7)
    box(ax, 660, 210, 110, 40, WHITE, ec=MAROON, lw=1.5, r=8, z=6)
    t(ax, 715, 230, "PaymentGateway", size=10, color=MAROON, fam=B_SB, z=7)
    arrow(ax, 612, 230, 658, 230, lw=2.0, ms=14, z=8)
    box(ax, 580, 140, 110, 30, WHITE, ec=MAROON, lw=1.4, r=8, z=6)
    t(ax, 635, 155, "<<interface>>", size=9.5, color=MAROON, fam=B_SB, z=7)
    arrow(ax, 635, 208, 635, 174, lw=1.8, ms=12, z=8)
    box(ax, 470, 92, 110, 28, WHITE, ec=MAROON, lw=1.3, r=8, z=6)
    t(ax, 525, 106, "Bank", size=9.5, color=INK, fam=BODY, z=7)
    box(ax, 690, 92, 110, 28, WHITE, ec=MAROON, lw=1.3, r=8, z=6)
    t(ax, 745, 106, "MobileMoney", size=9.5, color=INK, fam=BODY, z=7)
    arrow(ax, 525, 138, 528, 124, lw=1.5, ms=10, z=8)
    arrow(ax, 745, 138, 742, 124, lw=1.5, ms=10, z=8)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "The service depends on the abstraction, not on each concrete implementation.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w11_coupling.png")


# --------------------------------------------------------------------------
# 10. Interface — contract + wall socket
# --------------------------------------------------------------------------
def interface():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Interfaces", sub="A contract: \u201cany class implementing me must provide these operations\u201d")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "THE CONTRACT", size=13, color=MAROON, fam=H_B, z=6)
    uc(ax, 118, 140, 188, "<<interface>>\nPaymentGateway",
       ops=["processPayment()", "refundPayment()"], name_size=11)
    box(ax, 60, 104, 304, 26, MAROON_TINT, r=8, z=6)
    t(ax, 212, 117, "BankGateway and MobileGateway both implement it", size=10, color=MAROON_DARK, fam=B_SB, z=7)

    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "WALL-SOCKET ANALOGY", size=13, color=MAROON_DARK, fam=H_B, z=6)
    t(ax, 628, 268, "Your charger doesn't care whether the electricity", size=11, color=INK, fam=BODY, z=7)
    t(ax, 628, 246, "came from hydro, solar, thermal or wind.", size=11, color=INK, fam=BODY, z=7)
    t(ax, 628, 210, "It cares about the interface (the socket).", size=11.5, color=MAROON_SOFT, fam=B_SB, z=7)
    t(ax, 628, 168, "Application  ->  PaymentGateway", size=11, color=INK, fam=BODY, z=7)
    t(ax, 628, 138, "the app need not know the concrete provider", size=10, color=GREY, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Interfaces let the rest of the system communicate with a common contract.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w11_interface.png")


# --------------------------------------------------------------------------
# 11. Abstract class vs interface — table
# --------------------------------------------------------------------------
def abstract_vs_interface():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Abstract Class vs Interface", sub="A comparison students must understand clearly")

    rows = [
        ("Shared implementation", "Can provide shared implementation", "Primarily defines a contract"),
        ("State", "Can contain state", "Typically focuses on required operations"),
        ("Represents", "A common base abstraction", "A capability / contract"),
        ("Relationship", "Subclasses inherit from it", "Classes implement it"),
        ("Use when", "Classes share substantial behaviour", "Different classes must conform to the same contract"),
    ]
    x0, w1, w2, w3 = 30, 168, 308, 294
    y_top, rh = 330, 46
    box(ax, x0, y_top - rh - len(rows) * rh - 16, w1 + w2 + w3, 16 + rh + len(rows) * rh, WHITE, ec=MAROON, lw=1.6, r=12, z=4)
    box(ax, x0, y_top - rh, w1 + w2 + w3, rh, MAROON, r=0, z=5)
    t(ax, x0 + w1 / 2, y_top - rh / 2, "", size=11, color=WHITE, fam=H_SB, z=6)
    t(ax, x0 + w1 + w2 / 2, y_top - rh / 2, "ABSTRACT CLASS", size=12, color=WHITE, fam=H_SB, z=6)
    t(ax, x0 + w1 + w2 + w3 / 2, y_top - rh / 2, "INTERFACE", size=12, color=WHITE, fam=H_SB, z=6)
    for i, (k, a, dd) in enumerate(rows):
        yy = y_top - rh * (i + 1) - rh / 2
        fc = WHITE if i % 2 == 0 else MAROON_TINT
        box(ax, x0, y_top - rh * (i + 1) - rh, w1 + w2 + w3, rh, fc, r=0, z=5)
        t(ax, x0 + w1 / 2, yy, k, size=10.5, color=MAROON, fam=B_SB, z=6)
        t(ax, x0 + w1 + w2 / 2, yy, a, size=10.5, color=INK, fam=BODY, z=6)
        t(ax, x0 + w1 + w2 + w3 / 2, yy, dd, size=10.5, color=MAROON_SOFT, fam=BODY, z=6)
        ax.plot([x0, x0 + w1 + w2 + w3], [y_top - rh * (i + 1), y_top - rh * (i + 1)], color=GREY_LIGHT, lw=1.0, zorder=6)
    ax.plot([x0 + w1, x0 + w1], [y_top - rh, y_top - rh - len(rows) * rh], color=GREY_LIGHT, lw=1.0, zorder=6)
    ax.plot([x0 + w1 + w2, x0 + w1 + w2], [y_top - rh, y_top - rh - len(rows) * rh], color=GREY_LIGHT, lw=1.0, zorder=6)

    box(ax, 22, 18, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 31, "Exact possibilities depend on the language — do not assume Java, C# and C++ behave identically.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w11_abstract_vs_interface.png")


# --------------------------------------------------------------------------
# 12. Association vs inheritance
# --------------------------------------------------------------------------
def association_inheritance():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Association vs Inheritance", sub="HAS / USES / INTERACTS WITH vs IS-A")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "ASSOCIATION", size=14, color=MAROON, fam=H_B, z=6)
    t(ax, 212, 276, "\u201cHAS / USES / INTERACTS WITH\u201d", size=11.5, color=MAROON_SOFT, fam=B_SB, z=7)
    box(ax, 96, 160, 104, 44, MAROON_TINT, ec=MAROON, lw=1.5, r=8, z=6)
    t(ax, 148, 182, "Student", size=11, color=MAROON_DARK, fam=B_SB, z=7)
    box(ax, 240, 160, 104, 44, MAROON_TINT, ec=MAROON, lw=1.5, r=8, z=6)
    t(ax, 292, 182, "Course", size=11, color=MAROON_DARK, fam=B_SB, z=7)
    ax.plot([202, 238], [182, 182], color=MAROON, lw=1.8, zorder=8)
    t(ax, 212, 130, "Student TAKES Course", size=11, color=GREY, fam=B_IT, z=7)

    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "INHERITANCE", size=14, color=MAROON_DARK, fam=H_B, z=6)
    t(ax, 628, 276, "\u201cIS-A\u201d", size=11.5, color=MAROON_SOFT, fam=B_SB, z=7)
    box(ax, 560, 190, 104, 44, WHITE, ec=MAROON, lw=1.5, r=8, z=6)
    t(ax, 612, 212, "Person", size=11, color=MAROON_DARK, fam=B_SB, z=7)
    box(ax, 560, 118, 104, 44, WHITE, ec=MAROON, lw=1.5, r=8, z=6)
    t(ax, 612, 140, "Student", size=11, color=MAROON_DARK, fam=B_SB, z=7)
    gtri(ax, 612, 170, 34, 24, z=8)
    t(ax, 660, 128, "Student IS-A Person", size=11, color=GREY, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Ask: \u201cIs B genuinely a kind of A?\u201d — a Student is NOT a kind of Course.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w11_association_inheritance.png")


# --------------------------------------------------------------------------
# 13. Encapsulation — BankAccount
# --------------------------------------------------------------------------
def encapsulation():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Encapsulation & Information Hiding", sub="The class controls how its state changes")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "PROTECTED STATE", size=13, color=MAROON, fam=H_B, z=6)
    uc(ax, 130, 128, 164, "BankAccount",
       attrs=["-balance : Decimal"],
       ops=["+deposit()", "+withdraw()", "+getBalance()"], name_size=11)
    t(ax, 212, 112, "\u201c-\u201d = private visibility in UML", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "RULES ARE ENFORCED", size=13, color=MAROON_DARK, fam=H_B, z=6)
    t(ax, 628, 268, "account.withdraw(500)", size=12.5, color=MAROON_SOFT, fam=MONO, z=7)
    t(ax, 628, 236, "allows the object to enforce rules:", size=11, color=INK, fam=BODY, z=7)
    box(ax, 478, 180, 300, 40, WHITE, ec=MAROON, lw=1.3, r=8, z=6)
    t(ax, 628, 200, "if balance < 500:  reject withdrawal", size=11, color=INK, fam=MONO, z=7)
    box(ax, 478, 122, 300, 40, WHITE, ec=MAROON_SOFT, lw=1.3, r=8, z=6)
    t(ax, 628, 142, "account.balance = -500000   (blocked)", size=11, color=MAROON_SOFT, fam=MONO, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Encapsulation lets the class control how its state changes — and protect itself.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w11_encapsulation.png")


# --------------------------------------------------------------------------
# 14. Dependency + injection
# --------------------------------------------------------------------------
def dependency():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Dependencies & Dependency Injection", sub="Reduce coupling by providing the dependency")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON_SOFT, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "CREATES ITS OWN DEPENDENCY", size=12.5, color=MAROON_SOFT, fam=H_B, z=6)
    box(ax, 100, 210, 150, 44, MAROON_SOFT, r=8, z=6)
    t(ax, 175, 232, "RegistrationService", size=10.5, color=WHITE, fam=B_SB, z=7)
    box(ax, 100, 130, 150, 44, MAROON_SOFT, r=8, z=6)
    t(ax, 175, 152, "CourseRepository", size=10.5, color=WHITE, fam=B_SB, z=7)
    arrow(ax, 175, 208, 175, 178, lw=2.0, ms=13, z=8)
    t(ax, 175, 106, "strong coupling", size=10, color=GREY, fam=B_IT, z=7)

    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "DEPENDENCY IS PROVIDED", size=12.5, color=MAROON, fam=H_B, z=6)
    box(ax, 540, 210, 150, 44, MAROON, r=8, z=6)
    t(ax, 615, 232, "CourseRepository", size=10.5, color=WHITE, fam=B_SB, z=7)
    box(ax, 540, 130, 150, 44, MAROON, r=8, z=6)
    t(ax, 615, 152, "RegistrationService", size=10.5, color=WHITE, fam=B_SB, z=7)
    arrow(ax, 615, 178, 615, 208, lw=2.0, ms=13, z=8)
    t(ax, 615, 106, "RegistrationService(repository)", size=10.5, color=MAROON_DARK, fam=MONO, z=7)
    t(ax, 615, 82, "testability · flexibility · substitution", size=10, color=GREY, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "The service no longer has to construct the repository itself.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w11_dependency.png")


# --------------------------------------------------------------------------
# 15. Layered design
# --------------------------------------------------------------------------
def layers():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Layered Design", sub="Divide the system into logical levels")

    layers = [
        ("PRESENTATION LAYER", "Web / Mobile / Desktop", MAROON),
        ("APPLICATION / SERVICE LAYER", "use-case coordination", MAROON_SOFT),
        ("DOMAIN LAYER", "Student · Course · Registration", MAROON_SOFT),
        ("DATA ACCESS LAYER", "repositories / persistence", MAROON_DARK),
        ("DATABASE", "persistent storage", MAROON_DEEP),
    ]
    y = 52
    for i, (hd, sub, colr) in enumerate(layers):
        box(ax, 60, y, 720, 58, colr, r=12, z=6)
        t(ax, 420, y + 40, hd, size=13, color=WHITE, fam=H_SB, z=7)
        t(ax, 420, y + 17, sub, size=11, color=GOLD_LIGHT, fam=B_IT, z=7)
        if i < len(layers) - 1:
            arrow(ax, 420, y - 2, 420, y - 12, lw=2.2, ms=14, z=8)
        y += 70

    box(ax, 22, 16, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 29, "If the web UI becomes a mobile app, the business rules can remain usable.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w11_layers.png")


# --------------------------------------------------------------------------
# 16. Reuse — authentication component
# --------------------------------------------------------------------------
def reuse():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Design for Reuse", sub="One reusable authentication service for many applications")

    portals = ["Student Portal", "Staff Portal", "Mobile App", "Library System"]
    for i, name in enumerate(portals):
        x = 40 + i * 196
        box(ax, x, 220, 176, 56, WHITE, ec=MAROON, lw=1.6, r=10, z=6)
        t(ax, x + 88, 248, name, size=11.5, color=MAROON, fam=B_SB, z=7)
        arrow(ax, x + 88, 218, 420, 176, lw=1.8, ms=11, z=8)

    box(ax, 300, 110, 240, 56, MAROON, r=12, z=6)
    t(ax, 420, 152, "AUTHENTICATION SERVICE", size=12, color=WHITE, fam=H_SB, z=7)
    t(ax, 420, 128, "reusable component", size=10, color=GOLD_LIGHT, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Instead of implementing authentication four times, provide one reusable component.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w11_reuse.png")


# --------------------------------------------------------------------------
# 17. Traceability — R01
# --------------------------------------------------------------------------
def traceability():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Design Traceability", sub="Follow requirement R01 through models, code and test")

    chain = [
        ("R01", "students can register for courses"),
        ("Use Case", "Register Course"),
        ("Activity", "registration workflow"),
        ("Sequence", "object interaction"),
        ("Class Model", "Student · Course · Registration"),
        ("Design", "RegistrationService"),
        ("Code", "registerCourse()"),
        ("Test", "automated test"),
    ]
    cw, gap, x0 = 190, 12, 22
    for i, (hd, sub) in enumerate(chain):
        r, c = divmod(i, 4)
        x = x0 + c * (cw + gap)
        y = 268 - r * 132
        colr = MAROON if r == 0 else MAROON_SOFT
        box(ax, x, y, cw, 76, WHITE if r == 0 else MAROON_TINT, ec=colr, lw=1.6, r=12, z=5)
        t(ax, x + cw / 2, y + 52, hd, size=11.5, color=colr, fam=B_SB, z=6)
        t(ax, x + cw / 2, y + 22, sub, size=9, color=GREY, fam=B_IT, z=6)
        if i < len(chain) - 1:
            if c < 3:
                arrow(ax, x + cw + 2, y + 38, x + cw + gap - 2, y + 38, lw=2.0, ms=12, z=8)
            else:
                arrow(ax, x + cw / 2, y - 2, x + cw / 2, y - 12, lw=2.0, ms=12, z=8)

    box(ax, 22, 16, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 29, "\u201cWhere is Requirement R01 implemented?\u201d — traceability answers this.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w11_traceability.png")


# --------------------------------------------------------------------------
# 18. Integrated case study — architecture
# --------------------------------------------------------------------------
def case_study():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Integrated Case Study", sub="Online course registration — seven steps to a complete design")

    steps = [
        ("1", "Use Case", "Student registers"),
        ("2", "Classes", "Student · Course · Registration"),
        ("3", "Class Design", "attributes + operations"),
        ("4", "Service", "RegistrationService"),
        ("5", "Sequence", "register -> hasSpace -> create"),
        ("6", "State", "Requested -> Validated -> Confirmed"),
        ("7", "Architecture", "layers"),
    ]
    for i, (n, hd, sub) in enumerate(steps):
        r = i // 4
        c = i % 4
        if r == 0:
            x, y, bw = 22 + c * 200, 210, 186
        else:
            x, y, bw = 122 + c * 200, 96, 186
        box(ax, x, y, bw, 82, WHITE if r == 0 else MAROON_TINT, ec=MAROON, lw=1.6, r=12, z=5)
        ax.add_patch(Circle((x + 24, y + 58), 14, facecolor=MAROON, zorder=6))
        t(ax, x + 24, y + 58, n, size=11, color=WHITE, fam=H_SB, z=7)
        t(ax, x + bw / 2 + 10, y + 58, hd, size=11.5, color=MAROON, fam=B_SB, z=7)
        t(ax, x + bw / 2, y + 26, sub, size=9, color=GREY, fam=B_IT, z=7)
    arrow(ax, 320, 210, 338, 210, lw=2.0, ms=13, z=8)
    arrow(ax, 520, 210, 538, 210, lw=2.0, ms=13, z=8)
    arrow(ax, 720, 210, 738, 210, lw=2.0, ms=13, z=8)
    arrow(ax, 330, 192, 330, 174, lw=2.0, ms=13, z=8)
    arrow(ax, 520, 192, 520, 174, lw=2.0, ms=13, z=8)

    box(ax, 22, 16, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 29, "Behavioural model + object model + design model working together.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w11_case_study.png")


ALL = [
    progression, refinement, analysis_vs_design_class, entity_boundary_control,
    attributes, operations, responsibility, cohesion, coupling, interface,
    abstract_vs_interface, association_inheritance, encapsulation, dependency,
    layers, reuse, traceability, case_study,
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
    print("Generated", len(made), "week-11 visuals:")
    for m in made:
        print("  -", m)
