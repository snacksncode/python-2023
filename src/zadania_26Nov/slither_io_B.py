import unittest


def get_final_size_of_snakes(init: int, food: list[int], n: int) -> int:
    pass


class SlitherTest(unittest.TestCase):
    def test_1(self):
        self.assertTrue(get_final_size_of_snakes(2, [1, 2, 3], 4), [4, 2, 2, 2])
        self.assertTrue(get_final_size_of_snakes(2, [2, 2, 2], 4), [4, 4, 4, 2])
        self.assertTrue(get_final_size_of_snakes(2, [2, 2, 4], 4), [8, 4, 2, 2])
        self.assertTrue(
            get_final_size_of_snakes(2, [2, 2, 4, 4, 8, 1, 1], 3), [16, 8, 2]
        )
        self.assertTrue(
            get_final_size_of_snakes(2, [2, 1, 4, 4, 8, 1, 1], 3), [16, 2, 2]
        )


if __name__ == "__main__":
    unittest.main()
