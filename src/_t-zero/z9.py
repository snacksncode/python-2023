import unittest


def find_largest_sum(a: list[int]):
    # O(N**2)
    s = [0]
    for c in a:
        s.append(s[-1] + c)
    n = len(a)
    mx = max(a)
    for st in range(n):
        for en in range(st + 1, n + 1):  # beyond last
            mx = max(mx, s[en] - s[st])
    return mx


class TestIt(unittest.TestCase):
    def test_one_elem(self):
        self.assertEquals(find_largest_sum([1]), 1)

    def test_negative_elem(self):
        self.assertEquals(find_largest_sum([-1]), -1)

    def test_3_elem(self):
        self.assertEquals(find_largest_sum([1, -1, 1]), 1)

    def test_4(self):
        self.assertEquals(find_largest_sum([2, -1, 10]), 11)

    def test_5(self):
        self.assertEquals(find_largest_sum([1, -2, 3, -4, 5, -4, 5, -2, 1]), 6)

    def test_5(self):
        self.assertEquals(find_largest_sum([-1, -2, -3]), -1)
