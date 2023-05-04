from dataclasses import dataclass


@dataclass
class AA:
    i: int
    name: str


# instancje
a = AA(5, 'kadabra')
b = AA(6, 'karramba')


print(a)
print(b)
print(b.name)
