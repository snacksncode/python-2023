def mul(a, b, **kwargs):
    print(kwargs)
    return a * b


if __name__ == '__main__':
    # d = dict()
    # d['a'] = 18
    # d['b'] = 10
    # d['c'] = 11
    # print(mul(**d))
    print(mul(a=5, b=10, c=11))