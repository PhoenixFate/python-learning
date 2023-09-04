file = open("README.md")

while True:
    # 读取一行内容
    text = file.readline()

    # 判断是否读到内容
    if not text:
        break
    # 打印每一行的内容，内容末尾已经有\n了
    print(text, end="")

file.close()
