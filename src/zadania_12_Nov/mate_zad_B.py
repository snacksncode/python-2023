import unittest


def get_equal_capacity(leftovers: list[int]) -> int:
    pass


class MateZB_Test(unittest.TestCase):
    def test_1(self):
        assert get_equal_capacity([10, 20]) == 15

    def test_2(self):
        assert get_equal_capacity([20, 1, 1]) == 7

    def test_3(self):
        assert get_equal_capacity([20, 0, 0, 0, 0, 0, 0]) == 2

    def test_4(self):
        assert get_equal_capacity([1, 1, 2]) == 1

    def test_5(self):
        assert get_equal_capacity([2]) == 2


if __name__ == "__main__":
    unittest.main()
