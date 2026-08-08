#!/usr/bin/env python3
"""Gate: Inspiration Board + Visual Concepts match locked home/hub grammar.

Drives the real staged/source HTML files (not a reimplementation of the pages).
Exit 0 only when acceptance criteria hold on disk.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOARD = ROOT / "path-a" / "board" / "index.html"
PATH_A = ROOT / "path-a" / "index.html"
HOME = ROOT / "index.html"
HUB = ROOT / "evomarine" / "index.html"


def fail(msg: str) -> None:
    print(f"FAIL: {msg}", file=sys.stderr)
    sys.exit(1)


def must_contain(text: str, needle: str, where: str) -> None:
    if needle not in text:
        fail(f"{where}: missing {needle!r}")


def must_not_contain(text: str, needle: str, where: str) -> None:
    if needle in text:
        fail(f"{where}: must not contain {needle!r}")


def main() -> None:
    board = BOARD.read_text(encoding="utf-8")
    path_a = PATH_A.read_text(encoding="utf-8")
    home = HOME.read_text(encoding="utf-8")
    hub = HUB.read_text(encoding="utf-8")

    # --- Board chrome ---
    must_contain(board, 'href="/"', "board brand home")
    must_contain(board, "Shaped by Nature", "board north")
    must_contain(board, "EvoMarine", "board sibling")
    must_contain(board, "Visual Concepts", "board sibling name")
    must_not_contain(board, 'href="/path-a/">Path</a>', "board old Path label")
    must_not_contain(board, "Working board", "board status line")
    must_not_contain(board, "lede-more", "board second lede class")
    # No Back chrome
    if re.search(r">\s*Back\s*<", board):
        fail("board: Back chrome present")
    # Header stack
    must_contain(board, "Inspiration", "board kicker")
    must_contain(board, "<h1>Board</h1>", "board h1")
    # 01-08 section ids
    for sid in (
        "hypothesis",
        "drones",
        "teacher",
        "architecture",
        "transfer",
        "grounding",
        "open",
        "horizon",
    ):
        must_contain(board, f'id="{sid}"', f"board section {sid}")
    # Top nav must not be multi-anchor app nav
    for anchor in ("#hypothesis", "#drones", "#teacher", "#architecture"):
        # anchors may live in TOC, not top nav-links block
        nav_block = re.search(
            r'<nav class="nav-links"[^>]*>(.*?)</nav>', board, re.S
        )
        if not nav_block:
            fail("board: missing nav-links")
        if anchor in nav_block.group(1):
            fail(f"board: section anchor {anchor} still in top nav")

    # --- Visual Concepts ---
    must_contain(path_a, "Shaped by Nature", "path-a north")
    must_contain(path_a, "Inspiration Board", "path-a sibling")
    must_contain(path_a, "EvoMarine", "path-a sibling")
    must_contain(path_a, 'id="explorer"', "path-a explorer")
    must_contain(path_a, 'id="gallery"', "path-a gallery")
    must_contain(path_a, 'id="gallery-grid"', "path-a gallery grid")
    must_contain(path_a, "Mass-first P1", "path-a envelope")
    must_not_contain(path_a, "fonts.googleapis.com", "path-a google fonts")
    must_not_contain(path_a, "Instrument Serif", "path-a product font")
    must_not_contain(path_a, 'class="refuse"', "path-a refuse block")
    must_not_contain(path_a, ">Out<", "path-a Out label")
    must_not_contain(path_a, "Thruster-box default", "path-a refuse chips")
    must_not_contain(path_a, 'class="wins"', "path-a brochure wins")
    must_not_contain(path_a, "btn-primary", "path-a primary CTA stack")
    must_not_contain(path_a, "Prototype board", "path-a old CTA label")
    if re.search(r">\s*Back\s*<", path_a):
        fail("path-a: Back chrome present")
    must_contain(path_a, "Visual Concepts", "path-a identity")
    # System type tokens
    must_contain(path_a, "Iowan Old Style", "path-a display font family")
    must_contain(path_a, "system-ui", "path-a system ui font")

    # --- Frozen home + hub (content fingerprints) ---
    must_contain(home, "Vehicles Shaped by Nature", "home title slogan")
    must_contain(home, "Shaped by Nature", "home hero")
    must_contain(home, "EvoMarine", "home vertical")
    must_contain(hub, "Quiet Extended Presence", "hub lede")
    must_contain(hub, "Inspiration Board", "hub path")
    must_contain(hub, "Visual Concepts", "hub path")
    must_contain(hub, "Built Prototypes", "hub path soon")

    print("PASS: depth-pass gates on board + path-a + frozen home/hub")


if __name__ == "__main__":
    main()
