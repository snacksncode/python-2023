import unittest
from solution import open_lock
from random import randint

class KeyLockTest(unittest.TestCase):

    def test_simple(self):
        self.assertEquals(open_lock([1, 1], [2, 2]), 0)

    def test_simple1(self):
        self.assertEquals(open_lock([1, 2], [2, 1]), 0)

    def test_simple2(self):
        self.assertEquals(open_lock([1, 2, 5], [2, 1, 0]), 1)

    def test_simple3(self):
        self.assertEquals(open_lock([1, 2, 5], [2, 1, 0]), 1)

    def test_simple4(self):
        self.assertEquals(open_lock([5, 5, 6], [0, 0, -1]), -1)

    def test_simple5(self):
        self.assertEquals(open_lock([5, 5, 6], [0]), -1)

    def test_simple6(self):
        self.assertEquals(open_lock([12, 9, 89, 11, 55], [78, 81, 1, 79, 35]), 0)

    def test_simple7(self):
        self.assertEquals(open_lock([], []), -1)

    def test_simple8(self):
        self.assertEqual(open_lock([1000000, 2000000], [2000000, 1000000]), 0)

    def test_simple9(self):
        self.assertEqual(open_lock([1.5, 2.5, 3.5], [2.5, 1.5, 0]), -1)

    def test_simple10(self):
        self.assertEqual(open_lock([1, {2, 3}], [{3, 2}, 1]), -1)

    def test_simple11(self):
        self.assertEqual(open_lock([1, 2, 3], [0, 1, 4]), 1)

    def test_simple12(self):
        lock = [randint(1, 100) for _ in range(50)]
        key = [randint(1, 100) for _ in range(50)]
        self.assertEqual(open_lock(lock, key), 1)

    def test_simple13(self):
        lock1 = [randint(1, 10) for _ in range(500)]
        key1 = [10 - x for x in lock1]
        self.assertEqual(open_lock(lock1, key1), 0)

    def test_simple14(self):
        lock2 = [randint(-10, 10) for _ in range(50)]
        key2 = [10 - x for x in lock2]
        self.assertEqual(open_lock(lock2, key2), -1)

    def test_simple15(self):
        self.assertEqual(open_lock([1000000, 2000000, 3000000], [3000000, 2000000, 1000000]), 0)

    def test_simple16(self):
        lock3 = [randint(1, 100) for _ in range(15)]
        key3 = [randint(1, 100) for _ in range(10)]
        self.assertEqual(open_lock(lock3, key3), -1)

    def test_simple17(self):
        self.assertEquals(open_lock([5, 5, 6], [5, 5, -4]), -1)

    def test_simple18(self):
        self.assertEquals(open_lock([10], [10]), 0)

    def test_simple19(self):
        self.assertEquals(open_lock([-10], [-10]), -1)

    def test_simple20(self):
        self.assertEqual(open_lock([1, 1, 1, 1], [2, 3, 4, 5]), 1)

    def test_simple21(self):
        self.assertEqual(open_lock([1, 1, 1, 1], [2, 3, 4, 5]), 1)