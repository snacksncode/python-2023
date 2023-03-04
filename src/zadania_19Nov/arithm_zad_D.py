import unittest


def compute_diffs(w: list[int]) -> list[int]:
    diffs = []
    for idx in range(len(w) - 1):
        diffs.append(w[idx + 1] - w[idx])
    return diffs


# def is_arithmetic(w: list[int]) -> bool:
#     diffs = compute_diffs(w)
#     unique_diffs = set(diffs)
#     return len(unique_diffs) == 1


def is_arithmetic(w: list[int]) -> bool:
    n = len(w)
    r0 = w[1] - w[0]
    for idx in range(n - 1):
        if w[idx + 1] - w[idx] != r0:
            return False
    return True


class ArithTest(unittest.TestCase):
    def test_1(self):
        self.assertTrue(is_arithmetic([1, 2, 3]))
        self.assertTrue(is_arithmetic([15, 20, 25, 30]))
        self.assertTrue(is_arithmetic([15, 20]))
        self.assertTrue(is_arithmetic([15, 10, 5]))
        self.assertFalse(is_arithmetic([15, 20, 26]))
        self.assertFalse(is_arithmetic([15, 20, 25, 33]))
        self.assertFalse(is_arithmetic([5, 5, 4]))
        self.assertFalse(is_arithmetic([0, -1, 0]))


if __name__ == "__main__":
    unittest.main()
