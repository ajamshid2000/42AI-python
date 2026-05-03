#!/usr/bin/env python3
"""
Format a tuple representing date and time into MM/DD/YYYY HH:MM format.

Example output: 09/25/2019 03:30
"""

kata = (2019, 9, 25, 3, 30)

if __name__ == "__main__":
    year, month, day, hour, minute = kata
    print(f"{month:02}/{day:02}/{year:04} {hour:02}:{minute:02}")