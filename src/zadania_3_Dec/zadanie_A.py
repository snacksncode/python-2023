import unittest


def get_booking(flight_period: list[int]) -> bool:
    start = flight_period[0]
    end = flight_period[1]

    if start > end:
        return False
    if (end - start + 1) > 7:
        return False

    # for day in range(start, end + 1):
    #     if day % 7 == 0: return True
    # return False
    if start == end and start % 7 != 0:
        return False

    if (start % 7 == 0) or (start % 7 >= end % 7):
        return True
    return False


class BookingTest(unittest.TestCase):
    def test_1(self):
        self.assertTrue(get_booking([6, 8]))
        self.assertTrue(get_booking([2, 7]))
        self.assertTrue(get_booking([14, 14]))

        self.assertFalse(get_booking([2, 5]))
        self.assertTrue(get_booking([-1, 5]))
        self.assertFalse(get_booking([-1, 7]))  # zbyt długi okres

        self.assertFalse(
            get_booking([7, 2])
        )  # dzień wylotu musi być przed dniem powrotu


if __name__ == "__main__":
    unittest.main()
