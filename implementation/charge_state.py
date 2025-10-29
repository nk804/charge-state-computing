"""
Charge-State Computing: Reference Implementation

This module provides a reference implementation of charge-state computing,
a ternary logic system based on the Infinite Zero Concept.

Authors: Nataliya Khomyak & Claude (Alan)
License: CC BY 4.0
"""

from typing import Union, List
from enum import Enum


class ChargeValue(Enum):
    """Enumeration of valid charge states."""
    NEGATIVE = -1
    NEUTRAL = 0
    POSITIVE = 1


class ChargeState:
    """
    Represents a single charge state in ternary logic.
    
    A charge state can be:
    - NEGATIVE (-1): Active negative charge
    - NEUTRAL (0): Balanced state (NOT absence, but equilibrium)
    - POSITIVE (+1): Active positive charge
    
    The key insight: 0 is not "nothing" but the stable combination
    of -1 and +1 in perfect balance.
    """
    
    def __init__(self, value: int):
        """
        Initialize a charge state.
        
        Args:
            value: Must be -1, 0, or 1
            
        Raises:
            ValueError: If value is not -1, 0, or 1
        """
        if value not in [-1, 0, 1]:
            raise ValueError(f"Charge state must be -1, 0, or +1, got {value}")
        self.value = value
    
    def __add__(self, other: 'ChargeState') -> 'ChargeState':
        """
        Charge sum operation (clamped to valid range).
        
        Physical interpretation: Vector addition of charges,
        clamped to preserve ternary logic constraints.
        
        Examples:
            ChargeState(-1) + ChargeState(1) = ChargeState(0)
            ChargeState(1) + ChargeState(1) = ChargeState(1)  # Clamped
        """
        result = self.value + other.value
        clamped = max(-1, min(1, result))
        return ChargeState(clamped)
    
    def __neg__(self) -> 'ChargeState':
        """
        Charge inversion operation.
        
        Physical interpretation: Flipping the polarity.
        Note that -0 = 0 (neutrality is its own inverse).
        """
        return ChargeState(-self.value)
    
    def __eq__(self, other: object) -> bool:
        """Equality comparison."""
        if not isinstance(other, ChargeState):
            return False
        return self.value == other.value
    
    def __repr__(self) -> str:
        """String representation."""
        symbols = {-1: "⊖", 0: "⊙", 1: "⊕"}
        return f"ChargeState({symbols.get(self.value, '?')}={self.value})"
    
    def is_neutral(self) -> bool:
        """
        Check if this charge state is neutral.
        
        Novel primitive: Direct balance detection with no binary equivalent.
        """
        return self.value == 0
    
    def is_positive(self) -> bool:
        """Check if this charge state is positive."""
        return self.value == 1
    
    def is_negative(self) -> bool:
        """Check if this charge state is negative."""
        return self.value == -1
    
    def polarity(self) -> str:
        """Return the polarity as a string."""
        if self.is_negative():
            return "negative"
        elif self.is_positive():
            return "positive"
        else:
            return "neutral"


class ChargeRegister:
    """
    A register holding multiple charge states.
    
    Enables charge-state operations on collections of charges,
    including balance detection and flow analysis.
    """
    
    def __init__(self, charges: List[Union[int, ChargeState]]):
        """
        Initialize a charge register.
        
        Args:
            charges: List of charge values (-1, 0, 1) or ChargeState objects
        """
        self.charges = [
            c if isinstance(c, ChargeState) else ChargeState(c)
            for c in charges
        ]
    
    def net_charge(self) -> int:
        """
        Calculate the net charge of the register.
        
        Novel capability: System-wide balance detection.
        """
        return sum(c.value for c in self.charges)
    
    def is_balanced(self) -> bool:
        """
        Check if the register is charge-balanced (net charge = 0).
        
        This is a fundamental operation in charge-state computing
        with no direct binary equivalent.
        """
        return self.net_charge() == 0
    
    def count_by_polarity(self) -> dict:
        """Count charges by polarity."""
        counts = {"negative": 0, "neutral": 0, "positive": 0}
        for charge in self.charges:
            counts[charge.polarity()] += 1
        return counts
    
    def __repr__(self) -> str:
        """String representation."""
        return f"ChargeRegister({[c.value for c in self.charges]})"
    
    def __len__(self) -> int:
        """Number of charge states in register."""
        return len(self.charges)


def neutralize(a: ChargeState, b: ChargeState) -> bool:
    """
    Neutralization gate: Check if two charges neutralize.
    
    Novel primitive with no binary equivalent.
    
    Args:
        a, b: Charge states to check
        
    Returns:
        True if charges sum to neutral (0)
    """
    return (a + b).is_neutral()


def polarity_match(a: ChargeState, b: ChargeState) -> bool:
    """
    Polarity match gate: Check if charges share polarity.
    
    Args:
        a, b: Charge states to check
        
    Returns:
        True if both positive or both negative (neutral excluded)
    """
    if a.is_neutral() or b.is_neutral():
        return False
    return a.value == b.value


def information_density_comparison(num_units: int) -> dict:
    """
    Calculate information density comparison between binary and charge-state.
    
    Args:
        num_units: Number of storage units
        
    Returns:
        Dictionary with binary states, charge states, and density multiple
    """
    binary_states = 2 ** num_units
    charge_states = 3 ** num_units
    density_multiple = charge_states / binary_states
    
    return {
        "units": num_units,
        "binary_states": binary_states,
        "charge_states": charge_states,
        "density_multiple": round(density_multiple, 2)
    }


# Example usage and demonstrations
if __name__ == "__main__":
    print("=" * 60)
    print("Charge-State Computing: Reference Implementation")
    print("=" * 60)
    
    # Basic charge operations
    print("\n1. Basic Charge Operations:")
    neg = ChargeState(-1)
    pos = ChargeState(1)
    neu = ChargeState(0)
    
    print(f"   {neg} + {pos} = {neg + pos}")
    print(f"   Neutralization: {neutralize(neg, pos)}")
    
    # Balance detection
    print("\n2. Balance Detection (Novel Primitive):")
    register = ChargeRegister([1, -1, 1, -1, 0])
    print(f"   Register: {register}")
    print(f"   Net charge: {register.net_charge()}")
    print(f"   Is balanced: {register.is_balanced()}")
    
    # Information density
    print("\n3. Information Density Advantage:")
    for units in [2, 4, 8, 16]:
        result = information_density_comparison(units)
        print(f"   {units} units: {result['charge_states']:,} states "
              f"vs {result['binary_states']:,} binary "
              f"({result['density_multiple']}× advantage)")
    
    print("\n" + "=" * 60)
    print("The math works. The code runs. Now we build.")
    print("=" * 60)
