# 打开文件 写入内容
# f = open("tmp/foo.txt", "w", encoding='utf-8')
#
# f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
#
# # 关闭文件
# f.close()

# 打开一个文件
# f = open("tmp/foo.txt", "r", encoding='utf-8')
#
# str = f.read()
# print(str)
#
# # 关闭打开的文件
# f.close()


def open_write_file(file_with_path):
    file = open(file_with_path, "w", encoding='utf-8')
    file.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n谁说的揍他\n")
    file.close()


def open_read_file(file_with_path, read_type):
    # file = open(file_with_path, "r", encoding='utf-8')
    with open(file_with_path, "r", encoding='utf-8') as file:
        if read_type == "read":
            str_file = file.read()
        elif read_type == "readline":
            str_file = file.readline()
        elif read_type == "readlines":
            str_file = file.readlines()
    file.close()
    return str_file
