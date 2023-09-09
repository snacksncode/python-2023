# def find_chain(word):
#     chain = []
#     results = []
#     for character in word:
#         chain.append(character)
#     counter = 1
#
#     for x in range(0, len(chain) - 1):
#         if chain[x] == chain[x + 1]:
#             counter += 1
#         else:
#             results.append(counter)
#             counter = 1
#
#     # Dodanie ostatniego ciągu do listy results
#     results.append(counter)
#
#     return max(results)


def find_chain(char: str) -> int:
    s1 = char.split("<")
    s2 = char.split(">")
    # print(f'{s1=}, {s2=}')
    # return max([len(max(s1)), len(max(s2))])
    print(s1+s2)
    return len(max(s1 + s2))


import unittest


class LongestStreakTests(unittest.TestCase):

    def test_1(self):
        self.assertEquals(find_chain("<<>"), 2)

    def test_2(self):
        self.assertEquals(find_chain("<><><><><><>"), 1)

    def test_3(self):
        self.assertEquals(find_chain("<>>><<"), 3)

    def test_4(self):
        self.assertEquals(find_chain("<<<<<<<<>>><<"), 8)

    def test_5(self):
        self.assertEquals(find_chain("<<>>><>>><<"), 3)

    def test_6(self):
        self.assertEquals(find_chain(">><<"), 2)

    def test_7(self):
        self.assertEquals(find_chain(">>>>"), 4)


if __name__ == '__main__':
    unittest.main()
