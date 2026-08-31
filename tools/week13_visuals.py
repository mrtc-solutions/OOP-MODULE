"""
Week 13 visuals — MULTILAYER SYSTEMS, REUSABLE COMPONENTS AND ARCHITECTURAL DESIGN.
Architecture · layers · separation of concerns · components · interfaces ·
reuse · adaptability · dependencies · deployment.
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
# 1. Progression — where Week 13 fits
# --------------------------------------------------------------------------
def progression():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Where Week 13 Fits", sub="From classes to a maintainable, reusable, adaptable architecture")

    steps = [
        ("WEEKS 4\u201312", "what objects exist, how they\nbehave and interact", "MODELS", MAROON),
        ("WEEK 13", "how to organise those objects\ninto layers and components", "ARCHITECTURE", MAROON_SOFT),
        ("WEEK 14+", "integrating everything into a\ncomplete OO design solution", "INTEGRATION", MAROON_DARK),
    ]
    for i, (hd, sub, tag, colr) in enumerate(steps):
        x = 30 + i * 268
        box(ax, x, 110, 244, 216, WHITE, ec=colr, lw=1.8, r=14, z=5)
        box(ax, x, 288, 244, 38, colr, r=12, z=6)
        t(ax, x + 122, 307, hd, size=12.5, color=WHITE, fam=H_SB, z=7)
        t(ax, x + 122, 236, sub, size=11, color=GREY, fam=B_IT, z=7)
        t(ax, x + 122, 168, tag, size=13, color=MAROON_DARK, fam=H_B, z=7)
        if i < 2:
            arrow(ax, x + 248, 220, x + 264, 220, lw=2.4, ms=16, z=8)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "OOAD asks not only \u201cwhat objects do we need?\u201d but \u201chow should they be organised?\u201d",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w13_progression.png")


# --------------------------------------------------------------------------
# 2. Architecture vs class design
# --------------------------------------------------------------------------
def architecture_vs_class():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Architecture vs Class Design", sub="Architecture is broader than individual class design")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "CLASS DESIGN", size=13, color=MAROON, fam=H_B, z=6)
    t(ax, 212, 278, "\u201cWhat classes do we need?\u201d", size=11.5, color=GREY, fam=B_IT, z=7)
    for i, s in enumerate(["Student", "Course", "Registration", "Payment"]):
        box(ax, 100, 218 - i * 36, 224, 28, MAROON_TINT, r=8, z=6)
        t(ax, 212, 232 - i * 36, s, size=11, color=INK, fam=BODY, z=7)

    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "ARCHITECTURE", size=13, color=MAROON_DARK, fam=H_B, z=6)
    t(ax, 628, 278, "\u201cHow should these be organised?\u201d", size=11.5, color=GREY, fam=B_IT, z=7)
    for i, s in enumerate(["Presentation Layer", "Registration Service", "Registration Domain", "Repository", "Database"]):
        y = 224 - i * 32
        box(ax, 516, y - 12, 224, 26, WHITE, ec=MAROON, lw=1.3, r=8, z=6)
        t(ax, 628, y, s, size=10.5, color=INK, fam=BODY, z=7)
        if i < 4:
            arrow(ax, 628, y - 15, 628, y - 19, lw=1.6, ms=10, z=8)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Architecture is the overall plan of the software — its major parts, responsibilities and relationships.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w13_architecture_vs_class.png")


# --------------------------------------------------------------------------
# 3. The layers (four + database)
# --------------------------------------------------------------------------
def layers():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Basic Multilayer Architecture", sub="Each layer is a logical grouping of related responsibilities")

    layers = [
        ("PRESENTATION LAYER", "web pages · mobile screens · forms · buttons · dashboards", MAROON),
        ("APPLICATION / SERVICE LAYER", "RegistrationService · use-case coordination", MAROON_SOFT),
        ("DOMAIN / BUSINESS LAYER", "Student · Course · Registration · business rules", MAROON_SOFT),
        ("DATA ACCESS / INFRASTRUCTURE", "repositories · persistence", MAROON_DARK),
        ("DATABASE", "persistent storage", MAROON_DEEP),
    ]
    y = 52
    for i, (hd, sub, colr) in enumerate(layers):
        box(ax, 60, y, 720, 58, colr, r=12, z=6)
        t(ax, 420, y + 40, hd, size=13, color=WHITE, fam=H_SB, z=7)
        t(ax, 420, y + 17, sub, size=10.5, color=GOLD_LIGHT, fam=B_IT, z=7)
        if i < len(layers) - 1:
            arrow(ax, 420, y - 2, 420, y - 12, lw=2.2, ms=14, z=8)
        y += 70

    box(ax, 22, 16, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 29, "Understand every layer — don't just memorise the names.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w13_layers.png")


# --------------------------------------------------------------------------
# 4. Domain layer — centralised business rules
# --------------------------------------------------------------------------
def domain_rules():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "The Domain Layer", sub="Business rules live in one place, not in every interface")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON_SOFT, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "RULE DUPLICATED EVERYWHERE", size=12.5, color=MAROON_SOFT, fam=H_B, z=6)
    rule = "max 6 courses -> max 8 courses"
    box(ax, 60, 210, 304, 40, WHITE, ec=MAROON_SOFT, lw=1.4, r=10, z=6)
    t(ax, 212, 230, rule, size=11, color=MAROON_SOFT, fam=MONO, z=7)
    for i, s in enumerate(["website", "mobile app", "desktop app", "reports"]):
        box(ax, 80, 168 - i * 32, 264, 26, MAROON_TINT, ec="none", r=8, z=6)
        t(ax, 212, 181 - i * 32, s + " \u2014 copy of the rule", size=10, color=GREY, fam=B_IT, z=7)

    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "RULE CENTRALISED", size=12.5, color=MAROON, fam=H_B, z=6)
    box(ax, 516, 210, 224, 40, MAROON, r=10, z=6)
    t(ax, 628, 230, "Domain: maxCourses = 8", size=11, color=WHITE, fam=MONO, z=7)
    for i, s in enumerate(["website", "mobile app", "desktop app", "reports"]):
        box(ax, 536, 168 - i * 32, 184, 26, WHITE, ec=MAROON, lw=1.3, r=8, z=6)
        t(ax, 628, 181 - i * 32, s, size=10, color=INK, fam=BODY, z=7)
        if i < 3:
            arrow(ax, 628, 166 - i * 32, 628, 162 - i * 32, lw=1.4, ms=9, z=8)
    t(ax, 628, 106, "one change, one place", size=10.5, color=MAROON_DARK, fam=B_SB, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Centralised business rules mean the change is made once, not four times.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w13_domain_rules.png")


# --------------------------------------------------------------------------
# 5. Data access — why not every class access the DB
# --------------------------------------------------------------------------
def data_access():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "The Data Access Layer", sub="Route database access through repositories")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON_SOFT, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "EVERY CLASS -> DATABASE", size=12.5, color=MAROON_SOFT, fam=H_B, z=6)
    items = ["Student", "Course", "Registration", "Payment", "Report"]
    for i, n in enumerate(items):
        box(ax, 60, 236 - i * 34, 130, 26, WHITE, ec=MAROON_SOFT, lw=1.3, r=8, z=6)
        t(ax, 125, 249 - i * 34, n, size=10.5, color=INK, fam=BODY, z=7)
        arrow(ax, 192, 249 - i * 34, 254, 236, lw=1.5, ms=10, z=8)
    box(ax, 254, 150, 120, 40, MAROON_SOFT, r=10, z=6)
    t(ax, 314, 170, "Database", size=11, color=WHITE, fam=B_SB, z=7)
    t(ax, 212, 96, "many direct dependencies", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "VIA REPOSITORIES", size=12.5, color=MAROON, fam=H_B, z=6)
    items2 = ["Student", "Course", "Registration"]
    for i, n in enumerate(items2):
        box(ax, 496, 236 - i * 40, 130, 30, WHITE, ec=MAROON, lw=1.3, r=8, z=6)
        t(ax, 561, 251 - i * 40, n, size=10.5, color=INK, fam=BODY, z=7)
    arrow(ax, 561, 206, 561, 186, lw=1.8, ms=11, z=8)
    box(ax, 496, 156, 130, 30, MAROON, r=8, z=6)
    t(ax, 561, 171, "Repositories", size=10, color=WHITE, fam=B_SB, z=7)
    arrow(ax, 561, 154, 561, 134, lw=1.8, ms=11, z=8)
    box(ax, 496, 104, 130, 30, MAROON_DARK, r=8, z=6)
    t(ax, 561, 119, "Database", size=10, color=GOLD_LIGHT, fam=B_SB, z=7)
    t(ax, 628, 96, "one controlled dependency", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Changing database technology then affects far fewer classes.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w13_data_access.png")


# --------------------------------------------------------------------------
# 6. Separation of concerns
# --------------------------------------------------------------------------
def separation():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Separation of Concerns", sub="Different parts concentrate on different responsibilities")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON_SOFT, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "ONE HUGE CLASS", size=13, color=MAROON_SOFT, fam=H_B, z=6)
    box(ax, 60, 176, 304, 120, MAROON_SOFT, r=12, z=6)
    t(ax, 212, 272, "StudentRegistration.java", size=11.5, color=WHITE, fam=B_SB, z=7)
    for i, s in enumerate(["displayHTML()", "validatePassword()", "connectDatabase()", "calculateFees()", "sendEmail()", "generatePDF()"]):
        t(ax, 212, 246 - i * 19, s, size=9.5, color=GOLD_LIGHT, fam=MONO, z=7)

    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "SEPARATED RESPONSIBILITIES", size=12.5, color=MAROON, fam=H_B, z=6)
    parts = ["StudentController", "RegistrationService", "Course", "Registration", "PaymentService", "EmailService", "RegistrationRepository"]
    for i, s in enumerate(parts):
        r, c = divmod(i, 3)
        x = 496 + c * 118
        y = 216 - r * 44
        box(ax, x, y, 108, 32, WHITE, ec=MAROON, lw=1.3, r=8, z=6)
        t(ax, x + 54, y + 16, s, size=8.5, color=MAROON_SOFT, fam=B_SB, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Each part has a clearer purpose \u2014 easier to test, modify, reuse and understand.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w13_separation.png")


# --------------------------------------------------------------------------
# 7. Cohesion
# --------------------------------------------------------------------------
def cohesion():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Cohesion", sub="How closely related are the responsibilities within one component?")

    box(ax, 22, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "HIGH COHESION  (good)", size=13, color=MAROON, fam=H_B, z=6)
    uc(ax, 120, 130, 184, "RegistrationService", ops=["registerStudent()", "dropCourse()", "getRegisteredCourses()"], name_size=11)
    t(ax, 212, 110, "all about registration", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 438, 96, 380, 246, WHITE, ec=MAROON_SOFT, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "LOW COHESION  (bad)", size=13, color=MAROON_SOFT, fam=H_B, z=6)
    uc(ax, 536, 118, 184, "RegistrationService", ops=["registration()", "payroll()", "imageEditing()", "email()", "weatherForecast()"], ec=MAROON_SOFT, name_size=11)
    t(ax, 628, 106, "five unrelated concerns", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "A good class should have a clear reason for existing.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w13_cohesion.png")


# --------------------------------------------------------------------------
# 8. Coupling
# --------------------------------------------------------------------------
def coupling():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Coupling", sub="How strongly does one element depend on another?")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON_SOFT, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "HIGH COUPLING  (bad)", size=13, color=MAROON_SOFT, fam=H_B, z=6)
    items = ["WebPage", "MySQLDatabase", "SQL statements"]
    for i, s in enumerate(items):
        box(ax, 120, 226 - i * 42, 184, 32, WHITE, ec=MAROON_SOFT, lw=1.4, r=8, z=6)
        t(ax, 212, 242 - i * 42, s, size=10.5, color=MAROON_SOFT, fam=BODY, z=7)
        if i < 2:
            arrow(ax, 212, 224 - i * 42, 212, 220 - i * 42, lw=1.7, ms=11, z=8)
    t(ax, 212, 100, "web page knows the database internals", size=10, color=GREY, fam=B_IT, z=7)

    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "LOW COUPLING  (good)", size=13, color=MAROON, fam=H_B, z=6)
    items2 = ["WebPage", "RegistrationService", "RegistrationRepository", "Database"]
    for i, s in enumerate(items2):
        box(ax, 536, 226 - i * 34, 184, 28, WHITE, ec=MAROON, lw=1.3, r=8, z=6)
        t(ax, 628, 240 - i * 34, s, size=10.5, color=INK, fam=BODY, z=7)
        if i < 3:
            arrow(ax, 628, 224 - i * 34, 628, 220 - i * 34, lw=1.7, ms=11, z=8)
    t(ax, 628, 100, "cleaner separation", size=10, color=GREY, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Aim for high cohesion and appropriately low coupling.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w13_coupling.png")


# --------------------------------------------------------------------------
# 9. Component vs class
# --------------------------------------------------------------------------
def component_vs_class():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Component vs Class", sub="A component is a larger modular unit")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "CLASSES  (small building blocks)", size=12.5, color=MAROON, fam=H_B, z=6)
    for i, s in enumerate(["Student", "Course", "Registration"]):
        box(ax, 100, 226 - i * 40, 224, 30, MAROON_TINT, r=8, z=6)
        t(ax, 212, 241 - i * 40, s, size=11, color=INK, fam=BODY, z=7)
    t(ax, 212, 96, "attributes · operations · relationships", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "COMPONENT  (larger modular unit)", size=12.5, color=MAROON_DARK, fam=H_B, z=6)
    box(ax, 556, 206, 144, 40, MAROON, r=10, z=6)
    t(ax, 628, 226, "Registration Component", size=10.5, color=WHITE, fam=B_SB, z=7)
    t(ax, 628, 172, "contains many classes:", size=10.5, color=GREY, fam=B_IT, z=7)
    for i, s in enumerate(["RegistrationService", "Registration", "RegistrationRepository", "RegistrationValidator"]):
        box(ax, 556, 130 - i * 30, 144, 24, WHITE, ec=MAROON, lw=1.3, r=6, z=6)
        t(ax, 628, 142 - i * 30, s, size=8.5, color=MAROON_SOFT, fam=B_SB, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Think of a car: the engine is a component, but it contains many parts.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w13_component_vs_class.png")


# --------------------------------------------------------------------------
# 10. Component interfaces
# --------------------------------------------------------------------------
def component_interfaces():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Component Interfaces", sub="Components communicate through defined interfaces")

    box(ax, 300, 210, 240, 60, MAROON, r=10, z=6)
    t(ax, 420, 254, "Payment Interface", size=12, color=WHITE, fam=H_SB, z=7)
    t(ax, 420, 228, "processPayment() · refundPayment()", size=10, color=GOLD_LIGHT, fam=MONO, z=7)

    impl = ["MobileMoney", "BankGateway", "CardGateway"]
    for i, s in enumerate(impl):
        x = 100 + i * 280
        box(ax, x, 96, 180, 46, WHITE, ec=MAROON, lw=1.5, r=10, z=6)
        t(ax, x + 90, 119, s, size=11, color=MAROON_DARK, fam=B_SB, z=7)
        gtri(ax, x + 90, 158, 30, 22, z=8)
    t(ax, 420, 150, "implemented by", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "The system can replace one payment implementation without rewriting every client.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w13_component_interfaces.png")


# --------------------------------------------------------------------------
# 11. Reusable components
# --------------------------------------------------------------------------
def reuse():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Reusable Components", sub="One authentication component for many applications")

    apps = ["University Portal", "Library System", "Student Mobile App", "Staff Portal"]
    for i, s in enumerate(apps):
        x = 40 + i * 196
        box(ax, x, 220, 176, 56, WHITE, ec=MAROON, lw=1.6, r=10, z=6)
        t(ax, x + 88, 248, s, size=10.5, color=MAROON, fam=B_SB, z=7)
        arrow(ax, x + 88, 218, 420, 176, lw=1.8, ms=11, z=8)

    box(ax, 290, 104, 260, 62, MAROON, r=12, z=6)
    t(ax, 420, 148, "AUTHENTICATION COMPONENT", size=11.5, color=WHITE, fam=H_SB, z=7)
    t(ax, 420, 122, "login() · logout() · changePassword() · resetPassword()", size=8.5, color=GOLD_LIGHT, fam=MONO, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Reuse reduces effort, duplication and inconsistency \u2014 when the component is well designed.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w13_reuse.png")


# --------------------------------------------------------------------------
# 12. Adaptable components
# --------------------------------------------------------------------------
def adaptability():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Adaptable Components", sub="Configure or extend, rather than hard-code")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON_SOFT, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "HARD-CODED (rigid)", size=12.5, color=MAROON_SOFT, fam=H_B, z=6)
    box(ax, 60, 170, 304, 110, MAROON_SOFT, r=12, z=6)
    t(ax, 212, 256, "EmailNotification.java", size=11, color=WHITE, fam=B_SB, z=7)
    t(ax, 212, 224, "sendEmail() \u2014 assumes Gmail, HTML,", size=10, color=GOLD_LIGHT, fam=MONO, z=7)
    t(ax, 212, 204, "fixed sender, fixed format", size=10, color=GOLD_LIGHT, fam=MONO, z=7)
    t(ax, 212, 116, "adding SMS means rewriting", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "ADAPTABLE (extensible)", size=12.5, color=MAROON, fam=H_B, z=6)
    box(ax, 556, 220, 144, 36, MAROON, r=10, z=6)
    t(ax, 628, 238, "NotificationService", size=10, color=WHITE, fam=B_SB, z=7)
    for i, s in enumerate(["EmailNotification", "SMSNotification", "PushNotification"]):
        box(ax, 556, 160 - i * 40, 144, 32, WHITE, ec=MAROON, lw=1.3, r=8, z=6)
        t(ax, 628, 176 - i * 40, s, size=9.5, color=MAROON_SOFT, fam=B_SB, z=7)
        if i == 0:
            arrow(ax, 628, 218, 628, 196, lw=1.6, ms=10, z=8)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "New notification methods can be added without redesigning the whole system.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w13_adaptability.png")


# --------------------------------------------------------------------------
# 13. Component diagram
# --------------------------------------------------------------------------
def component_diagram():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "University Component Diagram", sub="Organisation and relationships of software components")

    nodes = [
        ("Web Application", 300, 392, 240),
        ("Authentication Component", 300, 316, 240),
        ("Registration Component", 300, 236, 240),
        ("Course Component", 80, 130, 200),
        ("Notification Component", 560, 130, 200),
        ("Database Component", 300, 52, 240),
    ]
    for name, x, y, w in nodes:
        box(ax, x, y, w, 48, WHITE, ec=MAROON, lw=1.6, r=10, z=6)
        t(ax, x + w / 2, y + 24, name, size=11, color=MAROON, fam=B_SB, z=7)
    arrow(ax, 420, 390, 420, 368, lw=2.0, ms=13, z=8)
    arrow(ax, 420, 314, 420, 288, lw=2.0, ms=13, z=8)
    arrow(ax, 300, 260, 200, 178, lw=1.8, ms=12, z=8)
    arrow(ax, 540, 260, 640, 178, lw=1.8, ms=12, z=8)
    arrow(ax, 200, 128, 380, 104, lw=1.8, ms=12, z=8)
    arrow(ax, 640, 128, 460, 104, lw=1.8, ms=12, z=8)

    box(ax, 22, 12, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 25, "A UML component diagram shows how the parts are organised and how they depend on one another.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w13_component_diagram.png")


# --------------------------------------------------------------------------
# 14. Packages + package vs component
# --------------------------------------------------------------------------
def packages():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Packages", sub="Package = organisation/grouping · Component = modular functionality")

    pkgs = [
        (30, "Authentication", ["User", "Role", "Permission"]),
        (200, "Academic", ["Student", "Course", "Programme", "Registration"]),
        (370, "Finance", ["Payment", "Invoice"]),
        (540, "Notification", ["Email", "SMS", "Push"]),
        (700, "Reporting", ["Report", "Summary"]),
    ]
    for x, name, items in pkgs:
        box(ax, x, 96, 132, 246, WHITE, ec=MAROON, lw=1.7, r=8, z=5)
        box(ax, x, 306, 132, 36, MAROON, r=8, z=6)
        t(ax, x + 66, 324, name, size=10, color=WHITE, fam=B_SB, z=7)
        for i, it in enumerate(items):
            y = 244 - i * 30
            box(ax, x + 10, y - 11, 112, 22, MAROON_TINT, r=6, z=6)
            t(ax, x + 66, y, it, size=9, color=INK, fam=BODY, z=7)
    box(ax, 22, 42, 796, 32, MAROON_TINT, ec=MAROON, lw=1.2, r=10, z=5)
    t(ax, 420, 58, "University System", size=12, color=MAROON_DARK, fam=B_SB, z=6)

    box(ax, 22, 12, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 25, "Packages group model elements into a namespace; components encapsulate functionality behind interfaces.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w13_packages.png")


# --------------------------------------------------------------------------
# 15. Dependency direction
# --------------------------------------------------------------------------
def dependency_direction():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Dependency Direction", sub="Dependencies should move in a controlled direction")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON_SOFT, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "EVERYTHING DEPENDS ON EVERYTHING", size=12, color=MAROON_SOFT, fam=H_B, z=6)
    nodes = [("Presentation", 120, 230), ("Database", 300, 230), ("Domain", 120, 140), ("UI", 300, 140), ("Controllers", 210, 190)]
    for name, x, y in nodes:
        box(ax, x - 58, y - 14, 116, 28, WHITE, ec=MAROON_SOFT, lw=1.3, r=8, z=6)
        t(ax, x, y, name, size=9, color=MAROON_SOFT, fam=B_SB, z=7)
    for (a, axx, ay) in nodes:
        for (b, bx, by) in nodes:
            if (a, axx, ay) != (b, bx, by):
                arrow(ax, axx, ay, bx, by, color=MAROON_SOFT, lw=0.8, ms=7, z=7)

    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "CONTROLLED DIRECTION", size=12.5, color=MAROON, fam=H_B, z=6)
    chain = ["Presentation", "Application", "Domain", "Infrastructure"]
    for i, s in enumerate(chain):
        box(ax, 536, 226 - i * 40, 184, 30, WHITE, ec=MAROON, lw=1.3, r=8, z=6)
        t(ax, 628, 241 - i * 40, s, size=10.5, color=INK, fam=BODY, z=7)
        if i < 3:
            arrow(ax, 628, 224 - i * 40, 628, 220 - i * 40, lw=1.7, ms=11, z=8)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Presentation -> Application -> Domain -> Infrastructure - not every part <-> every other part.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w13_dependency_direction.png")


# --------------------------------------------------------------------------
# 16. Benefits of multilayer architecture
# --------------------------------------------------------------------------
def benefits():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Why Multilayer Architecture Matters", sub="Five practical benefits")

    cards = [
        ("Maintainability", "change the UI without rewriting the business layer"),
        ("Reuse", "one service supports web, mobile and desktop"),
        ("Testability", "test a service without clicking through a UI"),
        ("Adaptability", "swap MySQL for PostgreSQL at the data-access boundary"),
        ("Team development", "separate teams per layer with clear boundaries"),
    ]
    for i, (hd, sub) in enumerate(cards):
        r, c = divmod(i, 3)
        x = 30 + c * 268
        y = 214 - r * 96
        box(ax, x, y, 244, 80, WHITE if r == 0 else MAROON_TINT, ec=MAROON, lw=1.6, r=12, z=5)
        t(ax, x + 122, y + 58, hd, size=12, color=MAROON, fam=B_SB, z=6)
        t(ax, x + 122, y + 24, sub, size=9.5, color=GREY, fam=B_IT, z=6)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Clear layer boundaries make the system easier to maintain, reuse, test, adapt and build as a team.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w13_benefits.png")


# --------------------------------------------------------------------------
# 17. Limitations of multilayer architecture
# --------------------------------------------------------------------------
def limitations():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Limitations of Multilayer Architecture", sub="More layers is not always better")

    cards = [
        ("Additional complexity", "Controller -> Service -> Domain -> Repository -> Database adds abstractions."),
        ("Performance overhead", "extra abstractions / network boundaries can cost time."),
        ("Overengineering", "a tiny app may not need 15 layers, 40 interfaces, 100 packages."),
        ("Incorrect layer responsibilities", "business logic scattered into controllers, repositories and UI."),
    ]
    for i, (hd, sub) in enumerate(cards):
        r, c = divmod(i, 2)
        x = 30 + c * 400
        y = 200 - r * 88
        box(ax, x, y, 380, 74, WHITE, ec=MAROON_SOFT, lw=1.6, r=12, z=5)
        t(ax, x + 190, y + 52, hd, size=12, color=MAROON_SOFT, fam=B_SB, z=6)
        t(ax, x + 190, y + 20, sub, size=9.5, color=GREY, fam=B_IT, z=6)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Architecture should match the problem \u2014 not be applied as a ritual.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w13_limitations.png")


# --------------------------------------------------------------------------
# 18. Deployment — logical vs physical
# --------------------------------------------------------------------------
def deployment():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Deployment Thinking", sub="Logical architecture = how software is organised · deployment = where it runs")

    box(ax, 22, 96, 380, 246, WHITE, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 212, 314, "LOGICAL ARCHITECTURE", size=12.5, color=MAROON, fam=H_B, z=6)
    for i, s in enumerate(["Presentation", "Application", "Domain", "Data Access"]):
        box(ax, 100, 226 - i * 36, 224, 28, MAROON_TINT, r=8, z=6)
        t(ax, 212, 240 - i * 36, s, size=10.5, color=INK, fam=BODY, z=7)
        if i < 3:
            arrow(ax, 212, 224 - i * 36, 212, 220 - i * 36, lw=1.5, ms=10, z=8)

    box(ax, 438, 96, 380, 246, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=5)
    t(ax, 628, 314, "DEPLOYMENT ARCHITECTURE", size=12.5, color=MAROON_DARK, fam=H_B, z=6)
    nodes = [("Student's Phone", "Mobile Application"), ("Application Server", "Registration Service · Authentication"), ("Database Server", "University Database")]
    for i, (hd, sub) in enumerate(nodes):
        box(ax, 536, 210 - i * 44, 184, 38, WHITE, ec=MAROON, lw=1.3, r=8, z=6)
        t(ax, 628, 222 - i * 44, hd, size=10, color=MAROON_DARK, fam=B_SB, z=7)
        t(ax, 628, 202 - i * 44, sub, size=8.5, color=GREY, fam=B_IT, z=7)
        if i < 2:
            arrow(ax, 628, 206 - i * 44, 628, 202 - i * 44, lw=1.6, ms=11, z=8)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "A UML deployment diagram shows the runtime arrangement of software artifacts on nodes.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w13_deployment.png")


ALL = [
    progression, architecture_vs_class, layers, domain_rules, data_access,
    separation, cohesion, coupling, component_vs_class, component_interfaces,
    reuse, adaptability, component_diagram, packages, dependency_direction,
    benefits, limitations, deployment,
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
    print("Generated", len(made), "week-13 visuals:")
    for m in made:
        print("  -", m)
