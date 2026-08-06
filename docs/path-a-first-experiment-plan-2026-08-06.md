# Path A · first-experiment plan (one page)

**Status:** **LOCKED · PERMANENT** · 2026-08-06 · founder Rua go + “lock permanent”  
**Reopen only:** explicit founder rewrite of rank or top protocol  
**Not a fab go:** tank/coupon/bench class only · buildable packages still need a separate go  
**Judge:** `briefs/path-a-job-card.md` (LOCKED · PERMANENT)  
**Grounding:** opportunity briefs bets 1–4 · `docs/path-a-papers-working-note-2026-08-06.md` · instrument  
**Stack map:** `docs/path-a-research-stack-permanent-2026-08-06.md`  

**Law reminder:** Abort-on-avoidance remains product law for any later field work. This plan is lab only. No co-presence claim. No finished AUV.

**Permanent rank (do not thrash):** #1 bet 1 (tank noise+power) · #2 bet 4 (hydrophone on same rig) · #3 bet 3 (hover) · #4 bet 2 (riblet coupons).

---

## Rank (bets 1–4) — what to test first

| Rank | Bet | Why this order | First test class |
|------|-----|----------------|------------------|
| **#1** | **1 · Quiet multi-mode / sparse thrust** | Job-card **primary** win = quieter + more efficient motion than a typical small prop AUV. Without a noise-at-useful-speed baseline, form/riblets/hover cannot be judged. | Tank: noise + power vs baseline prop |
| **#2** | **4 · Hydrophone-first layout** | Sensors v1 = hydrophone; kill is self-noise floor in **loiter**. Couples to #1 on the **same rig** (measure while thrusters run). | Spectra at candidate mounts on test body |
| **#3** | **3 · Hover / station-keep** | Secondary win = multi-hour loiter; hover power can kill battery. Run after sparse-thrust options exist to avoid testing continuous-prop “hover.” | Static + low-current power & noise |
| **#4** | **2 · Regime-matched riblets** | Primary win path includes riblets **where earned**, but wrong geometry or fouling wastes effort until a hull form and speed band exist. Coupon parallel OK; full-hull after #1 speeds known. | Flat-plate drag + fouling coupons |

**Top choice for the first session:** **#1 tank noise + power comparison**, with **#2 hydrophone location A/B** instrumented on the same carriage/body so one wet session serves quiet-first architecture.

---

## Top protocol (bet 1 + bet 4 coupled)

### What is measured
- Broadband / banded **self-noise** (or radiated proxy) of candidate thrusters at **0.3 · 0.8 · 1.5 m/s** (survey → transit band from job card).  
- **Electrical power** (or estimated energy per distance) at those speeds.  
- Hydrophone **spectra** on ≥2 mount locations (e.g. nose vs mid-body vs near thruster) during the same runs + static loiter.

### Candidates (minimal)
| Role | Example class | Notes |
|------|---------------|--------|
| Baseline | Well-designed small continuous prop (Path A size class) | Must beat this on noise-at-useful-speed |
| Sparse A | Intermittent / duty-cycled small thruster | Software duty cycle OK |
| Sparse B (optional) | Pulsed pump or low-RPM ducted if available in lab | Do not require soft fish hardware for v1 |

Body: sealed streamlined **dummy** or existing hull mock (~0.5–1.2 m intent) — not a finished vehicle.

### Done bar
1. Table: noise metric + power at three speeds for baseline vs ≥1 sparse candidate.  
2. Hydrophone spectra plots for loiter (thrusters off or minimal) and survey speed.  
3. Written call: which architecture advances, which is **killed**.

### Kill criteria (from briefs — do not soften)
| Source | Kill |
|--------|------|
| Bet 1 | Cannot beat a well-designed small prop on **noise-at-useful-speed** within Path A size/power |
| Bet 4 | Self-noise remains above useful ambient / listening bands during **loiter** |

If both kill: stop and reassess before riblets or soft undulatory spend.

### Minimal setup (lab class)
- Tow tank, flume, or controlled pool carriage · hydrophone + recorder · power meter · fixed speed control  
- No ocean, no animals, no autonomy, no makerspace vehicle program yet  

### Papers shelf (entry points)
- Zimmerman et al. AUV self-noise practice · Urick fundamentals  
- Sfakiotakis swimming modes (context only)  
- Full list: `docs/path-a-papers-working-note-2026-08-06.md`

---

## Sequenced follow-ons (after top protocol)

| Order | Experiment | Done bar | Kill (brief) |
|-------|------------|----------|--------------|
| Next | **Hover power** (bet 3) with preferred sparse architecture | Watts → estimated loiter hours on Path A battery | Hover power destroys multi-hour battery goal |
| Parallel / after speeds known | **Riblet coupons** (bet 2) at Re band from #1 | Smooth vs riblet ΔCd; fouling after mission-length soak | Net drag increase **or** unmanageable fouling in one cycle |

---

## Explicitly deferred (later go)

- Full Path A vehicle fab, CAD, STLs, sea trials  
- Soft undulatory modules as product identity  
- Volume-following / osteoderm first hull  
- Field approach near marine mammals  
- Buildable packages for shops (job card: packages only after explicit go)

---

## Refuse

- Treating this plan as “we are building the AUV”  
- Skipping baseline prop comparison  
- Claiming quiet co-presence from tank data  
- Reopening job card, skill-laws, or Eli landscape  
- Public-door product chrome  

---

*Integrity first · quiet-first · measure before biomimetic chrome · fab still needs a separate go.*
