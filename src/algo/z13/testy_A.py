import unittest

from solution_A import *


def is_correct(decomposition, n, k, x):
    if sum(decomposition) != n:
        return False
    if x in decomposition:
        return False
    for i in decomposition:
        if type(i) != int:
            return False
        if i < 1 or i > k:
            return False
    return True


class TaskATests(unittest.TestCase):

    def test_1(self):
        dec = get_decomposition(10, 5, 3)
        self.assertTrue(is_correct(dec, 10, 5, 3))

    def test_2(self):
        dec = get_decomposition(7, 5, 1)
        self.assertTrue(is_correct(dec, 7, 5, 1))

    def test_3(self):
        dec = get_decomposition(7, 3, 2)
        self.assertTrue(is_correct(dec, 7, 3, 2))

    def test_4(self):
        dec = get_decomposition(3, 2, 1)
        self.assertTrue(len(dec) == 0)

    def test_5(self):
        dec = get_decomposition(1, 1, 1)
        self.assertTrue(len(dec) == 0)

    def test_6(self):
        dec = get_decomposition(3, 2, 1)
        self.assertTrue(len(dec) == 0)


if __name__ == '__main__':
    unittest.main()
