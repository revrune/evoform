#!/usr/bin/env bash
# Stage thin public door only (research tree stays off the public surface).
# Output: _public/  — used by vercel.json build + local publish script.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="${1:-"$ROOT/_public"}"
rm -rf "$OUT"
mkdir -p "$OUT"
cp "$ROOT/index.html" "$ROOT/404.html" "$ROOT/version.json" "$OUT/"
if [ -d "$ROOT/path-a" ]; then
  cp -R "$ROOT/path-a" "$OUT/path-a"
fi
if [ -d "$ROOT/evomarine" ]; then
  cp -R "$ROOT/evomarine" "$OUT/evomarine"
fi
if [ -d "$ROOT/brand" ]; then
  cp -R "$ROOT/brand" "$OUT/brand"
fi
# Explicitly not copied: briefs/ docs/ AGENTS.md README.md prototypes/ CNAME .nojekyll tools/
echo "Staged public door → $OUT"
find "$OUT" -type f | sort
