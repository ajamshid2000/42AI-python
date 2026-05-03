
"""
Custom filter function implementation.
"""

from typing import Callable, Iterable, Any, Generator


def ft_filter(function_to_apply: Callable[[Any], bool], iterable: Iterable[Any]) -> Generator[Any, None, None]:
    """
    Filter elements of an iterable using a function.

    Args:
        function_to_apply: Function that returns True/False for each element.
        iterable: An iterable object (list, tuple, etc.).

    Yields:
        Elements for which function_to_apply returns True.
    """
    for element in iterable:
        if function_to_apply(element):
            yield element


if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]
    # Example: filter even numbers
    for num in ft_filter(lambda n: n % 2 == 0, x):
        print(num)