#!/usr/bin/env bash
# Publish thin public door to gh-pages (evoform.no).
# Research stays on main; door files only (incl. version.json).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
STAGE="$(mktemp -d)"
trap 'rm -rf "$STAGE"' EXIT

cp "$ROOT/index.html" "$ROOT/404.html" "$ROOT/CNAME" "$ROOT/.nojekyll" "$ROOT/version.json" "$STAGE/"
cd "$STAGE"
git init -q -b gh-pages
git config user.email "kai@revrune.local"
git config user.name "Kai"
git add index.html 404.html CNAME .nojekyll version.json
git commit -q -m "Publish thin public door $(date -u +%Y-%m-%dT%H:%MZ)"
git remote add origin git@github.com:revrune/evoform.git
git push -f origin gh-pages
echo "Pushed gh-pages. Check https://evoform.no/version.json (hard-refresh if CDN lags)."
