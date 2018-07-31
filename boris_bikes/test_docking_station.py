import unittest
from docking_station import DockingStation
from bike import Bike
from unittest import mock

class TestDockingStation(unittest.TestCase):

    def test_storage(self):
        d_station = DockingStation()
        self.assertEqual(d_station.storage, [])

    def test_be_able_to_take_a_bike(self):
        d_station = DockingStation()
        with mock.patch('bike.Bike') as mocked_bike:
            # print(mocked_bike)
            self.assertEqual(d_station.dock(mocked_bike), "Bike docked.")
            self.assertEqual(d_station.storage, [mocked_bike])

    def test_dock_then_release_a_bike(self):
        d_station = DockingStation()
        with mock.patch('bike.Bike') as mocked_bike:
            d_station.dock(mocked_bike)
            self.assertEqual(d_station.release(mocked_bike), "Bike released.")
            self.assertEqual(d_station.storage, [])

    def test_doesnt_release_if_bike_is_broken(self):
        d_station = DockingStation()
        with mock.patch('bike.Bike') as mocked_bike:
            mocked_bike = False
            d_station.dock(mocked_bike)
            with self.assertRaises(Exception) as context:
                d_station.release(mocked_bike)
            self.assertFalse("Bike is broken." in str(context.exception))
            self.assertEqual(d_station.storage, [mocked_bike])

    def test_raises_error_if_no_bike_is_in_docking_station(self):
        d_station = DockingStation()
        with mock.patch('bike.Bike') as mocked_bike:
            with self.assertRaises(Exception) as context:
                d_station.release(mocked_bike)
            self.assertTrue("No bike to release." in str(context.exception))

    def test_feature_docking_with_real_bike(self):
        d_station = DockingStation()
        bike = Bike()
        self.assertEqual(d_station.dock(bike), "Bike docked.")
        self.assertEqual(d_station.storage, [bike])


if __name__ == '__main__':
    unittest.main()
