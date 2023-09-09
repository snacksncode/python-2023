w = 10
print(w % 3)
z = -1
print(z % 3)

print(w.__hash__())
print(z.__hash__())

# po co "hashset" (czyli set w pythonie) ....
"""
- szybkie "insert / add"
- szybkie sprawdzenie .contains
- szybki delete
- usuwanie duplikatów
- elementy dowolnej wielkości (**) 
"""

bag = [0] * 1000  # tu będą tylko 0 i 1  (ale możemy wrzucać tylko elementy 0...999)

# wrzucamy 11, 27

bag[11] = 1
bag[27] = 1

# sprawdzenie czy 11 ?
print(bag[11] == 1)

ff = [1, 2, 3]
print(ff.__contains__(2))

"""
- ustawiamy "data space", czyli "bag = [0] * 1000"; 
- instert `x` bag[x] = 1
- remove `x` bag[x] = 0
- contains `x`: bag[x] == 1

------
bag = [[] for _ in range(10000)]
wyliczamy "hash" który dla danego x'a jest liczbą z przedziału [0,9999]
- contains `x`: bag[hash(x)].__contains__(x)
- remove `x`: bag[hash(x)].remove(x)
- insert: jeśli x nie jest w bag[hash(x)]: wykonujemy bag[hash(x)].append[x]
"""

print('-' * 10)
s = 'kadabra'  # -2059231447356545660
print(s.__hash__())
t = (1, 2, 3)  # 529344067295497451
print(t.__hash__())
tt = ('abra', 'kadabra')
print(tt.__hash__())  # 8076849099501633122



print(tt.__hash__() % 10)



pesel = 1234
imie = 'Jan'
nazwisko = 'Nowak'


h = (pesel, imie, nazwisko).__hash__()
print(h)
