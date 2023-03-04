def generate_user_names(prefix: str, min_id: int, max_id: int) -> list[str]:
    names = []
    for id_ in range(min_id, max_id + 1):
        names.append(prefix + str(id_))
    return names


if __name__ == "__main__":
    print(list(range(5, 9)))
    print(generate_user_names("user", 5, 10**5))
