import unittest


def is_cut_possible(material: list[int], product: list[int]) -> bool:
    pass


class BookingTest(unittest.TestCase):
    def test_1(self):
        self.assertTrue(is_cut_possible([10, 20], [10, 15]))
        self.assertTrue(is_cut_possible([10, 20], [10, 20]))
        self.assertTrue(is_cut_possible([10, 20], [20, 10]))  # potrzebny obrót

        self.assertTrue(is_cut_possible([10, 20], [20, 1]))
        self.assertFalse(is_cut_possible([10, 20], [21, 1]))
        self.assertFalse(is_cut_possible([10, 10], [10, 11]))
        self.assertTrue(is_cut_possible([10, 10], [9, 9]))


if __name__ == "__main__":
    unittest.main()
