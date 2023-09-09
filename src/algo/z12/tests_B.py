import unittest
from sol_B import *


class CostValueTest(unittest.TestCase):

    def test_1(self):
        self.assertEquals(get_best_value_package(costs=[1, 1, 1], values=[1, 2, 4], max_total_cost=2), 6)

    def test_2(self):
        self.assertEquals(get_best_value_package(costs=[1, 1, 1], values=[1, 2, 4], max_total_cost=1), 4)

    def test_3(self):
        self.assertEquals(get_best_value_package(costs=[1, 2, 3], values=[1, 2, 4], max_total_cost=4), 5)

    def test_4(self):
        self.assertEquals(get_best_value_package(costs=[2, 3, 4], values=[3, 3, 5], max_total_cost=5), 6)


if __name__ == '__main__':
    unittest.main()
