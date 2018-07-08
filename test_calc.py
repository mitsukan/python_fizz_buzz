import unittest     # Import the testing module
import calc     # Import the calc.py module

class TestCalc(unittest.TestCase): # test class inherits from unittest.TestCase

    def test_add(self): # all tests MUST start with test_ as a naming convention
        result = calc.add(10,5)
        self.assertEqual(result, 15)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10,5), 5)
        self.assertEqual(calc.subtract(-1,1), -2) # Multiple assertions will show up as only 1 test in the test runner, but will fail if one or more assertions fail.
        self.assertEqual(calc.subtract(-1,-1), 0) # This can possibly be used to test edge cases.

    def test_multiply(self):
        self.assertEqual(calc.multiply(3,3), 9)

    def test_divide(self):
        self.assertEqual(calc.divide(15,3), 5)
        self.assertRaises(ValueError, calc.divide, 10, 0) # first arg is the type of error to raise, 2nd is the function, 3rd and 4th are arguments separately.

# To run the test, we need to enter in the terminal:
# $ python -m unittest test_calc.py
# In order to have this file run unittest:

if __name__ == '__main__': # If we run this module directly:
    unittest.main() # run the code within the conditional
