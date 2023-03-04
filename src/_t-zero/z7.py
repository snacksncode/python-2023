def digital_root(x):
    while x > 9:
        sum_d = 0
        for d in str(x):
            sum_d += int(d)
        x = sum_d
    return x
