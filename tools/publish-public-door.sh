#!/usr/bin/env bash
# Publish public door + Path A concept to gh-pages (evoform.no).
# Research stays on main; public surface only.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
STAGE="$(mktemp -d)"
trap 'rm -rf "$STAGE"' EXIT

cp "$ROOT/index.html" "$ROOT/404.html" "$ROOT/CNAME" "$ROOT/.nojekyll" "$ROOT/version.json" "$STAGE/"
if [ -d "$ROOT/path-a" ]; then
  cp -R "$ROOT/path-a" "$STAGE/path-a"
fi
cd "$STAGE"
git init -q -b gh-pages
git config user.email "kai@revrune.local"
git config user.name "Kai"
git add -A
git commit -q -m "Publish public door + Path A $(date -u +%Y-%m-%dT%H:%MZ)"
git remote add origin git@github.com:revrune/evoform.git
git push -f origin gh-pages
echo "Pushed gh-pages. Check https://evoform.no/ and https://evoform.no/path-a/"
