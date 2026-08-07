# EvoForm

**Design in accordance with nature** · **Rua · Kai**  
**Folder:** `evoform` · **Started:** 2026-07-28  
**Earlier working name:** Biomime (BioMime is a medical stent brand)

**EvoForm** = evolution shapes form. Design that follows how living systems get good shapes under the laws of nature.

**Name locked (2026-08-05):** Keep **EvoForm**. Not cetacean-only branding. Co-presence *targets* may centre marine mammals (sister to CetaVox); **form teachers** are multi-taxon — any lineage that solved the physics we need (Living · Deep-time · Extreme · Synthetic · Speculative, always labeled).

**Umbrella + verticals (LOCKED · 2026-08-07):** EvoForm covers all biomimicry design. Specific avenues may use vertical names — **EvoMarine** (current · hang-with marine mammals) · **EvoAir** (quiet aerial · bird/insect teachers) · **EvoTerra** (ground/soil/terrain). Not three public brands to launch; architecture only until go. Detail: [`docs/ops/evoform-verticals-2026-08-07.md`](docs/ops/evoform-verticals-2026-08-07.md).

### Form teachers ≠ only hang-with subjects

Example **Living** lane — leatherback turtle (*Dermochelys coriacea*): longest known marine migrations; leathery carapace with interlocking / compliant structure that tolerates significant compression at depth; efficient long-range movement; internal volume usable as a model for component packing; body strategies that may thrash hardware less than hard-shell or thruster-box norms. **Not** “build a robot turtle.” **Yes** — extract mechanisms (compliance under pressure, migration-scale efficiency, packing geometry) with evidence trail, then transfer under physics and welfare constraints.

## Mission

**Biologically inspired, revolutionary marine vehicles** that can **hang with marine mammals** — stay with them longer, quieter, and more gracefully than a slow underwater box with a thruster.

Not only “efficient AUV.”  
**Co-presence platforms:** match the fluid competence of life so sensors (and careful humans/partners) can listen and observe on *their* terms — not a brief flyby.

## Sister project: CetaVox

| | **CetaVox** (`cetavox`) | **EvoForm** (`evoform`) |
|--|-------------------------|-------------------------|
| Job | **Decipher** what sounds mean | **Build platforms** that can stay in the acoustic and social world of marine mammals |
| Input | Existing recordings + new long-dwell data | Design problems + biology under physics |
| Output | Structure, patterns, meaning hypotheses | Opportunity briefs → real vehicle concepts |
| Link | Better co-presence → richer honest data for deciphering | Deciphering needs time *with* the animals, not only archive hours |

Ocean Sounds and others already record. CetaVox works patterns and meaning.  
EvoForm aims at the **missing machine**: vehicles life-shaped enough to loiter with whales and dolphins without wrecking the scene.

## North star

**In Accordance with Nature.**

Physics and the nature of the universe set the possible.  
Life (past, present, and potential) is our richest catalogue of solutions that already work inside those laws.  
Evidence-based speculation is welcome. Speculation presented as settled fact is not.

## Why fluid life is the first domain

Human marine vehicles are still **rudimentary** next to simple species: drag, noise, endurance, manoeuvre, soft bodies, sparse thrust.  
To hang with marine mammals you need more than slow survey mode — you need **modes they already own**:

- Quiet presence (don’t dominate the soundscape)  
- Efficient long dwell / loiter  
- Burst and cruise without thrashing  
- Stability for hydrophones and cameras while the animal moves  
- Bodies that survive clutter, current, and real sea handling  

## Lanes (always labeled)

| Label | Meaning |
|-------|---------|
| **Living** | Extant organisms / systems (fish, jelly, marine mammals themselves as teachers of form) |
| **Deep-time** | Extinct / fossil swimmers |
| **Extreme** | Deep, cold, high-pressure regimes |
| **Synthetic** | Soft robots, artificial muscle, living materials |
| **Speculative** | Plausible next forms — with evidence trail |

## How it works (product shape)

1. Someone brings a **human design problem** (default: co-presence marine vehicle)  
2. EvoForm explores multi-lane biology under physics  
3. Output: a **shareable collaborative opportunity brief** (instrument + studio)  
4. Public by default — wisdom open; strong revelations may become ventures later  

## Path A research (permanent · 2026-08-06)

**Canonical map:** [`docs/path-a-research-stack-permanent-2026-08-06.md`](docs/path-a-research-stack-permanent-2026-08-06.md)

| Layer | Path |
|-------|------|
| **Job card (LOCKED)** | [`briefs/path-a-job-card.md`](briefs/path-a-job-card.md) |
| **Eli instrument** | [`docs/research-instrument-path-a-eli-2026-08-06.md`](docs/research-instrument-path-a-eli-2026-08-06.md) |
| **Papers shelf** | [`docs/path-a-papers-working-note-2026-08-06.md`](docs/path-a-papers-working-note-2026-08-06.md) |
| **First-experiment plan (LOCKED)** | [`docs/path-a-first-experiment-plan-2026-08-06.md`](docs/path-a-first-experiment-plan-2026-08-06.md) · #1 tank noise+power + hydrophone · not fab |
| **Success pack** | [`docs/research-success-pack-2026-07-29.md`](docs/research-success-pack-2026-07-29.md) |
| **Showcase seed** | [`briefs/quiet-small-auv-survey.md`](briefs/quiet-small-auv-survey.md) |
| **Bets 1–5 + law** | `briefs/path-a-*.md` (propulsion · riblets · hover · hydrophone · foul-aware · abort law) |
| **Secondary volume-following** | [`briefs/leatherback-osteoderm-volume-following.md`](briefs/leatherback-osteoderm-volume-following.md) |

Path A hybrid sketch: streamlined sensor body · variable buoyancy · paired fins for hover · sparse/quiet thrust · pulsed or flexible transit only when earned.

## Honesty bar

| OK | Not OK |
|----|--------|
| Mechanisms + constraints + transfer notes | “Nature says invent this product” with no trail |
| Evidence-based speculation, labeled | Unlabeled speculation as fact |
| Physics / energy / scale / welfare checks | Free-lunch engineering or harassing animals for data |

## Status

- Mission linked to CetaVox co-presence need (2026-07-28).  
- Public door: thin spine only (https://www.evoform.no) · no product UI.  
- **Live host:** Vercel project **`evoform-no`** (team LeitnerLearning) · Cloudflare DNS · **not** GitHub Pages.  
- **Live publish path:** stage thin door (`tools/stage-public-door.sh`) → Vercel production. GHA **Deploy public door** when `VERCEL_*` secrets set; local fallback `tools/publish-public-door.sh`. Research tree on **main** is not public. Ops: `docs/ops/domains-email-vercel-2026-08-07.md`.  
- Path A research stack permanent (job card · instrument · papers · opportunity briefs · skill-laws).  
- Masters capacity primary from Aug 2026.

## Next (when we continue)

1. Study papers shelf + kill criteria on bets **1–4** (against the locked experiment plan)  
2. Run lab protocol only when founder schedules it — plan is locked; **fab/build packages still need a separate go**  
3. Do not re-rank bets 1–4 without founder rewrite of the experiment plan  
