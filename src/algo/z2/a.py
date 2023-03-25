d = dict()

d['a'] = 10
d['b'] = 12

print(d)


def f(a, b, c):
    print(a, b, c)


f(a=12, b=10, c=8)



f(**d, c=11)
