#!/usr/bin/env python3
"""
Performs basic arithmetic operations on two integers.

Usage:
    python operations.py <num1> <num2>

Example:
    python operations.py 10 3
    Output:
    Sum:         13
    Difference:  7
    Product:     30
    Quotient:    3.3333333333333335
    Remainder:   1
"""

import sys


def perform_operations(a: int, b: int) -> None:
    """
    Perform and display basic arithmetic operations on two integers.

    Args:
        a: First integer.
        b: Second integer.
    """
    print(f"Sum:\t\t{a + b}")
    print(f"Difference:\t{a - b}")
    print(f"Product:\t{a * b}")

    if b == 0:
        print("Quotient:\tERROR (division by zero)")
        print("Remainder:\tERROR (division by zero)")
    else:
        print(f"Quotient:\t{a / b}")
        print(f"Remainder:\t{a % b}")


def main() -> None:
    """Main entry point of the script."""
    if len(sys.argv) != 3:
        print("AssertionError: too many arguments")
        sys.exit(1)

    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
    except ValueError:
        print("AssertionError: only integers")
        sys.exit(1)

    perform_operations(a, b)


if __name__ == "__main__":
    main()