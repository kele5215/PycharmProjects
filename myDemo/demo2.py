# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 1000:
    print(b, end=" ")
    a, b = b, a + b
print("")
# if 语句*****************
# age = int(input("请输入你家狗的年龄: "))
# print("")
# if age < 0:
#     print("请输入大于零的数字！")
# elif age == 1:
#     print("xiang dang yu 14 sui de ren")
# elif age == 2:
#     print("xiang dang yu 22 sui de ren")
# elif age > 2:
#     human = 22 + (age - 2) * 5
#     print("dui ying ren lei de nianling: ", human)
#
# # 推出提示
# input("电机enter 建推出！")
# if 语句*****************

# while 循环*********************************
n = 100
counter = 11
sum = 0
while counter <= 100:
    sum += counter
    counter += 1
print("1 到 %d 之和为: %d" % (n, sum))

count = 0
while count < 5:
    print(count, "xiao yu 5")
    count += 1
else:
    print(count, "dayu huozhe dengyu 5", "oye")

a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])
print("")

for n in range(2, 100):
    for x in range(2, n):
        if n % x == 0:
            print(n, "dengyu", x, "*", n // x)
            break
    else:
        print(n, "shi zhi shu")

# while 循环*********************************
