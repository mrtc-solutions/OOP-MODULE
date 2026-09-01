"""
One-off fix: replace glyphs missing from Open Sans / Poppins (which ReportLab
silently renders as .notdef/tofu in the PDFs) with ASCII equivalents.
-> <-> are already the established convention in matplotlib visuals and Week 15.
"""
import os
import re

TOOLS = os.path.dirname(os.path.abspath(__file__))

ARROW = chr(0x2192)   # ->
LRARROW = chr(0x2194) # <->
BOX = chr(0x2500)     # -
WHITE_DIAM = chr(0x25C7)   # aggregation diamond
BLACK_DIAM = chr(0x25C6)   # composition diamond
BULLSEYE = chr(0x25CE)     # final state
FILLED = chr(0x25CF)       # initial state
TRI = chr(0x25B7)          # generalisation arrowhead

# exact targeted phrase replacements for non-Mono text (Mono spans keep their
# glyphs because DejaVu Sans Mono contains all of them).
PHRASES = {
    "w6_pdf": [
        ("(Car " + BOX*5 + TRI + " Vehicle)", "(Car --|> Vehicle)"),
        ("(Car " + WHITE_DIAM + BOX*4 + " Engine)", "(Car o-- Engine)"),
        ("Order " + BLACK_DIAM + BOX*4 + " OrderItem", "Order *-- OrderItem"),
        ("User " + TRI + " Student and User " + TRI + " Lecturer", "User --|> Student and User --|> Lecturer"),
    ],
    "w7_pdf": [
        ("filled circle</b> (" + FILLED + ")", "filled circle</b>"),
        ("bull's-eye</b> (" + BULLSEYE + ")", "bull's-eye</b>"),
        ("'" + FILLED + " / " + BULLSEYE + "'", "'filled circle / bull's-eye'"),
        ("Pending " + BOX*2 + "PaymentReceived" + BOX*2 + ARROW + " Paid", "Pending --PaymentReceived--> Paid"),
        ("[Pending] " + BOX*2 + "processPayment()" + BOX*2 + ARROW + " [Processing]", "[Pending] --processPayment()--> [Processing]"),
    ],
    "w8_pdf": [
        ("initial node (" + FILLED + ")", "initial node (filled circle)"),
        ("decision/merge diamond (" + WHITE_DIAM + ")", "decision/merge diamond"),
        ("final node (" + BULLSEYE + ")", "final node (bull's-eye)"),
    ],
    "w16_pdf": [
        ("(Department " + WHITE_DIAM + "\u2014 Lecturer)", "(Department o\u2014 Lecturer)"),
        ("(House " + BLACK_DIAM + "\u2014 Room)", "(House *\u2014 Room)"),
    ],
    "w6_pptx": [
        ("Order " + BLACK_DIAM + " OrderItem", "Order *-- OrderItem"),
        ("User " + TRI + " Student \u00b7 User " + TRI + " Lecturer", "User --|> Student \u00b7 User --|> Lecturer"),
        ("Course " + BLACK_DIAM + "-- CourseMaterial", "Course *-- CourseMaterial"),
        ("Order " + BLACK_DIAM + "-- OrderLine", "Order *-- OrderLine"),
    ],
}

def fix_pdf_arrows_and_symbols(w):
    path = os.path.join(TOOLS, f"w{w}_pdf.py")
    txt = open(path, encoding="utf-8").read()
    before = txt
    for a, b in PHRASES.get(f"w{w}_pdf", []):
        txt = txt.replace(a, b)
    txt = txt.replace(ARROW, "->").replace(LRARROW, "<-")
    open(path, "w", encoding="utf-8").write(txt)
    return before != txt

def fix_pptx(w):
    path = os.path.join(TOOLS, f"w{w}_pptx.py")
    txt = open(path, encoding="utf-8").read()
    for a, b in PHRASES.get(f"w{w}_pptx", []):
        txt = txt.replace(a, b)
    txt = txt.replace(ARROW, "->").replace(LRARROW, "<-")
    open(path, "w", encoding="utf-8").write(txt)

def fix_docx(w):
    path = os.path.join(TOOLS, f"w{w}_docx.py")
    txt = open(path, encoding="utf-8").read()
    txt = txt.replace(ARROW, "->").replace(LRARROW, "<-")
    open(path, "w", encoding="utf-8").write(txt)

if __name__ == "__main__":
    changed = []
    for w in range(6, 17):
        if fix_pdf_arrows_and_symbols(w):
            changed.append(f"w{w}_pdf")
        fix_pptx(w)
        fix_docx(w)
    print("PDF modules with changes:", changed)
    # verify no missing glyphs remain anywhere
    from fontTools.ttLib import TTFont
    cmap_os = TTFont(os.path.join(os.path.dirname(TOOLS), "assets", "fonts", "OpenSans-Regular.ttf")).getBestCmap()
    cmap_pp = TTFont(os.path.join(os.path.dirname(TOOLS), "assets", "fonts", "Poppins-Regular.ttf")).getBestCmap()
    bad_any = False
    for w in range(6, 17):
        for kind in ["pdf", "pptx", "docx"]:
            p = os.path.join(TOOLS, f"w{w}_{kind}.py")
            if not os.path.exists(p):
                continue
            txt = open(p, encoding="utf-8").read()
            miss = {ch for ch in set(txt) if ord(ch) > 127 and (ord(ch) not in cmap_os or ord(ch) not in cmap_pp)}
            if miss:
                bad_any = True
                print(f"  REMAINING {kind} w{w}:", [hex(ord(c)) for c in sorted(miss)])
    print("VERIFY:", "CLEAN" if not bad_any else "STILL HAS MISSING GLYPHS")
