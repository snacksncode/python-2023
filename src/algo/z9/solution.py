"""
Zadanie: mamy daną tablicę liczb całkowitych "a"; chcemy potencjalnie stworzyć inną tablicę
tej samej długości, "b", gdzie
b[i] = a[i] lub a[i] - a[j],
przy czym "j" może być inne dla każdego "i".

Chcemy by ostatecznie wszystkie elementy tablicy "b" miały tą samą parzystość... czyli by były wszystkie
parzyste, lub wszystkie nieparzyste. Dodatkowo wszystkie liczby tablicy "a" i "b" mają być > 0.

Przykład:

a = [1, 5, 6]
można wykorzystać do budowy
b = [1, 5, 5]  (wszystkie są nieparzyste, przy czym a[0]=b[0], a[1]=b[1], b[2] = a[2] - a[0])
lub
b = [1, 5, 1]  (teraz na ostatniej pozycji odjęliśmy 5, czyli a[1])

"""


def equalize_parity(a: list[int]) -> bool:
    a.sort()
    parity_list = []

    for i in range(len(a)):

        if a[i] % 2 == 0:
            parity_list.append(a[i])
        
    if len(parity_list) == len(a) or a[0] % 2 !=0:
        return True
    else:
        return False
    
