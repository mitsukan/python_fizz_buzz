from RPS import roshambo

def test_rock_beats_scissors():
    assert roshambo("rock","scissors") == "Player 1 wins!"
    assert roshambo("scissors", "rock") == "Player 2 wins!"