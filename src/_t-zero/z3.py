def swap_case(s: str):
    # res = s.swapcase()    #ha ha ha ..., but if we insist... lets play ord/chr
    res = ""

    for let in s:
        if ord("a") <= ord(let) <= ord("z"):
            res += chr(ord(let) + ord("A") - ord("a"))
        else:
            res += chr(ord(let) + ord("a") - ord("A"))
    return res


print(swap_case("aA"))
