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

## 🖥️ Running the Project

### Requirements
- Python 3.9+
- `pygame`
- `numpy`

Install dependencies:
```bash
pip install pygame numpy
