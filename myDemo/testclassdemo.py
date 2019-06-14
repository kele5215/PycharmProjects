from classdemo import MyClass
from classdemo import Complex
from classdemo import Test
from classdemo import People
from classdemo import Student
from classdemo import Sample
from classdemo import Parent, Child
from classdemo import Vector
import random

from urllib.request import urlopen

x = MyClass()

print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())

x = Complex(3.0, -4.5)
print(x.r, x.i)  # 输出结果：3.0 -4.5

t = Test()
t.prt()

# 实例化类
p = People('runoob', 3, 30)
p.speak()

# 实例化类
s = Student('ken', 10, 60, 3)
s.speak()

test = Sample("Tim", 25, 80, 4, "Python")
test.speak()  # 方法名同，默认调用的是在括号中排前地父类的方法

c = Child()
c.mymethod()
super(Child, c).mymethod()

v1 = Vector(2, 10)
v2 = Vector(5, 3)
print(v1 + v2)


# for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
#     line = line.decode("utf-8")
#     if "EST" in line or "EDT" in line:
#         print(line)


def lot6random():
    list_lot6 = [(random.sample(range(1, 43), 1))[0]]
    while True:
        int_random = random.sample(range(1, 43), 1)
        if int_random[0] not in list_lot6:
            list_lot6.append(int_random[0])
        if len(list_lot6) == 6:
            break

    list_lot6.sort()
    # print(list_lot6)
    return list_lot6


list_lot6_10 = []
for i in range(10):
    list_lot6_10.append(lot6random())

print("今天的幸运号码组合是:")
for i in range(len(list_lot6_10)):
    print("第{0:2d}组: ".format(i+1), list_lot6_10[i])
print("")
luckyindex = random.randrange(10)
print("上天帮我选中的幸运号码组合是:\n第{0}组 {1}".format(
    luckyindex + 1, list_lot6_10[luckyindex]))
