"""
Exploits University — brand constants, fonts and logo generation.
Shared by the PDF / PPTX / DOCX builders.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import Circle, Polygon
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(ROOT, "assets")
FONTS = os.path.join(ASSETS, "fonts")
BRAND = os.path.join(ASSETS, "brand")
VISUALS = os.path.join(ASSETS, "visuals")
OUTPUT = os.path.join(ROOT, "output")
for d in (ASSETS, FONTS, BRAND, VISUALS, OUTPUT):
    os.makedirs(d, exist_ok=True)

# --------------------------------------------------------------------------
# Brand palette
# --------------------------------------------------------------------------
MAROON       = "#7B1113"   # primary university colour
MAROON_DARK  = "#59090C"   # darker shade for gradients / footer
MAROON_DEEP  = "#400709"   # near-black maroon
MAROON_SOFT  = "#A94442"   # lighter maroon
MAROON_TINT  = "#F3E4E4"   # very light maroon tint (box backgrounds)
MAROON_TINT2 = "#F8EFEF"
GOLD         = "#C9A227"   # accent gold
GOLD_LIGHT   = "#E4C97C"
CREAM        = "#FAF6EC"   # page background
CREAM_2      = "#F3ECDC"
INK          = "#2B2626"   # body text
GREY         = "#6B6B6B"
GREY_LIGHT   = "#E8E3DA"
WHITE        = "#FFFFFF"

CHART_COLORS = ["#7B1113", "#A94442", "#C9A227", "#5A5A5A", "#B3797A",
                "#8C2B2D", "#E4C97C", "#9A9A9A"]

# --------------------------------------------------------------------------
# Font registration
# --------------------------------------------------------------------------
def _font(name):
    return os.path.join(FONTS, name)

_font_files = {
    "Poppins":           _font("Poppins-Regular.ttf"),
    "Poppins Medium":    _font("Poppins-Medium.ttf"),
    "Poppins SemiBold":  _font("Poppins-SemiBold.ttf"),
    "Poppins Bold":      _font("Poppins-Bold.ttf"),
    "Poppins ExtraBold": _font("Poppins-ExtraBold.ttf"),
    "Poppins Black":     _font("Poppins-Black.ttf"),
    "Poppins Italic":    _font("Poppins-Italic.ttf"),
    "Poppins Light":     _font("Poppins-Light.ttf"),
    "Open Sans":         _font("OpenSans-Regular.ttf"),
    "Open Sans SemiBold":_font("OpenSans-SemiBold.ttf"),
    "Open Sans Bold":    _font("OpenSans-Bold.ttf"),
    "Open Sans ExtraBold":_font("OpenSans-ExtraBold.ttf"),
    "Open Sans Italic":  _font("OpenSans-Italic.ttf"),
    "Open Sans Light":   _font("OpenSans-Light.ttf"),
    "DejaVu Sans Mono":  _font("DejaVuSansMono.ttf"),
    "DejaVu Sans Mono Bold": _font("DejaVuSansMono-Bold.ttf"),
}

_registered = False
def register_fonts():
    global _registered
    if _registered:
        return
    for fam, path in _font_files.items():
        if os.path.exists(path):
            fm.fontManager.addfont(path)
    _registered = True

H_FONT = "Poppins"          # headings
B_FONT = "Open Sans"        # body
M_FONT = "DejaVu Sans Mono" # code

# --------------------------------------------------------------------------
# Logo: circular university seal (straight-text crest)
# --------------------------------------------------------------------------
def make_seal(path=None, size=3.2, dpi=300):
    register_fonts()
    if path is None:
        path = os.path.join(BRAND, "eu_seal.png")

    fig = plt.figure(figsize=(size, size), dpi=dpi)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(-1.12, 1.12)
    ax.set_ylim(-1.12, 1.12)
    ax.set_aspect("equal")
    ax.axis("off")

    # rings
    ax.add_patch(Circle((0, 0), 1.02, facecolor=GOLD, edgecolor="none", zorder=1))
    ax.add_patch(Circle((0, 0), 0.94, facecolor=CREAM, edgecolor="none", zorder=2))
    ax.add_patch(Circle((0, 0), 0.90, facecolor=MAROON, edgecolor="none", zorder=3))
    ax.add_patch(Circle((0, 0), 0.90, facecolor="none", edgecolor=GOLD,
                        linewidth=1.6, zorder=4))
    ax.add_patch(Circle((0, 0), 0.80, facecolor="none", edgecolor=GOLD,
                        linewidth=0.9, alpha=0.55, zorder=4))

    # wordmark text
    ax.text(0, 0.62, "EXPLOITS", ha="center", va="center", color=CREAM,
            fontsize=21, fontweight="bold", family=H_FONT, zorder=5)
    ax.text(0, 0.44, "UNIVERSITY", ha="center", va="center", color=CREAM,
            fontsize=21, fontweight="bold", family=H_FONT, zorder=5)
    ax.plot([-0.40, 0.40], [0.335, 0.335], color=GOLD, lw=1.3, zorder=5)

    # torch flame (symmetric bulb + tip)
    ax.add_patch(Circle((0, 0.155), 0.088, facecolor=GOLD, edgecolor="none",
                        zorder=6))
    ax.add_patch(Polygon([(-0.062, 0.225), (0.062, 0.225), (0.0, 0.305)],
                         closed=True, facecolor=GOLD, edgecolor="none", zorder=6))
    ax.add_patch(Circle((0, 0.125), 0.042, facecolor=GOLD_LIGHT, edgecolor="none",
                        zorder=7))

    # open book
    book = CREAM
    ax.add_patch(Polygon([(0.0, -0.16), (-0.30, -0.10), (-0.36, 0.03),
                          (-0.19, 0.11), (0.0, 0.05)], closed=True,
                         facecolor=book, edgecolor="none", zorder=6))
    ax.add_patch(Polygon([(0.0, -0.16), (0.30, -0.10), (0.36, 0.03),
                          (0.19, 0.11), (0.0, 0.05)], closed=True,
                         facecolor=book, edgecolor="none", zorder=6))
    ax.plot([0, 0], [-0.16, 0.05], color=MAROON, lw=1.2, zorder=7)
    for yy in (-0.06, -0.01, 0.04):
        ax.plot([-0.24, -0.05], [yy, yy], color=MAROON, lw=0.9, alpha=0.8, zorder=7)
        ax.plot([0.05, 0.24], [yy, yy], color=MAROON, lw=0.9, alpha=0.8, zorder=7)

    # tagline
    ax.text(0, -0.45, "KNOWLEDGE  ·  EXCELLENCE  ·  SERVICE", ha="center",
            va="center", color=GOLD_LIGHT, fontsize=7.2, family=H_FONT, zorder=5)
    ax.plot([-0.30, -0.42], [-0.45, -0.45], color=GOLD, lw=1.0, zorder=5)
    ax.plot([0.30, 0.42], [-0.45, -0.45], color=GOLD, lw=1.0, zorder=5)

    fig.savefig(path, transparent=True)
    plt.close(fig)
    return path


def make_shield(path=None, size=2.0, dpi=300):
    """Small maroon shield with gold 'EU' — used in headers/footers."""
    register_fonts()
    if path is None:
        path = os.path.join(BRAND, "eu_shield.png")

    fig = plt.figure(figsize=(size, size), dpi=dpi)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.25, 1.25)
    ax.set_aspect("equal")
    ax.axis("off")

    ax.add_patch(Polygon([(-0.95, 0.95), (0.95, 0.95), (0.95, 0.35),
                          (0.0, -1.0), (-0.95, 0.35)], closed=True,
                         facecolor=MAROON, edgecolor=GOLD, linewidth=5.0, zorder=1))
    ax.add_patch(Polygon([(-0.70, 0.78), (0.70, 0.78), (0.70, 0.34),
                          (0.0, -0.78), (-0.70, 0.34)], closed=True,
                         facecolor="none", edgecolor=GOLD, linewidth=1.4, zorder=2))
    ax.text(0, 0.16, "EU", ha="center", va="center", color=CREAM,
            fontsize=38, fontweight="bold", family=H_FONT, zorder=3)
    ax.text(0, -0.32, "EST.", ha="center", va="center", color=GOLD,
            fontsize=8.5, family=H_FONT, zorder=3)

    fig.savefig(path, transparent=True)
    plt.close(fig)
    return path


def make_wordmark(path=None, size=(5.2, 1.5), dpi=300):
    """Horizontal lockup: shield + EXPLOITS UNIVERSITY wordmark."""
    shield = make_shield(os.path.join(BRAND, "eu_shield.png"))
    if path is None:
        path = os.path.join(BRAND, "eu_wordmark.png")

    fig = plt.figure(figsize=size, dpi=dpi)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")

    img = plt.imread(shield)
    ax.imshow(img, extent=[2, 34, 14, 86], zorder=2)

    ax.text(38, 66, "EXPLOITS", ha="left", va="center", color=MAROON,
            fontsize=25, fontweight="bold", family=H_FONT)
    ax.text(38, 40, "UNIVERSITY", ha="left", va="center", color=MAROON,
            fontsize=25, fontweight="bold", family=H_FONT)
    ax.plot([38, 93], [29, 29], color=GOLD, lw=1.4, zorder=2)
    ax.text(38, 18, "KNOWLEDGE · EXCELLENCE · SERVICE", ha="left", va="center",
            color=MAROON_SOFT, fontsize=8.5, family=H_FONT)

    fig.savefig(path, transparent=True)
    plt.close(fig)
    return path


if __name__ == "__main__":
    register_fonts()
    p1 = make_seal()
    p2 = make_shield()
    p3 = make_wordmark()
    print("Wrote:", p1)
    print("Wrote:", p2)
    print("Wrote:", p3)
