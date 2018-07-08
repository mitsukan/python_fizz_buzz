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

    def test_return_self_if_not_divisible_by_anything(self):
        self.assertEqual(fizzbuzz.run(2), 2)
        self.assertEqual(fizzbuzz.run(4), 4)
        self.assertEqual(fizzbuzz.run(8), 8)
