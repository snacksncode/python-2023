"""
dany będzie napis składający się ze znaków < oraz >
np s = <>>>><><>

A - znaleźć długość najdłuższego kawałka składającego się z takich samych znaków np. <<> -> 2; <> - 1; <>>><< -> 3

"""

def longest_repeat(char: str) -> int:
    counter = 1
    max_count = 1
    prv_char = 0
    for c in char:
        if c == prv_char:
            counter += 1
            max_count = max(max_count, counter)
        else:
            counter = 1
        prv_char = c
    return max_count

char = "<>>>><><>"

numbers_char = longest_repeat(char)

print(f"The longest string of the same characters '{char}' consists of {numbers_char} characters.")

