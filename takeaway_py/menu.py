
class Menu(object):

    def __init__(self):
        self.items = {}

    def add(self, item, price):
        self.items[item] = price