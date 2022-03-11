import unittest
import sys

sys.path.append("dice_game")
from player import Player


class TestPlayer(unittest.TestCase):
    def test_init_default_object(self):
        # Instantiate an object.
        object = Player()
        message = "given object is not instance of player class."
        self.assertIsInstance(object, Player, message)

    def setUp(self):
        # self.p1 = Player.setName(True)
        self.name = Player.name = "cuz"
        self.updated_name = Player.updateName = self.name

    def test_player_name(self):
        """Test if the name exist"""
        self.assertEqual(self.name, "cuz")

    def test_player_name_update(self):
        """Test if the name updated"""
        self.assertEqual(self.updated_name, self.name)


if __name__ == "__main__":
    unittest.main()
