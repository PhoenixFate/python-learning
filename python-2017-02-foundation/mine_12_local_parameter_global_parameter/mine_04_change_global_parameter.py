num = 10


def demo1():
    # 希望修改全局变量的值，使用global声明一下变量
    global num
    num = 100
    print("demo1 num:%d" % num)
    # 方法中不能修改全局变量的值


def demo2():
    print("demo2 num:%d" % num)


demo1()
demo2()
