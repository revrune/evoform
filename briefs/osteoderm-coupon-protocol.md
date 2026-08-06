# Osteoderm mosaic flexure coupon — protocol

**Date:** 2026-08-06 · **Seat:** Kai · **Rua go:** next actionable after opportunity brief  
**Parent brief:** `briefs/leatherback-osteoderm-volume-following.md`  
**Novelty pass:** `docs/novelty-pass-osteoderm-mosaic-2026-08-06.md`  
**Lane:** Synthetic analog of Living teacher · **not a vehicle** · not a pressure test to depth  

**Done bar:** printable tile geometry + BOM + test matrix + pass criteria vs solid control of **same mass**. Measure flex. No fabrication claim that EvoForm “has a hull.”

---

## 1. Purpose

Quantify whether a **suture-linked tile mosaic** delivers more **global flexure** (normalized deflection) than a **monolithic plate of equal mass and outer envelope**, while retaining useful integrity under moderate load.

This tests the Living design rule: **many small plates + soft joints → more total envelope flex for a given joint angle** (Chen flexibility parameter δ/L).

**Does not test:** hydrostatic collapse, 1000 m depth, acoustic self-noise in water, marine fouling, or propulsion.

---

## 2. Specimens

### 2.1 Geometry (Path A–scaled, not adult leatherback photocopy)

| Parameter | Value | Rationale |
|-----------|--------|-----------|
| Coupon outer plan | **120 × 60 mm** | Desk / 3-point span friendly |
| Nominal thickness | **3.0 mm** tile body | Printable; stiff enough to handle |
| Mosaic | **3 × 5** rectangular tiles (15 tiles) | n high enough to show cumulative flex |
| Tile body (before teeth) | ~22 × 18 mm | Leaves room for suture zone |
| Suture tooth half-angle | **θ = 30°** (2θ = 60° full included if mirrored) | Living reference (Chen ~30°) |
| Tooth amplitude A | **2.0 mm** | Printable interlocking |
| Inter-tile gap (open) | **1.0 mm** filled by elastomer | Soft phase |
| Edge frame | Optional 4 mm solid border on both mosaic and solid control | Shared mounting |

### 2.2 Two specimen types (required pair)

| ID | Construction | Mass target |
|----|--------------|-------------|
| **M** | Mosaic tiles + elastomer sutures + thin elastomer or TPU skin optional | m |
| **S** | Solid single plate same outer 120×60×t | **Match mass m** by reducing thickness or infill of S until m_S ≈ m_M ±5% |

Mass-matching is mandatory. Flex comparison without mass match is not honest.

### 2.3 Optional third

| ID | Construction |
|----|--------------|
| **M0** | Mosaic tiles with **no** elastomer (dry stack / tape only) | Shows joint necessity |

---

## 3. Materials (shop-floor default)

| Role | Default | Alternatives |
|------|---------|--------------|
| Tiles | PETG or PLA, 100% infill, 0.2 mm layers | Resin if available (brittle — note in log) |
| Soft suture | RTV silicone (Shore A ~20–40) poured into gaps | TPU 85A/95A printed hinges if multi-material printer |
| Optional skin | Thin silicone sheet or TPU film bonded on “outer” face | Living soft dermis analog |
| Mount | 3-point bend fixtures or two knife edges + mid load | Simple desk setup OK |

**BOM (one M+S pair):** ~50 g filament · 30–50 ml silicone · release agent · scale · ruler/calipers · phone slow-mo or dial indicator.

Print files: `prototypes/osteoderm-coupon/` (`generate_coupon.py` → STL).

---

## 4. Fabrication steps

1. Print **tiles** (or single mosaic panel with 1 mm gaps pre-modeled).  
2. Dry-fit interlocking teeth; confirm free motion before potting.  
3. Mask faces; pour / inject silicone into gaps; cure per product.  
4. Optional: bond outer skin.  
5. Weigh **M**. Adjust **S** print (thickness or sparse infill) until mass matches.  
6. Photograph both with scale bar. Log print settings.

---

## 5. Test matrix

Environment: dry air, room temperature first. Optional wet retest after 24 h water soak.

| Test | Method | Metric |
|------|--------|--------|
| **T1 Static flexure** | 3-point bend, span L = 100 mm, mid load stepped 0.5 / 1 / 2 / 3 N (or until 5 mm mid defl or damage) | Midspan deflection δ; plot F–δ; **δ/L** at 2 N |
| **T2 Recovery** | Unload; residual δ after 60 s | Plastic set % |
| **T3 Cyclic** | 20 cycles at load giving ~2 mm on M | Stiffness drop % cycle 1 → 20 |
| **T4 Integrity** | Visual: tooth crack, silicone tear, delamination | Pass/fail notes |
| **T5 (optional) Wet** | Repeat T1 after soak | δ change vs dry |

**Primary comparison:** at equal mass and equal outer span, **δ_M / δ_S at same force** (compliance ratio). Living hypothesis: ratio **> 1**.

---

## 6. Pass criteria (coupon-level, not product)

| Result | Interpretation |
|--------|----------------|
| δ_M / δ_S ≥ **1.5** at 2 N, no catastrophic tile fracture | **Support** for mosaic kinematics transfer at bench scale |
| 1.1–1.5 | **Weak support** — joint design may need softer interstitium or more plates |
| ≤ 1.0 | **Does not support** “many plates more flex” under this fabrication; revise gap/angle/material before any vehicle talk |
| Large residual set or joint tear by cycle 20 | Fatigue debt real — document for opportunity brief engineering debts |

**Hard refuse:** “coupon flexes → we have a 1000 m hull.” Volume-following still needs compressible volume management (physics bar).

---

## 7. Data log template

```
date:
operator:
print material / settings:
mass_M_g:
mass_S_g:
span_mm:
force_N | delta_M_mm | delta_S_mm | notes
cycles: stiffness notes
photos: path/
conclusion: support / weak / no-support
```

Store under `prototypes/osteoderm-coupon/runs/YYYY-MM-DD/`.

---

## 8. Safety

No pressure chamber. No compressed gas. Silicone: ventilate per SDS. 3D printer: standard filament safety.

---

## 9. What this unlocks next

| If coupon | Then |
|-----------|------|
| Supports | Optional: ridge-stiffened mosaic coupon · wet acoustic desk tap (qualitative) · Path A fairing concept sketch only |
| Weak / no | Revise joint recipe; do not escalate to vehicle narrative |
| Either way | Update opportunity brief §8 open Q with numbers |

---

## 10. Skill-law reminder

Leatherback osteoderm mosaic is a Living teacher for volume-following compliant outer structure. This coupon is a **Synthetic** analog of **flexure kinematics only**. Secondary to Path A. No robot turtle. No free lunch.

---

*Kai · coupon protocol · desk science · evidence before vehicle*
