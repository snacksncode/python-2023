import unittest
from z1 import reverse_string


class TestReverse(unittest.TestCase):
    def test_simple_a(self):
        self.assertEquals(reverse_string("a"), "z")

    def test_simple_z(self):
        self.assertEquals(reverse_string("z"), "a")

    def test_three(self):
        self.assertEquals(reverse_string("abc"), "xyz")

    def test_palindrome(self):
        self.assertEquals(reverse_string("abcba"), "zyxyz")
