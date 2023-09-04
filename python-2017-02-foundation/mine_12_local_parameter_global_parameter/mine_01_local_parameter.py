def demo1():
    # 定义一个局部变量
    num = 10
    print("在demo1中定义的局部变量：%d" % num)
    num2 = 20
    print(id(num2))
    return num2


def demo2():
    num = 20
    print("在demo2中定义的局部变量：%d" % num)
    pass


result = demo1()
print(id(result))
print(result)
demo2()
