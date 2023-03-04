import unittest


def bulk_mate_purchase_order(
    offers: list[list[int, float]], need_bottles: int
) -> float:
    pass


class MateZD_Test(unittest.TestCase):
    def test_1(self):
        self.assertAlmostEqual(bulk_mate_purchase_order([[10, 60], [1, 10]], 5), 50, 2)
        self.assertAlmostEqual(bulk_mate_purchase_order([[10, 60], [1, 10]], 8), 60, 2)
        self.assertAlmostEqual(
            bulk_mate_purchase_order([[20, 128], [1, 7], [400, 2200.0]], 100), 640, 2
        )
        self.assertAlmostEqual(
            bulk_mate_purchase_order([[20, 128], [1, 5], [400, 2200.0]], 100), 500, 2
        )
        self.assertAlmostEqual(
            bulk_mate_purchase_order([[20, 128], [1, 5], [1, 4.5], [400, 2200.0]], 100),
            450,
            2,
        )
        self.assertAlmostEqual(
            bulk_mate_purchase_order([[20, 100], [18, 95]], 100), 450, 2
        )  # ???


if __name__ == "__main__":
    unittest.main()
