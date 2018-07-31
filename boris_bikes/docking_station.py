from bike import Bike

class DockingStation(object):

    def __init__(self):
        self.storage = []

    def dock(self, bike):
        self.storage.append(bike)
        return "Bike docked."

    def release(self, bike):
        self.storage.remove(bike)
        return "Bike released."