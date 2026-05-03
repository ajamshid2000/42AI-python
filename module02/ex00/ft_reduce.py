
"""
Custom reduce function implementation.
"""

from typing import Callable, Iterable, Any, TypeVar

T = TypeVar('T')


def ft_reduce(function_to_apply: Callable[[T, T], T], iterable: Iterable[T]) -> T:
    """
    Apply a function of two arguments cumulatively to items in an iterable.

    Args:
        function_to_apply: Function taking two arguments.
        iterable: An iterable object (list, tuple, etc.).

    Returns:
        The final reduced value.

    Raises:
        TypeError: If iterable is empty.
    """
    iterator = iter(iterable)
    try:
        accumulator = next(iterator)
    except StopIteration:
        raise TypeError("ft_reduce() of empty sequence with no initial value")

    for element in iterator:
        accumulator = function_to_apply(accumulator, element)
    return accumulator


if __name__ == "__main__":
    lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
    # Example: join characters
    result = ft_reduce(lambda acc, x: acc + x, lst)
    print(result)  # Output: Hello world
