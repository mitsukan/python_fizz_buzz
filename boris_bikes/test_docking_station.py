import unittest
import docking_station

class TestDockingStation(unittest.TestCase):

    def test_docking_station(self):
        self.assertEqual(docking_station.storage(), "Hello World")




if __name__ == '__main__':
    unittest.main()
