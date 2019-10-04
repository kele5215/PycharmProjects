import os
import sys

# 获取当前工作目录，即当前python脚本工作的目录路径
print(os.getcwd())

# 当前目录
# print(os.ch())

# 返回当前目录: ('.')，相当于shell下cd.
print(os.curdir)

# 获取当前目录的父目录字符串名：('..')，相当于shell下cd.. 返回上一层目录
print(os.pardir)

# 可生成多层递归目录
# os.makedirs(r"c:\a\b\c")

# 若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
# os.removedirs(r"c:\a\b\c")

# 生成单级目录；相当于shell中mkdir dirname
# os.mkdir(r"c:\a\b")
# os.mkdir(r"cur_b")

# 删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
# os.rmdir(r"cur_b")

# 列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
print(os.listdir(os.curdir))

# 删除一个文件
# os.remove(r"C:\work\developer\PycharmProjects\delDemo.txt")

# 重命名文件/目录
# os.rename(r"C:\work\developer\PycharmProjects\test",
#           r"C:\work\developer\PycharmProjects\test2")

# 获取文件/目录信息
print(100 * '*')
print(os.stat(r"C:\work\developer\PycharmProjects\test2"))

# 输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
print(os.sep)

# 输出当前平台使用的行终止符，win下为"\r\n",Linux下为"\n"
print(os.linesep)

# 输出用于分割文件路径的字符串
print(os.pathsep)

# 输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
print(os.name)

# 运行shell命令，直接显示
# os.system("calc")

# 获取系统环境变量
print(os.environ)

# os.path.abspath(path)  #返回path规范化的绝对路径

# os.path.split(path)  #将path分割成目录和文件名二元组返回

# os.path.dirname(path)  #返回path的目录。其实就是os.path.split(path)的第一个元素

# os.path.basename(path) # 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素

# os.path.exists(path)  #如果path存在，返回True；如果path不存在，返回False

# os.path.isabs(path)  #如果path是绝对路径，返回True

# os.path.isfile(path)  #如果path是一个存在的文件，返回True。否则返回False

# os.path.isdir(path)  #如果path是一个存在的目录，则返回True。否则返回False

# os.path.join(path1[, path2[, ...]])  #将多个路径组合后返回，第一个绝对路径之前的参数将被忽略

# os.path.getatime(path)  #返回path所指向的文件或者目录的最后存取时间

# os.path.getmtime(path)  #返回path所指向的文件或者目录的最后修改时间

# os.path.getsize(path)  #返回path的大小
"""
sys模块
"""

print(sys.argv)
# print(sys.exit(n))  # 退出程序，正常退出时exit(0)
print(sys.version)  # 获取Python解释程序的版本信息
# print(sys.maxint)  # 最大的Int值
print(sys.path)  # 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
print(sys.platform)  # 返回操作系统平台名称
