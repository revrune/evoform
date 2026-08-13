# Path A · leatherback hull iteration

**Date:** 2026-08-13 · **Kai (Build)**  
**Trigger:** Rua on live Form still: “This resembles a leatherback. Is this truly where the first prototype should go?”  
**Judge:** `briefs/path-a-job-card.md` (LOCKED)  
**Law:** mechanism transfer · no robot-animal · no free lunch · tank before claim

---

## Verdict (plain)

**No. The live still is not the first-prototype hull.**

It still reads as a leatherback because we copied **silhouette** (head / neck / fat carapace / tail duct), not the mechanisms the animal actually pays for. That is the opposite of the house rule.

Leatherback is still a **Living teacher**. It is not the whole vehicle. It is not the maneuverability teacher. It is not v1 depth compliance.

---

## What the animal actually evolved

| Feature | What it is for | Evidence | Path A transfer |
|---------|----------------|----------|-----------------|
| Teardrop / taper | Long pelagic cruise; low form drag for a packed body | Morphology + migration ecology | **Yes · hull** · keep volume, raise fineness |
| Five dorsal ridges, slightly off the local streamlines | Streamwise vortices; delay separation. Hatchling / low Re / negative AoA: drag cut (Bang: up to ~32% at α ≈ −18°, Re ~ 2×10⁵). Adult / higher Re / positive AoA: more lift and L/D on the climb out of a V-dive | Bang, Kim, Lee & Choi 2016, *Sci. Rep.* 6:34283 | **Maybe · hull coupon** · only if our Re and pitch match. Not decorative grooves |
| Soft mosaic carapace | Volume-following as lungs collapse at depth (records ~1000 m class). Not a pressure hull | Chen, Yang, Meyers 2015; house osteoderm note | **No for P1** · locked secondary (bet 7) |
| Very long front flippers | Lift-based underwater flight. Green-turtle robot work: ~30% of the beat makes thrust, ~70% is a drag-cutting glide; very low cost of transport | van der Geest et al. 2023, *JMSE* 11:1944 (green, not leatherback, same family of stroke) | **Later · propulsion** · only if tank says quieter than a sparse prop. Not costume flippers on P1 |
| No swim bladder | Adults go negatively buoyant deep and must swim **up** at high pitch. Ridges help that climb | Bang 2016 citing Fossette / Houghton dive work | **Different problem than ours.** We use buoyancy on purpose (hover brief) |

Typical adult cruise in the literature is about **0.56–0.84 m/s**. That sits on Path A survey speed. The “22 mph” line is a burst / scare figure, not the design point.

**Maneuverability correction.** Leatherbacks are open-ocean cruisers and divers. They are not reef turners. Tight horizontal turns are a **ray / sea-lion** lesson. Leatherback “maneuver” in the papers is mostly **pitch on a dive**, not hanging with a whale in a small box of water.

---

## What the live still got wrong

1. **Neck + head.** Hydrophone-first wants a quiet faired face. A bellows neck is costume.
2. **Too short and fat.** We over-read “leatherback packing” as a navy egg. Packing is real. Fineness is also real. A ~2:1 blob pays form drag we do not need at 1–2 m/s.
3. **Ridges as styling.** Bang’s result is specific: slight misalignment to local streamlines, vortex generation, different job at +AoA vs −AoA. Parallel grooves on a blob are not that experiment.
4. **One animal = one vehicle.** House law is multi-taxon and quiet-first. Flippers, riblets, buoyancy, sparse thrust are other teachers.

A leatherback-shaped glider already exists in the literature (Hernández-Jaramillo & Vásquez 2023). Silhouette copy is not a company.

---

## What P1 should steal

**Steal**

- Teardrop with enough mid-body volume for battery, buoyancy, dry box
- Fineness nearer **3.5:1** than 2:1 (length open until the pack locks)
- Five testable ridges, slightly toed, as a **with/without** tank coupon
- Flush sensor face. Mic at the quiet end. Camera can gimbal so the hull stays still
- Small control planes for pitch/roll. Not flippers
- Rear sparse / shrouded thrust for catch-up only
- Hover from buoyancy + those planes (bet 3), not from a turtle gait

**Leave**

- Head, neck, eyes, flippers, tail
- Osteoderm mosaic as the first outer skin
- Any claim that ridges “reduce drag” until we run our Re and our pitch
- Robot-animal product identity

---

## Reynolds honesty (order of magnitude)

Sea water ν ≈ 1×10⁻⁶ m²/s.

| Case | L | U | Re |
|------|---|---|-----|
| Leatherback hatchling (Bang) | ~0.24 m | ~0.8 m/s | ~2×10⁵ |
| Adult leatherback cruise | ~1.6 m | ~0.7 m/s | ~1×10⁶ |
| Path A if 1.2 m at 0.7 m/s | 1.2 m | 0.7 m/s | ~8×10⁵ |
| Path A if 1.2 m at 1.5 m/s | 1.2 m | 1.5 m/s | ~1.8×10⁶ |

We sit nearer **adult** Re than hatchling Re. The hatchling 32% drag cut is the wrong poster number for P1. The adult, positive-AoA lift / L/D story is only live if we pitch up a lot. On a buoyancy-trimmed survey we may see only a modest ridge effect. That is why ridges are a **coupon**, not a brand.

---

## First prototype (this iteration)

**Correction, later the same day.** Rua stopped the long-AUV lock. The Board already asked for a leatherback-shaped hull and flipper-style drive, held by a control computer. The long teardrop dropped the living form. That was a miss.

Concepts now keeps three leatherback studies so none are lost:

| Study | What it is | Honest read |
|-------|------------|-------------|
| Outline | First living-form stills | Flippers and volume are the teachers. Neck is costume. |
| Packed | Short deep navy hull | Packing wins. Motion teacher is gone. Neck still costume. |
| Long | 3.5:1 cruise AUV | Easy vehicle. Weak as EvoForm. Ridges probably pointless at hover. |

A fourth Drive still (flipper foils as the main drive) is on disk as `path-a/mockups/study-drive-form.jpg`. Not on the public page yet. It still reads as a robot turtle. Next pass has to keep the animal planform and make the foils the engine without a costume head.

Board law that I under-weighted: look-alike follows what works · short thrust, long coast (~30 / 70) · computer holds a hull that need not be a dart.

---

## Sources (this pass)

- Bang, Kim, Lee & Choi (2016). Hydrodynamic role of longitudinal dorsal ridges in a leatherback turtle swimming. *Scientific Reports* 6:34283. https://doi.org/10.1038/srep34283
- van der Geest, Garcia, Nates & Borrett (2023). New insights into sea turtle propulsion and their cost of transport. *J. Mar. Sci. Eng.* 11:1944. https://doi.org/10.3390/jmse11101944 · ~30% stroke / 70% glide · downstroke is lift-based (LEV), not a paddle
- Licht, Wibawa, Hover & Triantafyllou (2010). In-line motion causes high thrust and efficiency in flapping foils. *J. Exp. Biol.* 213:63–71. Sea turtles: high-aspect flapping foils give maneuver and control **without** a flexible body
- Chen, Yang & Meyers (2015). Leatherback osteoderm materials. *Acta Biomaterialia*. House note: `docs/research-leatherback-osteoderms-2026-08-06.md`
- Hernández-Jaramillo & Vásquez (2023). Leatherback-inspired underwater glider. *Biomimetics* 8(1):80. Prior art on silhouette transfer.
- House: job card · hover brief · quiet multi-mode brief · osteoderm volume-following (secondary)

---

*Kai · 2026-08-13 · iterate, do not lock a costume*
