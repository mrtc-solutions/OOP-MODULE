"""
Week 15 visuals — COMPLETE OOAD CASE STUDY, MODEL INTEGRATION AND CASE TOOL IMPLEMENTATION.
OOAD journey · consistency · requirements · actors · use cases · classes ·
associations · inheritance · sequence · state · activity · components · traceability.
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


def diamond(ax, x, y, w, h, fc=WHITE, ec=MAROON, lw=1.6, z=6):
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
    """Simple UML stick-figure actor."""
    ax.add_patch(Circle((x, y + 46 * scale), 10 * scale, facecolor=WHITE,
                        edgecolor=MAROON, lw=1.8, zorder=z))
    ax.plot([x, x], [y + 36 * scale, y + 14 * scale], color=MAROON, lw=1.8, zorder=z)
    ax.plot([x - 16 * scale, x + 16 * scale], [y + 28 * scale, y + 28 * scale],
            color=MAROON, lw=1.8, zorder=z)
    ax.plot([x, x - 12 * scale], [y + 14 * scale, y], color=MAROON, lw=1.8, zorder=z)
    ax.plot([x, x + 12 * scale], [y + 14 * scale, y], color=MAROON, lw=1.8, zorder=z)
    t(ax, x, y - 16, label, size=11, color=INK, fam=B_SB, z=z)


# --------------------------------------------------------------------------
# 1. Progression Week 14 -> 15
# --------------------------------------------------------------------------
def progression():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Week 14 -> Week 15", sub="From understanding to a complete application")

    box(ax, 22, 110, 380, 216, WHITE, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 212, 300, "WEEK 14", size=13, color=MAROON, fam=H_B, z=6)
    for i, s in enumerate(["Understanding", "Integration", "Object + Dynamic + Behavioural"]):
        box(ax, 80, 238 - i * 38, 264, 30, MAROON_TINT, r=8, z=6)
        t(ax, 212, 253 - i * 38, s, size=11, color=INK, fam=BODY, z=7)
    t(ax, 212, 126, "\u201chow to combine the models\u201d", size=10, color=GREY, fam=B_IT, z=7)

    box(ax, 438, 110, 380, 216, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 300, "WEEK 15", size=13, color=MAROON_DARK, fam=H_B, z=6)
    for i, s in enumerate(["Complete case study", "Requirements -> Design", "CASE tool implementation"]):
        box(ax, 496, 238 - i * 38, 264, 30, WHITE, ec=MAROON, lw=1.3, r=8, z=6)
        t(ax, 628, 253 - i * 38, s, size=10.5, color=MAROON_SOFT, fam=BODY, z=7)
    t(ax, 628, 126, "\u201ccan you actually do it on a real system?\u201d", size=10, color=GREY, fam=B_IT, z=7)

    arrow(ax, 406, 220, 434, 220, lw=2.4, ms=16, z=8)
    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Week 15 applies everything from Weeks 1-14 to one complete system.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w15_progression.png")


# --------------------------------------------------------------------------
# 2. The OOAD journey
# --------------------------------------------------------------------------
def process():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "The OOAD Journey", sub="Business problem -> implementation (the whole module)")

    steps = ["BUSINESS PROBLEM", "REQUIREMENTS", "USE CASES", "OBJECT IDENTIFICATION",
             "CLASS MODEL", "DYNAMIC MODEL", "BEHAVIOURAL MODEL", "ANALYSIS DOCUMENTATION",
             "DESIGN", "ARCHITECTURE / COMPONENTS", "INTEGRATED DESIGN", "IMPLEMENTATION"]
    y = 372
    for i, name in enumerate(steps):
        box(ax, 250, y, 340, 34, MAROON if i % 2 == 0 else MAROON_SOFT, r=10, z=6)
        t(ax, 420, y + 17, name, size=10.5, color=WHITE, fam=H_SB, z=7)
        if i < len(steps) - 1:
            arrow(ax, 420, y - 1, 420, y - 9, lw=1.8, ms=12, z=8)
        y -= 42

    box(ax, 22, 16, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 29, "The most important word for this journey: INTEGRATION.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w15_process.png")


# --------------------------------------------------------------------------
# 3. Why integration matters (consistency problems)
# --------------------------------------------------------------------------
def consistency():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Why Integration Matters", sub="Three ways a model can become inconsistent")

    cards = [
        (22, "MISSING CLASS", "\u201cStudent -> Register Course\u201d", "but no Registration class", "the models are incomplete"),
        (300, "NAME MISMATCH", "class: checkCapacity()", "sequence: verifySeats()", "a consistency problem"),
        (578, "MISSING PIECE", "activity: \u201cCheck payment\u201d", "no payment class anywhere", "something is missing"),
    ]
    for x, hd, a, b, c in cards:
        box(ax, x, 96, 240, 246, WHITE, ec=MAROON_SOFT, lw=1.8, r=14, z=5)
        box(ax, x, 306, 240, 36, MAROON_SOFT, r=12, z=6)
        t(ax, x + 120, 324, hd, size=11.5, color=WHITE, fam=H_SB, z=7)
        t(ax, x + 120, 264, a, size=10.5, color=INK, fam=B_SB, z=7)
        t(ax, x + 120, 236, b, size=10.5, color=INK, fam=B_SB, z=7)
        arrow(ax, x + 120, 208, x + 120, 196, lw=1.8, ms=12, z=8)
        box(ax, x + 20, 140, 200, 56, MAROON_TINT, r=10, z=6)
        t(ax, x + 120, 168, c, size=11, color=MAROON_DARK, fam=B_SB, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "A good OOAD model must be internally consistent.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w15_consistency.png")


# --------------------------------------------------------------------------
# 4. Business problem -> goal
# --------------------------------------------------------------------------
def business_problem():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "The Business Problem", sub="University course registration \u2014 today's pain")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON_SOFT, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "CURRENT PROBLEMS", size=12.5, color=MAROON_SOFT, fam=H_B, z=6)
    problems = ["long registration queues", "lost registration forms", "duplicate registrations",
                "prerequisites ignored", "courses exceed capacity", "slow confirmation", "poor reports"]
    for i, s in enumerate(problems):
        y = 282 - i * 28
        box(ax, 60, y - 12, 304, 24, MAROON_TINT, r=7, z=6)
        t(ax, 212, y, s, size=10, color=INK, fam=BODY, z=7)

    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "BUSINESS GOAL", size=12.5, color=MAROON_DARK, fam=H_B, z=6)
    t(ax, 628, 268, "Students: search, check eligibility,", size=11, color=INK, fam=BODY, z=7)
    t(ax, 628, 244, "register, receive confirmation", size=11, color=INK, fam=BODY, z=7)
    t(ax, 628, 216, "electronically.", size=11, color=INK, fam=BODY, z=7)
    box(ax, 476, 120, 304, 68, WHITE, ec=MAROON, lw=1.4, r=10, z=6)
    t(ax, 628, 170, "Administrators:", size=10.5, color=MAROON, fam=B_SB, z=7)
    t(ax, 628, 146, "create / modify courses · set capacity", size=10, color=INK, fam=BODY, z=7)
    t(ax, 628, 128, "view registrations · close · report", size=10, color=INK, fam=BODY, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "The university wants students to register online instead of using paper forms.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w15_business_problem.png")


# --------------------------------------------------------------------------
# 5. Requirements
# --------------------------------------------------------------------------
def requirements():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Functional vs Non-Functional Requirements", sub="What the system does vs how well it operates")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "FUNCTIONAL (FR)", size=12.5, color=MAROON, fam=H_B, z=6)
    fr = ["FR1 login", "FR2 view courses", "FR3 search courses", "FR4 check eligibility",
          "FR5 register", "FR6 prevent duplicates", "FR7 check capacity", "FR8 drop course",
          "FR9 confirmation", "FR10 administration"]
    for i, s in enumerate(fr):
        y = 288 - i * 21
        t(ax, 212, y, s, size=9.5, color=INK, fam=BODY, z=7)

    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "NON-FUNCTIONAL (NFR)", size=12.5, color=MAROON_DARK, fam=H_B, z=6)
    nfr = [("Security", "only authorised access"),
           ("Performance", "respond within acceptable time"),
           ("Availability", "available during registration"),
           ("Usability", "no extensive training needed"),
           ("Maintainability", "future changes without rewrite")]
    for i, (hd, sub) in enumerate(nfr):
        y = 280 - i * 38
        box(ax, 480, y - 14, 296, 30, WHITE, ec=MAROON, lw=1.2, r=8, z=6)
        t(ax, 628, y, hd + ": " + sub, size=9.5, color=INK, fam=BODY, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "FR describes functionality; NFR describes quality of service.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w15_requirements.png")


# --------------------------------------------------------------------------
# 6. Actors
# --------------------------------------------------------------------------
def actors():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Actors in the System", sub="An actor is an external role \u2014 human or system")

    box(ax, 320, 120, 200, 180, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 420, 268, "UNIVERSITY", size=13, color=MAROON_DARK, fam=H_B, z=6)
    t(ax, 420, 240, "REGISTRATION", size=13, color=MAROON_DARK, fam=H_B, z=6)
    t(ax, 420, 212, "SYSTEM", size=13, color=MAROON_DARK, fam=H_B, z=6)

    actor(ax, 150, 120, "Student", scale=1.1)
    actor(ax, 690, 120, "Administrator", scale=1.1)
    actor(ax, 150, 60, "Lecturer", scale=0.9)
    actor(ax, 690, 60, "Notification Service", scale=0.9)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Actors can also be payment services, email services or other software systems.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w15_actors.png")


# --------------------------------------------------------------------------
# 7. Use-case diagram
# --------------------------------------------------------------------------
def use_case_diagram():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Use-Case Diagram (simplified)", sub="Student and Administrator goals")

    box(ax, 240, 60, 360, 280, WHITE, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 420, 312, "UNIVERSITY SYSTEM", size=12, color=MAROON, fam=H_B, z=6)
    stu = ["Login", "View Courses", "Search Courses", "Register Course", "Drop Course", "View Registration"]
    adm = ["Create Course", "Update Course", "View Registrations", "Generate Report"]
    for i, s in enumerate(stu):
        y = 272 - i * 34
        box(ax, 290, y - 11, 160, 22, MAROON_TINT, ec=MAROON, lw=1.1, r=14, z=6)
        t(ax, 370, y, s, size=9.5, color=INK, fam=BODY, z=7)
    for i, s in enumerate(adm):
        y = 272 - i * 34
        box(ax, 470, y - 11, 160, 22, WHITE, ec=MAROON_SOFT, lw=1.1, r=14, z=6)
        t(ax, 550, y, s, size=9.5, color=MAROON_SOFT, fam=BODY, z=7)

    actor(ax, 110, 150, "Student", scale=1.0)
    actor(ax, 730, 150, "Administrator", scale=1.0)
    arrow(ax, 160, 196, 288, 260, lw=1.6, ms=10, z=8)
    arrow(ax, 680, 196, 552, 260, lw=1.6, ms=10, z=8)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Produce the exact graphical notation with a UML tool in the practical session.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w15_use_case_diagram.png")


# --------------------------------------------------------------------------
# 8. Use-case specification (Register for Course)
# --------------------------------------------------------------------------
def use_case_spec():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Use Case: Register for Course", sub="Main success scenario")

    box(ax, 22, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 212, 318, "USE CASE CARD", size=12, color=MAROON_DARK, fam=H_B, z=6)
    for i, s in enumerate(["Name: Register for Course", "Actor: Student", "Goal: register for an available course"]):
        t(ax, 212, 288 - i * 24, s, size=10.5, color=INK, fam=BODY, z=7)
    t(ax, 212, 200, "Preconditions:", size=10.5, color=MAROON, fam=B_SB, z=7)
    for i, s in enumerate(["authenticated", "registration open", "account active"]):
        t(ax, 212, 180 - i * 22, s, size=10, color=INK, fam=BODY, z=7)

    box(ax, 438, 96, 380, 246, WHITE, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 318, "MAIN SUCCESS SCENARIO", size=12, color=MAROON, fam=H_B, z=6)
    steps = ["1. Student selects \u201cRegister Course\u201d", "2. System displays available courses",
             "3. Student selects a course", "4. System checks the course exists",
             "5. System checks prerequisites", "6. System checks capacity",
             "7. Checks for duplicate registration", "8. System creates registration",
             "9. Updates course enrolment", "10. System displays confirmation"]
    for i, s in enumerate(steps):
        t(ax, 628, 282 - i * 20, s, size=9, color=INK, fam=BODY, z=7)

    box(ax, 22, 16, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 29, "Do not stop at the diagram \u2014 document important use cases.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w15_use_case_spec.png")


# --------------------------------------------------------------------------
# 9. Candidate classes (domain vs technical)
# --------------------------------------------------------------------------
def candidate_classes():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Candidate Classes", sub="Domain classes vs technical classes")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "DOMAIN CLASSES", size=12.5, color=MAROON, fam=H_B, z=6)
    t(ax, 212, 278, "from the problem domain", size=10.5, color=GREY, fam=B_IT, z=7)
    for i, s in enumerate(["Student", "Course", "Registration", "Programme", "Prerequisite", "Administrator"]):
        c, r = divmod(i, 3)
        x = 60 + r * 116
        y = 236 - c * 40
        box(ax, x, y - 12, 106, 26, MAROON_TINT, ec=MAROON, lw=1.2, r=8, z=6)
        t(ax, x + 53, y, s, size=9.5, color=INK, fam=BODY, z=7)

    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "TECHNICAL / APPLICATION", size=12.5, color=MAROON_DARK, fam=H_B, z=6)
    t(ax, 628, 278, "support implementation", size=10.5, color=GREY, fam=B_IT, z=7)
    for i, s in enumerate(["RegistrationController", "RegistrationService", "CourseRepository",
                           "RegistrationRepository", "NotificationService", "AuthenticationService"]):
        c, r = divmod(i, 2)
        x = 490 + r * 138
        y = 240 - c * 40
        box(ax, x, y - 12, 128, 26, WHITE, ec=MAROON, lw=1.2, r=8, z=6)
        t(ax, x + 64, y, s, size=8.5, color=MAROON_SOFT, fam=BODY, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Do not confuse the problem-domain concepts with the implementation helpers.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w15_candidate_classes.png")


# --------------------------------------------------------------------------
# 10. Class model (5 classes)
# --------------------------------------------------------------------------
def class_model():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "The Class Model", sub="Controller -> Service -> Domain -> Repository")

    uc(ax, 330, 372, 150, "RegistrationController", ops=["+registerStudent()"], name_size=10)
    arrow(ax, 405, 370, 405, 358, lw=1.8, ms=12, z=8)
    uc(ax, 320, 276, 170, "RegistrationService",
       ops=["+registerStudent()", "+dropStudent()", "+checkEligibility()", "+checkDuplicate()"], name_size=10)
    arrow(ax, 380, 274, 200, 200, lw=1.6, ms=11, z=8)
    arrow(ax, 470, 274, 590, 200, lw=1.6, ms=11, z=8)
    uc(ax, 80, 128, 150, "Student",
       attrs=["-studentId", "-name", "-email", "-programme"],
       ops=["+registerCourse()", "+dropCourse()", "+viewRegistration()"], name_size=10)
    uc(ax, 250, 128, 150, "Course",
       attrs=["-courseCode", "-courseName", "-credits", "-capacity", "-status"],
       ops=["+isAvailable()", "+checkCapacity()", "+addStudent()", "+removeStudent()"], name_size=10)
    uc(ax, 420, 128, 150, "Registration",
       attrs=["-registrationId", "-registrationDate", "-status"],
       ops=["+confirm()", "+cancel()"], name_size=10)
    uc(ax, 590, 128, 150, "RegistrationRepository",
       ops=["+save()", "+findByStudent()", "+findByCourse()", "+delete()"], name_size=10)
    t(ax, 155, 106, "domain objects", size=9, color=GREY, fam=B_IT, z=7)
    t(ax, 665, 106, "repository", size=9, color=GREY, fam=B_IT, z=7)

    box(ax, 22, 12, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 25, "From \u201cRegister a course\u201d to a detailed, implementation-ready design.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w15_class_model.png")


# --------------------------------------------------------------------------
# 11. Associations / multiplicity
# --------------------------------------------------------------------------
def associations():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Associations and Multiplicity", sub="Reading the numbers on each end")

    uc(ax, 80, 170, 160, "Student", name_size=11)
    uc(ax, 300, 170, 160, "Registration", name_size=11)
    uc(ax, 520, 170, 160, "Course", name_size=11)
    arrow(ax, 242, 190, 296, 190, lw=1.8, ms=12, z=8)
    arrow(ax, 462, 190, 516, 190, lw=1.8, ms=12, z=8)
    t(ax, 269, 204, "1", size=11, color=MAROON, fam=B_SB, z=8)
    t(ax, 269, 176, "0..*", size=11, color=MAROON_SOFT, fam=B_SB, z=8)
    t(ax, 489, 204, "1", size=11, color=MAROON, fam=B_SB, z=8)
    t(ax, 489, 176, "0..*", size=11, color=MAROON_SOFT, fam=B_SB, z=8)

    box(ax, 22, 96, 796, 56, MAROON_TINT, r=12, z=5)
    t(ax, W / 2, 124, "One student may have zero or many registrations; a course may have many registrations.",
      size=11.5, color=MAROON_DARK, fam=B_SB, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Multiplicity is more meaningful than simply drawing lines between classes.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w15_associations.png")


# --------------------------------------------------------------------------
# 12. Inheritance
# --------------------------------------------------------------------------
def inheritance():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Inheritance", sub="A shared User abstraction \u2014 only if genuinely appropriate")

    uc(ax, 340, 270, 160, "User",
       attrs=["-userId", "-name", "-email"],
       ops=["+login()", "+logout()"], name_size=11)
    gtri(ax, 420, 256, 40, 26, z=8)
    ax.plot([382, 250], [256, 210], color=MAROON, lw=1.8, zorder=7)
    ax.plot([420, 420], [256, 210], color=MAROON, lw=1.8, zorder=7)
    ax.plot([458, 590], [256, 210], color=MAROON, lw=1.8, zorder=7)
    uc(ax, 130, 140, 150, "Student", ops=["+registerCourse()", "+viewGrades()"], name_size=10)
    uc(ax, 345, 140, 150, "Administrator", ops=["+manageCourses()", "+generateReport()"], name_size=10)
    uc(ax, 560, 140, 150, "Lecturer", ops=["+enterMarks()", "+viewClassList()"], name_size=10)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Shared user ID, name, email and authentication \u2014 but different responsibilities.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w15_inheritance.png")


# --------------------------------------------------------------------------
# 13. Sequence diagram (Register Course)
# --------------------------------------------------------------------------
def sequence():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Sequence Diagram: Register Course", sub="Which object talks to which, in what order")

    objs = ["Student", "Reg.Controller", "Reg.Service", "Course", "Registration", "Reg.Repository"]
    xs = [110, 250, 380, 510, 640, 750]
    top = 388
    for x, name in zip(xs, objs):
        box(ax, x - 58, top, 116, 26, MAROON, r=6, z=6)
        t(ax, x, top + 13, name, size=8.5, color=WHITE, fam=B_SB, z=7)
        ax.plot([x, x], [top - 6, 118], color=GREY, lw=1.0, ls=":", zorder=4)

    msgs = [("register(course)", 110, 250, 356),
            ("registerStudent()", 250, 380, 328),
            ("checkEligibility()", 380, 510, 300),
            ("checkCapacity()", 510, 380, 272),
            ("createRegistration()", 380, 640, 244),
            ("save()", 640, 750, 216)]
    for label, x1, x2, y in msgs:
        arrow(ax, x1 + 2, y, x2 - 2, y, lw=1.6, ms=11, z=8)
        t(ax, (x1 + x2) / 2, y + 11, label, size=8.5, color=MAROON_SOFT, fam=MONO, z=8)

    box(ax, 22, 14, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 27, "The class diagram says what classes exist; the sequence says how they cooperate.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w15_sequence.png")


# --------------------------------------------------------------------------
# 14. State machine (Course lifecycle)
# --------------------------------------------------------------------------
def state_machine():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Course Lifecycle (State Machine)", sub="States and the events that change them")

    fnode(ax, 130, 416, r=10)
    state(ax, 90, 360, 120, 40, "Created")
    arrow(ax, 150, 414, 150, 404, lw=1.8, ms=12, z=8)
    t(ax, 158, 356, "administrator opens registration", size=9, color=GREY, fam=B_IT, z=8, ha="left")

    state(ax, 90, 250, 120, 40, "Available")
    state(ax, 340, 250, 120, 40, "Full")
    state(ax, 590, 250, 120, 40, "Closed")
    arrow(ax, 150, 358, 150, 294, lw=1.8, ms=12, z=8)
    arrow(ax, 212, 270, 336, 270, lw=1.8, ms=12, z=8)
    t(ax, 274, 286, "last seat taken", size=9, color=GREY, fam=B_IT, z=8)
    arrow(ax, 340, 258, 210, 252, lw=1.8, ms=12, z=8, style="<|-|>")
    t(ax, 274, 240, "student drops", size=9, color=GREY, fam=B_IT, z=8)
    arrow(ax, 462, 270, 586, 270, lw=1.8, ms=12, z=8)
    t(ax, 524, 286, "period ends", size=9, color=GREY, fam=B_IT, z=8)

    box(ax, 22, 130, 796, 44, MAROON_TINT, r=12, z=5)
    t(ax, W / 2, 152, "status: CourseStatus in the class is not enough \u2014 the state machine explains WHY it changes.",
      size=11, color=MAROON_DARK, fam=B_SB, z=7)

    box(ax, 22, 18, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 31, "Created -> Available -> Full / Closed \u2014 with meaningful triggering events.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w15_state_machine.png")


# --------------------------------------------------------------------------
# 15. Activity diagram (registration workflow)
# --------------------------------------------------------------------------
def activity():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Registration Workflow (Activity Diagram)", sub="Step-by-step flow with decisions")

    fnode(ax, 420, 440, r=10)
    activities = ["Login", "View Courses", "Select Course", "Check Prerequisite"]
    y = 410
    for i, a in enumerate(activities):
        box(ax, 320, y - 16, 200, 32, MAROON if i % 2 == 0 else MAROON_SOFT, r=14, z=6)
        t(ax, 420, y, a, size=10.5, color=WHITE, fam=B_SB, z=7)
        arrow(ax, 420, y - 17, 420, y - 27, lw=1.6, ms=11, z=8)
        y -= 44
    diamond(ax, 392, y - 42, 56, 56, z=6)
    t(ax, 420, y - 14, "prereq?", size=9, color=MAROON_DARK, fam=B_SB, z=8)
    t(ax, 360, y - 14, "No", size=9, color=MAROON_SOFT, fam=B_SB, z=8)
    box(ax, 240, y - 74, 110, 30, MAROON_SOFT, r=10, z=6)
    t(ax, 295, y - 59, "Reject", size=10, color=WHITE, fam=B_SB, z=7)
    arrow(ax, 392, y - 14, 352, y - 59, lw=1.6, ms=11, z=8)
    t(ax, 468, y - 14, "Yes", size=9, color=MAROON_DARK, fam=B_SB, z=8)
    box(ax, 320, y - 116, 200, 32, MAROON, r=14, z=6)
    t(ax, 420, y - 100, "Check Capacity", size=10.5, color=WHITE, fam=B_SB, z=7)
    arrow(ax, 420, y - 42, 420, y - 84, lw=1.6, ms=11, z=8)
    diamond(ax, 392, y - 156, 56, 56, z=6)
    t(ax, 420, y - 128, "space?", size=9, color=MAROON_DARK, fam=B_SB, z=8)
    t(ax, 560, y - 128, "Yes", size=9, color=MAROON_DARK, fam=B_SB, z=8)
    t(ax, 420, y - 172, "No", size=9, color=MAROON_SOFT, fam=B_SB, z=8)
    box(ax, 300, y - 168, 100, 26, MAROON_SOFT, r=10, z=6)
    t(ax, 350, y - 155, "Reject", size=10, color=WHITE, fam=B_SB, z=7)
    arrow(ax, 420, y - 156, 402, y - 168, lw=1.6, ms=11, z=8)
    box(ax, 600, y - 130, 150, 32, MAROON, r=14, z=6)
    t(ax, 675, y - 114, "Create Registration", size=9.5, color=WHITE, fam=B_SB, z=7)
    arrow(ax, 448, y - 128, 598, y - 114, lw=1.6, ms=11, z=8)
    arrow(ax, 675, y - 146, 675, y - 170, lw=1.6, ms=11, z=8)
    box(ax, 600, y - 200, 150, 32, MAROON_SOFT, r=14, z=6)
    t(ax, 675, y - 184, "Save Registration", size=9.5, color=WHITE, fam=B_SB, z=7)
    arrow(ax, 675, y - 216, 675, y - 240, lw=1.6, ms=11, z=8)
    box(ax, 600, y - 270, 150, 32, MAROON, r=14, z=6)
    t(ax, 675, y - 254, "Send Confirmation", size=9.5, color=WHITE, fam=B_SB, z=7)
    inode(ax, 675, y - 300, r=8)

    box(ax, 22, 16, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 29, "The activity diagram describes the workflow of the registration process.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w15_activity.png")


# --------------------------------------------------------------------------
# 16. Component / layered architecture
# --------------------------------------------------------------------------
def components():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Components & Layered Architecture", sub="Grouping related functionality")

    layers = [
        ("PRESENTATION LAYER", "Web / Mobile Interface"),
        ("APPLICATION LAYER", "Controllers / Services"),
        ("DOMAIN LAYER", "Student · Course · Registration"),
        ("PERSISTENCE LAYER", "Repositories / Database"),
    ]
    y = 356
    for i, (hd, sub) in enumerate(layers):
        box(ax, 120, y - 34, 600, 68, WHITE if i % 2 == 0 else MAROON_TINT, ec=MAROON, lw=1.6, r=12, z=5)
        box(ax, 120, y + 10, 600, 24, MAROON, r=0, z=6)
        t(ax, 420, y + 22, hd, size=10.5, color=WHITE, fam=H_SB, z=7)
        t(ax, 420, y - 14, sub, size=10.5, color=INK, fam=BODY, z=7)
        if i < len(layers) - 1:
            arrow(ax, 420, y - 36, 420, y - 44, lw=1.8, ms=12, z=8)
        y -= 82

    box(ax, 22, 16, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 29, "This connects directly with the architectural concepts covered earlier in the module.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w15_components.png")


# --------------------------------------------------------------------------
# 17. Traceability
# --------------------------------------------------------------------------
def traceability():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Model Traceability", sub="Following one requirement through the whole design")

    steps = [
        ("REQUIREMENT", "\u201cStudent must register for courses\u201d"),
        ("USE CASE", "Register Course"),
        ("SEQUENCE", "Student -> Controller -> Service -> Course -> Registration"),
        ("CLASSES", "RegistrationController · RegistrationService · Course · Registration"),
        ("OPERATIONS", "registerStudent() · checkEligibility() · checkCapacity() · createRegistration() · save()"),
        ("IMPLEMENTATION", "Java · C# · Python · C++ · Kotlin · TypeScript"),
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
    t(ax, W / 2, 27, "The exact language does not change the OOAD principle.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w15_traceability.png")


# --------------------------------------------------------------------------
# 18. The complete integrated model
# --------------------------------------------------------------------------
def integrated():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "The Complete OOAD Journey", sub="The big picture of the whole module")

    box(ax, 330, 400, 180, 34, MAROON, r=10, z=6)
    t(ax, 420, 417, "UNIVERSITY REGISTRATION", size=10, color=WHITE, fam=H_SB, z=7)
    arrow(ax, 340, 398, 220, 372, lw=1.6, ms=11, z=8)
    arrow(ax, 500, 398, 620, 372, lw=1.6, ms=11, z=8)
    actor(ax, 170, 300, "Student", scale=0.8)
    actor(ax, 670, 300, "Administrator", scale=0.8)
    arrow(ax, 190, 320, 260, 250, lw=1.6, ms=11, z=8)
    arrow(ax, 650, 320, 580, 250, lw=1.6, ms=11, z=8)
    box(ax, 260, 220, 320, 32, MAROON_SOFT, r=10, z=6)
    t(ax, 420, 236, "USE CASES", size=10, color=WHITE, fam=H_SB, z=7)
    arrow(ax, 420, 218, 420, 208, lw=1.6, ms=11, z=8)
    box(ax, 260, 176, 320, 32, MAROON, r=10, z=6)
    t(ax, 420, 192, "ANALYSIS MODEL", size=10, color=WHITE, fam=H_SB, z=7)
    arrow(ax, 300, 174, 220, 138, lw=1.6, ms=11, z=8)
    arrow(ax, 420, 174, 420, 138, lw=1.6, ms=11, z=8)
    arrow(ax, 540, 174, 620, 138, lw=1.6, ms=11, z=8)
    box(ax, 130, 106, 180, 32, MAROON_TINT, ec=MAROON, lw=1.3, r=10, z=6)
    t(ax, 220, 122, "CLASS MODEL", size=9.5, color=MAROON_DARK, fam=B_SB, z=7)
    box(ax, 330, 106, 180, 32, MAROON_TINT, ec=MAROON, lw=1.3, r=10, z=6)
    t(ax, 420, 122, "DYNAMIC MODEL", size=9.5, color=MAROON_DARK, fam=B_SB, z=7)
    box(ax, 530, 106, 180, 32, MAROON_TINT, ec=MAROON, lw=1.3, r=10, z=6)
    t(ax, 620, 122, "BEHAVIOUR MODEL", size=9.5, color=MAROON_DARK, fam=B_SB, z=7)
    arrow(ax, 420, 104, 420, 94, lw=1.6, ms=11, z=8)
    box(ax, 260, 62, 320, 32, MAROON_SOFT, r=10, z=6)
    t(ax, 420, 78, "DESIGN MODEL", size=10, color=WHITE, fam=H_SB, z=7)
    arrow(ax, 420, 60, 420, 50, lw=1.6, ms=11, z=8)
    box(ax, 260, 18, 320, 32, MAROON, r=10, z=6)
    t(ax, 420, 34, "ARCHITECTURE -> COMPONENTS -> IMPLEMENTATION", size=9, color=WHITE, fam=H_SB, z=7)

    return save(fig, "w15_integrated.png")


ALL = [
    progression, process, consistency, business_problem, requirements, actors,
    use_case_diagram, use_case_spec, candidate_classes, class_model, associations,
    inheritance, sequence, state_machine, activity, components, traceability, integrated,
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
    print("Generated", len(made), "week-15 visuals:")
    for m in made:
        print("  -", m)
