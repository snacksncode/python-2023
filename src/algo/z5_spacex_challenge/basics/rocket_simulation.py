# const
dt = 0.0001
g = 10
MAX_THRUST = 20

# vars
h = 0
v = 0
t = 0
thrust = MAX_THRUST * 0.9999
mass = 1

# a == acceleration
# g = earth's gravity
# t = time
# v = velocity
# h = height

#  s = a * t ** 2 / 2
#  v = a * t
#


# symulacja
i = 0
while t < 2000:
    if mass > 0.5:
        acceleration = thrust / mass - g
        mass -= thrust * 0.01 * dt
    else:
        acceleration = -g
    h += v * dt
    v += acceleration * dt
    t += dt
    if i % 100 == 0:
        print(f'{t=:.3f},\t{h=:.3f},\t{v=:.3f},\t{mass=:.3f}')
    i += 1
    if h > 10 and v < 0:
        break
