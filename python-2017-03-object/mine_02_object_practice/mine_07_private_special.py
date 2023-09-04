class Woman:

    def __init__(self, name):
        self.name = name
        # 属性 方法 前面加__ 代表私有
        self.__age = 19
        print("%s ; %d" % (self.name, self.__age))

    def __secret(self):
        # 在对象的方法内部，能够正常访问私有属性
        print("%s 的年龄是: %d" % (self.name, self.__age))


woman = Woman("小美")
# 私有属性在外界不能直接访问
# 伪私有属性
print(woman._Woman__age)
# 私有方法在外界不能直接访问
# 伪私有方法
woman._Woman__secret()
# woman.__init__("xx")
