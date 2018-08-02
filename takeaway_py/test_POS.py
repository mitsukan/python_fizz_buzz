import unittest
from unittest import mock
import POS


class TestPOS(unittest.TestCase):

    def test_has_list_to_store_order(self):
        pos = POS.Till()
        self.assertIsInstance(pos.order, list)

    def test_can_receive_an_order(self):
        pos = POS.Till()
        pos.add("chips")
        pos.add("sausage")
        self.assertEqual(pos.order, ["chips", "sausage"])


    def test_can_total_up_the_order_using_menu_prices(self):
        with mock.patch('POS.Menu') as mock_menu:
            mock_menu().items = {"item1": 1.0, "item2": 2.0}
            pos = POS.Till()
            pos.add("item1")
            pos.add("item2")
            self.assertEqual(pos.total(), 3.0)



if __name__ == '__main__':
    unittest.main()