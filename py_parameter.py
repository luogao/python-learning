##函数的参数

#位置参数

def power(x,n=2): #默认为计算平方
    s = 1
    while n>0:
        n = n-1
        s = s * x
    return s

print(power(3,3))
print(power(5))

### 定义默认参数要牢记一点：默认参数必须指向不变对象！

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end())


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1, 2, 3))

nums = [1, 2, 3]
print(calc(*nums))

##*nums表示把nums这个list的所有元素作为可变参数传进去

