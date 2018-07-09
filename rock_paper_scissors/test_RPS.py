import unittest
from RPS import Roshambo

class TestRoshambo(unittest.TestCase):

    def test_input(self):
        """User should be able to input their choice"""
        new_game = Roshambo("rock")
        self.assertEqual(new_game.input, "rock")

    def test_choices(self):
        """Game has an array to store the possible choices"""
        new_game = Roshambo("rock")
        self.assertEqual(new_game.choices, ["rock", "paper", "scissors"])
