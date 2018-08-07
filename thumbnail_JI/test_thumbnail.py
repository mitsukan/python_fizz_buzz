import unittest
from unittest import mock
import thumbnail

class TestThumbnail(unittest.TestCase):

    def test_can_call_image_size(self):
        with mock.patch("thumbnail.Image") as mock_image:
            mock_pic = mock.Mock()
            resize = thumbnail.Resizer()
            resize.print_size(mock_pic).assert_called_once()


if __name__ == '__main__':
    unittest.main()