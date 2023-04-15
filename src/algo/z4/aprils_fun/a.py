from rich import print
import json
from collections import defaultdict

# Zadanie A + Testy


def is_unique_list(input: list):
    return len(input) == len(list(set(input)))


tests = [
    ['2', '2', '3'],
    ['a', 'aa', 'aaa'],
    [1, 2, 2],
    ['json', 'dumps', 'is', 'cool']
]

for test in tests:
    print(f"Is unique: {json.dumps(test)}: {is_unique_list(test)}")

print('\n-----------\n')

# Zadanie B + Testy


def find_duplicates(input: list):
    hash_map = defaultdict(lambda: 0)
    for entry in input:
        hash_map[entry] = hash_map[entry] + 1

    duplicates = []
    for entry in hash_map:
        times_appears = hash_map[entry]
        if times_appears > 1:
            duplicates.append(entry)

    # Ewentualnie "pythonic way":
    # duplicates = [_ for _ in hash_map if hash_map[_] > 1]
    return duplicates


tests_2 = [
    ['2', '2', '3'],
    ['a', 'aa', 'aaa'],
    [1, 2, 2],
    ['json', 'dumps', 'is', 'cool']
]

for test in tests_2:
    print(f"Duplicates: {json.dumps(test)}: {find_duplicates(test)}")
