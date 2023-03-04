import unittest


def get_min_caffeine_level(log: list[int]) -> float:
    pass


class MateZB_Test(unittest.TestCase):
    def test_1(self):
        self.assertAlmostEqual(get_min_caffeine_level([10, 0]), 500, 2)

    def test_2(self):
        self.assertAlmostEqual(get_min_caffeine_level([1, 0, 10, 0]), 50, 2)

    def test_3(self):
        self.assertAlmostEqual(get_min_caffeine_level([1, 0.5, 0.5, 0.5]), 100, 2)

    def test_4(self):
        self.assertAlmostEqual(get_min_caffeine_level([10]), 1000, 2)

    def test_5(self):
        self.assertAlmostEqual(
            get_min_caffeine_level([1, 0, 0, 0, 0, 0]), 12.5 / 2 / 2, 2
        )


if __name__ == "__main__":
    unittest.main()
