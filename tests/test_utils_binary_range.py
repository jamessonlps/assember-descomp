import unittest

from utils import get_binary_from_int


class TestGetBinaryFromIntRange(unittest.TestCase):
    def test_valid_values_preserve_output(self):
        self.assertEqual(get_binary_from_int(0), "000000000")
        self.assertEqual(get_binary_from_int(37), "000100101")
        self.assertEqual(get_binary_from_int(511), "111111111")
        self.assertEqual(get_binary_from_int(0, 1), "0")
        self.assertEqual(get_binary_from_int(1, 1), "1")
        self.assertEqual(get_binary_from_int(5, 4), "0101")
        self.assertEqual(get_binary_from_int(15, 4), "1111")

    def test_negative_default_width_raises_value_error(self):
        with self.assertRaises(ValueError):
            get_binary_from_int(-1)

    def test_overflow_default_width_raises_value_error(self):
        with self.assertRaises(ValueError):
            get_binary_from_int(512)

    def test_negative_custom_width_raises_value_error(self):
        with self.assertRaises(ValueError):
            get_binary_from_int(-1, 4)

    def test_overflow_custom_width_raises_value_error(self):
        with self.assertRaises(ValueError):
            get_binary_from_int(16, 4)
