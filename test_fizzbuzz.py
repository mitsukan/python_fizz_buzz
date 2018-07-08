import unittest
import fizzbuzz

class TestFizzBuzz(unittest.TestCase):

    def test_3_eq_fizz(self):
        self.assertEqual(fizzbuzz.run(3), "Fizz!")

    def test_5_eq_buzz(self):
        self.assertEqual(fizzbuzz.run(5), "Buzz!")
