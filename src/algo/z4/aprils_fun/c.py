# Zadanie C
program_input = [
    (5, 'Adam'),
    (3, 'Jane'),
    (5, 'Xiao'),
    (2, 'Jane')
]


def has_non_unique_names(program_input: list[tuple[int, str]]) -> bool:
    names = set()
    for entry in program_input:
        (_id, name) = entry
        if name in names:
            return True

        names.add(name)

    return False


print(f"Input: {program_input}")
print(has_non_unique_names(program_input))
