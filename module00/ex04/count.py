#!/usr/bin/env python3
"""
Text analyzer that counts upper-case, lower-case, punctuation, and space characters.

Usage:
    python count.py [text]

If no text is provided, it will prompt for input.
"""

import sys
import string


def text_analyzer(text: str = None) -> None:
    """
    Analyze the given text and display counts of different character types.

    Args:
        text: The text to analyze. If None or empty, prompts for input.

    Raises:
        SystemExit: If the input is not a string.
    """
    if text is None or text == "":
        text = input("What is the text to analyze?\n")

    if not isinstance(text, str):
        print("AssertionError: argument is not a string")
        sys.exit(1)

    spaces_count = 0
    upper_count = 0
    lower_count = 0
    punc_count = 0

    for char in text:
        if char == ' ':
            spaces_count += 1
        elif char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char in string.punctuation:
            punc_count += 1

    print(f"- {upper_count} upper letter(s)")
    print(f"- {lower_count} lower letter(s)")
    print(f"- {punc_count} punctuation mark(s)")
    print(f"- {spaces_count} space(s)")


def main() -> None:
    """Main entry point of the script."""
    if len(sys.argv) > 2:
        print("One argument needed!")
        sys.exit(1)
    elif len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    else:
        text_analyzer()


if __name__ == "__main__":
    main()
    
    
# text_analyzer("Python 2.0, released 2000, introduced features like List comprehensions and a garbage collection system capable of collecting reference cycles.")

# Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace.