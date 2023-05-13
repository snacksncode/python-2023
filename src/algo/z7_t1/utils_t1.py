def list_contains_only_ints(list):
    return all([isinstance(x, int) for x in list])


def list_contains_negative_ints(list):
    for num in list:
        if num < 0:
            return True

    return False
