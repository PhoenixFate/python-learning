import os
import sched
import time

# 重命名目录
# os.rename("a.txt", "b.txt")
# 删除目录
# os.remove("b.txt")

# 查看目录或文件列表
print(os.listdir("."))

# 判断某名称是文件还是目录
print("is file: %r" % os.path.isdir("README.md"))
print("is file: %s" % os.path.isfile("README.md"))

# os.mkdir("test")
# os.rmdir("test")

# 获得当前目录
print(os.getcwd())

# python2.x 默认ASCII 编码
# python3.x 默认 utf-8
