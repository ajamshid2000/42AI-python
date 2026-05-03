#!/usr/bin/env python3
"""
Executes a command-line script that processes arguments by reversing each string,
swapping case, and then reversing the order of the arguments.

Usage:
    python exec.py arg1 arg2 arg3 ...

Example:
    python exec.py Hello World
    Output: dLROw oLLEh
"""

import sys
from typing import List


def process_arguments(args: List[str]) -> List[str]:
    """
    Process a list of strings by reversing each string, swapping case,
    and reversing the order of the list.

    Args:
        args: List of strings to process.

    Returns:
        Processed list of strings.
    """
    return ["".join(reversed(x.swapcase())) for x in args][::-1]


def main() -> None:
    """Main entry point of the script."""
    if len(sys.argv) < 2:
        print("Usage: python exec.py arg1 arg2 ...")
        sys.exit(1)

    processed = process_arguments(sys.argv[1:])
    print(*processed, sep=" ")


if __name__ == "__main__":
    main()

