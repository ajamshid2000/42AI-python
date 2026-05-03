"""
Logger decorator and CoffeeMachine class for logging execution times.
"""

import time
import os
from random import randint
from functools import wraps
from typing import Any, Callable


def log(func: Callable) -> Callable:
    """
    Decorator to log function execution time.

    Args:
        func: The function to decorate.

    Returns:
        Wrapped function that logs execution time.
    """
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """Log the function execution."""
        log_file = "machine.log"
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed = end_time - start_time

        # Format function name for display
        display_name = func.__name__.replace('_', ' ').title()

        # Determine time format
        if elapsed < 1:
            time_str = f"{elapsed * 1000:.3f} ms"
        else:
            time_str = f"{elapsed:.3f} s"

        log_entry = f"(user)Running: {display_name:20}[ exec-time = {time_str} ]\n"

        with open(log_file, "a") as f:
            f.write(log_entry)

        return result

    return wrapper


class CoffeeMachine:
    """A simple coffee machine with logging."""

    def __init__(self) -> None:
        """Initialize the coffee machine."""
        self.water_level = 100

    @log
    def start_machine(self) -> bool:
        """
        Start the coffee machine.

        Returns:
            True if started, False if water level too low.
        """
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self) -> str:
        """
        Boil water.

        Returns:
            Status message.
        """
        return "boiling..."

    @log
    def make_coffee(self) -> None:
        """Make a cup of coffee."""
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_amount: int) -> None:
        """
        Add water to the machine.

        Args:
            water_amount: Amount of water to add.
        """
        time.sleep(randint(1, 5))
        self.water_level += water_amount
        print("Blub blub blub...")
        
if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)