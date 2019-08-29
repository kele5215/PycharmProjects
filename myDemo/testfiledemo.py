import os
from filedemo import open_write_file, open_read_file, file_flush

# 获取当前路径
# abspath = os.path.abspath('./')
abspath = os.getcwd()
print(abspath)
# file_path = os.path.join(abspath, "tmp\\foo.txt")
file_path = r"tmp\foo.txt"
print(file_path)
open_write_file(file_path)

# read()
print(open_read_file(file_path, "read"))
file_flush()

# readline()
print(open_read_file(file_path, "readline"))
file_flush()

# readlines()
print(open_read_file(file_path, "readlines"))
file_flush()

# seek和tell光标
print(open_read_file(file_path, "seek_tell"))
file_flush()
