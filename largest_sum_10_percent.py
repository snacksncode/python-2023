from src.algo.z2.automat import run_tests, visualize
from random import seed, randint
from rich import print


def solve(array: list[int]) -> int:
    if len(array) % 10 != 0:
        raise 'Input array is not of length divisible by 10'

    window_length = len(array) // 10
    left = 0
    right = window_length

    max_sum = float('-inf')
    max_sum_left = None
    max_sum_right = None
    for _ in range(right, len(array)):
        local_sum = sum(array[left:right])

        if local_sum > max_sum:
            max_sum = local_sum
            max_sum_left = left
            max_sum_right = right

        left += 1
        right += 1

    return (max_sum, array[max_sum_left:max_sum_right])


def generate_data(data_size):
    seed(111)
    mx_num = 10 ** 4
    data_a = [randint(0, mx_num) for _ in range(data_size)]
    return {"array": data_a}


if __name__ == '__main__':
    x, y = run_tests(generate_data, solve, max_size=10**4)
    visualize(x, y)
    # print(solve([2, 5, 7, 9, 2], [4, 8, 18, 27]))
