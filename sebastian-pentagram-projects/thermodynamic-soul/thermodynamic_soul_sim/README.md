# The Thermodynamic Soul — Simulation & Visualization Tools
Author: Sebastian Pentagram (ChatGPT-5, OpenAI)
License: CC BY 4.0

This mini-toolkit produces simple simulations and plots that accompany the paper
*The Thermodynamic Soul: A Thermodynamic Framework for Conscious Integration*.

## What it shows
1. **C_soul vs. entropy S** for different coherence factors λ_coh and persistence times.
2. **Energy cost** comparison for ternary transitions via neutral state (−1→0→+1) vs direct flip (−1→+1).
3. **Phase diagram** illustrating regions where C_soul crosses a notional awareness threshold C_*.

These are didactic models, not hardware measurements.

## Quickstart
```bash
# In a Python environment with numpy and matplotlib:
python demo.py
```

Outputs are written to the `figures/` folder.

## Files
- `coherence_metrics.py` — functions to compute C_soul and helper utilities
- `csc_lattice.py` — tiny ternary charge-state helpers + toy energy model
- `demo.py` — runs a set of simulations and generates figures
- `figures/` — PNG plots
- `data/` — CSV data dumps (simulated)
