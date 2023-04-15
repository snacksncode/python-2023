

def is_unique(elems: list) -> bool:
    unique_elems = set(elems)
    return len(unique_elems) == len(elems)



if __name__ == '__main__':
    print(is_unique(['aa', 'a', 'c', 'bb', 'a']))