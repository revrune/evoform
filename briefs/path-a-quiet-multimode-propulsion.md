# EvoForm opportunity brief  
**Title:** Quiet multi-mode / sparse thrust propulsion (Path A bet 1)  
**Status:** **PERMANENT house opportunity brief** · 2026-08-06 · Kai from Eli instrument · judge against Path A job card  
**Project:** EvoForm · *In Accordance with Nature* · *Form Shaped by Evolution*  
**Job card (LOCKED · PERMANENT):** `briefs/path-a-job-card.md`  
**Instrument:** `docs/research-instrument-path-a-eli-2026-08-06.md` · **Papers:** `docs/path-a-papers-working-note-2026-08-06.md`  
**Sister:** CetaVox benefits from long quiet dwell  

---

## 1. Design problem

**In plain language:**  
Path A needs **propulsion that is quiet enough for hydrophone-grade loiter** and efficient enough for multi-hour battery life — without defaulting to continuous high-RPM open props that raise self-noise and disturbance.

**Win order (from job card):**  
1. Lower disturbance + quieter self-noise **plus** more efficient motion than a typical small prop AUV  
2. Longer loiter hours  
3. Easy deploy  

**Envelope:** 0.5–1.2 m · survey/hover primary · ~1–2 m/s transit when needed · battery multi-hour · boat deployable.

**Must-nots:** Free-lunch thrusters · robot-fish product identity · continuous loud prop as the “solution” · unlabeled sci-fi actuators.

---

## 2. Accordance check (physics)

Water is dense. Thrust costs energy and usually noise. **Unsteady / sparse thrust** can trade continuous broadband prop noise for intermittent or lower-RPM sources — only if control and durability hold at Path A Reynolds and power density.

**Mode separation is physics, not branding:**

| Mode | Job | Propulsion bias |
|------|-----|-----------------|
| Hover / loiter | Hold depth/heading for sensors | Buoyancy + minimal sparse thrust (see hover brief) |
| Slow survey | 0.2–1 m/s quiet track | Sparse / pulsed / low continuous |
| Transit | Close distance ~1–2 m/s | Efficient form + short continuous or undulatory burst |

**Natural ceiling:** actuator power density, seal life, control bandwidth, acoustic radiation from cavitation and structure-borne vibration.

---

## 3. Mechanisms (lanes labeled)

### 3.1 Synthetic · continuous small prop (baseline to beat)

| | |
|--|--|
| **What** | High-RPM ducted or open prop on small AUVs |
| **Lane** | Synthetic |
| **Evidence** | High (industry standard) |
| **Transfer** | Baseline for noise + power comparison |
| **Do not claim** | That “quiet props” automatically meet co-presence without measurement |

### 3.2 Living · pulsed jet (jelly / salp lessons)

| | |
|--|--|
| **What** | Discrete momentum pulses, soft or semi-soft chamber |
| **Lane** | Living → Synthetic transfer |
| **Evidence** | Medium for efficiency per pulse; control hard |
| **Transfer** | Duty-cycled pump for survey; not sole transit solution |
| **Do not claim** | Infinite range from soft jet alone |

### 3.3 Living · undulatory BCF (carangiform / thunniform lessons)

| | |
|--|--|
| **What** | Body–caudal undulation; wake-aware thrust |
| **Lane** | Living · Synthetic robots (SoFi-class) |
| **Evidence** | High biology; medium-high robotics ocean demos (short endurance) |
| **Transfer** | Optional year-2+ module after sparse thrust baseline ships |
| **Do not claim** | Soft fish = multi-hour quiet loiter (unproven) |

### 3.4 Synthetic · sparse / intermittent hybrid (Path A primary bet)

| | |
|--|--|
| **What** | Architecture: mostly off or low duty cycle; continuous only when required |
| **Lane** | Synthetic + Living lessons |
| **Evidence** | Composition of known modes — **inferred** as system architecture |
| **Transfer** | Software + hardware mode manager; thruster selection by noise/power table |
| **Do not claim** | Zero noise; claim **lower measured self-noise than baseline prop at same useful speed** |

### 3.5 Synthetic · glider-style sparse energy (supporting)

| | |
|--|--|
| **What** | Buoyancy engines for depth change with tiny prop use |
| **Lane** | Synthetic |
| **Evidence** | High (Seaglider, Slocum class) |
| **Transfer** | Energy for depth-keeping; **not** active mammal-following alone |

---

## 4. Constraints & transfer notes

| Constraint | Implication |
|------------|-------------|
| Path A size / battery | Power density limits soft undulatory first builds |
| Hydrophone mission | Propulsion chosen by **spectra**, not brochure dB |
| Makerspace build posture | Start with quietest available sparse thruster + sealed hull |
| Salt + fouling | Moving soft skins need cleanability (see foul-aware brief) |
| Efficient slow transit (bet 6) | Composed here + riblets brief — not a separate product |

**Cross-links:**  
- Hover without continuous wash → `briefs/path-a-hover-station-keep.md`  
- Transit efficiency → this brief §3 + `briefs/path-a-riblets-regime-matched.md`  
- Sensor isolation → `briefs/path-a-hydrophone-first-layout.md`

---

## 5. Experiments & kill criteria

| Experiment | Done bar | Kill |
|------------|----------|------|
| Tank noise + power at 0.3–1.5 m/s | Compare candidate sparse thrusters vs well-designed small prop (same vehicle mass class) | Cannot beat well-designed small prop on **noise-at-useful-speed** within Path A size/power |
| Mode switch latency | Hover ↔ survey ↔ transit without instability | Mode thrash wastes battery or raises noise floor |
| Seal / duty-cycle life (bench) | Multi-hour intermittent duty without leak/overheat | Soft or exotic actuators fail before makerspace prop |

**First build sequence (instrument):** sealed body + buoyancy + quietest available sparse thrust + hydrophone self-noise characterisation — **before** undulatory modules.

---

## 6. Evidence trail (subset)

- Katzschmann et al. 2018 SoFi — DOI 10.1126/scirobotics.aar3449  
- Sfakiotakis et al. 1999 swimming modes — DOI 10.1109/48.757275  
- Eriksen et al. 2001 Seaglider — DOI 10.1109/48.972073  
- Dean & Bhushan 2010 riblets (drag context for transit) — DOI 10.1098/rsta.2010.0201  
- Full shelf: `docs/path-a-papers-working-note-2026-08-06.md`

---

## 7. Refuse

- Continuous high-noise prop as default product story  
- Soft-robot identity before endurance + noise solved  
- Robot-fish / robot-whale branding  
- Free-lunch efficiency claims  

---

*Path A bet 1 · shareable opportunity brief · integrity first · no free lunch*
