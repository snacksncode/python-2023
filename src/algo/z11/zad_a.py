"""
Przykład prostej tablicy z hashowaniem

https://pl.wikipedia.org/wiki/Tablica_mieszaj%C4%85ca

This:
https://www.lisedunetwork.com/wp-content/uploads/2014/02/Essentials-Elements-of-Library-Catalogue.jpg




"""


def get_new_bag(data_size: int):
    return [[] for _ in range(data_size)]


def insert_element(bag: list[list], element: int):
    M = len(bag)  # tyle mamy list w `bag`; każda ma ileś... elementów...
    h = element.__hash__()
    idx = h % M
    bag[idx].append(element)
    # todo -- wrzucić odpowiednio hash `h` do bag
    # 1) sprawdzić czy już jest w bag-u; jeśli tak to return
    # 2) jeśli nie jest, to sprawdzić indeks listy do której trzeba wrzucić element, np. `idx`, i potem wrzucić
    # ten element do bag[idx]
    #


def contains_element(bag: list[list], element: int) -> bool:
    M = len(bag)  # tyle mamy list w `bag`; każda ma ileś... elementów...
    h = element.__hash__()
    idx = h % M
    return bag[idx].__contains__(element)
    # todo: sprawdzić czy `x` z hashem `h` jest w `bag`
    # odpowiednio zawężony (do [0...M-1] hash ma być numerem listy)
    # wyliczyć "indeks listy" z hasha,
    # sprawdzić czy bag[idx] zawiera `element`


def remove_element(bag: list[list], element: int):
    if not contains_element(bag, element):
        return
    M = len(bag)  # tyle mamy list w `bag`; każda ma ileś... elementów...
    h = element.__hash__()
    idx = h % M
    bag[idx].remove(element)

    # todo: usunąć `x` z hashem `h` z `bag`
    # wyliczyć "indeks listy" z hasha,
    # usunąć z listy bag[idx] element `element`



def get_all_elems(bag: list[list]) -> list:
    res = []
    for list_ in bag:
        res.extend(list_)
    return res

if __name__ == '__main__':
    bag = get_new_bag(1000)  # np. bag[0] jest listą... i bag[999]...
    insert_element(bag, 's')
    insert_element(bag, 17)
    insert_element(bag, 32)

    print(contains_element(bag, 17), True)
    print(contains_element(bag, 18), False)
    remove_element(bag, 32)
    print(contains_element(bag, 32), False)
    remove_element(bag, 17)
    print(contains_element(bag, 17), False)
