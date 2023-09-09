import unittest

from model import Fraction
from helper import add


class FractionTests(unittest.TestCase):

    def test_simple(self):
        f1 = Fraction(0, 1)
        f2 = Fraction(1, 1)
        self.assertAlmostEqual(add(f1,f2).value(), 1.0)

    def test_one(self):
        f1 = Fraction(1, 1)
        f2 = Fraction(1, 1)
        self.assertAlmostEqual(add(f1,f2).value(), 2.0)

    def test_two(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 2)
        self.assertAlmostEqual(add(f1,f2).value(), 1.0)
