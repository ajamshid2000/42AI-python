import time
from random import randint
import os
#... your definition of log decorator...
def log(func):
    
    def loger(*args):
        f = open("machine.log", "a")
        start_time = time.time()
        res = func(*args)
        end_time = time.time()
        match func.__name__:
            case "start_machine":
                f.write(f'(cmaxime)Running: {"Start Machine":20}[ exec-time = {(end_time - start_time)*1000:.3f} ms ]\n')
            case "boil_water":
                f.write(f'(cmaxime)Running: {"Boil Water":20}[ exec-time = {(end_time - start_time)*1000:.3f} ms ]\n')
            case "make_coffee":
                f.write(f'(cmaxime)Running: {"Make Coffee":20}[ exec-time = {end_time - start_time:.3f} s ]\n')
            case "add_water":
                f.write(f'(cmaxime)Running: {"Add_Water":20}[ exec-time = {end_time - start_time:.3f} s ]\n')
        f.close()
        return res
        
    return loger
    
class CoffeeMachine():
    water_level = 100
    @log
    def start_machine(self):
        if self.water_level > 20:
            return True 
        else:
            print("Please add water!")
            return False
    @log
    def boil_water(self):
        return "boiling..."
    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20): 
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")
        
if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)