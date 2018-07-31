from bike import Bike

class DockingStation(object):

    def __init__(self):
        self.storage = []

    def dock(self, bike):
        self.storage.append(bike)
        return "Bike docked."

    def release(self, bike):
        if self.storage == []:
            raise Exception("No bike to release.")
        elif bike.is_working == False:
            raise Exception('Bike is broken.')
        else:
            self.storage.remove(bike)
        return "Bike released."