from collections import Counter
from random import randint


# wylosować 30 liczb z przedziału [0,99] i sprawdzić czy jakieś się powtórzyły


def solve_A_by_sort():
    w = []
    for i in range(30):
        w.append(randint(0, 99))
    w.sort()
    for idx in range(len(w) - 1):
        if w[idx] == w[idx + 1]:
            print(f"powtórzone: {w[idx]}")
            break


def solve_A_by_list():
    w = [0] * 100  # można "dotykać" w[0] ... w[99]
    for i in range(30):
        idx = randint(0, 99)
        w[idx] += 1
        if w[idx] > 1:
            print(f"powtórzone {idx}")


def solve_A_attempt1():
    w = [randint(0, 99) for i in range(30)]  # comprehension
    print(w)
    print(Counter(w))


if __name__ == "__main__":
    # solve_A_by_sort()
    # solve_A_by_list()
    solve_A_attempt1()
