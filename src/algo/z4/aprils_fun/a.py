from collections import defaultdict

w = [1, 2, 3, 3, 1, 2]

s = set(w)
print(s)

w = list(set(w))
print(w)

d = dict()

d[1] = 'akabra'
d[2] = 'xxx'
print(d)

dd: dict[int,list] = defaultdict(lambda: [])

dd[1].append(1)
dd[1].append(2)
dd[3].append(3)
print(dd)
