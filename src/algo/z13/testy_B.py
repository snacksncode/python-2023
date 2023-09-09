import unittest

from solution_B import *



class TaskBTests(unittest.TestCase):

    def test_1(self):
        area = get_area(3,1,1,3)
        self.assertEquals(area, 9)

    def test_2(self):
        area = get_area(1,1,4,4)
        self.assertEquals(area, 16)

    def test_3(self):
        area = get_area(1,1,6,2)
        self.assertEquals(area, 12)

    def test_4(self):
        area = get_area(1,1,4,1)
        self.assertEquals(area, 4)

    def test_5(self):
        area = get_area(4,4,1,1)
        self.assertEquals(area,16)

    def test_6(self):
        area = get_area(4,4,4,4)
        self.assertEquals(area,1)

    def test_7(self):
        area = get_area(4,4,2,2)
        self.assertEquals(area,9)


if __name__ == '__main__':
    unittest.main()
