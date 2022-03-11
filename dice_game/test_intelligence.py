import unittest
import sys

sys.path.append("dice_game")
from intelligence import Intelligence
from unittest.mock import patch


class TestIntelligence(unittest.TestCase):
    def test_init_default_object(self):
        # Instantiate an object.
        object = Intelligence()
        message = "given object is not instance of intelligence class."
        self.assertIsInstance(object, Intelligence, message)

    @unittest.mock.patch("intelligence.random")
    def test_level_1(self, mock_random):
        # check the level1 function return a number betwen 0 to 2
        Intelligence.level_1(self)
        mock_random.randrange.assert_called_with(0, 2)


if __name__ == "__main__":
    unittest.main()
