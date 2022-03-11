import unittest
from highscore import HighScore


class testHighScore(unittest.TestCase):

    def test_init_default_object(self):
        # Instantiate an object.
        object = HighScore()
        message = "given object is not instance of HighScore class."
        self.assertIsInstance(object, HighScore, message)

    def setUp(self):
        # test to print the score table
        self.test = HighScore.get_highScore(
            ["self", "self"], ["Cuz", "Ahmed"], [9, 8], [20, 19])


if __name__ == "__main__":
    unittest.main()
