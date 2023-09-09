word = 'kadabra'
chars = [*word]

print(chars)


def triangle(a, b, c):
    return a + b + c


if __name__ == '__main__':
    sides = [2, 3, 4]
    print(triangle(*sides))

    triangle(a=2, b=5, c=10)
    d = {'a': 2, 'b': 5, 'c': 10}
    triangle(**d)
