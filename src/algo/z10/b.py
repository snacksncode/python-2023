import string
from random import choice

s = string.ascii_lowercase  # małe literki
# .choice wybiera losowy element z listy
# 'x'.join(collection) tworzy 'axbxcxd' jeśli collection = [a,b,c,d]  (zamiast 'x' można dać dowolny, nawet pusty str)

print(''.join(choice(s) for _ in range(10)))

g = 'abcd'
print(g.replace('b', '.'))  # a.cd ; zamiast '.' można dać dowolny nwet pusty string


