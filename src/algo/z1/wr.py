from math import sin


def pakit(fn):
    def wrapper(*arg, **kwarg):
        print('before')
        fn(*arg, **kwarg)
        print('after')

    return wrapper


def timeit(fn):
    from datetime import datetime

    def wrapper(*args, **kwargs):
        st = datetime.now().timestamp()
        fn(*args, **kwargs)
        en = datetime.now().timestamp()
        print(f'executed {fn.__name__} in {(en-st)*1000:.3f} ms')

    return wrapper

@timeit
def foo(x):
    print(f'doing {x}')
    x = 12
    for _ in range(10000):
        x = 10 * sin(x)


if __name__ == '__main__':
    foo(12)
