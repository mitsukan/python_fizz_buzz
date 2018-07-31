import unittest
from bike import Bike

class TestBike(unittest.TestCase):

    def test_is_working(self):
        """Bikes can be broken, needs a default state"""
        bike = Bike()
        self.assertEqual(bike.is_working, True)