def find_greater_than(val: float, a: list[float]) -> list[tuple[float, int]]:
    # znaleźć wszystkie elementy więsze od val, razem z ich pozycjami (zwracamy pary (value, position))
    res = []
    for idx in range(len(a)):
        if a[idx] > val:
            res.append((a[idx], idx))
    return res


a = [0.1, 0.4, 0.9, 0.8, 0.1]

# find_greater_than(0.5, a) --> [(0.9,2), (0.8,3)]


# tuple

z = (1, 2, 5)
# z[0] = 5
# z.append(8)

import random

random.seed(55)


def get_random_list(n: int) -> list[float]:
    res = []
    for i in range(n):
        res.append(round(random.random(), 2))
    return res


import unittest


class TestFinder(unittest.TestCase):
    def test_simple(self):
        a = [0.1, 0.4, 0.9, 0.8, 0.1]
        res = find_greater_than(0.5, a)
        # assert res == [(0.9, 2), (0.8, 3)]
        self.assertEquals(res, [(0.9, 2), (0.8, 3)])

    def test_empty(self):
        a = [0.1, 0.4, 0.9, 0.8, 0.1]
        res = find_greater_than(0.95, a)
        assert res == []

    def test_full(self):
        a = [0.1, 0.4, 0.9, 0.8, 0.1]
        res = find_greater_than(0.05, a)
        self.assertEquals(res[:2], [(0.1, 0), (0.4, 1)])

    def test_some_small_random(self):
        random.seed(13)
        a = get_random_list(5)  # [0.26, 0.69, 0.68, 0.85, 0.19]
        res = find_greater_than(0.8, a)
        assert res == [(0.85, 3)]

    def test_large_test(self):
        random.seed(111)
        a = get_random_list(10**5)
        res = find_greater_than(0.8, a)
        # sprawdzić jak długo to trwa


s = "abra kadabra"

if __name__ == "__main__":
    unittest.main()
