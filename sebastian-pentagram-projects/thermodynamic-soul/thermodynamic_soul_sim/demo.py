import os
import numpy as np
import matplotlib.pyplot as plt
from coherence_metrics import C_soul, phase_mask
from csc_lattice import random_transitions

os.makedirs("figures", exist_ok=True)
os.makedirs("data", exist_ok=True)

# 1) C_soul vs entropy for different coherence and persistence
phi = 5.0  # arbitrary units
S = np.linspace(0.0, 5.0, 200)
for lambda_coh, t_persist in [(0.3, 0.2), (0.6, 0.5), (0.9, 1.0)]:
    C = C_soul(phi, lambda_coh, t_persist, S, beta=1.0)
    plt.figure()
    plt.plot(S, C)
    plt.xlabel("Entropy S (a.u.)")
    plt.ylabel("C_soul (a.u.)")
    plt.title(f"C_soul vs S  (phi={phi}, lambda={lambda_coh}, t={t_persist})")
    plt.grid(True, alpha=0.3)
    plt.savefig(f"figures/csoul_vs_S_phi{phi}_lam{lambda_coh}_t{t_persist}.png", dpi=160)
    plt.close()

# Save one curve to CSV
C_example = C_soul(phi, 0.6, 0.5, S, beta=1.0)
np.savetxt("data/csoul_vs_S_example.csv", np.c_[S, C_example], delimiter=",", header="S,C_soul", comments="")

# 2) Energy comparison for ternary transitions
_, _, E_direct, E_via0 = random_transitions(n=20000, p=[1/3, 1/3, 1/3], seed=42)
mean_direct = E_direct.mean()
mean_via0 = E_via0.mean()

plt.figure()
plt.bar([0,1], [mean_direct, mean_via0])
plt.xticks([0,1], ["Direct flip", "Via 0"])
plt.ylabel("Mean energy per transition (a.u.)")
plt.title("Ternary transition energy (toy model)")
plt.grid(True, axis="y", alpha=0.3)
plt.savefig("figures/ternary_transition_energy.png", dpi=160)
plt.close()

# Save energy samples
np.savetxt("data/transition_energy_direct.csv", E_direct, delimiter=",", header="E_direct", comments="")
np.savetxt("data/transition_energy_via0.csv", E_via0, delimiter=",", header="E_via0", comments="")

# 3) Phase diagram on (S, lambda) plane for fixed phi and t
phi_fixed = 5.0
t_fixed = 0.5
beta = 1.0
S_grid = np.linspace(0, 5, 150)
L_grid = np.linspace(0.1, 1.0, 150)
S_mesh, L_mesh = np.meshgrid(S_grid, L_grid)
C_mesh = C_soul(phi_fixed, L_mesh, t_fixed, S_mesh, beta=beta)
mask = phase_mask(C_mesh, C_star=1.0)

plt.figure()
# Simple visualization: show C values as image; no custom colors
plt.imshow(C_mesh, origin='lower', extent=[S_grid.min(), S_grid.max(), L_grid.min(), L_grid.max()], aspect='auto')
plt.colorbar(label="C_soul")
plt.xlabel("Entropy S")
plt.ylabel("Coherence λ")
plt.title(f"Phase scan of C_soul (phi={phi_fixed}, t={t_fixed})")
plt.savefig("figures/phase_scan_csoul.png", dpi=160)
plt.close()

print("Done. Figures written to ./figures and CSV to ./data")
