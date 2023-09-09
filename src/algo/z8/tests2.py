import unittest
from solution2 import construct_word
from random import randint


class Syllables2Test(unittest.TestCase):

    def test_1(self):
        self.assertTrue(construct_word({"ab"}, "ab"))

    def test_2(self):
        self.assertFalse(construct_word({"ab"}, "aba"))

    def test_3(self):
        self.assertTrue(construct_word({"aa"}, "aaaaaaaa"))

    def test_4(self):
        self.assertTrue(construct_word({"ab", "bc", "cd"}, "abcd"))

    def test_5(self):
        self.assertTrue(construct_word({"ab", "cd", "bc"}, "abcd"))  # kolejność w set-cie nie ma znaczenia

    def test_6(self):
        self.assertTrue(construct_word({"aa", "bb"}, "aaaa"))  # nie wszystkie sylaby muszą być wykorzystane

    def test_7(self):
        self.assertTrue(construct_word({"ab", "ba"}, "abababababab"))



if __name__ == '__main__':
    unittest.main()
