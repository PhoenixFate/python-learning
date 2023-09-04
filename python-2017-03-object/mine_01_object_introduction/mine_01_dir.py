# 提示 __方法名__ 格式的方法是 Python 提供的 内置方法 / 属性，稍后会给大家介绍一些常用的 内置方法 / 属性
"""
01	__new__	 方法	创建对象时，会被 自动 调用
02	__init__ 方法	对象被初始化时，会被 自动 调用
03	__del__	 方法	对象被从内存中销毁前，会被 自动 调用
04	__str__	 方法	返回对象的描述信息，print 函数输出使用

%d 可以以 10 进制 输出数字
%x 可以以 16 进制 输出数字
"""


def demo():
    """这是一个测试函数"""
    print("hello python")


# 变量、函数、数据 都是一个对象
demo()
print(demo.__doc__)
print(dir(demo))


class Test:
    def __init__(self):
        self.name = "hello"

    def say_hello(self):
        print(self.name + " hello")


print(dir(Test))
