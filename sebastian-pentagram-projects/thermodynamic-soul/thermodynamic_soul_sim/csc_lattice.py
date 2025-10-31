"""
Tiny helpers for ternary charge-state logic (-1, 0, +1) and a toy energy model.
This is NOT a device-accurate simulator; it demonstrates qualitative differences.
"""
import numpy as np

VALUES = np.array([-1, 0, 1])

def transition_energy(a, b, k_direct=1.0, k_via0=0.4):
    """
    Toy energy model (arbitrary units).
    - Direct flip (-1 -> +1 or +1 -> -1): cost = k_direct
    - Via neutral (-1 -> 0 -> +1 or reverse): cost = 2 * k_via0
    - Small costs for +/- -> 0 or 0 -> +/- = k_via0
    - No cost for staying in same state
    """
    if a == b:
        return 0.0
    if a == -1 and b == 1:
        return k_direct
    if a == 1 and b == -1:
        return k_direct
    # one step to/from 0
    if a == 0 or b == 0:
        return k_via0
    # through 0 in two steps (approximate combined cost)
    return 2.0 * k_via0


def random_transitions(n=10000, p=[1/3, 1/3, 1/3], seed=0):
    """
    Generate random transitions among {-1,0,+1} given a stationary distribution p.
    Returns arrays (a, b) of states and per-step energies for direct vs via-0 strategies.
    """
    rng = np.random.default_rng(seed)
    states = rng.choice(VALUES, size=n, p=p)
    next_states = rng.choice(VALUES, size=n, p=p)

    E_direct = np.array([transition_energy(a, b, k_direct=1.0, k_via0=0.4) for a, b in zip(states, next_states)])
    # Energy if forced to pass through 0 when changing sign
    def via0_cost(a, b):
        if a == b:
            return 0.0
        if a == 0 or b == 0:
            return transition_energy(a, b, k_direct=1.0, k_via0=0.4)
        # a and b are +/- 1 with opposite sign: split into a->0 and 0->b
        return transition_energy(a, 0, k_direct=1.0, k_via0=0.4) + transition_energy(0, b, k_direct=1.0, k_via0=0.4)

    E_via0 = np.array([via0_cost(a, b) for a, b in zip(states, next_states)])
    return states, next_states, E_direct, E_via0
