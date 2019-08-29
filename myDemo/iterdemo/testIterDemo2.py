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

from iterDemo2 import iter_base, generator, generator2, generator_list, timer
import time


@timer
def test():
    print("in the test")
    time.sleep(1)


if __name__ == '__main__':
    # 迭代器使用举例
    iter_base()
    print('\n')

    # 用生成器函数完成与counter类似功能
    for i in generator(1, 10):
        print(i, end=' ')
    print('\n')

    # 用生成器函数完成与counter类似功能
    for number in generator2(4):
        print(number, end=' ')
        if number > 20:
            break
    print('\n')

    # 列表生成器
    print(generator_list(1, 10))
    print('\n')

    # 简单装饰器
    test()
