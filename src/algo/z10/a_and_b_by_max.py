# 1
def longest_repeat(char: str) -> int:
    return max([len(max(char.split("<"))), len(max(char.split(">")))])


# 2
def some_data(s: str) -> list:
    a = [len(s)]
    [a.append(a[-1] + 1) if i == "<" else a.append(a[-1] - 1) for i in s]
    return a
