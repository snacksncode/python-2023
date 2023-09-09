import unittest
from sol_A import *


class SyllablesTest(unittest.TestCase):

    def test_1(self):
        self.assertEquals(get_min_number_of_operations([1, 0, -1, -1, 0, 2, 5, 0, -2]), 2)

    def test_2(self):
        self.assertEquals(get_min_number_of_operations([-1, 1, -1]), 2)

    def test_3(self):
        self.assertEquals(get_min_number_of_operations([-1, 1, 2, 3]), 1)

    def test_4(self):
        self.assertEquals(get_min_number_of_operations([-1, 0, -1]), 1)

    def test_5(self):
        self.assertEquals(get_min_number_of_operations([-1, 1, -1, 1, -1, 1, -1]), 4)

    def test_6(self):
        self.assertEquals(get_min_number_of_operations([1, -1, -2, -3, -4]), 1)

    def test_7(self):
        self.assertEquals(get_min_number_of_operations([1, 0, 1]), 0)

    def test_8(self):
        self.assertEquals(get_min_number_of_operations([1, 0, 1, -1]), 1)


if __name__ == '__main__':
    unittest.main()
