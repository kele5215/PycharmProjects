"""
python内置函数

https://www.cnblogs.com/derek1184405959/p/8065488.html

git命令汇总
https://www.cnblogs.com/derek1184405959/p/8691714.html

"""


# 普通参数
def func(name):  # name是形式参数
    print(name)  # 函数体


func('derek')  # 执行函数，'derek'是传入的实参
print('\n')


# 默认参数
def info(name, age, country='CN'):  # country定义了一个默认参数
    print('姓名:', name)
    print('年龄:', age)
    print('国籍：', country)


info('derek', 22)  # 调用时，没穿实参countrty，就用默认的参数
print('\n')


# 关键参数
def info(name, age, country='CN'):
    print('姓名:', name)
    print('年龄:', age)
    print('国籍：', country)


info(age=22, name='derek')  # 使用关键参数，可以不按顺序
print('\n')


# *args
def info(name, age, *args):  # *args会把多传入的参数变成一个元祖形式
    print(name, age, args)


info("derek", "22", "CN", "Python")  # derek 22 ('CN', 'Python')
print('\n')


# **kwargs
def info(name, *args, **kwargs):  # **kwargs 会把多传入的参数变成一个dict形式
    print(name, args)  # derek (22, 'CN', 'Python')
    print(kwargs)  # {'sex': 'Male', 'province': 'HeBei'}


info("derek", 22, "CN", "Python", sex="Male", province="HeBei")
print('\n')

# 局部变量
name = 'derek1'


def change_name(name):
    print('before change:', name)
    name = 'derek2'
    print('after change:', name)


change_name(name)
print('最后还是没改', name)
print('\n')


# #递归实现阶乘n! = (n-1)! × n
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
print('\n')
"""
满足下列条件之一就可称函数为高阶函数

某一函数当做参数传入另一个函数中

函数的返回值包含一个或多个函数
"""


# 简单的高阶函数
def func():
    print('in the func')
    return foo()


def foo():
    print('in the foo()')
    return 666


res = func()
print(res)
print('\n')


# map()是 Python 内置的高阶函数，
# 它接收一个函数 f 和一个list，
# 并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回
def func(x):
    return x * x


a = map(func, range(1, 10))
print(list(a))
print('\n')

# reduce()函数也是Python内置的一个高阶函数。
# reduce()函数接收的参数和 map()类似，一个函数 f，一个list，
# 但行为和 map()不同，reduce()传入的函数 f 必须接收两个参数，
# reduce()对list的每个元素反复调用函数f，并返回最终结果值
from functools import reduce


def f(x, y):
    return x + y


a = reduce(f, [1, 3, 5, 7, 9, 10, 11])
print(a)
print('\n')


# filter()函数是 Python 内置的另一个有用的高阶函数，
# filter()函数接收一个函数 f 和一个list，
# 这个函数 f 的作用是对每个元素进行判断，返回 True或 False，
# filter()根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list
def is_odd(x):
    return x % 2 == 1


a = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8])
print(list(a))
print('\n')

# lambda 函数是一种快速定义单行的最小函数，可以用在任何需要函数的地方
a = lambda x, y: x + y
print(a(2, 3))
print('\n')

# 局部作用域和全局作用域的访问顺序
x = 0


def grandpa():
    x = 1
    print("grandpa: ", x)

    def dad():
        x = 2
        print("dad ", x)

        def son():
            x = 3
            print("son ", x)

        son()

    dad()


grandpa()
print(x)
