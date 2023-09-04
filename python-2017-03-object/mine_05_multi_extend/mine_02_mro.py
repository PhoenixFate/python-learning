# mro: method resolution order 方法解决顺序
class A2(object):
    def __init__(self):
        self.name = "A name"

    def test(self):
        print("A test")

    def demo(self):
        print("A demo")


class B2(object):
    def __init__(self):
        self.name = "B name"

    def test(self):
        print("B test")

    def demo(self):
        print("B demo")


class C2(A2, B2):
    pass


c = C2()
print(c.name)
c.demo()
c.test()

# 确定C类对象调用的顺序
print(C2.__mro__)

