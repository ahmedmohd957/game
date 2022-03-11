"""This class represents the dice."""
import random


class Dice:
    def roll_dice(self):
        """Rolls the dice"""
        return random.randrange(1, 6)
