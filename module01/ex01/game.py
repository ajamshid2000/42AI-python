"""
Game of Thrones character classes.
"""

from typing import Optional


class GotCharacter:
    """
    Base class for Game of Thrones characters.

    Attributes:
        first_name (str): The character's first name.
        is_alive (bool): Whether the character is alive.
    """

    def __init__(self, first_name: Optional[str] = None, is_alive: bool = True) -> None:
        """
        Initialize a GotCharacter.

        Args:
            first_name: The character's first name.
            is_alive: Whether the character is alive.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def __str__(self) -> str:
        """Return a string representation of the character."""
        status = "alive" if self.is_alive else "dead"
        return f"{self.first_name} is {status}"

    def die(self) -> None:
        """Kill the character."""
        self.is_alive = False


class Stark(GotCharacter):
    """
    A class representing the Stark family.

    Attributes:
        family_name (str): The family name.
        house_words (str): The house words.
    """

    def __init__(self, first_name: Optional[str] = None, is_alive: bool = True) -> None:
        """
        Initialize a Stark character.

        Args:
            first_name: The character's first name.
            is_alive: Whether the character is alive.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self) -> None:
        """Print the house words."""
        print(self.house_words)

    def __str__(self) -> str:
        """Return a string representation of the Stark character."""
        return f"{super().__str__()} and is from House {self.family_name}"
        