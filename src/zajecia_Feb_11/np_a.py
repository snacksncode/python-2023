import numpy as np

a = [[1, 2, 3], [3, 4, 5]]
print(type(a))  # <class 'list'>
np_a = np.array(a)
print(type(np_a))  # <class 'numpy.ndarray'>

print(np_a.shape)  # (2, 3)
print(np_a)
"""
[[1 2 3]
 [3 4 5]]
 """

gg = np_a * 2
print(gg)

maska = np_a > 3
print(maska)
"""
[[False False False]
 [False  True  True]]
 """
gg_masked = gg * maska
print(gg_masked)
print("-" * 10)
a = np.array([[0, 1], [1, 0]])
b = np.array([[1, 2], [3, 4]])
print(a)
print(b)
print(a.dot(b))


print(np.linalg.det(a))
