
"""
Recipe class for representing cooking recipes.
"""

from typing import List


class Recipe:
    """
    A class to represent a cooking recipe.

    Attributes:
        name (str): The name of the recipe.
        cooking_lvl (int): The cooking level (difficulty).
        cooking_time (int): The cooking time in minutes.
        ingredients (List[str]): List of ingredients.
        description (str): Description of the recipe.
        recipe_type (str): Type of the recipe (e.g., starter, lunch, dessert).
    """

    def __init__(self, name: str, cooking_lvl: int, cooking_time: int,
                 ingredients: List[str], description: str, recipe_type: str) -> None:
        """
        Initialize a Recipe instance.

        Args:
            name: The name of the recipe.
            cooking_lvl: The cooking level (difficulty).
            cooking_time: The cooking time in minutes.
            ingredients: List of ingredients.
            description: Description of the recipe.
            recipe_type: Type of the recipe.

        Raises:
            ValueError: If any argument is invalid.
        """
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string")
        self.name = name

        if not isinstance(cooking_lvl, int) or not (1 <= cooking_lvl <= 5):
            raise ValueError("Cooking level must be an integer between 1 and 5")
        self.cooking_lvl = cooking_lvl

        if not isinstance(cooking_time, int) or cooking_time < 0:
            raise ValueError("Cooking time must be a non-negative integer")
        self.cooking_time = cooking_time

        if not isinstance(ingredients, list) or not ingredients:
            raise ValueError("Ingredients must be a non-empty list")
        self.ingredients = ingredients

        if not isinstance(description, str):
            raise ValueError("Description must be a string")
        self.description = description

        if not isinstance(recipe_type, str) or not recipe_type:
            raise ValueError("Recipe type must be a non-empty string")
        self.recipe_type = recipe_type

    def __str__(self) -> str:
        """
        Return a string representation of the recipe.

        Returns:
            Formatted string with recipe details.
        """
        return (f"{'Recipe name:':<20}{self.name}\n"
                f"{'Cooking level:':<20}{self.cooking_lvl}\n"
                f"{'Cooking time:':<20}{self.cooking_time} minutes\n"
                f"{'Ingredients:':<20}{', '.join(self.ingredients)}\n"
                f"{'Description:':<20}{self.description}\n"
                f"{'Recipe type:':<20}{self.recipe_type}")


if __name__ == "__main__":
    # Example usage
    try:
        recipe = Recipe("Pasta", 2, 30, ["pasta", "tomato", "cheese"], "Simple pasta dish", "lunch")
        print(recipe)
    except ValueError as e:
        print(f"Error: {e}")