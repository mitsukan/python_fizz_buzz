import mock_experiments
from unittest import mock
import unittest

m = mock.Mock()

assert isinstance(m.foo, mock.Mock)

if __name__ == '__main__':
    unittest.main()