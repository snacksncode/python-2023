"""
zadanie1:
 Mając dany "rozkład jazdy (z pliku gen_train_data.py), wyświetlić miasto z którego jest najwięcej 
 połączeń wychodzących.

"""
from get_train_data import generate_data


def get_city_most_connections(train_data: list[tuple[int, int]]) -> int:
    hash_map = dict()
    connections = [city[1] for city in train_data]

    for connection in connections:
        hash_map[connection] = hash_map.get(connection, 0) + 1

    max = float('-inf')
    city = None
    for entry in hash_map.items():
        if entry[1] > max:
            max = entry[1]
            city = entry[0]

    return city


train_data = generate_data(10)
print('Train data', train_data)
max = get_city_most_connections(train_data)
print('Max connections to:', max)
