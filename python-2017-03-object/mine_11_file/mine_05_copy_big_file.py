file_read = open("README.md")

file_write = open("README_copy_big.md", "w")

while True:
    text = file_read.readline()
    # 没有读取到内容，退出循环
    if not text:
        break
    file_write.write(text)

file_read.close()
file_write.close()
