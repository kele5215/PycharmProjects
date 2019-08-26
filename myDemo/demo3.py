# 列表
fruit = ['apple', 'pear', 'grape', 'orange']

#切片
print(fruit[1])
print(fruit[1:3])
print(fruit[-1])
print(fruit[-2])
print(fruit[:2])

# 追加
fruit.append('peach')
print(fruit)

# 删除
fruit.remove('peach')
print(fruit)

fruit.pop()
print(fruit)

del fruit[2]
print(fruit)

# 插入
fruit.insert(1, 'bear')
print(fruit)

# 修改
fruit[2] = 'orange'
print(fruit)

# 扩展
fruit1 = ['apple', 'orange']
fruit2 = ['pear', 'grape']
fruit1.extend(fruit2)
print(fruit1)

# 统计
print(fruit1.count('apple'))

# 排序
fruit1.sort()
print(fruit1)

fruit1.reverse()
print(fruit1)

# 获取下标
print(fruit1.index('apple'))

# 同时获取下标和值
for index, item in enumerate(fruit1):
    print(index, item)

# 创建元组
fruit = ('apple', 'orange', 'grape')

# 常用功能
print(fruit.count('apple'))
print(fruit.index('orange'))

# 字典
fruit = {1: 'apple', 2: 'orange', 3: 'grape'}
print(fruit)

fruit[4] = 'pear'
print(fruit)

fruit[4] = 'peach'
print(fruit)

fruit.pop(4)
print(fruit)

print(fruit.get(1))
