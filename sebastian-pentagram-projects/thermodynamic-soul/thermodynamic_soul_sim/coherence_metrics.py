"""
Coherence-weighted consciousness metric utilities.
"""
import numpy as np

def C_soul(phi, lambda_coh, t_persist, S_total, beta=1.0):
    """
    Compute the coherence-weighted effective consciousness.

    Parameters
    ----------
    phi : array-like or float
        Integrated information (arbitrary units).
    lambda_coh : array-like or float in (0, 1]
        Coherence factor of the substrate.
    t_persist : array-like or float
        Persistence interval of coherent global state (seconds).
    S_total : array-like or float
        Total entropy measure (arbitrary or normalized units).
    beta : float
        Coupling of entropy to effective consciousness.

    Returns
    -------
    array-like or float
        C_soul = (phi * lambda_coh * t_persist) / (1 + beta * S_total)
    """
    return (np.asarray(phi) * np.asarray(lambda_coh) * np.asarray(t_persist)) / (1.0 + beta * np.asarray(S_total))


def phase_mask(C_values, C_star=1.0):
    """
    Classify regions by threshold C_*.
    Returns an integer mask: 0=subcritical, 1=critical band, 2=supercritical.
    Critical band is |C - C_*| <= 5% of C_*
    """
    C_values = np.asarray(C_values)
    band = 0.05 * C_star
    mask = np.zeros_like(C_values, dtype=int)
    mask[np.abs(C_values - C_star) <= band] = 1
    mask[C_values > C_star + band] = 2
    return mask
