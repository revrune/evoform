# Vercel deploy · primary path (LOCKED · permanent · 2026-08-08)

**Founder note:** Sites live on **Vercel**. GitHub is a **record** (source history), not the ship path. Do not burn turns on GHA tokens, `vercel login`, or waiting for Actions.

## Primary ship path (use this)

1. Edit sources under `~/evoform` (`index.html`, `evomarine/`, `path-a/`, `version.json`, …).
2. Stage: `bash tools/stage-public-door.sh`
3. Deploy production:

```bash
python3 tools/deploy-vercel-rest.py
# optional marker:
python3 tools/deploy-vercel-rest.py --marker "your-marker-name"
```

4. Verify: `https://www.evoform.no/version.json` and the pages you changed.

### Auth the script uses

| Item | Value |
|------|--------|
| Token | OAuth access token in `~/.grok/mcp_credentials.json` → key `vercel:https://mcp.vercel.com/` → `token_response.access_token` |
| Team | `team_QwxzlThVmQiaDdYIKaFY7gMB` (Leitner Learning) |
| Project | `prj_ODHEe1C3BtGhJSSDEvReNER2pBsE` · name **evoform-no** |
| API | Upload each staged file: `POST https://api.vercel.com/v2/files?teamId=…` with header `x-vercel-digest: <sha1 hex>` · then `POST https://api.vercel.com/v13/deployments?teamId=…&forceNew=1` with `target: "production"` |

This is the same auth Vercel MCP uses. If REST returns `invalidToken` / 403, re-auth **Vercel MCP** in Grok (not GitHub secrets).

### Probe token (10s)

```bash
python3 - <<'PY'
import json, urllib.request
from pathlib import Path
t=json.loads(Path.home().joinpath(".grok/mcp_credentials.json").read_text())["vercel:https://mcp.vercel.com/"]["token_response"]["access_token"]
req=urllib.request.Request(
  "https://api.vercel.com/v9/projects/prj_ODHEe1C3BtGhJSSDEvReNER2pBsE?teamId=team_QwxzlThVmQiaDdYIKaFY7gMB",
  headers={"Authorization": f"Bearer {t}"},
)
print(urllib.request.urlopen(req, timeout=20).status)
PY
```

`200` = good. Do **not** use `/v2/user` as a health check (team tokens often 404 there).

## Forbidden defaults (stop doing these)

| Wrong path | Why |
|------------|-----|
| `gh run` / **Deploy public door** GHA as first choice | `VERCEL_TOKEN` secret is **invalid** (2026-08-08). Wastes ~1–5 min per fail. |
| `vercel deploy --token "$VERCEL_TOKEN"` with GHA secret | Same dead token. |
| Assume `vercel whoami` / CLI login always available | Local CLI often has **no credentials**. |
| Wait for GitHub Actions after every copy tweak | Vercel is production. Git push is optional archive. |

## Secondary (optional only)

| Path | When |
|------|------|
| `git push origin main` | Archive source after ship · **not** required for live evoform.no |
| GHA deploy workflow | Only after someone **replaces** `VERCEL_TOKEN` secret with a valid token and verifies one green run |
| `tools/publish-public-door.sh` | Redirects to `deploy-vercel-rest.py` (CLI path retired) |

## Sisters (same team pattern)

| Site | Domain | Notes |
|------|--------|--------|
| EvoForm | evoform.no | project **evoform-no** · this doc |
| CetaVox | cetavox.com | separate tree · same Vercel MCP auth pattern when deploying |
| Leitner Learning | leitnerlearning.com | sibling · same house |

## Done bar for Kai

- Ship to **www.evoform.no** via `tools/deploy-vercel-rest.py` (or equivalent REST with MCP token).
- Do **not** open with “let me try GHA / refresh VERCEL_TOKEN” unless REST auth is proven dead.
- On REST auth death: re-auth Vercel MCP once, then deploy · do not thrash GitHub secrets first.

---

*Locked 2026-08-08 · Team Rua · Kai · Vercel primary · GitHub = record*
