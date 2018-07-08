import unittest
import fizzbuzz

class TestFizzBuzz(unittest.TestCase):

    def test_fizz_divisible_by_3(self):
        self.assertEqual(fizzbuzz.run(3), "Fizz!")
        self.assertEqual(fizzbuzz.run(6), "Fizz!")

    def test_buzz_divisible_by_5(self):
        self.assertEqual(fizzbuzz.run(5), "Buzz!")
        self.assertEqual(fizzbuzz.run(10), "Buzz!")

    def test_fizzbuzz_divisible_by_15(self):
        self.assertEqual(fizzbuzz.run(15), "FizzBuzz!")
