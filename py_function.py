print("#################################################################")
##函数

#求绝对值
print(abs(100)) #100
print(abs(-100)) #100

#求最大值
print(max(1,2)) #2
print(max(2, 3, 1, -5)) #3

#数据类型转换
print(int('123')) #123

print(float('12.34')) #12.34

print(str(1.23)) #'1.23'

print(str(100)) #'100'

print(bool(1)) #True

print(bool('')) #False

#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”

a = abs
print(a(-1)) #1


n1 = 255
n2 = 1000

print(hex(255))

print("#################################################################")
##定义函数

#自定义一个求绝对值函数
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

my_abs(-123)
#函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回


#空函数
def nop():
    pass

#参数检查
#调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError
    #但是如果参数类型不对，Python解释器就无法帮我们检查

#返回多个值
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x,y)

r = move(100, 100, 60, math.pi / 6)
print(r)


#练习
#定义一个求一元二次方程的解的函数

def quadratic(a, b, c):
    x1 = (-b + math.sqrt(b*b - 4*a*c)) / (2*a)
    x2 = (-b - math.sqrt(b*b - 4*a*c)) / (2*a)
    return x1,x2

# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')