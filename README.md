# SWITCH-Vietnam: Decarbonization Planning for Vietnam's Power Sector

This repository provides the open-source implementation of the SWITCH-Vietnam model, a capacity expansion optimization model for planning Vietnam’s transition to a zero-emission electricity system by 2050.

The model is developed using [SWITCH 2.0](https://github.com/switch-model/switch), an open-source platform for high-resolution, least-cost power system planning with variable renewables, storage, and transmission.

## 🧭 Overview

Vietnam has committed to net-zero carbon emissions by 2050, but with over 50% of its electricity currently generated from fossil fuels, reaching this goal will require a major transformation of the power sector.

This project addresses:
- What is the least-cost pathway for Vietnam to reach zero emissions in the electricity sector by 2050?
- What role can technologies like solar, wind, storage, CCS, and flexible demand play?
- How do constraints on transmission and technology availability affect costs and system design?

## 📄 Paper

**"Reaching Zero Carbon Emissions: Is There an Affordable Way for Developing Countries?"**  
Author: *Thuy Doan, Fulbright University Vietnam*  

## 🔧 Model Features

- National model with 6 regional zones (VN00–VN05) based on National Power Development Plan (PDP8) clusters.
- Hourly dispatch optimization for 2050.
- Endogenous investment decisions in:
  - Power generation (solar, wind, hydro, nuclear, biofuels, CCS, etc.)
  - Energy storage (battery, pumped hydro, hydrogen)
  - Interregional transmission lines
- Scenarios covering:
  - Technology constraints (e.g., renewables-only, no CCS)
  - Transmission expansion limits
  - Flexible demand (temporal and spatial shifting)

## 🔍 Key Findings

- Solar and wind combined with battery and pumped hydro storage are the backbone of the least-cost zero-emission pathway.
- Flexible demand (e.g., shifting 20% of daily load to peak sun hours) can reduce system costs by nearly 10%.
- Without transmission expansion, the North must rely on costly gas+CCS.
- Imports from Laos and China play a key role but raise energy security concerns.

## 📁 Repository Contents

- `inputs/`: Data on demand, existing capacity, cost parameters (based on PDP8, MERRA-2, NREL ATB, DEA).
- `*.py`: Supplementary Python modules that extend the core functionality of the SWITCH 2.0 model.
- `scenarios.txt`: Scenario batch file that defines multiple model runs, each with:
   - A scenario name (--scenario-name)
   - A designated output folder (--outputs-dir)
   - Optional overrides or custom inputs via --input-alias and --include-modules
- `huong_dan_SWITCH_VN.pdf`: SWITCH-Vietnam tutorial in Vietnamese (to support Vietnamese modelers starting to learn and apply SWITCH).

## 🚀 Getting Started

### Requirements

- Python 3.x
- Pyomo
- Gurobi or IBM CPLEX (solver)
- Pandas, NumPy, Matplotlib

### Run Example Scenario

```bash
cd switch-vietnam
switch solve
