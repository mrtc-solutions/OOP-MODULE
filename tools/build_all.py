"""
Build all deliverables for a given week.
Usage:  python tools/build_all.py [week_number]

Week 1 uses the original builders (build_pdf / build_pptx / build_docx).
Week 2+ uses the parameterized engines with week content modules (wN_pdf / wN_pptx / wN_docx).
"""
import sys

from common import register_fonts, make_seal, make_shield, make_wordmark


def build_week(week):
    register_fonts()
    print("[1/4] Brand assets")
    make_seal()
    make_shield()
    make_wordmark()

    if week == 1:
        print("[2/4] Week 1 visuals")
        import visuals
        made = [fn() for fn in visuals.ALL]
        print(f"      generated {len(made)} visuals")
        print("[3/4] Week 1 documents")
        import build_pdf, build_pptx, build_docx
        print("     ", build_pdf.build())
        print("     ", build_pptx.build())
        print("     ", build_docx.build())
    elif week == 2:
        print("[2/4] Week 2 visuals")
        import week2_visuals
        made = [fn() for fn in week2_visuals.ALL]
        print(f"      generated {len(made)} visuals")
        print("[3/4] Week 2 documents")
        import w2_pdf, w2_pptx, w2_docx
        print("     ", w2_pdf.build(w2_pdf.CFG, w2_pdf.story))
        print("     ", w2_pptx.build_pptx())
        print("     ", w2_docx.build(w2_docx.CFG, w2_docx.content))
    elif week == 3:
        print("[2/4] Week 3 visuals")
        import week3_visuals
        made = [fn() for fn in week3_visuals.ALL]
        print(f"      generated {len(made)} visuals")
        print("[3/4] Week 3 documents")
        import w3_pdf, w3_pptx, w3_docx
        print("     ", w3_pdf.build(w3_pdf.CFG, w3_pdf.story))
        print("     ", w3_pptx.build_pptx())
        print("     ", w3_docx.build(w3_docx.CFG, w3_docx.content))
    elif week == 4:
        print("[2/4] Week 4 visuals")
        import week4_visuals
        made = [fn() for fn in week4_visuals.ALL]
        print(f"      generated {len(made)} visuals")
        print("[3/4] Week 4 documents")
        import w4_pdf, w4_pptx, w4_docx
        print("     ", w4_pdf.build(w4_pdf.CFG, w4_pdf.story))
        print("     ", w4_pptx.build_pptx())
        print("     ", w4_docx.build(w4_docx.CFG, w4_docx.content))
    elif week == 5:
        print("[2/4] Week 5 visuals")
        import week5_visuals
        made = [fn() for fn in week5_visuals.ALL]
        print(f"      generated {len(made)} visuals")
        print("[3/4] Week 5 documents")
        import w5_pdf, w5_pptx, w5_docx
        print("     ", w5_pdf.build(w5_pdf.CFG, w5_pdf.story))
        print("     ", w5_pptx.build_pptx())
        print("     ", w5_docx.build(w5_docx.CFG, w5_docx.content))
    elif week == 6:
        print("[2/4] Week 6 visuals")
        import week6_visuals
        made = [fn() for fn in week6_visuals.ALL]
        print(f"      generated {len(made)} visuals")
        print("[3/4] Week 6 documents")
        import w6_pdf, w6_pptx, w6_docx
        print("     ", w6_pdf.build(w6_pdf.CFG, w6_pdf.story))
        print("     ", w6_pptx.build_pptx())
        print("     ", w6_docx.build(w6_docx.CFG, w6_docx.content))
    else:
        print(f"No content module yet for week {week}.")
        return
    print("DONE.")


if __name__ == "__main__":
    week = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    build_week(week)
