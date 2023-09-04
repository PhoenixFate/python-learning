class Woman:
    """
        在定义属性或者方法时，在属性名或者方法名前面增加两个下划线，定义的就是私有属性或方法；
    """

    def __init__(self, name):
        self.name = name
        # 属性 方法 前面加__ 代表私有
        self.__age = 19
        print("出现了一个美女：%s ; %d" % (self.name, self.__age))

    def __secret(self):
        # 在对象的方法内部，能够正常访问私有属性
        print("func secret %s 的年龄是: %d" % (self.name, self.__age))


woman = Woman("小美")
# 私有属性在外界不能直接访问
# print(woman.__age)
"""
在python中，并没有真正意义上的私有，只有伪私有；
- python在给私有属性和私有方法命名时，实际是对名称做了一些特殊处理，是的外界无法访问到；
- 处理方式：在名称前加上 _类名，即 _类名__名称
"""
print(woman._Woman__age)

# 私有方法在外界不能直接访问
# woman.__secret()
woman._Woman__secret()
woman.__init__("xx")
