users = ["A", "B", "C"]
scores = [10, 80, 4]

"""
postortować userów wg. scores ... 
"""

# data = []
# for i in range(len(users)):
#     data.append((scores[i], users[i]))
data = [(s, u) for (s, u) in zip(scores, users)]
print(data)

data.sort()
print(data)
uu = [g[1] for g in data]
print(uu)

# -----
# d = dict()
# for (s, u) in zip(scores, users):
#     d[u] = s
# print(d)
