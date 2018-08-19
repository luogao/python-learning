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

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

print(reduce(fn, map(char2num, '13579')))

digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2num(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return digits[s]
    return reduce(fn, map(char2num,s))

print(str2num('2'))


# -*- coding: utf-8 -*-
# Task
def normalize(name):
    ret = name.capitalize()
    return ret

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def prod(L):
    def fn(x,y):
        return x * y
    return reduce(fn,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

def str2float(s):
    def fn(x,y):
        return x*10+y
    n=s.index('.')
    s1=list(map(int,[x for x in s[:n]]))
    s2=list(map(int,[x for x in s[n+1:]]))
    return reduce(fn,s1) + reduce(fn,s2)/10**len(s2)

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')


# 解析： 
# 这个答案非原创，也是某位前辈写的。 
# 1行，从 functools 包里调用 reduce 
# 3-4行，定义一个 fn() 函数，用来把S1，S2这两个list里面的元素变成一个数。 
# 5行，很关键的一步，利用 index() 函数确定字符串 S 中 ‘.’的位置。 
# 6-7行，先利用切片把我们传入的 str 分成以前以后两个部分（其实就是根据小数点分成整数和浮点数，分别处理），然后再把切割好的 str 利用 int 变成整数，map() 函数负责把 int 作用到截取的 str 的每个元素中去。 
# 8行，就说一个知识点，其他的都很好理解，m**n 这个表达的就是 m 的 n 次方。