"""This class represents the intelligence of the game."""
import random


class Intelligence:
    def level_1(self):
        """Computer randomly chooses whether to hold or continue."""
        hold = ["y", "n", "n"]
        return hold[random.randrange(0, 2)]

    def level_2(self):
        """Computer holds every round."""
        return "y"
