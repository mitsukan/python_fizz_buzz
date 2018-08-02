from menu import Menu

class Till(object):

    def __init__(self):
        self.order = []
        self.menu = Menu()

    def add(self, item):
        self.order.append(item)

    def total(self):
        running_total = 0
        for item in self.order:
            running_total += self.menu.items[item]
        return running_total