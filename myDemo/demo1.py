# -* - coding: UTF-8 -* -
import sys
from sys import path
import numpy as np
import keyword

print(keyword.kwlist)

# 注释*****************************
'''
zhushi1
zhushi2
'''
"""
zhisdlfj
sdfljsldf
"""
# 注释*****************************

# 字符串(String)*****************************
str = "Runoob"

print(str)  # 输出字符串
print(str[0:-1])
print(str[0])
print(str[2:5])
print(str[2:])
print(str * 2)
print(str + "你好！")
print("hello \n runoob")
print(r"hello \n runoob")
# 字符串(String)*****************************

# 等待用户输入********************************
# input("\n\n按下 enter 键后退出。")
# 等待用户输入********************************

# 同一行显示多条语句**************************

x = 'runoob'
sys.stdout.write(x + '\n')
# 同一行显示多条语句**************************

# 实现不换行需要在变量末尾加上 end=""**********
x = "a"
y = "b"
print(x)
print(y)

print("--------------")
print(x, end="")
print(y, end="")
print()
# 实现不换行需要在变量末尾加上 end=""**********

# import 与 from...import**********************

print('================Python import mode==========================')
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('\n python 路径为', path)
# import 与 from...import**********************

# Number（数字）*******************************
a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))

a = 111
print(isinstance(a, int))
# del a, b, c, d
print(type(b), type(c), type(d))
# Number（数字）*******************************

# List（列表）********************************
listSelf = ["abcd", 786, 2.23, "runOob", 70.2]
tinyList = [123, "runOob"]
print(listSelf)
for listItem in listSelf:
    print(type(listItem))
print("输出第一个元素: " + listSelf[0])
print(listSelf[1:3])
print(listSelf[2:])
print(tinyList * 2)
print(listSelf + tinyList)
listSelf[2:3] = []
print(listSelf)
# List（列表）********************************

# Set（集合）**********************************
student = {"Tom", "Jim", "Mary", "Tom", "Jack", "Rose"}
print(student)
for setItem in student:
    print(setItem, end="test ")
print(student.__len__())
student.add("rose")
print(student)
if "rose" in student:
    print("rose zai jihe zhong")
else:
    print("rose bu zai jihe zhong")

a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)
# Set（集合）**********************************

# Dictionary（字典）***************************
dictSelf = {}
dictSelf["one"] = "1 - wo shi cai niao"
dictSelf[2] = "2 - zheshi gong ju"
print(dictSelf)
print(dictSelf[2])
print(dictSelf.keys())
print(dictSelf.values())

dictSelf2 = dict([("Runoob", 1), ("Google", 2), ("Taobao", 3)])
print(dictSelf2)
dictSelf2 = dict(Runoob=4, Google=5, Taobao=6)
print(dictSelf2)
dictSelf2 = {x: x**2 for x in (1, 3, 5)}
print(dictSelf2)
# Dictionary（字典）***************************

# Python数据类型转换***************************
str1 = 2
print(hex(str1))
# Python数据类型转换***************************

list_float_arr = [
    [0.1, 0.2, 0.3],
    [1.1, 1.2, 1.3],
    [2.1, 2.2, 2.3],
]

for x in range(len(list_float_arr)):
    for y in range(len(list_float_arr)):
        if x > y:
            list_float_arr[x][y] = list_float_arr[y][x]
        else:
            list_float_arr[x][y] = list_float_arr[x][y] + list_float_arr[y][x]

print(list_float_arr)

list_float_arr_2 = [
    [0.1, 0.2, 0.3],
    [1.1, 1.2, 1.3],
    [2.1, 2.2, 2.3],
]
X1 = np.array(list_float_arr_2)
X2 = X1
print("list_float_arr_np: ", X2 + X1)

age = 22
print('我今年%d岁' % age)
print(9 // 2)

name = input('qing shu ru mingzi: ')
password = input('qing shu ru mi ma: ')

if name=='root' and password == '123':
    print('root login success')
else:
    print('cuowu')
