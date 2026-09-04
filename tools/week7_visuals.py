"""
Week 7 visuals — OBJECT-ORIENTED ANALYSIS: DYNAMIC MODELLING.
Event · State · Operations · Concurrency · Structure vs dynamic models · CASE tools.
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
# State-machine helpers
# --------------------------------------------------------------------------
def state(ax, x, y, w, h, name, ec=MAROON, fill=WHITE, size=11.5, lw=1.8):
    box(ax, x, y, w, h, fill, ec=ec, lw=lw, r=18, z=6)
    t(ax, x + w / 2, y + h / 2, name, size=size, color=MAROON_DARK, fam=H_SB, z=7)
    return (x, y, w, h)


def initial(ax, x, y, r=7, color=MAROON_DARK, z=8):
    ax.add_patch(Circle((x, y), r, facecolor=color, edgecolor="none", zorder=z))


def final(ax, x, y, r=10, color=MAROON_DARK, z=8):
    ax.add_patch(Circle((x, y), r, fill=False, edgecolor=color, lw=2.0, zorder=z))
    ax.add_patch(Circle((x, y), r * 0.55, facecolor=color, edgecolor="none", zorder=z))


def trans(ax, x1, y1, x2, y2, label=None, color=MAROON, lw=1.8, ls="-", lp=None,
          ls_off=(0, 0), size=9.5):
    arrow(ax, x1, y1, x2, y2, color=color, lw=lw, style=ls, z=8)
    if label is not None:
        mx, my = (x1 + x2) / 2 + ls_off[0], (y1 + y2) / 2 + ls_off[1]
        t(ax, mx, my, label, size=size, color=MAROON_SOFT, fam=B_IT, z=9)


def uc(ax, x, y, w, name, attrs=None, ops=None, name_color=WHITE, fill=WHITE,
       ec=MAROON, line_h=18, pad=9, name_size=11.5):
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
# 1. Structural vs dynamic
# --------------------------------------------------------------------------
def structural_vs_dynamic():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Structural vs Dynamic Modelling", sub="What exists vs what happens")

    rows = [
        ("Question", "What exists?", "What happens?"),
        ("Elements", "Classes · Attributes · Associations", "Events · States · Transitions"),
        ("Focus", "Structure", "Behaviour over time"),
        ("Example", "Student — Course", "Pending -> Paid -> Shipped"),
    ]
    box(ax, 22, 250, 380, 40, MAROON, r=10, z=7)
    t(ax, 212, 270, "STRUCTURAL", size=13, color=WHITE, fam=H_B, z=8)
    box(ax, 438, 250, 380, 40, MAROON_DARK, r=10, z=7)
    t(ax, 628, 270, "DYNAMIC", size=13, color=WHITE, fam=H_B, z=8)
    yy = 210
    for q, s_val, d_val in rows:
        t(ax, 60, yy, q, size=11, color=GREY, fam=B_SB, ha="left", z=7)
        t(ax, 212, yy, s_val, size=10.5, color=INK, fam=BODY, z=7)
        t(ax, 628, yy, d_val, size=10.5, color=INK, fam=BODY, z=7)
        yy -= 42

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Structural = the system's parts · Dynamic = how those parts behave as events occur.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w7_structural_vs_dynamic.png")


# --------------------------------------------------------------------------
# 2. Car analogy
# --------------------------------------------------------------------------
def car_analogy():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "A Simple Analogy — the Car", sub="Structural model = design/parts · dynamic model = behaviour")

    box(ax, 22, 130, 380, 240, WHITE, ec=MAROON, lw=1.6, r=12, z=6)
    t(ax, 212, 344, "STRUCTURAL MODEL", size=12, color=MAROON, fam=H_B, z=7)
    uc(ax, 100, 150, 220, "Car",
       attrs=["registrationNo", "model", "colour"],
       ops=["start()", "stop()", "accelerate()", "brake()"], line_h=17, pad=7, name_size=11.5)
    t(ax, 212, 130, "what a Car is", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 438, 130, 380, 240, MAROON_TINT, ec=MAROON, lw=1.6, r=12, z=6)
    t(ax, 628, 344, "DYNAMIC MODEL", size=12, color=MAROON, fam=H_B, z=7)
    st = ["Off", "Starting", "Running", "Stopped"]
    xx, yy = 470, 150
    for i, nm in enumerate(st):
        state(ax, xx, yy, 150, 44, nm, size=11)
        if i < len(st) - 1:
            lab = ["Start button pressed", "Engine running", "Brake pressed"][i]
            trans(ax, xx + 150, yy + 22, xx + 210, yy + 22, lab, size=8.5)
        xx += 180
    t(ax, 628, 130, "how the Car behaves", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "The class diagram tells us the parts; the state machine tells us what happens when events occur.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w7_car_analogy.png")


# --------------------------------------------------------------------------
# 3. What is an event
# --------------------------------------------------------------------------
def events():
    W, H = 840, 460
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "What Is an Event?", sub="Something that happens — to which the system can respond")

    cats = [
        ("USER-GENERATED", ["Click Login", "Submit Form", "Select Product", "Upload File"], MAROON),
        ("SYSTEM-GENERATED", ["Timer expires", "Backup completed", "Session timeout"], MAROON_DARK),
        ("EXTERNAL", ["Payment gateway confirmation", "Bank transaction response", "Sensor detects movement"], MAROON_SOFT),
        ("DATA-RELATED", ["Payment received", "Stock reaches zero", "Balance below threshold"], "#8C2B2D"),
    ]
    pos = [(22, 240), (438, 240), (22, 60), (438, 60)]
    for (cname, items, col), (x, y) in zip(cats, pos):
        box(ax, x, y, 380, 160, WHITE, ec=col, lw=1.6, r=12, z=6)
        box(ax, x, y + 128, 380, 32, col, r=12, z=7)
        t(ax, x + 190, y + 144, cname, size=11.5, color=WHITE, fam=H_B, z=8)
        yy = y + 104
        for it in items:
            t(ax, x + 24, yy, "-", size=11, color=col, fam=B_B, ha="left", z=7)
            t(ax, x + 40, yy, it, size=11, color=INK, fam=BODY, ha="left", z=7)
            yy -= 24

    box(ax, 22, 16, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 29, "Examples: user clicks Login · customer places Order · ATM card inserted · payment received.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w7_events.png")


# --------------------------------------------------------------------------
# 4. Event vs state
# --------------------------------------------------------------------------
def event_vs_state():
    W, H = 840, 420
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Event vs State", sub="A common student mistake — they are not the same")

    box(ax, 22, 130, 380, 230, WHITE, ec=MAROON, lw=1.8, r=14, z=6)
    box(ax, 22, 330, 380, 30, MAROON, r=14, z=7)
    t(ax, 212, 345, "EVENT", size=13, color=WHITE, fam=H_B, z=8)
    t(ax, 212, 290, "something that HAPPENS", size=12.5, color=INK, fam=B_SB, z=7)
    t(ax, 212, 250, "\"Customer clicks Pay\"", size=12, color=MAROON_SOFT, fam=MONO, z=7)
    t(ax, 212, 200, "an instantaneous occurrence", size=11, color=GREY, fam=B_IT, z=7)
    t(ax, 212, 160, "a trigger for a transition", size=11, color=GREY, fam=B_IT, z=7)

    box(ax, 438, 130, 380, 230, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=6)
    box(ax, 438, 330, 380, 30, MAROON_DARK, r=14, z=7)
    t(ax, 628, 345, "STATE", size=13, color=WHITE, fam=H_B, z=8)
    t(ax, 628, 290, "something that IS / EXISTS", size=12.5, color=INK, fam=B_SB, z=7)
    t(ax, 628, 250, "\"Payment Pending\"", size=12, color=MAROON_SOFT, fam=MONO, z=7)
    t(ax, 628, 200, "a condition over a period of time", size=11, color=GREY, fam=B_IT, z=7)
    t(ax, 628, 160, "a situation the object is in", size=11, color=GREY, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Event = something happens · State = something is —  PaymentReceived is an event; Paid is a state.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w7_event_vs_state.png")


# --------------------------------------------------------------------------
# 5. Order lifecycle
# --------------------------------------------------------------------------
def order_states():
    W, H = 840, 400
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "The Order Lifecycle", sub="An object changes state as events occur")

    initial(ax, 60, 200)
    states = ["Pending", "Paid", "Processing", "Shipped", "Delivered"]
    labs = ["payment received", "process order", "dispatch", "delivered"]
    xx = 110
    for i, nm in enumerate(states):
        if i == 0:
            trans(ax, 60, 200, 110, 200)
        state(ax, xx, 178, 130, 44, nm)
        if i < len(states) - 1:
            trans(ax, xx + 130, 200, xx + 178, 200, labs[i])
        xx += 178
    final(ax, xx - 22, 200)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Read it as a story: the order begins Pending, and each event moves it to the next state.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w7_order_states.png")


# --------------------------------------------------------------------------
# 6. State diagram notation
# --------------------------------------------------------------------------
def notation():
    W, H = 840, 460
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "State-Machine Notation", sub="Initial state · states · transitions · final state")

    box(ax, 22, 120, 796, 220, WHITE, ec=MAROON_SOFT, lw=1.4, r=12, z=6)
    initial(ax, 90, 300)
    trans(ax, 90, 300, 90, 240, "starts here")
    state(ax, 40, 190, 140, 46, "Pending", size=12)
    trans(ax, 180, 213, 250, 213, "event / trigger")
    state(ax, 250, 190, 140, 46, "Paid", size=12)
    trans(ax, 390, 213, 460, 213, "transition")
    state(ax, 460, 190, 140, 46, "Shipped", size=12)
    trans(ax, 600, 213, 600, 130)
    final(ax, 600, 120)

    box(ax, 40, 300, 150, 40, MAROON, r=9, z=7)
    t(ax, 115, 320, "initial state", size=10.5, color=WHITE, fam=H_SB, z=8)
    box(ax, 460, 300, 150, 40, MAROON_DARK, r=9, z=7)
    t(ax, 535, 320, "final state", size=10.5, color=WHITE, fam=H_SB, z=8)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "The filled circle begins the lifecycle; the bull's-eye ends it; arrows carry the event labels.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w7_notation.png")


# --------------------------------------------------------------------------
# 7. Guards
# --------------------------------------------------------------------------
def guards():
    W, H = 840, 460
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Guards — Conditions on Transitions", sub="An event alone is sometimes not enough")

    state(ax, 320, 380, 200, 48, "Withdrawal Requested", size=11.5)
    ax.plot([420, 250], [380, 300], color=MAROON, lw=1.8, zorder=7)
    ax.plot([420, 590], [380, 300], color=MAROON, lw=1.8, zorder=7)

    state(ax, 130, 220, 240, 50, "Cash Dispensed", fill=MAROON_TINT, size=11.5)
    state(ax, 470, 220, 240, 50, "Insufficient Funds", fill=CREAM_2, ec=MAROON_DARK, size=11.5)

    t(ax, 320, 340, "[balance sufficient]", size=11.5, color=MAROON_SOFT, fam=B_IT, z=9)
    t(ax, 540, 340, "[balance insufficient]", size=11.5, color=MAROON_SOFT, fam=B_IT, z=9)

    box(ax, 22, 60, 796, 120, WHITE, ec=MAROON, lw=1.4, r=12, z=6)
    t(ax, 60, 156, "A guard is a condition in square brackets:", size=12, color=MAROON_DARK, fam=B_SB, ha="left", z=7)
    t(ax, 60, 128, "the transition happens only if the condition is true.", size=12, color=INK, fam=BODY, ha="left", z=7)
    t(ax, 60, 100, "e.g. payment received [amount >= total]  ·  requestReturn [within return period]", size=11.5, color=MAROON_SOFT, fam=MONO, ha="left", z=7)

    box(ax, 22, 16, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 29, "The same event can lead to different states, depending on the guard.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w7_guards.png")


# --------------------------------------------------------------------------
# 8. Entry / exit / do
# --------------------------------------------------------------------------
def entry_exit_do():
    W, H = 840, 440
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Entry, Exit and Do Behaviour", sub="Behaviour attached to a state, not a transition")

    box(ax, 22, 120, 796, 200, WHITE, ec=MAROON, lw=1.6, r=12, z=6)
    state(ax, 320, 200, 200, 70, "Processing", size=13)
    t(ax, 330, 250, "entry / startTimer()", size=11, color=MAROON_SOFT, fam=MONO, ha="left", z=8)
    t(ax, 330, 230, "do / processOrder()", size=11, color=MAROON_SOFT, fam=MONO, ha="left", z=8)
    t(ax, 330, 210, "exit / logCompletion()", size=11, color=MAROON_SOFT, fam=MONO, ha="left", z=8)

    box(ax, 22, 60, 380, 46, MAROON, r=9, z=7)
    t(ax, 212, 83, "entry — when the state is entered", size=10.5, color=WHITE, fam=B_SB, z=8)
    box(ax, 438, 60, 380, 46, MAROON_DARK, r=9, z=7)
    t(ax, 628, 83, "exit — when the state is left", size=10.5, color=WHITE, fam=B_SB, z=8)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "do — behaviour while the object remains in the state (e.g. processOrder()).",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w7_entry_exit_do.png")


# --------------------------------------------------------------------------
# 9. Payment state machine
# --------------------------------------------------------------------------
def payment_states():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "A Complete State Machine — Online Payment", sub="Read it as a story")

    initial(ax, 420, 420)
    trans(ax, 420, 420, 420, 385)
    state(ax, 320, 335, 200, 50, "Pending", size=12.5)
    trans(ax, 420, 335, 420, 285, "submitPayment()")
    state(ax, 320, 235, 200, 50, "Processing", size=12.5)

    ax.plot([420, 240], [235, 140], color=MAROON, lw=1.8, zorder=7)
    ax.plot([420, 600], [235, 140], color=MAROON, lw=1.8, zorder=7)
    t(ax, 300, 190, "[payment successful]", size=10.5, color=MAROON_SOFT, fam=B_IT, z=9)
    t(ax, 560, 190, "[payment failed]", size=10.5, color=MAROON_SOFT, fam=B_IT, z=9)

    state(ax, 120, 90, 200, 50, "Paid", fill=MAROON_TINT, size=12.5)
    state(ax, 520, 90, 200, 50, "Failed", fill=CREAM_2, ec=MAROON_DARK, size=12.5)
    trans(ax, 220, 90, 220, 40)
    final(ax, 220, 30)
    trans(ax, 620, 90, 620, 40)
    final(ax, 620, 30)

    box(ax, 22, 12, 796, 22, MAROON_DARK, r=10, z=5)
    t(ax, W / 2, 23, "The payment begins Pending; after submission it enters Processing; success leads to Paid, failure to Failed.",
      size=10.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w7_payment_states.png")


# --------------------------------------------------------------------------
# 10. Operation vs event
# --------------------------------------------------------------------------
def operation_vs_event():
    W, H = 840, 420
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Operation vs Event", sub="Another common confusion")

    box(ax, 22, 130, 380, 230, WHITE, ec=MAROON, lw=1.8, r=14, z=6)
    box(ax, 22, 330, 380, 30, MAROON, r=14, z=7)
    t(ax, 212, 345, "OPERATION", size=13, color=WHITE, fam=H_B, z=8)
    t(ax, 212, 290, "behaviour/service the object", size=12, color=INK, fam=BODY, z=7)
    t(ax, 212, 268, "can perform or provide", size=12, color=INK, fam=BODY, z=7)
    t(ax, 212, 228, "calculateTotal()", size=13, color=MAROON_SOFT, fam=MONO, z=7)
    t(ax, 212, 180, "can be invoked / called", size=11, color=GREY, fam=B_IT, z=7)

    box(ax, 438, 130, 380, 230, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=6)
    box(ax, 438, 330, 380, 30, MAROON_DARK, r=14, z=7)
    t(ax, 628, 345, "EVENT", size=13, color=WHITE, fam=H_B, z=8)
    t(ax, 628, 290, "something that occurs and", size=12, color=INK, fam=BODY, z=7)
    t(ax, 628, 268, "can trigger behaviour", size=12, color=INK, fam=BODY, z=7)
    t(ax, 628, 228, "PaymentReceived", size=13, color=MAROON_SOFT, fam=MONO, z=7)
    t(ax, 628, 180, "happens, then triggers", size=11, color=GREY, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Event = something happens · Operation = a behaviour/service that can be invoked.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w7_operation_vs_event.png")


# --------------------------------------------------------------------------
# 11. Operation causing state change
# --------------------------------------------------------------------------
def operation_state_change():
    W, H = 840, 420
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Operations Can Change State", sub="An ATM's operations move it between states")

    uc(ax, 40, 130, 240, "ATM",
       attrs=["location", "status"],
       ops=["insertCard()", "enterPIN()", "withdrawCash()", "ejectCard()"], line_h=18, pad=8, name_size=12)

    ax.plot([280, 330], [210, 210], color=MAROON, lw=2.0, zorder=7)
    t(ax, 305, 226, "invoke", size=9.5, color=GREY, fam=B_IT, z=9)

    state(ax, 330, 240, 160, 44, "Idle", size=11)
    trans(ax, 410, 240, 410, 196, "insertCard()", size=9.5)
    state(ax, 330, 152, 160, 44, "Card Inserted", size=11)
    trans(ax, 490, 174, 590, 174, "ejectCard()", size=9.5)
    state(ax, 590, 152, 170, 44, "Idle", size=11)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "insertCard() moves the ATM Idle -> Card Inserted; ejectCard() returns it to Idle.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w7_operation_state_change.png")


# --------------------------------------------------------------------------
# 12. Sequential vs concurrent
# --------------------------------------------------------------------------
def concurrency():
    W, H = 840, 430
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Sequential vs Concurrent Behaviour", sub="One-after-another vs at-the-same-time")

    box(ax, 22, 120, 380, 250, WHITE, ec=MAROON, lw=1.8, r=14, z=6)
    box(ax, 22, 340, 380, 30, MAROON, r=14, z=7)
    t(ax, 212, 355, "SEQUENTIAL", size=12.5, color=WHITE, fam=H_B, z=8)
    state(ax, 140, 260, 140, 42, "Enter PIN", size=11)
    trans(ax, 210, 260, 210, 216, size=9)
    state(ax, 140, 174, 140, 42, "Validate PIN", size=11)
    trans(ax, 210, 174, 210, 130, size=9)
    state(ax, 140, 88, 140, 42, "Display account", size=11)
    t(ax, 212, 150, "A  ->  B  ->  C", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 438, 120, 380, 250, MAROON_TINT, ec=MAROON, lw=1.8, r=14, z=6)
    box(ax, 438, 340, 380, 30, MAROON_DARK, r=14, z=7)
    t(ax, 628, 355, "CONCURRENT", size=12.5, color=WHITE, fam=H_B, z=8)
    state(ax, 528, 250, 200, 42, "Order Placed", size=11)
    ax.plot([628, 560], [250, 196], color=MAROON, lw=1.8, zorder=7)
    ax.plot([628, 696], [250, 196], color=MAROON, lw=1.8, zorder=7)
    state(ax, 470, 152, 180, 42, "Process Payment", size=10)
    state(ax, 606, 152, 180, 42, "Prepare Order", size=10)
    t(ax, 628, 130, "both proceed independently", size=10.5, color=GREY, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Concurrency = multiple activities occurring during the same period, not strictly one after another.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w7_concurrency.png")


# --------------------------------------------------------------------------
# 13. Airport concurrency
# --------------------------------------------------------------------------
def airport():
    W, H = 840, 440
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Concurrency in Real Life — the Airport", sub="Two activities proceed at the same time")

    state(ax, 320, 360, 200, 46, "Check-in", size=12)
    ax.plot([420, 250], [360, 300], color=MAROON, lw=1.8, zorder=7)
    ax.plot([420, 590], [360, 300], color=MAROON, lw=1.8, zorder=7)

    state(ax, 130, 220, 240, 50, "Security Screening", fill=MAROON_TINT, size=11.5)
    state(ax, 470, 220, 240, 50, "Baggage Processing", fill=MAROON_TINT, size=11.5)

    ax.plot([250, 380], [220, 120], color=MAROON, lw=1.8, zorder=7)
    ax.plot([590, 460], [220, 120], color=MAROON, lw=1.8, zorder=7)
    t(ax, 300, 176, "Security complete", size=9.5, color=MAROON_SOFT, fam=B_IT, z=9)
    t(ax, 545, 176, "Baggage processed", size=9.5, color=MAROON_SOFT, fam=B_IT, z=9)

    state(ax, 300, 70, 240, 50, "Ready for Boarding", size=12)

    box(ax, 22, 16, 796, 22, MAROON_DARK, r=10, z=5)
    t(ax, W / 2, 27, "Security screening and baggage processing happen concurrently, then join before boarding.",
      size=10.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w7_airport.png")


# --------------------------------------------------------------------------
# 14. UML concurrent regions
# --------------------------------------------------------------------------
def concurrent_regions():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "UML Concurrent Regions", sub="A composite state with two parallel regions")

    box(ax, 60, 60, 720, 340, WHITE, ec=MAROON, lw=2.0, r=16, z=5)
    t(ax, 420, 372, "Order Processing", size=13, color=MAROON, fam=H_B, z=7)
    ax.plot([60, 780], [300, 300], color=MAROON, lw=1.2, zorder=6)

    t(ax, 230, 326, "Payment", size=11, color=GREY, fam=B_SB, z=7)
    t(ax, 620, 326, "Delivery", size=11, color=GREY, fam=B_SB, z=7)

    state(ax, 120, 240, 200, 44, "Processing", size=11)
    trans(ax, 220, 240, 220, 196, size=9)
    state(ax, 120, 152, 200, 44, "Paid", fill=MAROON_TINT, size=11)

    state(ax, 520, 240, 200, 44, "Preparing", size=11)
    trans(ax, 620, 240, 620, 196, size=9)
    state(ax, 520, 152, 200, 44, "Dispatched", fill=MAROON_TINT, size=11)

    ax.plot([220, 340], [108, 60], color=MAROON, lw=1.8, zorder=7)
    ax.plot([620, 500], [108, 60], color=MAROON, lw=1.8, zorder=7)
    state(ax, 320, 24, 200, 36, "Completed", size=11)

    box(ax, 22, 10, 796, 22, MAROON_DARK, r=10, z=5)
    t(ax, W / 2, 21, "The two regions execute concurrently and join when both are complete.",
      size=10.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w7_concurrent_regions.png")


# --------------------------------------------------------------------------
# 15. ATM structural + dynamic
# --------------------------------------------------------------------------
def atm_both():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Two Models That Complement Each Other", sub="The ATM — what exists and how it behaves")

    box(ax, 22, 150, 380, 270, WHITE, ec=MAROON, lw=1.6, r=12, z=6)
    t(ax, 212, 396, "STRUCTURAL — WHAT EXISTS", size=11.5, color=MAROON, fam=H_B, z=7)
    uc(ax, 90, 180, 240, "ATM",
       attrs=["location", "status"],
       ops=["insertCard()", "validatePIN()", "withdraw()", "ejectCard()"], line_h=17, pad=7, name_size=11.5)

    box(ax, 438, 150, 380, 270, MAROON_TINT, ec=MAROON, lw=1.6, r=12, z=6)
    t(ax, 628, 396, "DYNAMIC — HOW IT BEHAVES", size=11.5, color=MAROON, fam=H_B, z=7)
    st = ["Idle", "Card Inserted", "PIN Verification", "Authenticated", "Transaction", "Card Ejected"]
    yy = 356
    for i, nm in enumerate(st):
        state(ax, 470, yy, 170, 34, nm, size=10)
        if i < len(st) - 1:
            trans(ax, 555, yy + 17, 555, yy - 11, size=8)
        yy -= 42

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Neither model replaces the other — together they give a complete understanding.",
      size=11.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w7_atm_both.png")


# --------------------------------------------------------------------------
# 16. Hospital state machine
# --------------------------------------------------------------------------
def hospital():
    W, H = 840, 470
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "Complete Example — Hospital Appointment", sub="A full state machine with a cancellation path")

    initial(ax, 115, 400)
    trans(ax, 115, 400, 115, 386)
    state(ax, 30, 340, 170, 46, "Appointment\nRequested", size=10)
    trans(ax, 115, 340, 115, 296, "confirmAppointment", size=8.5)
    state(ax, 30, 250, 170, 46, "Confirmed", size=11)
    trans(ax, 115, 250, 115, 206, "patientArrives", size=8.5)
    state(ax, 30, 160, 170, 46, "Checked In", size=11)
    trans(ax, 200, 183, 300, 183, "joinQueue", size=8.5)
    state(ax, 300, 160, 170, 46, "Waiting", size=11)
    trans(ax, 470, 183, 570, 183, "doctorCallsPatient", size=8)
    state(ax, 570, 160, 170, 46, "With Doctor", size=11)
    trans(ax, 655, 160, 655, 116, "consultationComplete", size=8)
    state(ax, 570, 70, 170, 46, "Completed", size=11)
    trans(ax, 655, 70, 655, 30, size=7)
    final(ax, 655, 20)

    # cancellation path
    ax.plot([200, 430], [273, 273], color=MAROON_SOFT, lw=1.6, zorder=7)
    t(ax, 315, 284, "cancelAppointment", size=8.5, color=MAROON_SOFT, fam=B_IT, z=9)
    state(ax, 430, 250, 170, 46, "Cancelled", fill=CREAM_2, ec=MAROON_DARK, size=11)
    trans(ax, 515, 250, 515, 206, size=7)
    final(ax, 515, 196)

    box(ax, 22, 12, 796, 22, MAROON_DARK, r=10, z=5)
    t(ax, W / 2, 23, "Appointment Requested -> Confirmed -> Checked In -> Waiting -> With Doctor -> Completed (or Cancelled).",
      size=10.5, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w7_hospital.png")


# --------------------------------------------------------------------------
# 17. Traffic light
# --------------------------------------------------------------------------
def traffic_light():
    W, H = 840, 420
    fig, ax = canvas(W / 100, H / 100)
    title(ax, W, "The Traffic Light", sub="A very simple state machine — and concurrency at an intersection")

    # cycle
    initial(ax, 110, 300)
    trans(ax, 110, 300, 110, 262)
    state(ax, 60, 220, 140, 42, "Red", size=12)
    trans(ax, 130, 220, 130, 178, "timer expires", size=9)
    state(ax, 60, 136, 140, 42, "Green", size=12)
    trans(ax, 200, 157, 330, 157, "timer expires", size=9)
    state(ax, 330, 136, 140, 42, "Yellow", size=12)
    trans(ax, 400, 136, 400, 120, size=9)
    ax.plot([400, 400], [120, 90], color=MAROON, lw=1.8, zorder=7)
    trans(ax, 400, 90, 130, 90, "timer expires", size=9, color=MAROON_SOFT)
    trans(ax, 130, 90, 130, 136, size=9)
    t(ax, 265, 80, "back to Red", size=9, color=GREY, fam=B_IT, z=9)

    # intersection concurrency
    box(ax, 480, 200, 340, 150, MAROON_TINT, ec=MAROON, lw=1.4, r=10, z=6)
    t(ax, 650, 326, "INTERSECTION", size=11.5, color=MAROON, fam=H_B, z=7)
    t(ax, 650, 296, "North/South controller", size=11, color=INK, fam=MONO, z=7)
    t(ax, 650, 272, "East/West controller", size=11, color=INK, fam=MONO, z=7)
    t(ax, 650, 236, "coordinated concurrent regions", size=10, color=GREY, fam=B_IT, z=7)

    box(ax, 22, 22, 796, 26, MAROON_DARK, r=12, z=5)
    t(ax, W / 2, 35, "Red -> Green -> Yellow -> Red — and at an intersection, two controllers run concurrently and coordinate.",
      size=11, color=GOLD_LIGHT, fam=B_SB)
    return save(fig, "w7_traffic_light.png")


ALL = [
    structural_vs_dynamic, car_analogy, events, event_vs_state, order_states,
    notation, guards, entry_exit_do, payment_states, operation_vs_event,
    operation_state_change, concurrency, airport, concurrent_regions, atm_both,
    hospital, traffic_light,
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
    print("Generated", len(made), "week-7 visuals:")
    for m in made:
        print("  -", m)
