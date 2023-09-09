import unittest

from zad_a import *


class HashTableTests(unittest.TestCase):

    def setUp(self) -> None:
        self.bag = get_new_bag(1000)

    def test_1(self):
        insert_element(self.bag, 10)
        self.assertTrue(contains_element(self.bag, 10))

    def test_2(self):
        insert_element(self.bag, 10)
        insert_element(self.bag, 10)
        self.assertTrue(contains_element(self.bag, 10))

    def test_3(self):
        insert_element(self.bag, 10)
        insert_element(self.bag, 20)
        self.assertTrue(contains_element(self.bag, 20))

    def test_4(self):
        insert_element(self.bag, 10)
        remove_element(self.bag, 10)
        self.assertFalse(contains_element(self.bag, 10))

    def test_5(self):
        self.assertFalse(contains_element(self.bag, 10))

    def test_6(self):
        insert_element(self.bag, 10)
        insert_element(self.bag, 'kadabra')
        insert_element(self.bag, ('a', 'b'))
        self.assertTrue(contains_element(self.bag, 'kadabra'))
        self.assertTrue(contains_element(self.bag, ('a', 'b')))
        self.assertTrue(contains_element(self.bag, 10))


if __name__ == '__main__':
    unittest.main()
