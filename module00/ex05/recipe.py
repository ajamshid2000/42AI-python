#!/usr/bin/env python3
"""
A simple cookbook management system.

This script allows users to add, delete, print, and list recipes in a cookbook.
"""

from typing import Dict, List, Any
import sys

cookbook: Dict[str, Dict[str, Any]] = {
    "Sandwich": {
        "ingredients": ['ham', 'bread', 'cheese', 'tomatoes'],
        "meal": "lunch",
        "prep_time": "10"
    },
    "Cake": {
        "ingredients": ['flour', 'sugar', 'eggs'],
        "meal": "dessert",
        "prep_time": "60"
    },
    "Salad": {
        "ingredients": ['avocado', 'arugula', 'tomatoes', 'spinach'],
        "meal": "lunch",
        "prep_time": "15"
    }
}


def add_recipe() -> None:
    """
    Add a new recipe to the cookbook.

    Prompts the user for recipe details and adds it to the cookbook.
    """
    try:
        name = input("Enter name\n").strip()
        ingredients_input = input("Enter ingredients (separated by spaces):\n").strip()
        meal_type = input("Enter a meal type:\n").strip()
        prep_time = input("Enter a preparation time (minutes):\n").strip()

        if not name or not ingredients_input or not meal_type or not prep_time:
            print("Error: All fields are required.")
            return

        ingredients = ingredients_input.split()
        new_recipe = {
            "ingredients": ingredients,
            "meal": meal_type,
            "prep_time": prep_time
        }
        cookbook[name] = new_recipe
        print(f"Recipe '{name}' added successfully.")

    except KeyboardInterrupt:
        print("\nOperation cancelled.")
    except Exception as e:
        print(f"Error: {e}")


def delete_recipe() -> None:
    """
    Delete a recipe from the cookbook.

    Prompts the user for the recipe name and removes it if it exists.
    """
    try:
        recipe_name = input("Please enter a recipe name to delete:\n").strip()
        if recipe_name in cookbook:
            del cookbook[recipe_name]
            print(f"Recipe '{recipe_name}' deleted successfully.")
        else:
            print(f"Error: Recipe '{recipe_name}' not found.")
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
    except Exception as e:
        print(f"Error: {e}")


def print_recipe(recipe_name: str = None) -> None:
    """
    Print the details of a specific recipe.

    Args:
        recipe_name: Name of the recipe to print. If None, prompts for input.
    """
    if recipe_name is None:
        try:
            recipe_name = input("Please enter a recipe name to get its details:\n").strip()
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            return
        except Exception as e:
            print(f"Error: {e}")
            return

    if recipe_name not in cookbook:
        print(f"Error: Recipe '{recipe_name}' not found.")
        return

    recipe = cookbook[recipe_name]
    print(f"Recipe for {recipe_name}:")
    print(f"Ingredients: {', '.join(recipe['ingredients'])}")
    print(f"To be eaten for {recipe['meal']}.")
    print(f"Takes {recipe['prep_time']} minutes of cooking.\n")


def print_cookbook() -> None:
    """Print all recipes in the cookbook."""
    if not cookbook:
        print("The cookbook is empty.")
        return

    for name in cookbook:
        print_recipe(name)


def quit_program() -> None:
    """Quit the program."""
    print("Cookbook closed. Goodbye")
    sys.exit(0)


def main() -> None:
    """Main entry point of the script."""
    print("Welcome to the Python Cookbook!\n")

    while True:
        print("List of available options:")
        print("1: Add a recipe")
        print("2: Delete a recipe")
        print("3: Print a recipe")
        print("4: Print the cookbook")
        print("5: Quit")

        try:
            choice = input("Please select an option!\n").strip()
        except KeyboardInterrupt:
            print("\nGoodbye")
            break
        except Exception as e:
            print(f"Error reading input: {e}")
            continue

        if choice == '1':
            add_recipe()
        elif choice == '2':
            delete_recipe()
        elif choice == '3':
            print_recipe()
        elif choice == '4':
            print_cookbook()
        elif choice == '5':
            quit_program()
        else:
            print("Sorry, this option does not exist.")


if __name__ == "__main__":
    main()

