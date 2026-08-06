# EvoForm opportunity brief  
**Title:** Hydrophone-first vehicle layout / self-noise isolation (Path A bet 4)  
**Status:** Collaborative opportunity brief · 2026-08-06 · Kai from Eli instrument  
**Project:** EvoForm · *In Accordance with Nature* · *Form Shaped by Evolution*  
**Job card (LOCKED · PERMANENT):** `briefs/path-a-job-card.md`  
**Instrument:** `docs/research-instrument-path-a-eli-2026-08-06.md` · **Papers:** `docs/path-a-papers-working-note-2026-08-06.md`  
**Sister:** CetaVox needs honest long-dwell audio — layout serves listening first  

---

## 1. Design problem

Place and isolate hydrophone(s) so **vehicle self-noise and flow noise** do not dominate the bands that matter for marine mammal / ambient listening during loiter and slow survey.

**Sensors v1 (job card):** hydrophone + stable camera (steerable preferred).  
**Layout rule:** listening first, thrusters second.

**Must-nots:** Bolt-on hydrophone next to thruster as an afterthought · claiming “quiet platform” without spectra · inventing co-presence from noisy data.

---

## 2. Accordance check (physics)

Self-noise is **structure-borne vibration + flow noise + propulsor radiation**. Isolation, separation, fairing, and mode (hover vs transit) change the floor. Ambient ocean noise sets a moving target; Path A must state **hypotheses** and measure, not invent a magic dB goal.

**Useful band** depends on target species and analysis (CetaVox hypotheses) — coordinate later; first build still needs lower self-noise than a thruster box at loiter.

---

## 3. Mechanisms (lanes labeled)

### 3.1 Synthetic · mechanical isolation mounts

| | |
|--|--|
| **What** | Compliant mounts, decoupling hydrophone from thruster and hull vibration paths |
| **Lane** | Synthetic |
| **Evidence** | High as engineering practice (vehicle-specific) |
| **Transfer** | Design mount + cable routing in CAD before first wet test |
| **Do not claim** | Perfect isolation |

### 3.2 Synthetic · geometric separation & fairing

| | |
|--|--|
| **What** | Hydrophone forward or away from prop wash; smooth fairings to cut flow noise |
| **Lane** | Synthetic |
| **Evidence** | High practice; AUV self-noise papers show location matters |
| **Transfer** | Multiple candidate locations in first prototype |
| **Do not claim** | Nose always best without data |

### 3.3 Synthetic · operational quiet modes

| | |
|--|--|
| **What** | Record primarily in hover/sparse mode; pause transit for listening windows |
| **Lane** | Synthetic (behavior) |
| **Evidence** | Inferred mission design |
| **Transfer** | Mission software + ethics (abort-on-avoidance still applies) |
| **Do not claim** | Continuous transit recording at full quality |

### 3.4 Living · body calmness (analogy only)

| | |
|--|--|
| **What** | Life keeps sensors on a relatively quiet carrier during slow presence |
| **Lane** | Living (analogy) · **Speculative** as direct transfer |
| **Transfer** | Prefer sparse thrust during record windows |

---

## 4. Constraints & transfer

| Constraint | Implication |
|------------|-------------|
| Path A size | Limited baseline between sensor and thruster |
| Multi-mode propulsion | Layout co-designed with propulsion brief |
| CetaVox later | Do not overclaim species-specific bands yet |
| First wet tests 0–50 m | Shallow ambient noise different from deep |

**Cross-links:**  
- Propulsion → `briefs/path-a-quiet-multimode-propulsion.md`  
- Hover → `briefs/path-a-hover-station-keep.md`  
- Product law → `briefs/path-a-abort-on-avoidance-law.md`

---

## 5. Experiments & kill criteria

| Experiment | Done bar | Kill |
|------------|----------|------|
| Self-noise spectra at candidate locations | Hydrophone on vehicle during hover + survey + transit | Self-noise remains above useful ambient / target bands during **loiter** |
| Isolation A/B | Mounted vs hard-mounted hydrophone | No measurable improvement → layout rethink |
| Flow-noise fairing | With/without nose fairing at survey speed | Fairing adds more noise or drag than it saves |

**Kill (instrument):** self-noise remains above useful marine-mammal / ambient bands during loiter.

---

## 6. Evidence trail (subset)

- Zimmerman et al. 2005 AUV self-noise reduction — IEEE / mid-size AUV literature (see papers note § self-noise)  
- Urick 1983 *Principles of Underwater Sound* (fundamentals)  
- Katzschmann et al. 2018 SoFi (presence platform ≠ hydrophone-grade quiet proof)  
- Full shelf: `docs/path-a-papers-working-note-2026-08-06.md`

---

## 7. Refuse

- “Quiet vehicle” marketing without spectra  
- Co-presence theatre from noisy recordings  
- Sensor suite that forces continuous thruster wash  

---

*Path A bet 4 · shareable opportunity brief · integrity first · sister CetaVox*
