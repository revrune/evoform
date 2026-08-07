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

## Optional follow-ups (not go)

1. Send-as @domain from Gmail (pinned)
2. DMARC → reject after reports
3. Cosmetic: remove leftover GitHub Pages custom-domain settings in repo Settings
4. Rewire any Pages-only deploy scripts to Vercel so door publish matches host map
5. Varde catch-up after token reset ~2026-08-09

## Verify (quick)

```bash
curl -sI https://www.leitnerlearning.com | head -5   # server: Vercel · 200
curl -sI https://www.evoform.no | head -5
curl -sI https://www.cetavox.com | head -5
dig +short _dmarc.evoform.no TXT
```

---

*Riven handoff absorbed · Kai verified · Rua locked permanent 2026-08-07*
