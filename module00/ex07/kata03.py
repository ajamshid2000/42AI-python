#!/usr/bin/env python3
"""
Print a string padded with dashes to make it 42 characters long.

Example output: --------------------------The right format
"""

kata = "The right format"

if __name__ == "__main__":
    padding = "-" * (42 - len(kata))
    print(f"{padding}{kata}", end="")