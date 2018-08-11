# 函数式编程-高阶函数

# 函数本身也可以赋值给变量，即：变量可以指向函数

a = abs(-10)
print(a)
print(abs)
f = abs
print(f)

def add(x, y, f):
  return f(x) + f(y)

print(add(5,-6,abs))

# 把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。