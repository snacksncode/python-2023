import unittest
from solution import split_to_syllables
from random import randint

class SyllablesTest(unittest.TestCase):

    def test_1(self):
        self.assertEquals(split_to_syllables("ab"), ["ab"])

    def test_2(self):
        self.assertEquals(split_to_syllables("abc"), ["ab", "bc"])

    def test_3(self):
        self.assertEquals(split_to_syllables("abab"), ["ab", "ba", "ab"])

    def test_4(self):
        self.assertEquals(split_to_syllables("aaaa"), ["aa", "aa", "aa"])

    def test_5(self):
        self.assertEquals(split_to_syllables("abcd"), ["ab", "bc", "cd"])

    def test_6(self):
        self.assertEquals(split_to_syllables("aabb"), ["aa", "ab", "bb"])



if __name__ == '__main__':
    unittest.main()

