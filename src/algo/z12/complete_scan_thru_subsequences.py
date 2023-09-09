

"""
przedmioty

values = [2, 7, 1, 6]
costs =  [5, 2, 2, 1]

----
ograniczenie:
sum(chosen_items) <= 4


Q: Jak sprawdzić wszystkie możliwości...

Hint: Wszystkie liczby [0,7] w reprezentacji binarnej:

0b000
0b001
0b010
0b011
0b100
0b101
0b110
0b111


"""

def get_bin_representation(x: int, n: int) -> str:
    return bin(x)[2:].zfill(n)

if __name__ == '__main__':
    N = 4
    for mask in range(2 ** N):
        # sprawdzić jaki jest koszt wybranych przedmiotów dla danej wartości `mask`
        # bierzemy przedmiot 0 jeśli mask[0] = 1
        # nie bierzemy go jeśli mask[0] = 1
        maska = get_bin_representation(mask, N)
        print(maska)
        for item_position in range(N):
            print(f'item # {item_position}: {"bierzemy" if maska[item_position]=="1" else "nie bierzemy"}')



