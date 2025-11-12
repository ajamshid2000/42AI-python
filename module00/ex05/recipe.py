cookbook = {
    "Sandwhich" : {
        "ingredients" : ['ham', 'bread', 'cheese', 'tomatoes'],
        "meal" : "lunch",
        "prep_time": "10"
        },
    "Cake" : {
        "ingredients" : ['flour', 'sugar', 'eggs'],
        "meal" : "dessert",
        "prep_time" : "60"
        },
    "Salad" : {
        "ingredients" : ['avocado', 'arugula', 'tomatoes', 'spinach'],
        "meal" : "lunch",
        "prep_time" : "15"
        }
}

def add_recipe():
    try:
        name = input("Enter name\n")
        ingredients = input("Enter ingredients:\n")
        meal_type = input("Enter a meal type:\n")
        prep_time = input("Enter a preparation time:\n")
    except Exception as e:
        print(e.__class__.__name__, "there was an error reading")
        exit()
    newrecipe = {"ingredients": ingredients.split(), "meal": meal_type, "prep_time": prep_time}
    cookbook.update({name : newrecipe})

def delete_recipe():
    try:
        recipe_name = input("Please enter a recipe name to get deleted:\n")
    except Exception as e:
        print(e.__class__.__name__, "there was an error reading")
        exit()
    cookbook.pop(recipe_name)

def print_recipe(*args):
    if(not args[0]):
        try:
            recipe_name = input("Please enter a recipe name to get its details:\n")
        except Exception as e:
            print(e.__class__.__name__, "there was an error reading")
            exit()
    else: recipe_name = args[0]    
    x = cookbook.get(recipe_name)["ingredients"]
    print("Ingredients list:", end = " ")
    print("Recipe for ",x)
    x = cookbook.get(recipe_name)["meal"]
    print("to be eaten for "+ x +".")
    x = cookbook.get(recipe_name)["prep_time"]
    print("Takes "+ x +" minutes of cooking\n")

def print_cookbook():
    for x in cookbook:
        print(x + " ")
        print_recipe(x)

def quit_programe():
    print("Cookbook closed. Goodbye")
    exit()
    
print("Welcome to the Python Cookbook !\n")
while(1):
    print("List of available option:\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n")
    try:
        in_num = input("Please select an option!\n")
    except BaseException as e:
        print(e.__class__.__name__, "there was an error reading")
        exit()
    match in_num:
        case '1': 
            add_recipe()
        case '2': 
            delete_recipe()
        case '3': 
            print_recipe()
        case '4': 
            print_cookbook()
        case '5': 
            quit_programe()
        case _: 
            print("Sorry, this option does not exist.")

