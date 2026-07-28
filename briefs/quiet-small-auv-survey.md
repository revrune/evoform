# EvoForm opportunity brief  
**Lane:** Fluid locomotion · water first  
**Status:** Showcase seed (from 2026-07-28 product talk) — collaborative, not a finished engineering spec  
**Project:** EvoForm · *In Accordance with Nature*

---

## 1. Design problem

**Title:** Quiet, efficient small AUV for long surveys  

**In plain language:**  
We need a **small underwater vehicle** that can:

- Survey for a long time on limited energy  
- Move and hover with **low noise / low disturbance** (better data, less wildlife impact, stealth where needed)  
- Hold station or crawl slowly in **mild current**  
- Fit a research / coastal / nearshore budget and handling (boat deployable, not a submarine)

**Typical constraints (adjust in collaboration):**

| Constraint | Example range |
|------------|----------------|
| Size | ~0.3–1.5 m length; one–two person deploy |
| Speed | Mostly slow survey (0.2–1.5 m/s), occasional transit |
| Depth | Coastal / shelf first (e.g. 0–200 m), not full ocean |
| Energy | Battery; hours to a day+ preferred |
| Noise | Prefer low acoustic and hydrodynamic disturbance |
| Control | Stable heading, depth, and path for sensors (camera, sonar, eDNA, CTD) |
| Environment | Kelp, rock, soft bottom, mild current; some clutter |

**Must-nots (starting set):**  
No assumption of unlimited power. No “just copy a dolphin skin” without mechanism. No unlabeled sci-fi thrusters.

---

## 2. Accordance check (physics first)

Water is dense and incompressible. Motion costs **drag** and **inertia**. What works depends on **scale and speed** (Reynolds number roughly: inertial vs viscous).

For a **small AUV at survey speeds**, you are usually in a **mixed / inertial regime**: vortices, pressure drag, and surface design matter a lot; pure “microbe swimming physics” does not. Life still wins by:

- Shaping the **body + boundary layer**  
- Timing thrust (**unsteady** propulsion)  
- Using **flexibility and resonance** instead of constant hard push  
- Separating **slow efficient cruise**, **hover**, and **burst** instead of one thruster mode for everything  

**Natural ceiling:** energy, materials, control bandwidth, and the fluid itself — not marketing.

---

## 3. Natural strategies (multi-lane)

### 3.1 Living · soft pulsed jet (jellyfish, salps)

| | |
|--|--|
| **What** | Soft body + pulsed water jet; high efficiency per distance in some regimes |
| **Mechanism** | Momentum in discrete pulses; body elasticity recovers energy; large volume, low exhaust speed can be efficient |
| **Transfer** | Soft or semi-soft rear “bell”; pulsed pump rather than continuous high-RPM prop; duty-cycled thrust for quiet survey |
| **Status** | **Established** as biological strategy; **inferred** for small AUVs |
| **Do not claim** | “Jellyfish = free infinite range.” Efficiency depends on size, pulse timing, and mission profile |

### 3.2 Living · body–caudal undulation (fish: carangiform / thunniform)

| | |
|--|--|
| **What** | Posterior body and tail wave; thrust from interacting with own wake |
| **Mechanism** | Controlled vorticity; flexible foil; continuous but distributed deformation |
| **Transfer** | Flexible caudal “fin” or multi-joint tail; avoid over-rigid “hinged plate only” |
| **Status** | **Established** biology; **inferred / demonstrated** in robotic fish |
| **Do not claim** | Instant tuna efficiency at any size |

### 3.3 Living · median / paired fin “labriform” & rajiform (wrasses, rays)

| | |
|--|--|
| **What** | Pectoral or large wing-like fins for precise, often quieter local control |
| **Mechanism** | Distributed force; fine vectoring; good for station-keeping and clutter |
| **Transfer** | Side fins or “ray wings” for hover; main body stays calm for sensors |
| **Status** | **Established** biology; **inferred** for inspection-class AUVs |
| **Do not claim** | Best for long open-water transit without hybridizing with another cruise mode |

### 3.4 Living · streamlining + surface strategies

| | |
|--|--|
| **What** | Low drag shapes; surface textures; mucus; appendage tucking |
| **Mechanism** | Delay separation, manage turbulence, reduce skin friction and form drag |
| **Transfer** | Hull fineness ratio; fairing of sensors; bio-inspired coatings only with evidence at your Re |
| **Status** | **Established** (shape); **mixed** (riblets/denticle analogues) |
| **Do not claim** | “Shark skin sticker always cuts 30% drag on any AUV” |

### 3.5 Living · buoyancy + sparse thrust

| | |
|--|--|
| **What** | Near-neutral buoyancy; small forces for depth and station |
| **Mechanism** | Don’t fight gravity/buoyancy every second; thrusters only correct error |
| **Transfer** | Variable buoyancy system (VBS); survey = drift + micro-corrections |
| **Status** | **Established** in nature and in gliders / some AUVs |

### 3.6 Extreme · deep / cold / high-pressure body plans

Soft, low-density, efficient slow movers. **Inferred** design lessons — not one-to-one products.

### 3.7 Deep-time · extinct efficient swimmers

Same fluid laws; different morphospace. **Evidence-based speculation** when linking form → function carefully.

### 3.8 Synthetic · soft robots, artificial muscles, hybrid living materials

**Synthetic** lane — real labs; product readiness uneven. Power, heat, reliability, marine environment, ethics must be explicit.

---

## 4. Abstract principles

1. Match propulsor to mission phase — transit ≠ survey ≠ hover.  
2. Prefer unsteady / pulsed / flexible thrust when continuous props waste energy and raise noise.  
3. Buy efficiency from buoyancy and drag before buying a bigger battery.  
4. Keep the sensor body calm — put violence of thrust aft or outboard.  
5. Design the wake on purpose.  
6. Quiet is a fluid problem as much as a motor problem.  
7. Scale honestly — a 40 cm robot is not a tuna and not a copepod.

---

## 5. Design directions

### Path A — Quiet survey hybrid (recommended first collaboration target)

- Streamlined rigid center (sensors, battery, computer)  
- Variable buoyancy for depth and low-cost station assist  
- Paired fins or soft lateral actuators for hover / slow crabbing  
- Pulsed jet or flexible tail for transit  
- Control: survey mode defaults to minimum thruster duty cycle  

### Path B — Robotic fish primary  
### Path C — Glider-first  
### Path D — Soft bell / pulsed  

---

## 6. Open questions

- Coastal species for quiet station-keeping in mild current?  
- For 0.5–1 m vehicles at ~0.5 m/s: quieter for equal thrust — low-RPM large prop, undulatory fin, or pulsed jet?  
- Soft-tail handling on a working deck; fouling on flexible surfaces  
- Acoustic impact vs traditional props  

---

## 7. Honesty seal

- No single organism is “the” AUV design  
- No guaranteed range or dB numbers without prototype + protocol  
- Biomimetic skin alone does not fix a bad hull or bad control  
- Synthetic / soft paths are not field-ready by default  

---

## 8. One-line summary

**In accordance with nature:** a small survey AUV should not fight the sea with one loud continuous prop if life shows that **buoyancy, low drag, flexible multi-mode thrust, and sparse timed forces** already solve long, quiet presence in water.

---

*Seeded from EvoForm product talk 2026-07-28. Collaborators welcome to upgrade labels with papers and tank tests.*
