import unittest
from docking_station import DockingStation

class TestDockingStation(unittest.TestCase):

    def test_docking_station(self):
        d_station = DockingStation()
        self.assertEqual(d_station.helloworld(), "Hello World")

    def test_storage(self):
        d_station = DockingStation()
        self.assertEqual(d_station.storage, [])

if __name__ == '__main__':
    unittest.main()
