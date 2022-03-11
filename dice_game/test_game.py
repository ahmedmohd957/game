import unittest
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
        self.p1 = Player.name = "Ahmed"
        self.p2 = Player.name = "Cuz"

    def test_start(self):
        # Test the number of player must bee 1 or 2
        self.assertTrue(self.number_of_players == 2 or self.number_of_players == 1)

    def test_roll(self):
        # check the roll function
        res = Dice.roll_dice(self)
        exp = 0 < res >= 6
        self.assertTrue(exp)


if __name__ == "__main__":
    unittest.main()
