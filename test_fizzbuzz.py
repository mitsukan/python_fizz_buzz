import unittest
import fizzbuzz

class TestFizzBuzz(unittest.TestCase):

    def test_fizz_divisible_by_3(self):
        self.assertEqual(fizzbuzz.run(3), "Fizz!")
        self.assertEqual(fizzbuzz.run(6), "Fizz!")

    def test_5_eq_buzz(self):
        self.assertEqual(fizzbuzz.run(5), "Buzz!")
