#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# name = input('please enter your name: ')
# print('hello,',name)

print("1024 * 768 = ",1024*768)

# 4个空格为一个缩进,确保不要混用tab和空格
# 当语句以:号结尾时,缩进的语句视为代码块


print('''line1
line2
line3''')


# 与或非对应 and or not None是一个特殊的空值
age = 17

if age >= 18:
    print('adult')
else:
    print('teenager')
a = 'ABC'
b = a
a = 'XYZ'
print(b,a)

# 用/除法计算结果是浮点数,即使两个整数恰好整除,结果也是浮点数
print(9 / 3) #3.0

# //是地板除,两个整数的除法仍然是整数
10//3 #3

# % 取余

##字符串和编码

#测试中文输出
print("中文测试正常")

#格式化
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
print('growth rate: %d%%' % 7)


s1 = 72
s2 = 85

r = (s1 / s2) * 100
print('%.1f%%' % r)

##使用list和tuple

#list
#定义一个list
classmates = ['Michael', 'Bob', 'Tracy']

#过去list元素个数
len(classmates)

#用索引访问list中每个位置的元素,从0开始
print(classmates[0]) #list中第一个元素 classmates[-1]指的是其中最后一个元素,以此类推

#往list中追加元素到末尾
classmates.append('Adam')

#把元素插入到指定的位置
classmates.insert(1, 'Jack')

#删除list末尾的元素
classmates.pop()

#删除指定位置的元素，用pop(i)方法，其中i是索引位置
classmates.pop(1)

#把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1] = 'Sarah'


##条件判断
# if <条件判断1>:
#     <执行1>
# elif <条件判断2>:
#     <执行2>
# elif <条件判断3>:
#     <执行3>
# else:
#     <执行4>
#if语句的完整形式

#if从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else

age = 3
print("your age is", age)

if age >= 18:
    print("adult")
elif age >= 6:
    print('teenager')
else:
    print("kid")


#input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。Python提供了int()函数来完成这件事情
# s = input('birth: ')
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')

height = 1.75
weight = 80.5

bmi = weight / (height*height)

print(bmi)

if bmi > 32:
    print("严重肥胖")
elif bmi >= 28:
    print("肥胖")
elif bmi >= 25:
    print("过重")
elif bmi >= 18.5:
    print("正常")
else:
    print("过轻")

##循环

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

#Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)


sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

L = ['Bart', 'Lisa', 'Adam']

for name in L:
    print("hello, "+name + "!")

#break的作用是提前结束循环
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

#continue的作用是提前结束本轮循环，并直接开始下一轮循环
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)


##使用dict和set
#dict
#要删除一个key，用pop(key)方法，对应的value也会从dict中删除

#!!!dict内部存放的顺序和key放入的顺序是没有关系的

# 和list比较，dict有以下几个特点：
    # 查找和插入的速度极快，不会随着key的增加而变慢；
    # 需要占用大量的内存，内存浪费多。

# 而list相反：
    # 查找和插入的时间随着元素的增加而增加；
    # 占用空间小，浪费内存很少。

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

#set
#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
#要创建一个set，需要提供一个list作为输入集合
s = set([1, 2, 3])
print(s)

#通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果

#通过remove(key)方法可以删除元素

