import unittest


def get_full_bottles(leftovers: list[int], capacity: int) -> int:
    if capacity == 0:
        return len(leftovers)  # "corner case"
    total = sum(leftovers)
    full_bottles = int(total / capacity)
    return min(len(leftovers), full_bottles)


class MateZA_Test(unittest.TestCase):
    def test_1(self):
        res = get_full_bottles([200, 200, 200], 500)
        assert res == 1

    def test_2(self):
        res = get_full_bottles([100, 200, 200, 50, 500], 500)
        assert res == 2

    def test_3(self):
        res = get_full_bottles([100, 100, 100], 500)
        assert res == 0

    def test_4(self):
        res = get_full_bottles([800], 500)
        assert res == 1

    def test_5(self):
        res = get_full_bottles([0, 0, 0], 500)
        assert res == 0

    def test_6(self):
        res = get_full_bottles([0, 0, 10], 0)
        assert res == 3

    def test_7(self):
        res = get_full_bottles([900, 900, 900], 500)
        assert res == 3


if __name__ == "__main__":
    unittest.main()
