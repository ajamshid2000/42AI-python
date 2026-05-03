#!/usr/bin/env python3
"""
Print the creators of programming languages from a dictionary.

Example output:
Python was created by Guido van Rossum
Ruby was created by Yukihiro Matsumoto
PHP was created by Rasmus Lerdorf
"""

kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

if __name__ == "__main__":
    for language, creator in kata.items():
        print(f"{language} was created by {creator}")