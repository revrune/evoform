# EvoForm opportunity brief  
**Title:** Regime-matched riblets + fouling-aware design (Path A bet 2)  
**Status:** **PERMANENT house opportunity brief** · 2026-08-06 · Kai from Eli instrument · judge against Path A job card  
**Project:** EvoForm · *In Accordance with Nature* · *Form Shaped by Evolution*  
**Job card (LOCKED · PERMANENT):** `briefs/path-a-job-card.md`  
**Instrument:** `docs/research-instrument-path-a-eli-2026-08-06.md` · **Papers:** `docs/path-a-papers-working-note-2026-08-06.md`  

---

## 1. Design problem

Reduce **skin friction** on the Path A hull at survey and slow-transit Reynolds numbers **without** increasing drag from wrong geometry, and **without** unmanageable fouling in riblet recesses.

**Job-card primary win:** more efficient motion than typical small prop AUV — form first, riblets **where earned**.

**Must-nots:** Shark-skin stickers without s+/h+ analysis · deep open mosaic gaps that cannot be cleaned · claiming antifouling from denticles alone.

---

## 2. Accordance check (physics)

Riblets reduce turbulent skin friction only in a **narrow geometric regime** (classically discussed in wall units s+, h+). Outside that band they are neutral or harmful. Coastal fouling fills micro-grooves and can erase the benefit in one mission cycle.

**Path A speeds (~0.2–2 m/s) and length (~0.5–1.2 m)** set the Reynolds band for sizing. Measure; do not copy aircraft or yacht riblet pitch blindly.

---

## 3. Mechanisms (lanes labeled)

### 3.1 Living · shark dermal denticles / engineered riblets

| | |
|--|--|
| **What** | Streamwise micro-grooves that lower turbulent skin friction when correctly scaled |
| **Lane** | Living → Synthetic |
| **Evidence** | High for controlled-flow drag reduction (Dean & Bhushan review; Bechert optimization) |
| **Transfer** | Hull panels or full skin with computed pitch/height for Path A Re |
| **Do not claim** | Automatic antifouling; automatic efficiency at any speed |

### 3.2 Synthetic · manufacturing paths

| | |
|--|--|
| **What** | Cast elastomer, CNC/micro-mold, printed masters, films |
| **Lane** | Synthetic |
| **Evidence** | Medium–high for lab coupons; field marine durability varies |
| **Transfer** | Coupon-first (flat plate → hull section) before whole vehicle |
| **Do not claim** | Makerspace print automatically hits turbulent riblet scale |

### 3.3 Synthetic · foul-release / cleanable outer treatment (paired)

| | |
|--|--|
| **What** | Coatings or skins that release soft foulants or allow easy wipe-down |
| **Lane** | Synthetic (see foul-aware skin brief) |
| **Evidence** | High for materials class; application-specific |
| **Transfer** | **Required pair** with riblets on Path A — not optional chrome |

---

## 4. Constraints & transfer

| Constraint | Implication |
|------------|-------------|
| Mission cycle fouling | Design for inspection + clean between missions (job card §6) |
| Drag measurement | Need baseline smooth hull of same form |
| Efficient slow transit (bet 6) | Riblets + form + sparse thrust composed — see propulsion brief |
| Depth 0–50 m first | Pressure on micro-structure secondary; fouling primary |

**Cross-links:**  
- Propulsion / transit → `briefs/path-a-quiet-multimode-propulsion.md`  
- Outer skin system → `briefs/path-a-foul-aware-outer-skin.md`  
- Coupon protocol pattern (osteoderm) → `briefs/osteoderm-coupon-protocol.md` (process analogy only)

---

## 5. Experiments & kill criteria

| Experiment | Done bar | Kill |
|------------|----------|------|
| Flat-plate drag at Path A Re band | Smooth vs riblet ΔCd with correct s+/h+ | Net drag **increase** |
| Hull-section towing or recirculating flume | Same with realistic curvature | Benefit vanishes on real form |
| Fouling coupon immersion (relevant water) | Growth rate + cleanability after one mission-length soak | Unmanageable fouling within one mission cycle |
| Regime mis-size control | Intentionally wrong pitch shows increased drag | If “wrong” still looks good, instrumentation is broken — fix methods |

---

## 6. Evidence trail (subset)

- Dean & Bhushan 2010 — DOI 10.1098/rsta.2010.0201  
- Bechert et al. 1997 — DOI 10.1017/S0022112096004673  
- Lejars et al. 2012 foul-release — DOI 10.1021/cr200350v  
- Full shelf: `docs/path-a-papers-working-note-2026-08-06.md`

---

## 7. Refuse

- Shark-skin marketing without regime analysis  
- Open osteoderm-style gaps as default riblet carrier  
- Free-lunch “always less drag” claims  

---

*Path A bet 2 · shareable opportunity brief · integrity first*
