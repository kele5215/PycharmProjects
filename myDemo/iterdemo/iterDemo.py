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
import support
import fibonacciFunc
# import filedemo


class MyNumbers:
    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        if self.b <= 100:
            x = self.b
            self.a = self.b
            self.b = self.a + self.b
            return x
        else:
            raise StopIteration


myNumClass = MyNumbers()
myIter = iter(myNumClass)

for item in myIter:
    print(item)
print("")


def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(13)  # f 是一个迭代器，由生成器返回生成

# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()

print("")


def changeMe(myList):
    mylist.append([1, 2, 3, 4, 5])
    print(mylist)
    return


mylist = [10, 20, 30]
changeMe(mylist)
print(mylist)


def printInfo(name, age):
    print("my name: ", name)
    print("my age: ", age)


printInfo(age=50, name="chunlei")
print("")


def printinfo(arg1, *vartupleself):
    print("shu chu: ")
    print(arg1)
    # print(vartupleself)
    for var in vartupleself:
        print("self: ", var)


# 调用printinfo 函数
printinfo(10)
printinfo(70, 60, 50)


def printinfo(arg1, **vardictself):
    print("输出: ")
    print(arg1)
    print(vardictself)


printinfo(1, a=2, b=3)

sum = lambda arg1, arg2: arg1 * arg2
print(sum(15, 15))


# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2
    print("函数内 : ", total)
    return total


# 调用sum函数
total2 = sum(10, 20)
print("函数外 : ", total2)

support.print_func("Runoob")

fibonacciFunc.fib(100)
fList = fibonacciFunc.fib2(100)
print(fList)
print(fibonacciFunc.__name__)

if __name__ == '__main__':
    print('程序自身在运行')
else:
    print('我来自另一模块')

print(dir(fibonacciFunc))
print(dir())
