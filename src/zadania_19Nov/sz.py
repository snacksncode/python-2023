from datetime import datetime
from random import randint


def ts():
    return datetime.now().timestamp()


pare_liczb = [randint(0, 10**6) for i in range(10000)]

# w = set()
w = []
for i in range(10**8):
    # w.add(i)
    w.append(i)

st = ts()

present = 0
for liczba in pare_liczb:
    if liczba in w:
        present += 1

en = ts()
print(f"elapsed: {en - st:.3f}s, present={present}")
