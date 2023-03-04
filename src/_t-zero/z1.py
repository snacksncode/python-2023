import string


def reverse_string(s: str):
    letters = string.ascii_lowercase
    n = len(letters)
    res = ""
    for letter in s:
        idx = letters.index(letter)
        res += letters[n - 1 - idx]
    return res[::-1]
