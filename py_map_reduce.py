# map reduce


def f(x):
    return x * x


L = [1, 2, 3, 4, 5, 6, 7, 8]
r = list(map(f, L))
print(L)
print(r)

s = list(map(str, L))
print(s)

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算

from functools import reduce


def add(x, y):
    return x + y


print(reduce(add, [1, 2, 3, 4, 5, 6]))


def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9]))

