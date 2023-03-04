from math import sqrt

w = [1, 2, 3, 4, 5]

# stworzyć listę trzecich potęg liczb w `w`


u = []
for x in w:
    u.append(x**3)
print(u)

z = [x**3 for x in w]  # comprehension

print(z)

# .. trzecich poteg, ale tylko liczb > 2

z = [x**3 for x in w if x > 2]
print(z)

print("7" in str(747))

g = [0, 1] * 10

print(g)
