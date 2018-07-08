import unittest
import fizzbuzz

class TestFizzBuzz(unittest.TestCase):

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz.run(3), "Fizz!")
