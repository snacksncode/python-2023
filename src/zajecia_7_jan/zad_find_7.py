def sol1(n: int):
    count = 0
    for i in range(n):
        if "7" not in str(i):
            count += 1
    return count


def sol2(n: int):
    count = 0
    for i in range(n):
        x = i
        found = False
        while x != 0:
            if x % 10 == 7:
                found = True
                break
            x //= 10
        if not found:
            count += 1
    return count


# print(sol1(10 ** 7))
print(sol2(10**7))
