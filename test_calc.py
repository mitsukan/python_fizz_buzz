import unittest     # Import the testing module
import calc     # Import the calc.py module

class TestCalc(unittest.TestCase): # test class inherits from unittest.TestCase

    def test_add(self): # all tests need to start with test_ as a naming convention
        self.assertEqual(calc.add(10,5), 15)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10,5), 5)

# To run the test, we need to enter in the terminal:
# $ python -m unittest test_calc.py
# In order to have this file run unittest:

if __name__ == '__main__': # If we run this module directly:
    unittest.main() # run the code within the conditional
