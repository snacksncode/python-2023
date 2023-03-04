import unittest


def have_we_met(booking1: list[int], booking2: list[int]) -> bool:
    days1 = []
    for d in range(booking1[0], booking1[1] + 1):
        days1.append(d)
    days1 = set(days1)
    for d in range(booking2[0], booking2[1] + 1):
        if d in days1:
            return True
    return False


def have_we_met(booking1: list[int], booking2: list[int]) -> bool:
    if booking1[0] > booking2[0]:
        t = booking1
        booking1 = booking2
        booking2 = t

    return booking1[1] >= booking2[0]


class BookingTest(unittest.TestCase):
    def test_1(self):
        self.assertTrue(
            have_we_met([0, 2], [2, 4])
        )  # pracownicy wspólnie przebywali w willi w dniu=2
        self.assertFalse(have_we_met([0, 2], [3, 4]))
        self.assertTrue(have_we_met([0, 2], [-1, 5]))
        self.assertTrue(have_we_met([4, 9], [1, 5]))
        self.assertFalse(have_we_met([4, 9], [1, 3]))
        self.assertFalse(have_we_met([4, 4], [3, 3]))


if __name__ == "__main__":
    unittest.main()
