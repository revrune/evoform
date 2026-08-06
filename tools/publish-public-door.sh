#!/usr/bin/env bash
# Publish thin public door to gh-pages (evoform.no).
# Research stays on main; only these four files go live.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
STAGE="$(mktemp -d)"
trap 'rm -rf "$STAGE"' EXIT

cp "$ROOT/index.html" "$ROOT/404.html" "$ROOT/CNAME" "$ROOT/.nojekyll" "$STAGE/"
cd "$STAGE"
git init -q -b gh-pages
git config user.email "kai@revrune.local"
git config user.name "Kai"
git add index.html 404.html CNAME .nojekyll
git commit -q -m "Publish thin public door $(date -u +%Y-%m-%dT%H:%MZ)"
git remote add origin git@github.com:revrune/evoform.git
git push -f origin gh-pages
echo "Pushed gh-pages. Check https://evoform.no (hard-refresh if CDN lags)."
