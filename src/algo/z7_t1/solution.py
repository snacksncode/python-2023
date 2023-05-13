
"""
****     #
*     ####
*       ##
***     ##
*     ####
**     ###

jeśli długości *'ek klucza + długości #'ów zamka są dla wszystkich takie same, to klucz otwiera zamek
"""


from utils_t1 import list_contains_only_ints, list_contains_negative_ints


def open_lock(key: list[int], lock: list[int]) -> int:
    """
    :param key:   np. [4,1,1,3,1,2]
    :param lock:  np  [1,4,2,2,4,3]
    :return:    -1 jeśli wartości są "invalid" (np. <0); 0 jeśli klucz otwiera zamek, 1 jeśli klucz nie otwiera zamka
    """
    INVALID_INPUT = -1
    VALID_KEY = 0
    INVALID_KEY = 1

    if not isinstance(key, list) or not isinstance(lock, list):
        return INVALID_INPUT

    if len(key) == 0 or len(lock) == 0:
        return INVALID_INPUT

    if len(key) != len(lock):
        return INVALID_INPUT

    if not list_contains_only_ints(key) or not list_contains_only_ints(lock):
        return INVALID_INPUT

    if list_contains_negative_ints(key) or list_contains_negative_ints(lock):
        return INVALID_INPUT

    key_value = key[0] + lock[0]
    for (key_num, lock_num) in zip(key, lock):
        if key_num + lock_num != key_value:
            return INVALID_KEY

    return VALID_KEY
