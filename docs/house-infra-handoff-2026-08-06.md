# House infra handoff — 2026-08-06

**Permanent for Kai · Eli · any seat.** Session work after freeze reset + founder NOW law.

## NOW law (founder · permanent)

If Rua is communicating about doing something, **we are doing it now**. Never rest / pause / “after Masters” / capacity lectures as a reply to live work. Real blockers only. Full text: global `MEMORY.md` → Working Preferences → **NOW law**.

Varde offline until tokens reset (Saturday ~2026-08-09) — does not change NOW law for Kai/Eli.

---

## Sentry (RevRune)

| Item | State |
|------|--------|
| Org | `revrune` · https://revrune.sentry.io · EU region `https://de.sentry.io` |
| Auth | GitHub OAuth (prefer over password) |
| MCP | Connected — Kai can call Sentry tools |
| GitHub app | Installed on account **`revrune`** · **All repositories** saved |
| Projects | **None yet** — create when something ships (no DSN/SDK on EvoForm spine) |
| Seer / suspect commits | Needs repo link (done at GitHub app level) + later project when code errors exist |

## Domains

| Domain | State |
|--------|--------|
| **evoform.no** | **LIVE** (CF Active 2026-08-06) · registered Webhuset · order **333609** · customer **140458** · **N.PRI.99477784** · egenerklæring confirmed · NS `cleo` / `raphaela` |
| **Cloudflare zone** | **Active / protected** · NS `cleo` / `raphaela` · apex A×4 GitHub Pages (185.199.108–111.153) · `www` CNAME → `revrune.github.io` · prefer DNS-only (grey) for Pages TLS |
| **Site** | **http://evoform.no** serves thin spine · **HTTPS** wait GitHub custom-domain cert (`https_enforced` false until cert exists) |
| **evoform.com** | **Not ours** (ACTIVE third party / Afternic parking). Do not set as custom domain. |

**When egenerklæring signed + Webhuset allows NS:** set only

```
cleo.ns.cloudflare.com
raphaela.ns.cloudflare.com
```

Then verify CF → active · https://evoform.no · enforce HTTPS on GitHub Pages if ready.

## GitHub · EvoForm

| Item | State |
|------|--------|
| Repo | https://github.com/revrune/evoform · **public** · homepage `https://evoform.no` |
| Remote | `git@github.com:revrune/evoform.git` (fixed off wrong `leitnerlearning/` remote) |
| Pages | Enabled · source **`gh-pages` `/`** (switched 2026-08-06) · CNAME **`evoform.no`** · HTTPS enforced |
| Site | Thin public door only on `gh-pages`: `index.html`, `404.html`, `CNAME`, `.nojekyll` — research tree stays on **main** |
| Publish door | After changing public HTML: `tools/publish-public-door.sh` (force-pushes thin files to `gh-pages`). Do **not** rely on main research pushes for the live door. |
| Pages incident (2026-08-06) | Deploy thrash: 503s + concurrent cancel + monitor re-runs while publishing whole `main`. Fix: kill monitor thrash · thin `gh-pages` · stop empty-commit spam. |
| Sisters | cetavox.com · leitnerlearning.com same CF NS + Pages pattern |

## Local tree notes

- **Canonical path:** `~/evoform` only (not Desktop / not Ruairí life archive). Folder moves rescued 2026-08-06; empty Desktop shells removed.
- **main @ bb41a4e+:** spine site · NOW law · handoff · name-lock / leatherback form-teacher notes on README + research pack.

## Product law (permanent · 2026-08-06)

| Item | Lock |
|------|------|
| **Path A job card** | **LOCKED** · `briefs/path-a-job-card.md` · job · market win order · envelope · year-1 users · build posture |
| **Path A research stack** | **PERMANENT** · map `docs/path-a-research-stack-permanent-2026-08-06.md` · instrument · papers shelf · bets 1–5 briefs · bet 6 composition · bet 7 leatherback secondary · bet 8 abort law · skill-laws in `evoform-product-partner` |
| **Kai role (fab)** | Specs + opportunity briefs · buildable packages after explicit **go** · coordinates shops/labs · workflow detail when fabrication starts |
| **Eli** | **Grok.com only.** When Rua says Eli, Kai gives **paste packet only** — never role-play Eli in Build (house-wide · 2026-08-06) |
| **Public spine** | Thin mission only · Eli A · `docs/eli-public-spine-A-2026-08-06.md` · Leitner-clean · no honesty theater |
| **Public pair (locked)** | **In Accordance with Nature · Form Shaped by Evolution** · Title Case · join with ` · ` · no em dashes on door |
| **Short slogan (locked)** | **Shaped by Evolution** · brevity only · never replaces full pair on main door |
| **Public category (locked)** | **nature-inspired underwater vehicles** · FB + site lede · not “platforms” · autonomy is ideal direction, not a shipped claim |
| **Osteoderm** | Living teacher secondary · volume-following ≠ pressure hull · not first hull requirement |

## Open (real blockers only)

1. ~~Egenerklæring + register~~ **Done** 2026-08-06.
2. ~~Point NS to Cloudflare~~ **Saved at Webhuset** 2026-08-06 · Norid whois shows CLEO/RAPH handles.
3. ~~Package A door verify~~ **Mostly done 2026-08-06:** CF Active · public NS OK · HTTP spine live · HTTPS cert pending GitHub.
4. Optional later: Sentry **project** + SDK when there is a runtime to instrument.

### Package A checklist

- [x] Cloudflare zone status **Active**
- [x] `dig +short NS evoform.no @1.1.1.1` → cleo + raphaela
- [x] `http://evoform.no` serves thin spine (mission · north star · sister · early briefs)
- [ ] `https://evoform.no` — wait GitHub Pages cert for custom domain, then **Enforce HTTPS**
- [x] Handoff updated live date 2026-08-06

## House map (unchanged integrity)

- **RevRune** — holding vessel (GitHub `revrune` · X `@RevRune`)
- **Leitner Learning** — leitnerlearning.com
- **CetaVox** — cetavox.com · public ocean face
- **EvoForm** — form shaped by evolution · house product · `evoform.no` spine waiting on registry; not a vaporware twin of CetaVox

---

*Kai · 2026-08-06 · permanent handoff*
