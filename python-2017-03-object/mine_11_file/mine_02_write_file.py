# open
# read/write
# close

# 1.卡开文件
# 默认以只读 方式打开文件
# 文件打开的方式：
# r
# w
# a
# r+
# w+
# a+
file = open("README.md", "a+")

# 2.写入文件
file.write("python write\n")
file.write("hello")

# 3.关闭文件
file.close()
