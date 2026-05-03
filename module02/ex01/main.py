"""
Variable arguments to object converter module.
"""

from typing import Any, Dict, Optional


class ObjectC:
    """
    A class that dynamically sets attributes from a dictionary.
    """

    def __init__(self, arguments: Dict[str, Any]) -> None:
        """
        Initialize ObjectC with arbitrary attributes.

        Args:
            arguments: Dictionary of attribute names and values.
        """
        for name, value in arguments.items():
            setattr(self, name, value)


def what_are_the_vars(*args: Any, **kwargs: Any) -> Optional[ObjectC]:
    """
    Convert positional and keyword arguments into an object with those attributes.

    Args:
        *args: Positional arguments converted to var_0, var_1, etc.
        **kwargs: Keyword arguments as named attributes.

    Returns:
        ObjectC with the arguments as attributes, or None if conflicts exist.
    """
    arguments: Dict[str, Any] = {}

    # Add positional arguments
    for i, arg in enumerate(args):
        arguments[f'var_{i}'] = arg

    # Add keyword arguments
    for key, value in kwargs.items():
        # Conflict: keyword arg has same name as positional var
        if key in arguments:
            return None
        arguments[key] = value

    return ObjectC(arguments)


def doom_printer(obj: Optional[ObjectC]) -> None:
    """
    Print all non-private attributes of an object.

    Args:
        obj: Object to print, or None.
    """
    if obj is None:
        print("ERROR")
        print("end")
        return

    for attr in dir(obj):
        if not attr.startswith('_'):
            value = getattr(obj, attr)
            print(f"{attr}: {value}")
    print("end")


if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars(None, [])
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
    doom_printer(obj)