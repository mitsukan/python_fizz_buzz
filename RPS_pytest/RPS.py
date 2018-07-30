def roshambo(p1,p2):
    if (p1 == "rock" and p2 == "scissors") or (p1 == "scissors" and p2 == "paper"):
        return "Player 1 wins!"
    elif (p2 == "rock" and p1 == "scissors")or (p2 == "scissors" and p1 == "paper"):
        return "Player 2 wins!"