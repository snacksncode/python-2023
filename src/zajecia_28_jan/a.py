a = []
a.append("aa")
a.append("bb")
a.append("zz")

w = ["x", "y", "z"]
a.extend(w)
print(a)

f = ["abra", "kadabra", "hokus", "pokus"]
print("-".join(f))

# zadanie -- wyliczyć ile ma być znaków '*' w rzędzie o nr. "x"
# (dla x=0 ma być 1)
# 1, 3, 5, 7 ....... 1 + x * 2
#
# każdy rzad ma 1 + 2 * N elementow
#
#
#
#
# treeee = []
# N = 5
# for x in range(N):
#     green_leaves = 1 + x * 2
#     leaves = ['*'] * green_leaves
#     # print(leaves)
#     total = 1 + 2 * N
#     air_elements = total - green_leaves
#     air_left = ['.'] * (air_elements // 2)
#     air_righ = ['.'] * (air_elements // 2)
#     line = air_left + leaves + air_righ
#     s = ''.join(line)
#     print(s)
