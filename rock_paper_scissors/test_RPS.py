import unittest
from RPS import Roshambo
from unittest.mock import Mock
from unittest.mock import patch

class TestRoshambo(unittest.TestCase):

    # def test_input(self):
    #     """User should be able to input their choice"""
    #     new_game = Roshambo("rock")
    #     self.assertEqual(new_game.input, "rock")

    def test_choices(self):
        """Game has an array to store the possible choices"""
        new_game = Roshambo("rock")
        self.assertEqual(new_game.outcomes, ["rock", "paper", "scissors"])

    def test_randomise(self):
        """Game has a computer that randomises between the choices"""
        new_game = Roshambo("rock")
        @patch(RPS.random)
        self.assertEqual(new_game.randomise(), "rock")

    # def test_play(self):
    #     """Be able to play the game, comparing the existing choices saved in the class object"""
    #     new_game = Roshambo("rock")
    #     self.assertEqual(new_game.play("rock"), )
