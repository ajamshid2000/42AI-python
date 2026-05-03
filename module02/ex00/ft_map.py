
"""
Custom map function implementation.
"""

from typing import Callable, Iterable, Any, Generator


def ft_map(function_to_apply: Callable[[Any], Any], iterable: Iterable[Any]) -> Generator[Any, None, None]:
    """
    Apply a function to all elements of an iterable.

    Args:
        function_to_apply: Function to apply to each element.
        iterable: An iterable object (list, tuple, etc.).

    Yields:
        Transformed elements.
    """
    for element in iterable:
        yield function_to_apply(element)


if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]
    # Example: increment each number
    print(list(ft_map(lambda t: t + 1, x)))
    # Output: [2, 3, 4, 5, 6]