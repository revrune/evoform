#!/usr/bin/env python3
"""Emergency restore: deploy staged public door using VERCEL_TOKEN or MCP creds."""
import os, sys
sys.path.insert(0, str(__file__).rsplit("/", 2)[0] if False else "/tmp/evoform")
# Just run the standard deploy if creds exist
os.chdir("/tmp/evoform")
# Prefer MCP creds path injection
token = os.environ.get("VERCEL_TOKEN")
if token:
    import json
    from pathlib import Path
    Path.home().joinpath(".grok").mkdir(exist_ok=True)
    creds = {
      "vercel:https://mcp.vercel.com/": {
        "token_response": {"access_token": token}
      }
    }
    Path.home().joinpath(".grok/mcp_credentials.json").write_text(json.dumps(creds))
import subprocess
subprocess.check_call([sys.executable, "tools/deploy-vercel-rest.py", "--marker", "leatherback-crop-restore"])
