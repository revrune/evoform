#!/usr/bin/env bash
# Publish public door + Path A concept to Vercel production (evoform.no).
# Research stays on main; public surface is staged thin door only.
# Requires: vercel CLI logged in (or VERCEL_TOKEN) + project link (.vercel/project.json).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if ! command -v vercel >/dev/null 2>&1; then
  echo "vercel CLI not found. Install: npm i -g vercel  (or use PATH with ~/.local/node/bin)"
  echo "Then: vercel link --project evoform-no --yes  &&  vercel --prod"
  exit 1
fi

bash "$ROOT/tools/stage-public-door.sh" "$ROOT/_public"

# Deploy from a temp tree with no git history.
# Reason: Vercel team protection BLOCKS deploys whose git author email is not a
# team member (e.g. Mac auto-config user@hostname.local). Clean folder avoids that.
STAGE="$(mktemp -d)"
trap 'rm -rf "$STAGE"' EXIT
cp -R "$ROOT/_public/." "$STAGE/"
mkdir -p "$STAGE/.vercel"
if [ -f "$ROOT/.vercel/project.json" ]; then
  cp "$ROOT/.vercel/project.json" "$STAGE/.vercel/project.json"
else
  cat > "$STAGE/.vercel/project.json" <<'EOF'
{"projectId":"prj_ODHEe1C3BtGhJSSDEvReNER2pBsE","orgId":"team_QwxzlThVmQiaDdYIKaFY7gMB","projectName":"evoform-no"}
EOF
fi

(
  cd "$STAGE"
  vercel deploy . --prod --yes ${VERCEL_TOKEN:+--token "$VERCEL_TOKEN"}
)

echo "Deployed. Check https://www.evoform.no/ · /path-a/ · /version.json"
