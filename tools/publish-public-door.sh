#!/usr/bin/env bash
# Publish public door to Vercel production (evoform.no).
# PRIMARY path locked 2026-08-08: MCP OAuth REST — not GHA, not vercel CLI login.
# See: docs/ops/vercel-deploy-primary-2026-08-08.md
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

exec python3 "$ROOT/tools/deploy-vercel-rest.py" "$@"
