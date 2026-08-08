#!/usr/bin/env python3
"""Gate: EvoMarine depth + redundancy ownership on Board and Visual Concepts.

Drives the real source HTML files (not a reimplementation of the pages).
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

EXPLORER_DEFAULT = "/path-a/mockups/form-threequarter.jpg"


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
    must_not_contain(board, 'href="/path-a/">Path</a>', "board old Path label")
    must_not_contain(board, "Working board", "board status line")
    must_not_contain(board, "lede-more", "board second lede class")
    if re.search(r">\s*Back\s*<", board):
        fail("board: Back chrome present")
    must_contain(board, "Inspiration", "board kicker")
    must_contain(board, "<h1>Board</h1>", "board h1")
    # Mirror Concepts: EvoMarine only in top nav (not Visual Concepts label)
    board_nav = re.search(r'<nav class="nav-links"[^>]*>(.*?)</nav>', board, re.S)
    if not board_nav:
        fail("board: missing nav-links")
    if "Visual Concepts" in board_nav.group(1):
        fail("board: Visual Concepts should not appear in top nav")
    if "EvoMarine" not in board_nav.group(1):
        fail("board: EvoMarine missing from top nav")
    # No page lede under Board title (Concepts pattern)
    if re.search(r"<h1>Board</h1>\s*<p class=\"(page-sub|lede)\"", board):
        fail("board: no sub/lede under Board title")
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
        # Non-empty body after section open
        m = re.search(rf'id="{sid}"[^>]*>.*?</section>', board, re.S)
        if not m or len(m.group(0)) < 200:
            fail(f"board section {sid}: body too thin")
    nav_block = re.search(r'<nav class="nav-links"[^>]*>(.*?)</nav>', board, re.S)
    if not nav_block:
        fail("board: missing nav-links")
    for anchor in ("#hypothesis", "#drones", "#teacher", "#architecture"):
        if anchor in nav_block.group(1):
            fail(f"board: section anchor {anchor} still in top nav")

    # Board owns envelope chips + sequence
    # Envelope ownership chips (plain labels OK)
    if "Heavy first build" not in board and "Mass-first P1" not in board:
        fail("board envelope chips: missing first-build scale chip")
    must_contain(board, "0–50 m first", "board depth chip")
    must_contain(board, "Boat or crane", "board deploy chip")
    if "Mic + camera" not in board and "Hydrophone" not in board:
        fail("board sensors chip missing")
    must_contain(board, 'id="sequence"', "board sequence ownership")
    must_contain(board, "<strong>Now</strong>", "board sequence Now")
    must_contain(board, "<strong>Next</strong>", "board sequence Next")
    must_contain(board, "<strong>Later</strong>", "board sequence Later")

    # --- Visual Concepts chrome + form UI ---
    must_contain(path_a, "Shaped by Nature", "path-a north")
    must_contain(path_a, "EvoMarine", "path-a sibling")
    must_contain(path_a, 'id="explorer"', "path-a explorer")
    must_contain(path_a, 'id="gallery"', "path-a gallery")
    must_contain(path_a, 'id="gallery-grid"', "path-a gallery grid")
    must_contain(path_a, "view-tabs", "path-a view tabs")
    must_contain(path_a, "hotspot", "path-a hotspot wiring")
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
    must_contain(path_a, "Iowan Old Style", "path-a display font family")
    must_contain(path_a, "system-ui", "path-a system ui font")

    # --- Redundancy: no dual form stack ---
    must_not_contain(path_a, "hero-visual", "path-a dual hero class")
    # Decorative hero image using same path as explorer default (outside #viewer)
    outside_viewer = re.sub(
        r'<div class="viewer"[^>]*>.*?</div>', "", path_a, count=1, flags=re.S
    )
    # Still allow og:image and JS view config; ban standalone img tags of default mockup
    standalone = re.findall(
        rf'<img[^>]+src="{re.escape(EXPLORER_DEFAULT)}"[^>]*>', outside_viewer
    )
    # viewer-img is inside .viewer (stripped); any remaining img with that src is a dual stack
    if standalone:
        fail(
            "path-a: decorative form-threequarter img outside explorer viewer "
            f"({len(standalone)} occurrence(s))"
        )

    # --- Redundancy: Concepts must not own full envelope/sequence sections ---
    must_not_contain(path_a, 'id="specs"', "path-a full envelope section")
    must_not_contain(path_a, "First-build envelope", "path-a envelope heading")
    must_not_contain(path_a, 'id="sequence"', "path-a sequence section id")
    must_not_contain(path_a, 'class="sequence"', "path-a sequence list")
    # Chip-style full duplicate of board envelope
    for fact in ("0–50 m first", "Boat or crane", "Heavy first build", "Mass-first P1"):
        if f'<span class="chip">{fact}' in path_a or re.search(
            rf"<p class=\"v\">{re.escape(fact)}", path_a
        ):
            fail(f"path-a: duplicate envelope fact presentation for {fact!r}")

    # Gallery not pure re-list of explorer view set alone
    must_contain(path_a, "const gallery", "path-a gallery data")
    gal_m = re.search(r"const gallery\s*=\s*\[(.*?)\];", path_a, re.S)
    if not gal_m:
        fail("path-a: cannot parse gallery array")
    gal_body = gal_m.group(1)
    explorer_only = (
        "form-threequarter.jpg",
        "form-profile.jpg",
        "form-top.jpg",
        "systems-cutaway.jpg",
    )
    for name in explorer_only:
        if name in gal_body:
            fail(f"path-a gallery re-lists explorer view image {name}")
    if "hover.jpg" not in gal_body and "boat-deploy.jpg" not in gal_body:
        fail("path-a gallery lacks non-explorer studies")

    # Quiet pointer into Board notes from hotspots
    must_contain(path_a, "Board notes", "path-a board pointer")

    # --- Frozen home + hub ---
    must_contain(home, "Vehicles Shaped by Nature", "home title slogan")
    must_contain(home, "Shaped by Nature", "home hero")
    must_contain(home, "EvoMarine", "home vertical")
    must_contain(hub, "Quiet Extended Presence", "hub lede")
    must_contain(hub, "Inspiration Board", "hub path")
    must_contain(hub, "Visual Concepts", "hub path")
    must_contain(hub, "Built Prototypes", "hub path soon")
    # Hub stays thin one-line paths (no door job essay)
    must_not_contain(hub, "none yet", "hub no empty-state essay")
    must_not_contain(hub, "Why and how", "hub no board job line")
    must_not_contain(hub, "p-job", "hub no p-job chrome")

    # Board lead phrase + Concepts bridge (Eli craft)
    # QEP may live in body/meta, not forced under Board title
    must_contain(path_a, "EvoMarine", "concepts nav sibling")
    # Nav should not label this page as Inspiration Board
    nav = re.search(r'<nav class="nav-links"[^>]*>(.*?)</nav>', path_a, re.S)
    if nav and "Inspiration Board" in nav.group(1):
        fail("path-a: Inspiration Board should not appear in top nav")
    must_contain(path_a, "<h2>Leatherback sea turtle</h2>", "concepts title")
    must_not_contain(path_a, "Leatherback sea turtle concept", "concepts no double concept")
    must_not_contain(path_a, "Leatherback Sea Turtle inspired", "concepts no redundant inspired line")
    must_not_contain(path_a, "Leatherback Path A", "concepts no Path A title")
    must_not_contain(path_a, "Pictures and hotspots", "concepts no lede fluff")
    must_contain(path_a, "board:", "concepts hotspot board links")
    must_contain(path_a, "system:", "concepts gallery system labels")

    print("PASS: depth + redundancy + Eli craft gates on hub/board/path-a")



if __name__ == "__main__":
    main()
