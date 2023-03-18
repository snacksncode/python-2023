"""
mamy dane dwie listy liczb tej samej wielkości, np. a = [2,5,7,9], b=[4,8,18,27]
dla każdej liczby z tablicy "a" sprawdzić ile jest takich liczb z tablicy "b" które się przez nią dzielą;
zwrócić te krotności jako listę czyli tutaj -- wynik = [3,0,0,2]
🇦 Napisać funkcję rozwiązującą ten ↑↑ problem

"""


def check_numbers(a: list[int], b: list[int]) -> list[int]:
    res = []
    for i in range(len(a)):
        counter = 0
        for j in range(len(b)):
            if b[j] % a[i] == 0:
                counter += 1
        res.append(counter)
    return res


a = [2, 5, 7, 9]
b = [4, 8, 18, 27]

print(check_numbers(a, b))
