import unittest
from unittest.mock import patch
import sys

sys.path.append("dice_game")
import dice


class TestDice(unittest.TestCase):
    def test_init_default_object(self):
        # Instantiate an object.
        object = dice.Dice()
        message = "given object is not instance of dice class."
        self.assertIsInstance(object, dice.Dice, message)

    @unittest.mock.patch("dice.random")
    def test_roll_dice(self, mock_random):
        # check the dice_roll function return a number betwen 1 to 6
        dice.Dice.roll_dice(self)
        mock_random.randrange.assert_called_with(1, 6)


if __name__ == "__main__":
    unittest.main()
