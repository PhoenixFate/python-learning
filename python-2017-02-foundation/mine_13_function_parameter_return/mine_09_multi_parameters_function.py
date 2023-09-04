# *args arguments表示接受一个元祖
# **kwargs keyword arguments表示接受一个字典


def demo(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)


demo(1, 2, 3, 4, 5, name="小王", age=12)
