#!/usr/bin/env python3
"""
Print the elements of a tuple in a formatted string.

Example output: the 3 numbers are: 19, 42, 21
"""

kata = (19, 42, 21)

if __name__ == "__main__":
    print("the 3 numbers are:", ", ".join(str(x) for x in kata))