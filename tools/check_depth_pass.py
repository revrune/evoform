#!/usr/bin/env python3
"""Permanent gate: public chrome + ownership for Board and Visual Concepts.

Law: docs/public-chrome-board-concepts-locked-2026-08-08.md
Drives the real source HTML (not a reimplementation). Exit 0 only if locked
rules hold on disk.
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
SEAL = ROOT / "docs" / "public-chrome-board-concepts-locked-2026-08-08.md"

EXPLORER_DEFAULT = "/path-a/mockups/form-threequarter.jpg"
BOARD_SECTIONS = (
    "hypothesis",
    "drones",
    "teacher",
    "architecture",
    "transfer",
    "grounding",
    "open",
    "horizon",
)
# Brochure / jargon phrases banned as public voice (body text, not asset paths)
BANNED_PUBLIC = (
    "form language",
    "regime-matched",
    "streamwise geometry",
    "control path live",
    "transfer stack",
)


def fail(msg: str) -> None:
    print(f"FAIL: {msg}", file=sys.stderr)
    sys.exit(1)


def must_contain(text: str, needle: str, where: str) -> None:
    if needle not in text:
        fail(f"{where}: missing {needle!r}")


def must_not_contain(text: str, needle: str, where: str) -> None:
    if needle in text:
        fail(f"{where}: must not contain {needle!r}")


def nav_inner(html: str, where: str) -> str:
    m = re.search(r'<nav class="nav-links"[^>]*>(.*?)</nav>', html, re.S)
    if not m:
        fail(f"{where}: missing nav-links")
    return m.group(1)


def assert_shared_chrome(html: str, where: str) -> None:
    """Chrome law §1 — both deep pages."""
    must_contain(html, 'href="/"', f"{where} brand→home")
    must_contain(html, "Shaped by Nature", f"{where} north")
    must_contain(html, 'href="/evomarine/"', f"{where} EvoMarine")
    if re.search(r">\s*Back\s*<", html):
        fail(f"{where}: Back chrome present")
    nav = nav_inner(html, where)
    if "Inspiration Board" in nav:
        fail(f"{where}: Inspiration Board must not appear in top nav")
    if "Visual Concepts" in nav:
        fail(f"{where}: Visual Concepts must not appear in top nav")
    # EvoMarine is the only path link in nav-links
    if not re.search(r'href="/evomarine/"[^>]*>\s*EvoMarine\s*<', nav):
        fail(f"{where}: EvoMarine missing from top nav")
    # No multi-anchor app nav
    for anchor in ("#hypothesis", "#drones", "#teacher", "#architecture", "#explorer"):
        if anchor in nav:
            fail(f"{where}: section anchor {anchor} still in top nav")


def main() -> None:
    if not SEAL.is_file():
        fail(f"missing permanent seal: {SEAL.relative_to(ROOT)}")

    board = BOARD.read_text(encoding="utf-8")
    path_a = PATH_A.read_text(encoding="utf-8")
    home = HOME.read_text(encoding="utf-8")
    hub = HUB.read_text(encoding="utf-8")

    # --- §1 Chrome: both pages ---
    assert_shared_chrome(board, "board")
    assert_shared_chrome(path_a, "path-a")

    must_contain(board, 'class="page-kicker">Inspiration</', "board kicker")
    must_contain(board, "<h1>Board</h1>", "board h1")
    if re.search(r"<h1>Board</h1>\s*<p class=\"(page-sub|lede)\"", board):
        fail("board: no sub/lede under Board title")

    must_contain(path_a, 'class="page-kicker">Visual</', "path-a kicker")
    must_contain(path_a, "<h1>Concepts</h1>", "path-a h1")
    if re.search(r"<h1>Concepts</h1>\s*<p class=\"(page-sub|lede)\"", path_a):
        fail("path-a: no sub/lede under Concepts title")

    # --- §2 Ownership: Board ---
    for sid in BOARD_SECTIONS:
        must_contain(board, f'id="{sid}"', f"board section {sid}")
        m = re.search(rf'id="{sid}"[^>]*>.*?</section>', board, re.S)
        if not m or len(m.group(0)) < 200:
            fail(f"board section {sid}: body too thin")

    if "Heavy first build" not in board and "Mass-first P1" not in board:
        fail("board: missing first-build scale chip")
    must_contain(board, "0–50 m first", "board depth chip")
    must_contain(board, "Boat or crane", "board deploy chip")
    if "Mic + camera" not in board and "Hydrophone" not in board:
        fail("board: sensors chip missing")
    must_contain(board, 'id="sequence"', "board sequence ownership")
    must_contain(board, "<strong>Now</strong>", "board sequence Now")
    must_contain(board, "<strong>Next</strong>", "board sequence Next")
    must_contain(board, "<strong>Later</strong>", "board sequence Later")

    # --- §2 Ownership: Concepts form UI only ---
    must_contain(path_a, 'id="explorer"', "path-a explorer")
    must_contain(path_a, 'id="gallery"', "path-a gallery")
    must_contain(path_a, 'id="gallery-grid"', "path-a gallery grid")
    must_contain(path_a, "view-tabs", "path-a view tabs")
    must_contain(path_a, "hotspot", "path-a hotspot wiring")
    must_contain(path_a, "board:", "path-a hotspot board links")
    must_contain(path_a, "Board notes", "path-a quiet board pointer")
    must_contain(path_a, "<h2>Leatherback sea turtle</h2>", "path-a form title")
    must_contain(path_a, "study-tabs", "path-a study tabs")
    must_contain(path_a, 'id: "outline"', "path-a Outline study")
    must_contain(path_a, 'id: "packed"', "path-a Packed study")
    must_contain(path_a, 'id: "long"', "path-a Long study")
    for rel in (
        "path-a/mockups/form-threequarter.jpg",
        "path-a/mockups/study-packed-form.jpg",
        "path-a/mockups/study-long-form.jpg",
    ):
        if not (ROOT / rel).is_file():
            fail(f"path-a: missing keeper still {rel}")

    must_not_contain(path_a, 'id="specs"', "path-a no full envelope section")
    must_not_contain(path_a, "First-build envelope", "path-a no envelope heading")
    must_not_contain(path_a, 'id="sequence"', "path-a no sequence section")
    must_not_contain(path_a, 'class="sequence"', "path-a no sequence list")
    for fact in ("0–50 m first", "Boat or crane", "Heavy first build", "Mass-first P1"):
        if f'<span class="chip">{fact}' in path_a or re.search(
            rf'<p class="v">{re.escape(fact)}', path_a
        ):
            fail(f"path-a: duplicate envelope fact presentation for {fact!r}")

    must_not_contain(path_a, "hero-visual", "path-a no dual hero")
    outside_viewer = re.sub(
        r'<div class="viewer"[^>]*>.*?</div>', "", path_a, count=1, flags=re.S
    )
    if re.findall(
        rf'<img[^>]+src="{re.escape(EXPLORER_DEFAULT)}"[^>]*>', outside_viewer
    ):
        fail("path-a: decorative form-threequarter outside explorer viewer")

    gal_m = re.search(r"const gallery\s*=\s*\[(.*?)\];", path_a, re.S)
    if not gal_m:
        fail("path-a: cannot parse gallery array")
    gal_body = gal_m.group(1)
    for name in (
        "form-threequarter.jpg",
        "form-profile.jpg",
        "form-top.jpg",
        "systems-cutaway.jpg",
    ):
        if name in gal_body:
            fail(f"path-a gallery re-lists explorer view {name}")
    if "hover.jpg" not in gal_body and "boat-deploy.jpg" not in gal_body:
        fail("path-a gallery lacks non-explorer studies")
    must_contain(path_a, "system:", "path-a gallery system labels")

    # Product-brochure leftovers
    must_not_contain(path_a, "fonts.googleapis.com", "path-a no Google fonts")
    must_not_contain(path_a, "Instrument Serif", "path-a no product font")
    must_not_contain(path_a, 'class="refuse"', "path-a no refuse block")
    must_not_contain(path_a, 'class="wins"', "path-a no brochure wins")
    must_not_contain(path_a, "btn-primary", "path-a no primary CTA stack")
    must_not_contain(path_a, "Leatherback Path A", "path-a no Path A title")
    must_not_contain(path_a, "Leatherback sea turtle concept", "path-a no double concept")
    must_contain(path_a, "Iowan Old Style", "path-a house display font")
    must_contain(path_a, "system-ui", "path-a system ui font")

    # --- §3 Public English (banned stacks in body copy) ---
    for page, label in ((board, "board"), (path_a, "path-a")):
        body = page.split("<body", 1)[-1].lower()
        # Ignore script asset paths loosely: check visible-ish by stripping tags first
        visible = re.sub(r"<script[\s\S]*?</script>", " ", body)
        visible = re.sub(r"<[^>]+>", " ", visible)
        for phrase in BANNED_PUBLIC:
            if phrase in visible:
                fail(f"{label}: banned public phrase {phrase!r}")
        if "—" in page.split("<body", 1)[-1]:
            # Allow in comments only; ban in body markup text nodes roughly
            if re.search(r">[^<]*—[^<]*<", page.split("<body", 1)[-1]):
                fail(f"{label}: em dash in public markup text")

    # --- §4 Home + hub frozen thin ---
    must_contain(home, "Vehicles Shaped by Nature", "home title slogan")
    must_contain(home, "Shaped by Nature", "home hero")
    must_contain(home, "EvoMarine", "home vertical")
    must_contain(home, 'href="/evomarine/"', "home EvoMarine link")
    must_contain(hub, "Quiet Extended Presence", "hub lede")
    must_contain(hub, "Inspiration Board", "hub path")
    must_contain(hub, "Visual Concepts", "hub path")
    must_contain(hub, "Built Prototypes", "hub path soon")
    must_not_contain(hub, "none yet", "hub no empty-state essay")
    must_not_contain(hub, "Why and how", "hub no door job line")
    must_not_contain(hub, "p-job", "hub no p-job chrome")

    # House strip on every public page (2026-08-15)
    for page, label in (
        (home, "home"),
        (hub, "evomarine"),
        (path_a, "path-a"),
        (board, "board"),
    ):
        must_contain(page, "Revealing Mystery", f"{label} house slogan")
        must_contain(page, "cetavox.com", f"{label} CetaVox")
        must_contain(page, "leitnerlearning.com", f"{label} Leitner")

    print("PASS: permanent chrome + ownership gate (board · concepts · home · hub)")
    print(f"  seal: {SEAL.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
