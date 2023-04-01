"""
zadanie3:
 Mając dany "rozkład jazdy" (z pliku gen_train_data.py), napisać funkcję która sprawdzi czy można dojechać
 z miasta "a" do miasta "b" z dokładnie jedną przesiadką, czyli czy istnieje para połączeń typu (a,c),(c,b).

"""
from zadanie_a import extract_destination_info, print_destinations


def is_connected_with_stopover(train_data: list[tuple[int, int]], a: int, b: int) -> bool:
    destinations = extract_destination_info(train_data)
    # print_destinations(destinations)

    # if a ---> (some c) --> b
    for c in destinations[a]:
        if b in destinations[c]:
            return True
    return False


if __name__ == '__main__':
    data = [(1, 2), (2, 3)]
    print(is_connected_with_stopover(data, 1, 3))
