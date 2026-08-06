#!/usr/bin/env python3
"""Structural check: Path A opportunity briefs + papers note exist with required headings."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = {
    "docs/path-a-papers-working-note-2026-08-06.md": [
        r"## Sources",
        r"DOI|doi\.org|ISBN|ieeexplore",
    ],
    "briefs/path-a-quiet-multimode-propulsion.md": [
        r"## 1\. Design problem",
        r"[Kk]ill",
        r"[Ll]ane",
        r"path-a-job-card",
    ],
    "briefs/path-a-riblets-regime-matched.md": [
        r"## 1\. Design problem",
        r"[Kk]ill",
        r"[Ll]ane",
        r"path-a-job-card",
    ],
    "briefs/path-a-hover-station-keep.md": [
        r"## 1\. Design problem",
        r"[Kk]ill",
        r"[Ll]ane",
        r"path-a-job-card",
    ],
    "briefs/path-a-hydrophone-first-layout.md": [
        r"## 1\. Design problem",
        r"[Kk]ill",
        r"[Ll]ane",
        r"path-a-job-card",
    ],
    "briefs/path-a-foul-aware-outer-skin.md": [
        r"## 1\. Design problem",
        r"[Kk]ill",
        r"[Ll]ane",
        r"path-a-job-card",
    ],
    "briefs/path-a-abort-on-avoidance-law.md": [
        r"PRODUCT LAW|product law",
        r"Abort|abort",
        r"path-a-job-card",
    ],
    "briefs/leatherback-osteoderm-volume-following.md": [
        r".+",  # exists; secondary pointer target
    ],
    "docs/path-a-first-experiment-plan-2026-08-06.md": [
        r"LOCKED|PERMANENT",
        r"Quiet multi-mode|sparse thrust|bet 1",
        r"Hydrophone|bet 4",
        r"[Kk]ill",
        r"path-a-job-card",
        r"not a fab|Not a fab|fab still|later go",
    ],
    "docs/path-a-research-stack-permanent-2026-08-06.md": [
        r"First-experiment plan",
        r"LOCKED · PERMANENT",
    ],
}


def main() -> int:
    failed = 0
    for rel, patterns in REQUIRED.items():
        path = ROOT / rel
        if not path.is_file():
            print(f"FAIL missing file: {rel}")
            failed += 1
            continue
        text = path.read_text(encoding="utf-8")
        for pat in patterns:
            if not re.search(pat, text, re.MULTILINE | re.IGNORECASE):
                print(f"FAIL {rel}: no match for /{pat}/")
                failed += 1
        # papers note: count DOI-like or distinct sources
        if "papers-working-note" in rel:
            dois = re.findall(r"10\.\d{4,}/[^\s\)]+", text)
            # also count numbered sources under ## Sources
            nums = re.findall(r"^\d+\.\s+\*\*", text, re.M)
            print(f"OK {rel}: {len(dois)} DOI strings, {len(nums)} numbered sources")
            if len(nums) < 10 and len(dois) < 10:
                print(f"FAIL {rel}: need ≥10 sources")
                failed += 1
        else:
            print(f"OK {rel}")

    # job card still locked
    jc = (ROOT / "briefs/path-a-job-card.md").read_text(encoding="utf-8")
    if "LOCKED" not in jc or "PERMANENT" not in jc:
        print("FAIL job card not LOCKED PERMANENT")
        failed += 1
    else:
        print("OK job card LOCKED PERMANENT")

    # index not expanded with waitlist
    idx = (ROOT / "index.html").read_text(encoding="utf-8")
    if re.search(r"waitlist|for sale|join the mission", idx, re.I):
        print("FAIL index.html has marketing chrome")
        failed += 1
    else:
        print("OK index.html no waitlist/sale chrome")

    if failed:
        print(f"TOTAL FAIL {failed}")
        return 1
    print("ALL STRUCTURE CHECKS PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
