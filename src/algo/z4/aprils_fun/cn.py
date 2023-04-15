from random import choice
from string import ascii_lowercase


def random_str(n = 4):
    return ''.join([choice(ascii_lowercase) for _ in range(n)])

if __name__ == '__main__':
    for i in range(10):
        print(random_str())
