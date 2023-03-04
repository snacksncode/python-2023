def reverse_number(x: int):
    if not isinstance(x, int) or x < 0 or "0" in str(x):
        raise ValueError
    as_string = str(x)
    rev_str = as_string[::-1]
    res = int(rev_str)
    return res
