"""
Shared matplotlib drawing helpers for building brand-styled diagrams.
Used by weekly visual modules (week2_visuals, week3_visuals, ...).
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Polygon

from common import (register_fonts, VISUALS, MAROON, MAROON_DARK, MAROON_DEEP,
                    MAROON_SOFT, MAROON_TINT, MAROON_TINT2, GOLD, GOLD_LIGHT,
                    CREAM, CREAM_2, INK, GREY, GREY_LIGHT, WHITE, CHART_COLORS)

register_fonts()

H_XB  = ("Poppins", 800)
H_B   = ("Poppins", 700)
H_SB  = ("Poppins", 600)
H_MD  = ("Poppins", 500)
BODY  = ("Open Sans", 400)
B_SB  = ("Open Sans", 600)
B_B   = ("Open Sans", 700)
B_IT  = ("Open Sans", 400, "italic")
MONO  = ("DejaVu Sans Mono", 400)
SYM   = "DejaVu Sans"

DPI = 150


def canvas(w, h, bg=CREAM):
    fig = plt.figure(figsize=(w, h), dpi=DPI)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, w * 100)
    ax.set_ylim(0, h * 100)
    ax.axis("off")
    fig.patch.set_facecolor(bg)
    return fig, ax


def box(ax, x, y, w, h, fc, ec="none", lw=0, r=10, alpha=1.0, z=5):
    p = FancyBboxPatch((x, y), w, h,
                       boxstyle=f"round,pad=0,rounding_size={r}",
                       mutation_aspect=1, facecolor=fc, edgecolor=ec,
                       linewidth=lw, alpha=alpha, zorder=z)
    ax.add_patch(p)
    return p


def chev(ax, x, y, w, h, fc, z=5, r=4):
    p = Polygon([(x + r, y), (x + w - r, y), (x + w, y + h / 2),
                 (x + w - r, y + h), (x + r, y + h), (x, y + h / 2)],
                closed=True, facecolor=fc, edgecolor="none", zorder=z)
    ax.add_patch(p)
    return p


def t(ax, x, y, s, size=13, color=INK, fam=BODY, ha="center", va="center",
      ls=1.3, z=10, style="normal", weight="normal"):
    family, w, st = None, weight, style
    if isinstance(fam, (tuple, list)):
        family = fam[0]
        if len(fam) > 1:
            w = fam[1]
        if len(fam) > 2:
            st = fam[2]
    else:
        family = fam
    ax.text(x, y, s, fontsize=size, color=color, family=family, fontweight=w,
            fontstyle=st, ha=ha, va=va, linespacing=ls, zorder=z)


def arrow(ax, x1, y1, x2, y2, color=MAROON, lw=2.2, ms=18, style="-|>", z=8):
    a = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style,
                        mutation_scale=ms, color=color, lw=lw, zorder=z,
                        shrinkA=0, shrinkB=0)
    ax.add_patch(a)


def title(ax, W, s, size=21, color=MAROON, y=None, sub=None):
    if y is None:
        y = ax.get_ylim()[1] - 42
    t(ax, W / 2, y, s, size=size, color=color, fam=H_B)
    ax.plot([W / 2 - 26, W / 2 + 26], [y - 18, y - 18], color=GOLD, lw=2.4, zorder=8)
    if sub:
        t(ax, W / 2, y - 40, sub, size=12.5, color=GREY, fam=B_IT)


def save(fig, name):
    path = os.path.join(VISUALS, name)
    fig.savefig(path, facecolor=fig.get_facecolor())
    plt.close(fig)
    return path
