#!/usr/bin/env python3
"""
Format a tuple of numbers into a specific string format.

Example output: module_00, ex_04 : 132.42, 1.00e+04, 1.23e+04
"""

kata = (0, 4, 132.42222, 10000, 12345.67)

if __name__ == "__main__":
    module_num, ex_num, float_num, sci1, sci2 = kata
    print(f"module_{module_num:02}, ex_{ex_num:02} : {float_num:.2f}, {sci1:.2e}, {sci2:.2e}")