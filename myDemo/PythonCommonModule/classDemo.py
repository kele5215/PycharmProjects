# _*_ coding:UTF8 _*_


class Car(object):
    def __init__(self, type, price):
        self.type = type
        self.price = price

    def carInfo(self):
        print("type:%s,price:%d" % (self.type, self.price))


tesla = Car('tesla', 20000)
jeep = Car('jeep', 200)

tesla.carInfo()
jeep.carInfo()


# 对象之间的交互
class Garen:
    camp = 'Demacia'

    def __init__(self, name, aggressivity=58, life_value=455):  # 初始攻击力和生命值
        self.name = name
        self.aggressivity = aggressivity
        self.life_value = life_value

    def attack(self, enemy):  # 普通攻击技能，攻击敌人
        enemy.life_value -= self.aggressivity  # 根据攻击力，减掉敌人生命值


# 组合的方式
class Equip():
    def file(self):
        print('release fire skill')


class Riven:
    camp = 'Noxus'

    def __init__(self, name, aggressivity=54, life_value=4514):
        self.name = name
        self.aggressivity = aggressivity
        self.life_value = life_value
        self.equip = Equip()  # 用Equip类产生一个装备,赋值给实例的equip属性

    def attack(self, enemy):
        enemy.life_value -= self.aggressivity


g1 = Garen('盖伦')
r1 = Riven("瑞文")

print(g1.life_value)
r1.attack(g1)  # 交互
print(g1.life_value)


class People(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def eat(self):
        print("%s is eating..." % self.name)

    def talk(self):
        print("%s is talking..." % self.name)

    def sleep(self):
        print("%s is sleeping..." % self.name)


class Man(People):
    def __init__(self, name, age, sex, money):
        super(Man, self).__init__(name, age, sex)
        self.money = money

        print("%s 一出生就有 %s money" % (self.name, self.money))

    def sleep(self):
        print("man is sleeping ")


class Woman(People):
    def get_birth(self):
        print("%s is born a baby...." % self.name)


m1 = Man("jack", 22, 'male', 10000)
m1.sleep()

w1 = Woman("alex", 26, 'female')
w1.get_birth()

print(100 * "#")

r3 = Riven("瑞文")
r3.equip.file()  # 可以使用组合的类产生的对象所持有的方法

print(100 * "#")


class Course(object):
    def __init__(self, name, period, price):
        self.name = name
        self.period = period
        self.price = price

    def tell_info(self):
        print('%s %s %s ' % (self.name, self.period, self.price))


class Teacher(People):
    def __init__(self, name, age, sex, job):
        super(Teacher, self).__init__(name, age, sex)
        self.job = job
        self.course = []
        self.students = []


class Student(People):
    def __init__(self, name, age, sex):
        super(Student, self).__init__(name, age, sex)
        self.course = []


# 老师和学生对象
jack = Teacher('jack', 28, 'male', 'c++')
s1 = Student('derek', 12, 'female')

# 课程
python = Course('python', '3month', 3000)
linux = Course('linux', '4month', 5000)

# 为老师和学生添加课程
jack.course.append(python)
jack.course.append(linux)

s1.course.append(linux)

# 为老师添加学生
jack.students.append(s1)

for obj in jack.course:
    obj.tell_info()

print(100 * "#")


class Dog(object):
    def __init__(self, name):
        self.name = name

    @staticmethod
    def eat():
        print('is eating')


d = Dog('xiaohei')
d.eat()


class Dog2(object):
    def __init__(self, name):
        self.name = name

    @classmethod
    def eat(cls):
        print('is eating')


d = Dog2('xiaohei')
d.eat()


class Dog3(object):
    def __init__(self, name):
        self.name = name

    @property
    def eat(self):
        print('is eating')


d = Dog3('xiaohei')
d.eat


#  所谓多态：定义时的类型和运行时的类型不一样，此时就成为多态
class F1(object):
    def show(self):
        print('F1.show')


class S1(F1):
    def show(self):
        print('S1.show')


class S2(F1):
    def show(self):
        print('S2.show')


def Func(obj):
    print(obj.show())


# s1_obj = S1()
# Func(s1_obj)

# s2_obj = S2()
# Func(s2_obj)

s1_obj = S1()
Func(s1_obj)  # 在Func函数中传入S1类的对象 s1_obj，执行 S1 的show方法，结果：S1.show

s2_obj = S2()
Func(s2_obj)  # 在Func函数中传入Ss类的对象 ss_obj，执行 Ss 的show方法，结果：S2.show

print(100 * "#")


class Func2():
    """ test __doc__ """

    def func(self):
        pass


print(Func2.__doc__)

print(100 * "#")


class Foo:
    def __str__(self):
        return 'test __str__'


obj = Foo()
print(obj)

print(100 * "#")


class Dog(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("%s is eating..." % self.name, food)


d = Dog("NiuHanYang")
choice = input(">>:").strip()


def bulk(self):  # 添加的方法
    print("%s is yelling...." % self.name)


# hasattr() 函数用于判断对象是否包含对应的属性。
if hasattr(d, choice):  # 输入的字符串，判断是否有对应字符串的方法
    func1 = getattr(d, choice)
    func1('')
else:
    setattr(d, choice, bulk)  # d.talk = bulk   #通过setattr在类外部添加方法
    func2 = getattr(d, choice)
    func2(d)

# if hasattr(d, choice):  # 删除
#     delattr(d, choice)
