
class recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        if(isinstance(name, str) and len(name) > 0):
            self.name = name
        else: print("name given as argument is not either str or is empty"); exit()
        if(isinstance(cooking_lvl, int)):
            self.cooking_lvl = cooking_lvl
        else: print("cooking_lvl given as argument is not int"); exit()
        if(isinstance(cooking_time, int)):
            self.cooking_time = cooking_time
        else: print("cooking_time given as argument is not int"); exit()
        if(isinstance(ingredients, list) and len(ingredients) > 0):
            self.ingredients = ingredients
        else: print("ingredients given as argument is not either list or is empty"); exit()
        if(isinstance(description, str)):
            self.description = description
        else: print("description given as argument is not str"); exit()
        if(isinstance(recipe_type, str) and len(recipe_type) > 0):
            self.recipe_type = recipe_type
        else: print("recipe_type given as argument is not either str or is empty"); exit()
        
    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = str(f"{'name:':20}{self.name}\n{'cooking level:':20}{self.cooking_lvl}\n{'cooking time:':20}{self.cooking_time}\n{'ingredients list:':20}{self.ingredients}\n{'description:':20}{self.description}\n{'type:':20}{self.recipe_type}")
        return txt
            
            
a = recipe("a",1,1,["a"],"","a")

print(a)