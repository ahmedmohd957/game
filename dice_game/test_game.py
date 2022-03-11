import unittest
import sys

sys.path.append("dice_game")
from game import Game
from player import Player
from dice import Dice


class TestGame(unittest.TestCase):
    def test_init_default_object(self):
        # Instantiate an object.
        object = Game()
        message = "given object is not instance of game class."
        self.assertIsInstance(object, Game, message)

    def setUp(self):
        self.number_of_players = 2
        self.player1_score = 20
        self.player2_score = 20
        self.player_turn = 0
        self.level_of_intelligence = 1
        self.is_cheating = False
        self.p_1 = Player.name = "Ahmed"
        self.p_2 = Player.name = "Cuz"

    def test_start(self):
        # Test the number of player must bee 1 or 2
        self.assertTrue(self.number_of_players == 2 or self.number_of_players == 1)
        if self.number_of_players == 1:
            self.p_2 = "Computer"
            self.assertTrue(self.p_2 == "Computer")
        else:
            self.assertTrue(self.p_1 == "Ahmed" and self.p_2 == "Cuz")

    def test_roll(self):
        # check the roll function
        res = Dice.roll_dice(self)
        exp = 0 < res <= 6
        self.assertTrue(exp)

    def test_computer(self):
        # test the computer function
        if self.number_of_players == 1:
            self.assertTrue(
                self.level_of_intelligence == 1 or self.level_of_intelligence == 2
            )

    def test_score_below_100(self):
        # test if the score is below 100
        if self.player1_score < 100 and self.player2_score < 100:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_cheat(self):
        # testing the cheat function
        self.number_of_players = 1
        self.is_cheating = True
        self.assertTrue(self.is_cheating)


if __name__ == "__main__":
    unittest.main()
