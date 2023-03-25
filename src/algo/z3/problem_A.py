from random import seed, randint

from src.algo.z2.automat import run_tests, visualize


def solve(a: list[int]) -> int:
    N = len(a)
    n = N // 10
    best = sum(a[:n])
    for start in range(0, N - n):
        best = max(best, sum(a[start: start + n]))
    return best


def generate_data(data_size):
    seed(111)
    mx_num = 10 ** 4
    data_a = [randint(0, mx_num) for _ in range(data_size)]
    return {"a": data_a}


if __name__ == '__main__':
    x, y = run_tests(generate_data, solve, max_size=4 * 10 ** 5)
    visualize(x, y)
    # print(solve(a=[1,1,1,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,2,3,1,1,1,1,2,1,1,1,1,1]))
