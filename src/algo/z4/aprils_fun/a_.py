from rich import print
import json
from collections import defaultdict

# Zadanie A + Testy


def is_unique_list(elems: list):
    return len(elems) == len(list(set(elems)))


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


def find_duplicates(elems: list):
    hash_map = defaultdict(lambda: 0)
    for entry in elems:
        hash_map[entry] = hash_map[entry] + 1

    duplicates = []
    for (entry, times_appears) in hash_map.items():
        if times_appears > 1:
            duplicates.append(entry)

    # Ewentualnie "pythonic way":
    # duplicates = [_ for _ in hash_map if hash_map[_] > 1]
    return duplicates


tests_2 = [
    ['2', '2', '3'],
    ['a', 'aa', 'aaa'],
    [1, 2, 2, 2, 3, 3],
    ['json', 'dumps', 'is', 'cool']
]

for test in tests_2:
    print(f"Duplicates: {json.dumps(test)}: {find_duplicates(test)}")
