# const
dt = 0.001
a = 10

# vars
s = 0
v = 0
t = 0

# a == acceleration
# t = time
# v = velocity
# s = distance

#  s = a * t ** 2 / 2
#  v = a * t
#


# symulacja
while t < 10:
    s += v * dt
    v += a * dt
    t += dt

print(s)
print(a * t ** 2 / 2)
