from random import randint


def experyment(k, n) -> bool:
    w = [0] * n
    for i in range(k):
        idx = randint(0, n - 1)
        w[idx] += 1
        if w[idx] > 1:
            return True
    return False


def compute_probability(k, n, n_experiments):
    exp_true = 0
    for i in range(n_experiments):
        if experyment(k, n):
            exp_true += 1
    print(f"true in {exp_true} of {n_experiments} cases; p={exp_true / n_experiments}")


compute_probability(30, 100, 10**4)
