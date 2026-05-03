#!/usr/bin/env python3
"""
Filter words from a string that are longer than a specified length.

Usage:
    python filterwords.py "<sentence>" <length>

Example:
    python filterwords.py "Hello world from Python" 4
    Output: ['Hello', 'world', 'Python']
"""

import sys
from typing import List


def filter_words(sentence: str, min_length: int) -> List[str]:
    """
    Filter words from a sentence that are longer than the specified minimum length.
    Only alphabetic characters are considered in words.

    Args:
        sentence: The input sentence.
        min_length: Minimum word length.

    Returns:
        List of filtered words.
    """
    words = sentence.split()
    filtered = []
    for word in words:
        # Keep only alphabetic characters
        clean_word = ''.join(c for c in word if c.isalpha())
        if len(clean_word) > min_length:
            filtered.append(clean_word)
    return filtered


def main() -> None:
    """Main entry point of the script."""
    if len(sys.argv) != 3:
        print("ERROR")
        sys.exit(1)

    sentence = sys.argv[1]
    try:
        min_length = int(sys.argv[2])
    except ValueError:
        print("ERROR")
        sys.exit(1)

    if min_length < 0:
        print("ERROR")
        sys.exit(1)

    result = filter_words(sentence, min_length)
    print(result)


if __name__ == "__main__":
    main()
