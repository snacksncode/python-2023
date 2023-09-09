def get_decomposition(n, k, x) -> list[int]:
    if x != 1:
        return [1] * n
    # x == 1
    if k == 1:
        return []

    if k == 2 and x % 2 == 1:
        return []

    if k == 2 and x % 2 == 0:
        return [2] * (x // 2)

    # from now on: x=1, k>=3
    if n == 1: return []

    if n % 2 == 1:
        return [3] + [2] * ((n - 3) // 2)
    else:
        return [2] * (n // 2)
