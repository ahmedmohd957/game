
import random

class Intelligence:
    
    def level_1(self):
        """rolls the dice"""
        hold = ["y", "n", "n"]
        return hold[random.randrange(0, 2)]

    def level_2(self):
        """rolls the dice"""
        return "y"
