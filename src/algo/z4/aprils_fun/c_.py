# Zadanie C
program_input = [
    (5, 'Adam'),
    (3, 'Jane'),
    (5, 'Xiao'),
    (2, 'Jane')
]


def has_non_unique_names(program_input: list[tuple[int, str]]) -> bool:
    names = set()
    for _id, name in program_input:
        if name in names:
            return True

        names.add(name)

    return False


print(f"Input: {program_input}")
print(has_non_unique_names(program_input))
