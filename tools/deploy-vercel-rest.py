#!/usr/bin/env python3
"""Deploy staged EvoForm public door to Vercel production.

PRIMARY ship path (locked 2026-08-08):
  Auth = Grok Vercel MCP OAuth token (~/.grok/mcp_credentials.json)
  API  = REST file upload + deployment create
  NOT  = GitHub Actions VERCEL_TOKEN, vercel CLI login

Usage:
  bash tools/stage-public-door.sh          # if sources changed
  python3 tools/deploy-vercel-rest.py
  python3 tools/deploy-vercel-rest.py --marker my-marker --skip-stage
  python3 tools/deploy-vercel-rest.py --probe   # auth check only

Docs: docs/ops/vercel-deploy-primary-2026-08-08.md
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "_public"
CREDS = Path.home() / ".grok" / "mcp_credentials.json"
MCP_KEY = "vercel:https://mcp.vercel.com/"

TEAM_ID = "team_QwxzlThVmQiaDdYIKaFY7gMB"
PROJECT_ID = "prj_ODHEe1C3BtGhJSSDEvReNER2pBsE"
PROJECT_NAME = "evoform-no"


def die(msg: str, code: int = 1) -> None:
    print(f"FAIL: {msg}", file=sys.stderr)
    sys.exit(code)


def load_token() -> str:
    if not CREDS.is_file():
        die(
            f"missing {CREDS} — re-auth Vercel MCP in Grok, then retry. "
            "Do not fall back to GHA VERCEL_TOKEN."
        )
    data = json.loads(CREDS.read_text(encoding="utf-8"))
    entry = data.get(MCP_KEY) or data.get("vercel")
    if not entry:
        die(f"no {MCP_KEY!r} entry in mcp_credentials — re-auth Vercel MCP")
    tr = entry.get("token_response") or {}
    token = tr.get("access_token")
    if not token:
        die("mcp_credentials has no access_token — re-auth Vercel MCP")
    return token


def api(
    method: str,
    url: str,
    token: str,
    *,
    data: bytes | None = None,
    content_type: str | None = None,
    extra_headers: dict | None = None,
    timeout: int = 180,
) -> tuple[int, bytes]:
    headers = {"Authorization": f"Bearer {token}"}
    if content_type:
        headers["Content-Type"] = content_type
    if extra_headers:
        headers.update(extra_headers)
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()


def probe(token: str) -> None:
    # Team tokens often 404 /v2/user — probe project instead.
    code, body = api(
        "GET",
        f"https://api.vercel.com/v9/projects/{PROJECT_ID}?teamId={TEAM_ID}",
        token,
        timeout=30,
    )
    if code != 200:
        die(
            f"auth probe failed HTTP {code}: {body[:240]!r}. "
            "Re-auth Vercel MCP. Do not thrash GHA secrets."
        )
    meta = json.loads(body)
    print(f"PROBE_OK project={meta.get('name')} id={meta.get('id')}")


def stage() -> None:
    script = ROOT / "tools" / "stage-public-door.sh"
    subprocess.check_call(["bash", str(script)], cwd=str(ROOT))


def upload_file(token: str, content: bytes) -> str:
    digest = hashlib.sha1(content).hexdigest()
    code, body = api(
        "POST",
        f"https://api.vercel.com/v2/files?teamId={TEAM_ID}",
        token,
        data=content,
        content_type="application/octet-stream",
        extra_headers={
            "Content-Length": str(len(content)),
            "x-vercel-digest": digest,
        },
    )
    if code not in (200, 201, 409):
        die(f"file upload HTTP {code}: {body[:300]!r}")
    return digest


def deploy(token: str, marker: str | None) -> str:
    if not PUBLIC.is_dir():
        die(f"missing staged tree {PUBLIC} — run stage-public-door.sh first")

    files_meta = []
    for path in sorted(PUBLIC.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(PUBLIC).as_posix()
        content = path.read_bytes()
        digest = upload_file(token, content)
        files_meta.append({"file": rel, "sha": digest, "size": len(content)})
        print(f"  up {rel} ({len(content)} B)")

    payload: dict = {
        "name": PROJECT_NAME,
        "project": PROJECT_ID,
        "files": files_meta,
        "projectSettings": {
            "framework": None,
            "buildCommand": None,
            "installCommand": None,
            "outputDirectory": None,
        },
        "target": "production",
    }
    if marker:
        payload["meta"] = {"marker": marker, "source": "deploy-vercel-rest"}

    code, body = api(
        "POST",
        f"https://api.vercel.com/v13/deployments?teamId={TEAM_ID}&forceNew=1",
        token,
        data=json.dumps(payload).encode(),
        content_type="application/json",
    )
    if code not in (200, 201):
        die(f"create deployment HTTP {code}: {body[:400]!r}")

    dep = json.loads(body)
    dep_id = dep["id"]
    print(f"DEPLOY {dep_id} url={dep.get('url')} state={dep.get('readyState')}")

    for i in range(60):
        code, body = api(
            "GET",
            f"https://api.vercel.com/v13/deployments/{dep_id}?teamId={TEAM_ID}",
            token,
            timeout=60,
        )
        if code != 200:
            die(f"poll HTTP {code}: {body[:200]!r}")
        d = json.loads(body)
        state = d.get("readyState")
        print(f"  poll {i}: {state}")
        if state == "READY":
            print("READY", dep_id)
            print("https://www.evoform.no/")
            print("https://www.evoform.no/version.json")
            return dep_id
        if state in ("ERROR", "CANCELED"):
            die(f"deployment {state}: {dep_id}")
        time.sleep(2)

    die("timeout waiting for READY")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--probe", action="store_true", help="auth check only")
    ap.add_argument("--skip-stage", action="store_true", help="use existing _public/")
    ap.add_argument("--marker", default=None, help="optional deployment meta marker")
    ap.add_argument(
        "--no-stage-on-missing",
        action="store_true",
        help=argparse.SUPPRESS,
    )
    args = ap.parse_args()

    token = load_token()
    if args.probe:
        probe(token)
        return

    probe(token)
    if not args.skip_stage:
        print("staging…")
        stage()
    elif not PUBLIC.is_dir():
        die("_public missing and --skip-stage set")

    print("deploying production…")
    deploy(token, args.marker)


if __name__ == "__main__":
    main()
