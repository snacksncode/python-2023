import unittest


def generate_and_check(a, r, w):
    n = len(w)
    w_ = [a + r * i for i in range(n)]
    bad_places = 0
    for i in range(n):
        if w[i] != w_[i]:
            bad_places += 1
    return bad_places <= 1


def is_almost_arithmetic(w: list[int]) -> bool:
    if generate_and_check(w[0], w[1] - w[0], w):
        return True
    w.reverse()
    if generate_and_check(w[0], w[1] - w[0], w):
        return True
    return False


class AlmostArithTest(unittest.TestCase):
    def test_1(self):
        self.assertTrue(is_almost_arithmetic([1, 2, 3]))
        self.assertTrue(is_almost_arithmetic([15, 20, 25, 35]))
        self.assertTrue(is_almost_arithmetic([15, 20]))
        self.assertTrue(is_almost_arithmetic([15, 10, 5]))
        self.assertTrue(is_almost_arithmetic([15, 20, 26]))
        self.assertTrue(is_almost_arithmetic([15, 20, 25, 33]))
        self.assertTrue(is_almost_arithmetic([5, 5, 4]))
        self.assertTrue(is_almost_arithmetic([0, -1, 0]))

        self.assertFalse(is_almost_arithmetic([0, -1, 0, 10]))
        self.assertFalse(is_almost_arithmetic([0, 0, 0, 10, 20]))
        self.assertFalse(is_almost_arithmetic([0, 1, 3, 6]))


if __name__ == "__main__":
    unittest.main()
