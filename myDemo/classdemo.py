class MyClass:
    i = 12345

    def f(self):
        return "Hello world"


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


class Test:
    def prt(self):
        print(self)
        print(self.__class__)


class People:
    name = ""
    age = 0
    __weight = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("{0:10} shuo : wo {1:2d}".format(self.name, self.age))


class Student(People):
    grade = ""

    def __init__(self, n, a, w, g):
        People.__init__(self, n, a, w)
        self.grade = g

    def speak(self):
        print("{0:10} shuo: wo {1:2d} sui le , wo zai du {2:2d}nianjia".
              format(self.name, self.age, self.grade))


class Speaker:
    topic = ""
    name = ""

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


# 多重继承
class Sample(Speaker, Student):
    a = ''

    def __init__(self, n, a, w, g, t):
        Student.__init__(self, n, a, w, g)
        Speaker.__init__(self, n, t)


class Parent:
    def mymethod(self):
        print("我是爹！")


class Child(Parent):
    def mymethod(self):
        print("我市儿子！")


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "Vector ({0:d} {1:d})".format(self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)
