import unittest
import menu

class TestMenu(unittest.TestCase):

    def test_Menu_class_has_dictionary(self):
        # expectation for class to have a hash of items with prices.
        m = menu.Menu()
        self.assertIsInstance(m.items, dict)

    def test_can_add_item_to_menu(self):
        m = menu.Menu()
        m.add("chips", 1.7)
        self.assertEqual(m.items, {"chips": 1.7})


if __name__ == '__main__':
    unittest.main()