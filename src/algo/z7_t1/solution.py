
"""
Słowa sklejamy z sylab w następujący sposób:

słowo:

"abac"

... trzeba złożyć z 2-literowych "sylab"
ab←→ba -> aba
aba←→ac -> abac

(czyli dołączana sylaba 2-literowa ma mieć taką pierwszą literę, jak ostatnia litera słowa do którego jest dołączana)

"""


def split_to_syllables(word: str) -> list[str]:
    new_word = []
    for i in range(len(word)-1):
        s = word[i] + word[i+1]
        new_word.append(s)
    return new_word

word = "abba"
result = split_to_syllables(word)
print(result)







