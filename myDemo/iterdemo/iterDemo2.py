# Python3 迭代器与生成器

# 迭代是Python最强大的功能之一，是访问集合元素的一种方式。
#
# 迭代器是一个可以记住遍历的位置的对象。
#
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
#
# 迭代器有两个基本的方法：iter() 和 next()。
#
# 字符串，列表或元组对象都可用于创建迭代器：

# import sys

# listSelf = [1, 2, 3, 4]
# iterSelf = iter(listSelf)
#
# for iterItem in iterSelf:
#     print(iterItem, end=" ")
# print(" ")
#
# listSelf2 = [1, 2, 3, 4]
# iterSelf2 = iter(listSelf2)
# while True:
#     try:
#         print(next(iterSelf2))
#     except StopIteration:
#         sys.exit()
# print("")

import time


def iter_base():
    city = ['beijing', 'shanghai', 'tinajin', 'chongqin']
    it = iter(city)
    print(type(it))

    print(it.__next__())
    print(it.__next__())

    print('\n')

    for x in it:
        print(x)


# 用生成器函数完成与counter类似功能
def generator(low, high):
    while low <= high:
        yield low
        low += 1


# 生成器产生无限多的值
def generator2(start=0):
    while True:
        yield start
        start += 1


# 列表生成器
def generator_list(low, high):
    a = [i * 2 for i in range(low, high)]
    return a


# 简单装饰器
def timer(func):
    def wrapper():
        start_time = time.time()
        func()
        stop_time = time.time()

        print("run time %s" % (stop_time - start_time))

    return wrapper
