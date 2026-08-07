# House ops — domains, email, Vercel (2026-08-07)

**LOCKED · PERMANENT** · Rua go 2026-08-07 · option A RevRune scope  
**Supersedes** Pages/DNS sections of `docs/house-infra-handoff-2026-08-06.md`  
**Seats:** Riven (live edge) · Kai (disk/git) · Eli (Expert) · Varde (out until ~2026-08-09)

## Law in one line

Public doors live on **Vercel** (team **LeitnerLearning**) + **Cloudflare** DNS/mail.  
**GitHub Pages is retired** for these custom domains.  
**RevRune** is not the host umbrella — code/Sentry/X labels only; public faces are the three brands.

## Host map

| Domain | Vercel project | Apex | Production |
|--------|----------------|------|------------|
| leitnerlearning.com | `leitnerlearning` | 308 → www | https://www.leitnerlearning.com |
| evoform.no | `evoform-no` | 308 → www | https://www.evoform.no |
| cetavox.com | `cetavox` | 308 → www | https://www.cetavox.com |

Also: `*.vercel.app` production URLs remain valid project aliases.

## DNS (Cloudflare · DNS-only / grey cloud)

Authoritative intent (CNAME flattening on apex):

| Zone | @ and www CNAME target |
|------|-------------------------|
| leitnerlearning.com | `9ce55f17dc1531b0.vercel-dns-017.com` |
| evoform.no | `c1439b7f5fb3fe79.vercel-dns-017.com` |
| cetavox.com | `d9abb672572b7c42.vercel-dns-017.com` |

**Do not:**

- Point custom domains at GitHub Pages (`185.199.x` / `revrune.github.io`)
- Orange-cloud (proxy) the Vercel CNAMEs
- Copy one project’s `vercel-dns` hostname onto another project’s domain

## Email

- **Cloudflare Email Routing** on all three zones
- Catch-all → Gmail (account destination verified once)
- CF-managed MX + SPF/DKIM rows are **Locked** — do not hand-delete
- **PINNED:** send-as @domain from Gmail — do not start without Rua reopen

## DMARC

Per zone TXT `_dmarc`:

```
v=DMARC1; p=quarantine; rua=mailto:dmarc@<domain>
```

Optional later: tighten to `p=reject` after watching reports.

## Code vs edge

| Truth | Owner |
|-------|--------|
| Source repos (`~/sprakflow`, `~/evoform`, `~/cetavox`) · git | **Kai** |
| DNS · Vercel domain attach · CF mail | **Riven** (web Build) / dashboards |
| Product judgment | **Eli** (Expert) |

No Riven workspace files to merge for the 2026-08-07 domain migration — dashboard + DNS only.

## RevRune scope (option A)

| Layer | Status |
|-------|--------|
| Public product brands | Leitner · EvoForm · CetaVox |
| Vercel team | **LeitnerLearning** |
| GitHub org | **`revrune/*`** until deliberate migrate |
| Sentry | org **revrune** |
| X @RevRune | Political/ideas — not product host |
| “House RevRune” on doors | Quiet internal only — not deploy story, not product lead |

## Public door deploy (EvoForm · rewired 2026-08-07)

| Piece | Role |
|-------|------|
| `vercel.json` | Build stages thin door → `_public/` only |
| `tools/stage-public-door.sh` | Copies `index.html` · `404.html` · `version.json` · `path-a/**` |
| `tools/publish-public-door.sh` | Local production deploy via Vercel CLI |
| GHA `Deploy public door` | Same on push of door paths when secrets set |
| **Not public** | `briefs/` · `docs/` · research tree · prototypes |

**GHA secrets** (repo `revrune/evoform`): `VERCEL_TOKEN` · `VERCEL_ORG_ID`=`team_QwxzlThVmQiaDdYIKaFY7gMB` · `VERCEL_PROJECT_ID`=`prj_ODHEe1C3BtGhJSSDEvReNER2pBsE`

**Deploy identity (LOCKED · 2026-08-07):** Vercel **BLOCKS** CLI deploys when git author is `*@*.local` (Mac auto git email) — not a team member.  
- Founder **main email** + git + Vercel owner: **ruairithered@gmail.com** (`ruairithered-4228`)  
- Global git: `user.name=Ruairí Ó Daimhín` · `user.email=ruairithered@gmail.com` (set 2026-08-07)  
- Local publish script deploys from a **git-free temp folder** as belt-and-suspenders  
- Do **not** “fix” by upgrading to Pro for this error  

**Path A mockups (LOCKED · 2026-08-07 · edge closed):**  
- Serve from Vercel: `/path-a/mockups/*.jpg`  
- HTML paths must be **absolute** `/path-a/mockups/…` (not `./mockups/`, not jsDelivr while private)  
- Cause of empty viewer: `trailingSlash: false` → page at `/path-a` → relative mockups → `/mockups/` 404  
- Fix commit: `77d4986` · Riven re-check: all assets 200  

**gh-pages / Pages workflow retired** for custom-domain truth. Do not re-aim DNS at GitHub.

## Optional follow-ups (not go)

1. Send-as @domain from Gmail (pinned)
2. DMARC → reject after reports
3. Cosmetic: remove leftover GitHub Pages custom-domain settings in repo Settings
4. ~~Rewire Pages deploy scripts to Vercel~~ **done 2026-08-07**
5. Varde catch-up after token reset ~2026-08-09
6. Add Vercel Git integration or GHA secrets so every door push auto-ships

## Verify (quick)

```bash
curl -sI https://www.leitnerlearning.com | head -5   # server: Vercel · 200
curl -sI https://www.evoform.no | head -5
curl -sI https://www.cetavox.com | head -5
dig +short _dmarc.evoform.no TXT
```

---

*Riven handoff absorbed · Kai verified · Rua locked permanent 2026-08-07*
