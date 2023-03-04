import random
import string
import unittest
from z3 import swap_case


class TestReverse(unittest.TestCase):
    def test_simple1(self):
        self.assertEquals(swap_case("aAB"), "Aab")

    def test_simple2(self):
        self.assertEquals(swap_case("azAZ"), "AZaz")

    def test_bulk(self):
        for _ in range(1000):
            s = ""
            for i in range(1000):
                s += random.choice(string.ascii_letters)
            self.assertEquals(swap_case(s), s.swapcase())
