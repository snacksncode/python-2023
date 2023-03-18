import random
import pandas as pd
import seaborn as sns
import time
import matplotlib.pyplot as plt


def random_list(lenght: int) -> (list, list):
    return tuple([[random.randint(1, 10) for _ in range(lenght)] for _ in range(2)])


def measure_time(func):
    def wrapper(*args):
        start_time: float = time.time()
        func(*args[0])
        execution_time: float = time.time() - start_time
        return execution_time

    return wrapper


@measure_time
def fun(list_a: list, list_b: list):
    result = []
    for numbers_a in list_a:
        result.append(0)
        for numbers_b in list_b:
            if numbers_b % numbers_a == 0:
                result[-1] += 1


list_len = 40

chart = [[], []]  # time, len_of_list
for i in range(1000):
    list_len += 1
    print(i, list_len)
    chart[0].append(fun(random_list(list_len)))
    chart[1].append(list_len)

am = pd.DataFrame({'len of array': chart[0], 'time': chart[1]})
am.head()

sns.lineplot(data=am, x="len of array", y="time")
plt.xscale('log')
plt.yscale('log')

plt.show()
