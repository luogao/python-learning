#### Slice 切片

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3]) # ['Michael', 'Sarah', 'Tracy']

newL = L[1:2]
print(newL) # ['Sarah']

reverseL = L[-2:]
print(reverseL) # ['Bob', 'Jack']

L1 = list(range(100))
print(L1[:10]) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(L1[-10:])) # 10

print()

print(L1[::5]) # [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

print(L1[:10:2]) # [0, 2, 4, 6, 8]

# copyL1 = L1[:]
# print(copyL1)

T = (0, 1, 2, 3, 4, 5)
print(T[:3])

S = 'ABCDEFG'
print(S[0:-1])

# TASK

def trim(s):
  if (s[:1] == ' '):
    return trim(s[1:])
  if (s[-1:] == ' '):
    return trim(s[:-1])
  return s
  

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')