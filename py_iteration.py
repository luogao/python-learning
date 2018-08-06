## Iteration

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
  print(key)

print()

for value in d.values():
  print(value)

for ch in 'ABC':
  print(ch)

# 判断是否是一个可迭代对象
from collections import Iterable 

print(isinstance('abc', Iterable))

print(isinstance(123, Iterable)) # 整数不可迭代

# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身

for i in enumerate(['A', 'B', 'C']):
  print(i)

for i in [1,2,3,4,5]:
  print(i)

for x, y, z in [(1, 2, 3), (4, 5, 6), (7, 8, 9)]:
  print(x, y, z)


# Task
def findMinAndMax(L):
  if L != []:
    max = L[0]
    min = L[0]
    for n in L:
      if max < n:
        max = n
      if min > n:
        min = n
    return (min, max)
  else:
    return (None, None)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')