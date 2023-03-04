import unittest


def get_final_snake_size(init: int, food: list[int]) -> int:
    pass


class SlitherTest(unittest.TestCase):
    def test_1(self):
        self.assertTrue(get_final_snake_size(2, [1, 2, 3]), 4)
        self.assertTrue(get_final_snake_size(2, [1, 2, 4]), 8)
        self.assertTrue(get_final_snake_size(2, [2, 7, 10, 1, 8, 4]), 16)
        self.assertTrue(get_final_snake_size(2, [2, 7, 10, 1, 8]), 4)
        self.assertTrue(get_final_snake_size(2, [2, 2, 2, 2, 2]), 4)
        self.assertTrue(get_final_snake_size(1, [2, 4, 6]), 1)


if __name__ == "__main__":
    unittest.main()
