import unittest
import RPS

class TestRPS(unittest.TestCase):

    def test_rock_beats_scissors(self):
        self.assertEqual(RPS.roshambo("rock", "scissors"), "Player 1 wins!")
        self.assertEqual(RPS.roshambo("scissors", "rock"), "Player 2 wins!")

    def test_scissors_beats_paper(self):
        self.assertEqual(RPS.roshambo("scissors", "paper"), "Player 1 wins!")
        self.assertEqual(RPS.roshambo("paper", "scissors"), "Player 2 wins!")

    def test_paper_beats_rock(self):
        self.assertEqual(RPS.roshambo("paper", "rock"), "Player 1 wins!")

if __name__ == '__main__':
    unittest.main()