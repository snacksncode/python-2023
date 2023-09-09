from zad_a import *
w = [90, 72, 1, 5, 8, 10, 12]

for x in w:
    print(f'{x=} hash={x.__hash__()}')

print('---------')
bag = get_new_bag(100)
for x in w:
    insert_element(bag, x)

print(get_all_elems(bag))


zz = 3.1415
print(zz.__hash__())