import json

s = set()

s.add(3)
s.add(5)
s.add(7)
s.add(5)

print(s)
print(5 in s)  # O(1) -- "szybkie"

# złożoność obliczeniowa....

w = [1]
w.append(5)  # O(1)
w = [0] + w  # O(N) --- "wolne"
print(w)

w.sort()  # N log N   (log o podstawie 2)

# --------------------

w = [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
]  # 7600 x 4300
w[3] = 1
print(w)

# g = [0] * (10**7) #10 mln int-ów == 87MB
# g = [0] * (10**8) #100 mln int-ów == 770MB; 7.7B/element

# input()

gg = dict()
gg[1] = 1
gg[17] = 1
gg[19] = 2
print(gg)
print(17 in gg)
# w[0] =


del gg[17]

gg["kadabra"] = 19
# gg[(1,2)] = 99
# gg[(1,2)] += 1

print(gg)
s = json.dumps(gg)
print(s)
print(type(s))  # serializacja

with open("../zajecia_7_jan/dane.txt", "w") as f:
    f.write(s)

with open("../zajecia_7_jan/dane.txt", "r") as ff:
    # lines = ff.readlines()
    # for line in lines:
    #     print(line)
    sss = ff.read()
print("----> ", sss)

d = json.loads(sss)
print(d)
print(type(d))  # deserializacja

for k, v in d.items():
    print(f"key={k} value={v}")
