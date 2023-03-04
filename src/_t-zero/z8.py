def find_divisors(d: int) -> list[int]:
    return [x for x in range(1, d + 1) if d % x == 0]
