from filedemo import open_write_file, open_read_file

open_write_file("tmp/foo.txt")
print(open_read_file("tmp/foo.txt", "readlines"))
