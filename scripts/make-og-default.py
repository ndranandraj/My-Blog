#!/usr/bin/env python3
"""
Regenerate the default social share card at static/images/og-default.png.

This is the fallback OG image used by PaperMod's opengraph partial when a post
does not set `cover.image` in its front matter. Set as the site-wide default
via `params.images = ["/images/og-default.png"]` in hugo.toml.

Why not Hugo's `images.Text` filter? It would tie us to a checked-in TTF, force
manual line-wrap handling for long post titles, and the marginal value of
per-post overlay is low when most flagship posts ship with hand-designed covers
anyway. This script generates a single static fallback that LinkedIn / X /
WhatsApp / Bluesky / Mastodon all show on any post without a cover.

To use a different font, point FONT_SANS / FONT_BOLD at a checked-in TTF and
re-run. The Liberation Sans defaults below are metric-equivalent to Arial and
ship with most Linux distros, so the script runs without extra setup.

Usage:
    python3 scripts/make-og-default.py
"""
from PIL import Image, ImageDraw, ImageFont
import os
from pathlib import Path

# Output relative to the repo root (this file lives in scripts/)
REPO_ROOT = Path(__file__).resolve().parent.parent
OUT = REPO_ROOT / "static" / "images" / "og-default.png"

W, H = 1200, 630

# Palette — matches .home-featured-visual bg (dark slate) and the warm clay
# accent that shows up across the site's editorial chrome.
BG = (15, 17, 21)              # #0F1115 dark slate
INK = (240, 238, 230)          # #F0EEE6 cream
INK_MUTED = (184, 180, 168)    # #B8B4A8 warm muted text
INK_DIM = (136, 136, 132)      # #888884 footer text
ACCENT = (201, 100, 66)        # #C96442 warm clay
HAIRLINE = (47, 49, 53)        # subtle border

# Fonts — Liberation Sans is the Linux Arial-equivalent and is on most distros.
# Swap to Inter TTF if you check one in.
FONT_SANS = "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf"


def main() -> None:
    img = Image.new("RGB", (W, H), BG)

    # Soft clay glow in the bottom-right via two layered ellipses on an alpha
    # overlay. PIL has no native gradient API; this is the cheap stand-in.
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.ellipse([W - 600, H - 600, W + 200, H + 200], fill=(*ACCENT, 18))
    od.ellipse([W - 380, H - 380, W + 80,  H + 80],  fill=(*ACCENT, 14))
    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")

    d = ImageDraw.Draw(img)

    # Eyebrow
    eyebrow = ImageFont.truetype(FONT_BOLD, 22)
    d.text((80, 78), "NDRANANDRAJ.COM", font=eyebrow, fill=ACCENT)
    d.line([(80, 116), (200, 116)], fill=ACCENT, width=2)

    # Title
    title_font = ImageFont.truetype(FONT_BOLD, 132)
    d.text((80, 200), "Anand's Blog", font=title_font, fill=INK)

    # Tagline (matches the homepage profile subtitle without the em dash)
    tag_font = ImageFont.truetype(FONT_SANS, 36)
    d.text((80, 372), "Tech, travel, photography, and random thoughts.",
           font=tag_font, fill=INK_MUTED)

    # Footer rule + two-up footer text
    d.line([(80, H - 84), (W - 80, H - 84)], fill=HAIRLINE, width=1)
    footer_font = ImageFont.truetype(FONT_SANS, 22)
    d.text((80, H - 60), "Personal blog by Anand",
           font=footer_font, fill=INK_DIM)

    right_label = "Read at ndranandraj.com  →"
    bbox = d.textbbox((0, 0), right_label, font=footer_font)
    d.text((W - 80 - (bbox[2] - bbox[0]), H - 60), right_label,
           font=footer_font, fill=INK_MUTED)

    # Small clay dot top-right, a quiet brand signal
    d.ellipse([W - 110, 90, W - 86, 114], fill=ACCENT)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT, "PNG", optimize=True)
    print(f"Wrote {OUT} ({os.path.getsize(OUT)} bytes, {img.size})")


if __name__ == "__main__":
    main()
