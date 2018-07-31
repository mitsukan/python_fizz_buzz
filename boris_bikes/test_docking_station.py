import unittest
from docking_station import DockingStation
from unittest import mock

class TestDockingStation(unittest.TestCase):

    def test_storage(self):
        d_station = DockingStation()
        self.assertEqual(d_station.storage, [])

    def test_be_able_to_take_a_bike(self):
        d_station = DockingStation()
        with mock.patch('bike.Bike') as mocked_bike:
            self.assertEqual(d_station.dock(mocked_bike), "Bike docked.")

if __name__ == '__main__':
    unittest.main()
