import unittest
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

if __name__ == '__main__':
    unittest.main()