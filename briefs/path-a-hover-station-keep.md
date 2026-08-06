# EvoForm opportunity brief  
**Title:** Hover / station-keep without continuous prop wash (Path A bet 3)  
**Status:** **PERMANENT house opportunity brief** · 2026-08-06 · Kai from Eli instrument · judge against Path A job card  
**Project:** EvoForm · *In Accordance with Nature* · *Form Shaped by Evolution*  
**Job card (LOCKED · PERMANENT):** `briefs/path-a-job-card.md`  
**Instrument:** `docs/research-instrument-path-a-eli-2026-08-06.md` · **Papers:** `docs/path-a-papers-working-note-2026-08-06.md`  

---

## 1. Design problem

Hold depth, attitude, and slow station for **hydrophone + camera** in mild current **without** continuous prop wash destroying self-noise floor and battery life.

**Job-card secondary win:** multi-hour loiter on one battery.  
**Primary win still rules:** quieter + lower disturbance than thruster box.

**Must-nots:** Pure glider that cannot observe with control · continuous props for “hover” as default · claiming zero energy hover in current without measurement.

---

## 2. Accordance check (physics)

Hover is a **force balance** problem: buoyancy, weight, drag from current, and control authority. Continuous thrusters solve it by burning power and radiating noise. Life and gliders solve long presence with **buoyancy engines** and **fine foil force**, not constant RPM.

**Mild current** is the honest first target. Strong current may force short prop bursts — measure when noise becomes unacceptable for the hydrophone mission.

---

## 3. Mechanisms (lanes labeled)

### 3.1 Synthetic · variable buoyancy (glider lessons)

| | |
|--|--|
| **What** | Change displaced volume / ballast to rise, sink, or trim |
| **Lane** | Synthetic |
| **Evidence** | High (Seaglider, Slocum endurance) |
| **Transfer** | Active or semi-active buoyancy for 0–50 m (design toward 200 m) |
| **Do not claim** | Glider alone = co-presence follow mode |

### 3.2 Living · paired / median fins (labriform lessons)

| | |
|--|--|
| **What** | Small vectoring fins for attitude and slow station |
| **Lane** | Living → Synthetic |
| **Evidence** | High biology; medium robotics |
| **Transfer** | Paired fins for hover assist with sparse thruster backup |
| **Do not claim** | Ray-wing product identity |

### 3.3 Synthetic · minimal sparse thrust assist

| | |
|--|--|
| **What** | Intermittent micro-bursts only when buoyancy+fins insufficient |
| **Lane** | Synthetic |
| **Evidence** | Inferred system design |
| **Transfer** | Tied to multi-mode propulsion architecture |
| **Do not claim** | Silent in all sea states |

---

## 4. Constraints & transfer

| Constraint | Implication |
|------------|-------------|
| Multi-hour battery | Hover power budget is a hard number — instrument kill criterion |
| Sensor stability | Attitude hold for camera/hydrophone matters as much as depth |
| Norwegian-adjacent seas later | Current and cold increase power needs — design margins |
| Path A size | Buoyancy engine must fit 0.5–1.2 m hull |

**Cross-links:**  
- Propulsion modes → `briefs/path-a-quiet-multimode-propulsion.md`  
- Hydrophone isolation → `briefs/path-a-hydrophone-first-layout.md`

---

## 5. Experiments & kill criteria

| Experiment | Done bar | Kill |
|------------|----------|------|
| Static hover power (tank / pool) | Watts and estimated hours on Path A battery | Hover power destroys multi-hour battery goal |
| Low-current station-keep | Hold heading/depth with buoyancy+fins; log noise | Continuous prop required for mild current → architecture fails mission |
| Noise during hover | Spectra vs prop-hover baseline | Self-noise not below useful band for loiter listening |

---

## 6. Evidence trail (subset)

- Eriksen et al. 2001 Seaglider — DOI 10.1109/48.972073  
- Webb et al. 2001 Slocum — DOI 10.1109/48.972077  
- Sfakiotakis et al. 1999 modes (labriform / MPF) — DOI 10.1109/48.757275  
- Full shelf: `docs/path-a-papers-working-note-2026-08-06.md`

---

## 7. Refuse

- Pure glider marketed as mammal co-presence vehicle  
- Continuous prop wash as “hover solution”  
- Free-lunch zero-power station-keep in current  

---

*Path A bet 3 · shareable opportunity brief · integrity first*
