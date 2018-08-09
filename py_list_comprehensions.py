# ###List Comprehensions

print(list(range(1,11)))

L = []
for i in range(1, 11):
  L.append(i * i)

print(L)

# OR
newL = [ x * x for x in range(1, 11) if x % 2 == 0]
print(newL)

S = [m + n for m in 'ABC' for n in 'DEF']
print(S)

import os # 导入os模块
fileName = [d for d in os.listdir('.')] # os.listdir可以列出文件和目录
print(fileName)


# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value
D = {'x': 'A', 'y': 'B', 'z': 'C'}
for key, value in D.items():
  print(key, ': ', value)

# 因此，列表生成式也可以使用两个变量来生成list

dl = [key+ ': '+ value for key, value in D.items()]
print(dl)

sl = ['Hello', 'World', 'IBM', 'Apple']
sll = [s.lower() for s in sl]
print(sll)

# -*- coding: utf-8 -*-
# Task

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [l.lower() for l in L1 if isinstance(l,str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')