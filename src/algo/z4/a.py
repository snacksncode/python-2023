# export PYTHONPATH=~/PycharmProjects/python1-2022
from src.algo.z4.libs.f import foo
# from libs.f import foo

print(__file__)
print('-------------')
with open('kadabra.txt') as f:
    print(f.readlines())
print('-------------')

print('uruchamiam funkcje')
print(foo(10))
