import unittest

from solution import equalize_parity


class NumbersParityTest(unittest.TestCase):

    def test_1(self):
        self.assertTrue(equalize_parity([1, 1]))
        self.assertTrue(equalize_parity([1, 2]))
        self.assertTrue(equalize_parity([2, 2]))

        self.assertFalse(equalize_parity([2, 3]))  # all elems of b must be >0

    def test_2(self):
        self.assertTrue(equalize_parity([1]))
        self.assertTrue(equalize_parity([2]))

    def test_3(self):
        self.assertFalse(equalize_parity([2, 6, 8, 4, 3]))
        self.assertFalse(equalize_parity([2, 4, 5, 4, 3]))

    def test_4(self):
        self.assertFalse(equalize_parity([2, 5, 5, 4]))

    def test_5(self):
        self.assertTrue(equalize_parity([100, 100, 1]))


if __name__ == '__main__':
    unittest.main(verbosity=2)
