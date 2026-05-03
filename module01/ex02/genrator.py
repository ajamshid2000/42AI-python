
"""
Text generator with options to shuffle, unique, or order words.
"""

from random import randint
from typing import Generator, Optional, List


def generator(text: str, sep: str = " ", option: Optional[str] = None) -> Generator[str, None, None]:
    """
    Splits the text according to sep and yields the substrings.
    Option specifies if an action is performed on the substrings before yielding.

    Args:
        text: The text to split.
        sep: The separator to split on.
        option: "shuffle", "unique", or "ordered".

    Yields:
        Substrings from the text.

    Raises:
        ValueError: If text is invalid or option is unknown.
    """
    if not isinstance(text, str) or not text.isprintable():
        raise ValueError("ERROR")

    words: List[str] = text.split(sep)

    if option == "shuffle":
        for i in range(len(words)):
            j = randint(0, len(words) - 1)
            words[i], words[j] = words[j], words[i]
    elif option == "unique":
        words = list(set(words))
    elif option == "ordered":
        words.sort()
    elif option is not None:
        raise ValueError("ERROR")

    for word in words:
        yield word


if __name__ == "__main__":
    text = "Le Lorem Ipsum est simplement du faux texte."
    print("Normal:")
    for word in generator(text, sep=" "):
        print(word)
    print("----------------------------")
    print("Shuffle:")
    for word in generator(text, sep=" ", option="shuffle"):
        print(word)
    print("----------------------------")
    print("Ordered:")
    for word in generator(text, sep=" ", option="ordered"):
        print(word)
    print("----------------------------")
    print("Unique:")
    try:
        for word in generator(text, sep=" ", option="unique"):
            print(word)
    except ValueError as e:
        print(e)
