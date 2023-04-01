"""
zadanie2:
 Mając dany "rozkład jazdy" (z pliku gen_train_data.py), napisać funkcję która sprawdzi czy można dojechać
 z miasta "a" do miasta "b" (bez przesiadek).

"""

from zadanie_a import extract_destination_info


def is_connected(train_data: list[tuple[int, int]], a: int, b: int) -> bool:
    destinations = extract_destination_info(train_data)
    return b in destinations[a]


if __name__ == '__main__':
    data = [(1, 2), (2, 3)]
    print(is_connected(data, 2, 3))
