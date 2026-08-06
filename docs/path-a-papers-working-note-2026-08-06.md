# Path A · papers working note

**Date:** 2026-08-06 · **Kai**  
**Status:** **PERMANENT** evidence shelf · 2026-08-06
**Purpose:** Shared evidence shelf for Path A opportunity briefs. Expands instrument reading list (`docs/research-instrument-path-a-eli-2026-08-06.md` §6).  
**Law:** In Accordance with Nature · lanes labeled · no free lunch · paywalled items cited by DOI/abstract only  
**Judge:** `briefs/path-a-job-card.md` (LOCKED · PERMANENT)

**How to use:** Each opportunity brief cites a subset. Prefer open access when learning; DOI is enough for collaboration.

---

## Theme index

| Theme | Briefs that use it |
|-------|-------------------|
| Soft robotic fish / ocean demos | Propulsion, hover |
| Undulatory / BCF propulsion | Propulsion, transit |
| Riblets / shark-skin drag | Riblets |
| AUV / platform self-noise | Hydrophone layout, propulsion |
| Glider buoyancy / endurance | Hover, propulsion (sparse energy) |
| Antifouling / foul-release | Riblets, foul-aware skin |
| Soft robots in seawater durability | Propulsion (later undulatory) |
| Leatherback / compliance (secondary) | Volume-following only |
| Context (CETI scale awareness) | Ethics notes only |

---

## Sources (≥10)

### Soft fish · synthetic + living lessons

1. **Katzschmann et al. (2018).** *Exploration of underwater life with an acoustically controlled soft robotic fish.* **Science Robotics** 3(16): eaar3449.  
   - DOI: [10.1126/scirobotics.aar3449](https://doi.org/10.1126/scirobotics.aar3449)  
   - **Lane:** Synthetic / Living · **Strength:** High (real-ocean reef swimming demo, ~18 m class historically)  
   - **Path A:** Soft presence possible; endurance and multi-hour quiet still open · not a finished co-presence platform  

2. **Marchese, Onal & Rus (2014).** *Autonomous Soft Robotic Fish Capable of Escape Maneuvers Using Fluidic Elastomer Actuators.* **Soft Robotics** 1(1).  
   - DOI: [10.1089/soro.2013.0009](https://doi.org/10.1089/soro.2013.0009)  
   - **Lane:** Synthetic · **Strength:** High (tank / lab actuation)  
   - **Path A:** Soft actuation baseline; salt durability and loiter not solved  

### Undulatory propulsion · living + synthetic

3. **Sfakiotakis, Lane & Davies (1999).** *Review of fish swimming modes for aquatic locomotion.* **IEEE Journal of Oceanic Engineering** 24(2): 237–252.  
   - DOI: [10.1109/48.757275](https://doi.org/10.1109/48.757275)  
   - **Lane:** Living (classification) · **Strength:** High (canonical mode map: BCF, MPF, etc.)  
   - **Path A:** Mode language for transit vs hover vs survey  

4. **Lauder & Tytell (2005).** *Hydrodynamics of undulatory propulsion.* In *Fish Biomechanics* (Fish Physiology Vol. 23). Elsevier.  
   - DOI chapter family: see Elsevier Fish Physiology 23; review entry via [DOI 10.1016/S1546-5098(05)23011-X](https://doi.org/10.1016/S1546-5098(05)23011-X) (series)  
   - **Lane:** Living · **Strength:** High  
   - **Path A:** Cost-of-transport and wake-aware thrust · scale honesty  

5. **Yu et al. (review line, open access survey).** Undulatory biomimetic underwater robots — use a recent open review as entry, e.g. **Biomimetics** undulatory propulsion surveys (2023+).  
   - Example open door: MDPI *Biomimetics* search “undulatory underwater robot” · verify year/title when citing in a paper  
   - **Lane:** Synthetic · **Strength:** Medium (reviews vary)  
   - **Path A:** Control complexity and salt durability are recurring kill risks  

### Riblets · living → engineered

6. **Dean & Bhushan (2010).** *Shark-skin surfaces for fluid-drag reduction in turbulent flow: a review.* **Philosophical Transactions of the Royal Society A** 368: 4775–4806.  
   - DOI: [10.1098/rsta.2010.0201](https://doi.org/10.1098/rsta.2010.0201)  
   - **Lane:** Living / Synthetic transfer · **Strength:** High for drag physics in controlled flow  
   - **Path A:** Regime-matched riblets only; wrong spacing increases drag  

7. **Bechert et al. (1997).** *Experiments on drag-reducing surfaces and their optimization with an adjustable geometry.* **Journal of Fluid Mechanics** 338: 59–87.  
   - DOI: [10.1017/S0022112096004673](https://doi.org/10.1017/S0022112096004673)  
   - **Lane:** Synthetic (riblet optimization) · **Strength:** High  
   - **Path A:** s+ / h+ sizing method for Path A Reynolds  

### Self-noise · synthetic engineering

8. **Zimmerman, Chwaleba & others (2005).** *Decreasing the radiated acoustic and vibration noise of a mid-size AUV.* IEEE Journal of Oceanic Engineering / related IEEE vehicle noise work (IEEE document 1435585).  
   - IEEE entry: [ieeexplore.ieee.org/document/1435585](https://ieeexplore.ieee.org/document/1435585/)  
   - **Lane:** Synthetic · **Strength:** Medium–high (measured self-noise reduction practice)  
   - **Path A:** Hydrophone layout kill criteria depend on spectra during loiter  

9. **Urick (1983).** *Principles of Underwater Sound* (3rd ed.). Peninsula / McGraw-Hill classic.  
   - ISBN 0932146627 (common) · not a DOI monograph  
   - **Lane:** Synthetic (acoustics) · **Strength:** High for fundamentals  
   - **Path A:** Ambient vs self-noise framing for “useful band” language  

### Gliders · buoyancy endurance

10. **Eriksen et al. (2001).** *Seaglider: A Long-Range Autonomous Underwater Vehicle for Oceanographic Research.* **IEEE Journal of Oceanic Engineering** 26(4): 424–436.  
    - DOI: [10.1109/48.972073](https://doi.org/10.1109/48.972073)  
    - **Lane:** Synthetic · **Strength:** High  
    - **Path A:** Sparse energy / multi-hour loiter lessons · **not** a follow/hover substitute alone  

11. **Webb, Simonetti & Jones (2001).** *SLOCUM: An underwater glider propelled by environmental energy.* **IEEE Journal of Oceanic Engineering** 26(4): 447–452.  
    - DOI: [10.1109/48.972077](https://doi.org/10.1109/48.972077)  
    - **Lane:** Synthetic · **Strength:** High  
    - **Path A:** Buoyancy engine as endurance tool  

### Antifouling · foul-release

12. **Lejars, Margaillan & Bressy (2012).** *Fouling release coatings: A nontoxic alternative to biocidal antifouling coatings.* **Chemical Reviews** 112(8): 4347–4390.  
    - DOI: [10.1021/cr200350v](https://doi.org/10.1021/cr200350v)  
    - **Lane:** Synthetic · **Strength:** High (materials review)  
    - **Path A:** Cleanable / foul-release skins for multi-mission use  

13. **Callow & Callow (2011).** *Trends in the development of environmentally friendly fouling-resistant marine coatings.* **Nature Communications** 2: 244.  
    - DOI: [10.1038/ncomms1251](https://doi.org/10.1038/ncomms1251)  
    - **Lane:** Synthetic · **Strength:** High  
    - **Path A:** Non-biocidal directions preferred for research ethics where possible  

### Soft seawater durability (sparse)

14. **Soft robotics in real seawater — durability.** Literature remains **sparse** relative to tank demos. Treat follow-on SoFi / soft AUV field reports carefully; always check sealing, biofouling, and actuator lifetime claims.  
    - **Lane:** Synthetic · **Strength:** Low–medium · **Label:** often **Speculative** for multi-hour Path A loiter until measured  
    - **Path A:** Kill soft-identity product before endurance/noise solved  

### Leatherback · secondary volume-following only

15. **Davenport et al. / leatherback diving physiology literature.** Entry via reviews of leatherback depth and carapace compliance (see internal `docs/research-leatherback-osteoderms-2026-08-06.md` for house trail).  
    - **Lane:** Living · **Strength:** Medium for physiology · engineered transfer early  
    - **Path A:** Secondary only — do not delay upper-water quiet platform  

### Context only (not a competitor build plan)

16. **CETI / Project CETI public science narrative** (sperm whale bioacoustics at scale).  
    - Portal: [projectceti.org](https://www.projectceti.org/)  
    - **Lane:** Speculative / context · **Strength:** Program-level, not EvoForm vehicle evidence  
    - **Path A:** Awareness only — EvoForm does not outspend or twin-launch  

### Internal Path A packs (house)

17. EvoForm `briefs/quiet-small-auv-survey.md` · `docs/research-success-pack-2026-07-29.md` · `docs/research-instrument-path-a-eli-2026-08-06.md` · `briefs/leatherback-osteoderm-volume-following.md` · `briefs/path-a-job-card.md`

---

## Confidence rules

| Label | Use |
|-------|-----|
| **High** | Multiple independent studies or canonical reviews; transfer limits still apply |
| **Medium** | Solid demos or mixed field results |
| **Low / Speculative** | Sparse seawater durability, unmeasured co-presence, unvalidated noise claims |

Never present a tank demo as multi-hour hydrophone-grade quiet co-presence.

---

## Gaps (honest)

- **Vehicle-specific self-noise spectra** for Path A size: measure, do not invent.  
- **Riblets at Path A Reynolds in fouled coastal water:** lab drag ≠ one mission cycle with growth.  
- **Soft undulatory multi-hour salt life:** still an open engineering risk.

---

*Integrity first · multi-taxon teachers · evidence trail · sister CetaVox benefits from quieter loiter.*
