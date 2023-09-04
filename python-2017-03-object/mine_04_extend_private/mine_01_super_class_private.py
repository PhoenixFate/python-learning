class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("私有方法：%d  %d" % (self.num1, self.__num2))

    def test(self):
        self.__test()
        print("私有方法：%d  %d" % (self.num1, self.__num2))


class B(A):

    def demo(self):
        # 1.在子类方法中，不能访问父类私有属性
        # print(super().__num2)
        # print(self.__num2)
        # 2.在子类方法中，不能访问父类私有方法
        # super().__test()
        # self.__test()
        # 3.通过父类共有方法 访问私有属性，私有方法
        super().test()


b = B()
print(b)

# 在外界不能够访问私有属性 私有方法
# print(b.__num2)
# b.__test
b.test()
b.demo()
