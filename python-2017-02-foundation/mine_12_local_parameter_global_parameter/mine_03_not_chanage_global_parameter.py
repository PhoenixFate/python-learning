num = 10


def demo1():
    num = 100
    print("demo1 num:%d" % num)
    # 方法中不能修改全局变量的值


def demo2():
    print("demo2 num:%d" % num)


demo1()
demo2()
