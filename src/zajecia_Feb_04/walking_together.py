import unittest


def are_walking_together(
    pos_a: list[float], pos_b: list[float], tolerance: float
) -> bool:
    # zwrócić true jeśli na każdej pozycji pos_a i pos_b nie różnią się o więcej niż `tolerance`
    # zakładamy len(pos_a) == len(pos_b)
    n = len(pos_a)
    for idx in range(n):
        if abs(pos_a[idx] - pos_b[idx]) > tolerance:
            return False
    return True


import random

random.seed(55)


def get_random_list(n: int) -> list[float]:
    res = []
    for i in range(n):
        res.append(round(random.random(), 2))
    return res


class TestFinder(unittest.TestCase):
    def test_simple(self):
        a = [0.1, 0.4, 0.9, 0.8, 0.1]
        b = [0.2, 0.4, 0.8, 0.8, 0.1]
        self.assertTrue(are_walking_together(a, b, 0.1))

    def test_simple2(self):
        a = [0.1, 0.4, 0.9, 0.8, 0.1]
        b = [0.2, 0.4, 0.8, 0.8, 0.1]
        self.assertFalse(are_walking_together(a, b, 0.05))

    def test_simple3(self):
        a = [0.1, 0.4]
        b = [0.1, 0.4]
        self.assertTrue(are_walking_together(a, b, 0.00))

    def test_simple4(self):
        a = get_random_list(10**5)
        b = [0.1 * random.random() + e for e in a]
        self.assertTrue(are_walking_together(a, b, 0.1))

    def test_assert_type(self):
        a = [0.1, 0.4]
        b = (0.1, 0.4)
        # assert a == b   # just error
        # self.assertEqual(a, b)
        """
        Expected :[0.1, 0.4]
        Actual   :(0.1, 0.4)
        """


if __name__ == "__main__":
    unittest.main()
