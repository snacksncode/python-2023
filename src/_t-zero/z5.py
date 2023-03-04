import unittest
from z2 import reverse_number


class TestReverse(unittest.TestCase):
    def test_simple1(self):
        self.assertEquals(reverse_number(2), 2)

    def test_simple2(self):
        self.assertEquals(reverse_number(12), 21)

    def test_simple3(self):
        self.assertEquals(reverse_number(12345678), 87654321)

    def test_simple4(self):
        large1 = int("1" * 100 + "2")
        large2 = int("2" + "1" * 100)
        self.assertEquals(reverse_number(large1), large2)

    def test_illegal_arg(self):
        with self.assertRaises(ValueError):
            reverse_number(1.0)
        with self.assertRaises(ValueError):
            reverse_number(-1)
        with self.assertRaises(ValueError):
            reverse_number(10)
