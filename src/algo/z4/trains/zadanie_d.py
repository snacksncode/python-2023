"""
zadanie4(*):
 Mając dany "rozkład jazdy" (z pliku gen_train_data.py), napisać funkcję która znajdzie najdłuższą możliwą
 trasę (z przesiadkami), w której nie jedziemy przez żadne z miast więcej niż raz.

"""
from random import seed

from gen_train_data import generate_data
from zadanie_a import extract_destination_info, print_destinations


def find_longest_trip(train_data: list[tuple[int, int]]) -> bool:
    pass


def random_travel(at: int, destinations: list[list[int]]):
    MAX_STEPS = 10
    # jesteśmy na "at"
    for i in range(MAX_STEPS):
        next_at = 0  # ... wybrać z możliwych destinations[at]
        # print...
        # at = next_at


if __name__ == '__main__':
    seed(107)
    # train_data = [(1, 2), (2, 4), (4, 3), (3, 1), (3, 5), (5, 1), (4, 5)]
    # train_data = [(1, 2), (2, 4), (4, 3), (3, 1)]
    train_data = generate_data(25)

    destinations = extract_destination_info(train_data)
    print_destinations(destinations)
