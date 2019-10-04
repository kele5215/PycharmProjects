# _*_ coding:UTF8 _*_

import socket

name = [1, 2, 3]
try:
    print(name[5])
except IndexError as e:
    print("列表操作错误", e)

data = {'zhang': 12}
try:
    print(data['li'])
except KeyError as e:
    print("没有这个key", e)

try:
    open("test.txt")

except (KeyError, IndexError) as e:
    print("没有这个key", e)

except IndexError as e:
    print("列表操作错误", e)

except Exception as e:
    print("未知错误", e)

else:
    print("一切正常")

finally:
    print("不管有没有错，都执行")

try:
    raise Exception('错误')
except Exception as e:
    print(e)

# 创建socket对象
sock = socket.socket()
# 绑定IP和端口,参数是一个元组(ip,port)
sock.bind(('localhost', 8080))
# 开始监听,最大挂起5个
sock.listen(5)
# 阻塞,等待连接
conn, addr = sock.accept()
# 接收请求数据,接收大小为1024字节
content = conn.recv(1024)
print(content.decode())
# 发送请求结果,必须以bytes类型
conn.send(b'jieshouwanbi')
# 关闭链接
conn.close()
