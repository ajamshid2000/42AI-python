#!/usr/bin/env python3
"""
Determines if a given integer is even, odd, or zero.

Usage:
    python whois.py <number>

Example:
    python whois.py 42
    Output: I'm Even.
"""

import sys


def check_number(num_str: str) -> None:
    """
    Check if the provided string represents an integer and classify it.

    Args:
        num_str: String representation of the number.

    Raises:
        SystemExit: If invalid input or wrong number of arguments.
    """
    if not num_str.isdigit():
        print("AssertionError: argument is not an integer")
        sys.exit(1)

    x = int(num_str)
    if x == 0:
        print("I'm Zero")
    elif x % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


def main() -> None:
    """Main entry point of the script."""
    if len(sys.argv) != 2:
        print("AssertionError: more than one argument is provided")
        sys.exit(1)

    check_number(sys.argv[1])


if __name__ == "__main__":
    main()