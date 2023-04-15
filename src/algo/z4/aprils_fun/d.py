# Zadanie D
program_input = [
    (5, 'Adam'),
    (3, 'Jane'),
    (5, 'Xiao'),
    (2, 'Jane')
]


def has_non_unique_names(program_input: list[tuple[int, str]]) -> bool:
    ids = set()
    for entry in program_input:
        (user_id, _name) = entry
        if user_id in ids:
            return True

        ids.add(user_id)


print(f"Input: {program_input}")
print(has_non_unique_names(program_input))
