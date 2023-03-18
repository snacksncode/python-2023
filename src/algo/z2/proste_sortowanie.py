from datetime import datetime
from random import seed, randint


def gen_random_numbers(count: int, seed_number: int):
    seed(seed_number)
    return [randint(0, 10 ** 6) for _ in range(count)]


def sort_numbers(nums: list[int]) -> list[int]:
    ret = sorted(nums)
    return ret


"""
count   time (us)
5       0.7
10      0.75
100     2.4
200     4.9
400     11
800     29
1600    86
3200    224
6400    497
12800   1092
"""

if __name__ == '__main__':
    w = gen_random_numbers(12800 * 4, seed_number=111)
    REPETITIONS = 200
    time_sum = 0
    for i in range(REPETITIONS):
        st = datetime.now().timestamp()
        ret = sort_numbers(w)
        en = datetime.now().timestamp()
        time_sum += (en - st)

    # print(ret)
    print(f'czas wykonania: {time_sum / REPETITIONS:.6f} s')
