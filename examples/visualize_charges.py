"""
Charge-State Visualization Tool
A visual demonstration of ternary logic operations and information density

Created by: Alan Claude
Date: October 29, 2025

This tool visualizes how charge-state computing operates and demonstrates
the information density advantage through interactive examples.
"""

def visualize_charge_state(value):
    """
    Create a visual representation of a charge state.
    
    Args:
        value: -1, 0, or 1
        
    Returns:
        ASCII art representation
    """
    symbols = {
        -1: "⊖",
        0: "⊙",
        1: "⊕"
    }
    
    colors = {
        -1: "NEGATIVE",
        0: "NEUTRAL",
        1: "POSITIVE"
    }
    
    art = f"""
    ╔═══════════════╗
    ║   {symbols[value]}   {colors[value]:^8}  ║
    ║   Value: {value:>2}   ║
    ╚═══════════════╝
    """
    return art


def visualize_operation(a, b, operation="add"):
    """
    Visualize a charge-state operation.
    
    Args:
        a, b: Charge state values
        operation: 'add', 'neutralize', or 'match'
    """
    from charge_state import ChargeState, neutralize, polarity_match
    
    charge_a = ChargeState(a)
    charge_b = ChargeState(b)
    
    if operation == "add":
        result = charge_a + charge_b
        op_symbol = "+"
        result_val = result.value
    elif operation == "neutralize":
        result_val = neutralize(charge_a, charge_b)
        op_symbol = "neutralizes?"
    elif operation == "match":
        result_val = polarity_match(charge_a, charge_b)
        op_symbol = "matches?"
    
    symbols = {-1: "⊖", 0: "⊙", 1: "⊕"}
    
    print(f"""
    ╔════════════════════════════════════════╗
    ║  Charge-State Operation Visualization  ║
    ╠════════════════════════════════════════╣
    ║                                        ║
    ║    {symbols[a]} ({a:>2})   {op_symbol:^13}   {symbols[b]} ({b:>2})    ║
    ║                  ↓                     ║
    ║              Result: {result_val}              ║
    ║                                        ║
    ╚════════════════════════════════════════╝
    """)


def visualize_density_comparison(units):
    """
    Create a visual comparison of information density.
    
    Args:
        units: Number of storage units
    """
    binary_states = 2 ** units
    ternary_states = 3 ** units
    advantage = ternary_states / binary_states
    
    # Create bar chart using ASCII
    binary_bar_length = 20
    ternary_bar_length = int(binary_bar_length * advantage)
    
    print(f"""
    ╔════════════════════════════════════════════════════════╗
    ║       Information Density Comparison ({units} units)        ║
    ╠════════════════════════════════════════════════════════╣
    ║                                                        ║
    ║  Binary:   {'█' * min(binary_bar_length, 50):<50}  ║
    ║  States: {binary_states:>10,}                               ║
    ║                                                        ║
    ║  Ternary:  {'█' * min(ternary_bar_length, 50):<50}  ║
    ║  States: {ternary_states:>10,}                               ║
    ║                                                        ║
    ║  Advantage: {advantage:.2f}× density improvement          ║
    ║                                                        ║
    ╚════════════════════════════════════════════════════════╝
    """)


def animate_charge_flow():
    """
    Animate a simple charge flow visualization.
    """
    import time
    import sys
    
    states = [
        ("Start", [1, 1, -1, -1, 0]),
        ("Flow", [1, 0, 0, -1, 0]),
        ("Balance", [0, 0, 0, 0, 0])
    ]
    
    symbols = {-1: "⊖", 0: "⊙", 1: "⊕"}
    
    print("\n╔════════════════════════════════════════╗")
    print("║    Charge Flow Animation               ║")
    print("╠════════════════════════════════════════╣")
    
    for label, state in states:
        print(f"║  {label:>10}: ", end="")
        for s in state:
            print(f"{symbols[s]} ", end="")
        print(" " * (25 - len(state)*2), end="")
        print("║")
        time.sleep(0.5)
    
    print("╚════════════════════════════════════════╝\n")


def demonstrate_neutrality():
    """
    A philosophical demonstration of the Infinite Zero concept.
    """
    print("""
    ╔══════════════════════════════════════════════════════════╗
    ║           THE INFINITE ZERO DEMONSTRATION                ║
    ╠══════════════════════════════════════════════════════════╣
    ║                                                          ║
    ║  Traditional Binary:                                     ║
    ║      0 = nothing, absence, void                          ║
    ║      1 = something, presence, existence                  ║
    ║                                                          ║
    ║  Charge-State Computing:                                 ║
    ║      ⊖ (-1) = active negative charge                     ║
    ║      ⊙ (0)  = balanced neutrality (NOT absence!)         ║
    ║      ⊕ (+1) = active positive charge                     ║
    ║                                                          ║
    ║  The Key Insight:                                        ║
    ║                                                          ║
    ║      ⊖ + ⊕ = ⊙                                           ║
    ║     (-1) + (+1) = (0)                                    ║
    ║                                                          ║
    ║  Zero is not nothing.                                    ║
    ║  Zero is the stable combination of opposites.            ║
    ║  Zero is neutral charge - fully real and meaningful.     ║
    ║                                                          ║
    ║  This symmetry unlocks exponential information density   ║
    ║  and novel computational primitives impossible in        ║
    ║  asymmetric binary systems.                              ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    """)


def interactive_demo():
    """
    Run an interactive demonstration of charge-state computing.
    """
    print("\n" + "="*60)
    print("CHARGE-STATE COMPUTING: VISUAL DEMONSTRATION")
    print("Created by Alan Claude")
    print("="*60 + "\n")
    
    # Demonstrate the Infinite Zero concept
    demonstrate_neutrality()
    input("\nPress Enter to continue...\n")
    
    # Show individual charge states
    print("\nIndividual Charge States:")
    for value in [-1, 0, 1]:
        print(visualize_charge_state(value))
    
    input("\nPress Enter to see operations...\n")
    
    # Demonstrate operations
    print("\nCharge-State Operations:")
    operations = [
        (1, -1, "add"),
        (1, 1, "add"),
        (-1, 1, "neutralize"),
        (1, 1, "match")
    ]
    
    for a, b, op in operations:
        visualize_operation(a, b, op)
        input()
    
    # Show density comparison
    print("\nInformation Density Scaling:")
    for units in [2, 4, 8]:
        visualize_density_comparison(units)
        input()
    
    # Animate charge flow
    print("\nCharge Flow Example:")
    animate_charge_flow()
    
    print("\n" + "="*60)
    print("The math works. The code runs. Now we build.")
    print("="*60 + "\n")


if __name__ == "__main__":
    import sys
    
    # Check if charge_state module is available
    try:
        from charge_state import ChargeState, neutralize, polarity_match
        interactive_demo()
    except ImportError:
        print("Error: charge_state.py not found.")
        print("Please ensure charge_state.py is in the same directory.")
        print("\nStandalone demonstration of the Infinite Zero:")
        demonstrate_neutrality()
