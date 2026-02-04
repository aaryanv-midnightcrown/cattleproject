# Probabilistic Cattle Movement Forecasting  
**AI-assisted geospatial modeling prototype (South Sudan)**

---

## 📌 Project Overview

Unpredictable cattle movement in South Sudan contributes to local conflict, resource scarcity, and humanitarian risk.  
Despite the availability of open-source satellite imagery and geospatial data, there is currently no reliable, real-time framework for detecting, tracking, or forecasting cattle presence and movement over time.

This project explores how **AI-based probabilistic modeling**, combined with **geospatial indicators**, can be used to:
- Estimate **where cattle are likely to be located**
- Forecast **how cattle movement may evolve over time**
- Communicate **confidence and uncertainty** rather than false certainty

This repository contains **two iterations** of the system, each representing a meaningful technical and conceptual evolution.

---

## 🧠 Core Design Philosophy

- Predictions are **relative, not absolute**
- Outputs are **confidence-based**, not binary
- Models explicitly account for **uncertainty and incomplete data**
- All geospatial inputs are designed to be **replaceable with real satellite data**

This is a **decision-support prototype**, not a surveillance or tracking system.

---

## 📂 Project Structure


---

## 🚀 Version History

---

## 🔹 Version 1 (v1): Baseline Spatial AI Prototype

### Goal
Demonstrate that AI-driven spatial reasoning can highlight **relative cattle presence likelihood** using simplified geospatial inputs.

### Key Features
- Grid-based map representing geographic space
- Synthetic indicators for:
  - Water access
  - Human settlements
  - Known or recent cattle presence
- Heat-style visualization showing:
  - Strong
  - Probable
  - Possible presence
- Confidence levels normalized **per batch**, ensuring:
  - Dark regions always exist
  - Outputs reflect *relative certainty*, not fixed thresholds

### Limitations
- No temporal modeling
- No explicit movement forecasting
- AI logic focused on static spatial suitability

### Takeaway
v1 establishes the **core idea**: AI can surface spatial patterns of cattle presence under uncertainty — but does not yet model movement over time.

---

## 🔹 Version 2 (v2): Probabilistic Movement Forecasting Framework

### Goal
Extend v1 into a **temporally aware, movement-oriented forecasting system** aligned with real-world constraints in South Sudan.

### Major Improvements

#### 🛰️ Geospatial Framing
- All inputs explicitly framed as **satellite-derived or open-source proxies**:
  - Vegetation productivity (NDVI-like signal)
  - Surface water
  - Settlements
  - Historical cattle presence

#### 🧠 AI & Modeling Enhancements
- Movement suitability surface instead of static heatmap
- Temporal smoothing:
  - Previous predictions influence future likelihood
- Herd inertia:
  - Recent presence increases near-term probability
- Confidence tiers computed **per timestep**, not globally

#### ⏱️ Time-Aware Simulation
- Discrete timesteps simulate evolving conditions
- Herd priors shift between timesteps
- Model reflects *change*, not snapshots

#### 📊 Interpretability & Transparency
- In-app legend explaining:
  - Map symbols
  - Confidence tiers
  - AI output meaning
- Clear separation between:
  - Data generation
  - AI modeling
  - Visualization

### What v2 Represents
v2 is no longer just a visualization — it is a **conceptual forecasting framework** that could be extended to real satellite imagery, humanitarian planning, or conflict-risk analysis.

---

## Version 3 (v3): Logistic Regression Model Implemented
---

## 🧠 What’s New in Version 3

- Real neural network (PyTorch)
- Persistent learning across sessions
- Multi-factor environmental modeling
- Variable counts per scenario (including zero)
- Interactive, clean UI (Pygame)
- Scenario-normalized prediction confidence
- Explicit model saving and loading

This is **not** a scripted simulation — the AI actually learns.

---

## 🛰️ Modeled Factors (Satellite & Environment)

Each grid cell is evaluated using the following inputs:

1. **Water Sources**  
   Rivers, ponds, seasonal water bodies

2. **Vegetation Quality (NDVI proxy)**  
   Represents forage availability detectable via satellite imagery

3. **Villages**  
   Areas of economic reliance on cattle

4. **Cattle Camps**  
   Temporary human-managed herd locations

5. **Food Scarcity (Climate-driven)**  
   Amplifies reliance on vegetation and villages

6. **Water Scarcity (Climate-driven)**  
   Increases attraction to water sources

7. **Temperature Preference**  
   Models heat stress avoidance in cattle

Each factor can appear **multiple times or not at all** in a scenario.

---

## 🤖 AI Model Overview

- **Model Type:** Fully-connected neural network  
- **Framework:** PyTorch  
- **Input:** 9 features per grid cell  
- **Output:** Probability of cattle presence  
- **Training:** Incremental, scenario-based  
- **Persistence:** Model weights saved to disk  

Predictions are visualized as a confidence heatmap:
- Light yellow → low probability
- Yellow → likely
- Dark yellow → strong confidence (relative to the scenario)

---

## 🎮 Controls

| Key | Action |
|---|---|
| **A** | Toggle AI prediction overlay |
| **N** | Generate new scenario and train AI |
| **S** | Save AI model |
| **K** | Show/hide legend |
| **↑ / ↓** | Select environmental variable |
| **[ / ]** | Decrease / increase selected variable count |

---

Install dependencies:

```bash
pip3 install pygame numpy torch


## Running the Project

### Requirements
- Python 3.9+
- `pygame`
- `numpy`

Install dependencies:
```bash
pip install pygame numpy
