class Roshambo(object):

    def __init__(self, choice):
        # self.input = input
        self.outcomes = ["rock", "paper", "scissors"]
        self.choice = choice
        # apart from [0] > [2], the larger the number will win.
