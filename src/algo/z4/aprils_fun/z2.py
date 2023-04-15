


def filter_nonunique(elems: list[str]) -> list[str]:
    res = []
    seen = set()
    for e in elems:
        if e in seen:
            res.append(e)
        seen.add(e)
    return sorted(list(set(res)))

if __name__ == '__main__':
    print(filter_nonunique)
