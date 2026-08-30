"""
One-shot build of all Week N deliverables (brand assets -> visuals -> PDF/PPTX/DOCX).
Usage:  python tools/build_all.py [week_number]
"""
import sys

from common import register_fonts, make_seal, make_shield, make_wordmark


def main():
    register_fonts()
    print("[1/5] Brand assets")
    make_seal()
    make_shield()
    make_wordmark()

    print("[2/5] Week visuals")
    import visuals
    made = [fn() for fn in visuals.ALL]
    print(f"      generated {len(made)} visuals")

    print("[3/5] PDF module")
    import build_pdf
    print("     ", build_pdf.build())

    print("[4/5] PPTX presentation")
    import build_pptx
    print("     ", build_pptx.build())

    print("[5/5] DOCX assignment")
    import build_docx
    print("     ", build_docx.build())

    print("DONE.")


if __name__ == "__main__":
    main()
