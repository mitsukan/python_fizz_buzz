import unittest
import menu

class TestMenu(unittest.TestCase):

    def test_Menu_class_has_dictionary(self):
        # expectation for class to have a hash of items with prices.
        m = menu.Menu()
        self.assertIsInstance(m.items, dict)


if __name__ == '__main__':
    unittest.main()