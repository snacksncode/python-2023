# Zadanie D
program_input = [
    (5, 'Adam'),
    (3, 'Jane'),
    (5, 'Xiao'),
    (2, 'Jane')
]


def has_non_unique_ids(program_input: list[tuple[int, str]]) -> bool:
    ids = set()
    for user_id, _name in program_input:
        if user_id in ids:
            return True

        ids.add(user_id)

    return False


print(f"Input: {program_input}")
print(has_non_unique_ids(program_input))
