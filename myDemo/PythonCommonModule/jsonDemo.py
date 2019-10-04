import json

dic = {'name': 'alvin', 'age': 23, 'sex': 'male'}
print(type(dic))

j = json.dumps(dic)
print(type(j))

# -------------------等价于json.dump(dic,f)
with open('序列话对象', 'w', encoding='utf-8') as myFile:
    myFile.write(j)
myFile.close()

# -----------------------------反序列化<br>

print("LOAD " + 100 * '#')
#  等价于data=json.load(f)
with open('序列话对象', 'r', encoding='utf-8') as read_file:
    data = json.loads(read_file.readline())
    print(data)

print("DEMO2  " + 100 * '#')
# 序列化
info = {'name': 'derek', 'age': '22'}

with open('test', 'w') as f:
    f.write(json.dumps(info))

# 反序列化
with open('test', 'r') as f:
    info = json.loads(f.read())
    print(info)
