
"""
****     #
*     ####
*       ##
***     ##
*     ####
**     ###

jeśli długości *'ek klucza + długości #'ów zamka są dla wszystkich takie same, to klucz otwiera zamek


"""



def open_lock(key: list[int], lock: list[int]) -> int:

    if len(key) != len(lock):
        return -1

    try:
        x = key[0]+lock[0]
    except IndexError:
        return -1
    for i in range(len(key)):
        if key[i] < 0 or lock[i] < 0:
            return -1
            break
        elif key[i] >= 0 and lock[i] >= 0:
            for j in range(len(key)):
                if key[j]+lock[j] != x:
                    return 1
                    break
        return 0

    """
    :param key:   np. [4,1,1,3,1,2]
    :param lock:  np  [1,4,2,2,4,3]
    :return:    -1 jeśli wartości są "invalid" (np. <0); 0 jeśli klucz otwiera zamek, 1 jeśli klucz nie otwiera zamka
    """
# result = open_lock(key, lock)
# print(result)