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