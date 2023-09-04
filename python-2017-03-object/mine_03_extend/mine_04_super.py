class Animal4:

    def __init__(self):
        self.name = "animal"
        pass

    def eat(self):
        print("eat")

    def drink(self):
        print("drink")

    def run(self):
        print("run")

    def sleep(self):
        print("sleep")


class Dog4(Animal4):

    def bark(self):
        print("汪汪汪")


# 继承的特效：传递性
# 在 Python 中 super 是一个 特殊的类
# super() 就是使用 super 类创建出来的对象
class XiaoTianQuan4(Dog4):
    def fly(self):
        print("fly")

    def bark(self):
        # 调用父类的方法
        super().bark()
        # python2.x中的方法 不推荐使用
        # Dog4.bark(self)
        print("啸天犬 专有咆哮")


xiao_tian_quan = XiaoTianQuan4()
xiao_tian_quan.fly()
xiao_tian_quan.bark()
print(xiao_tian_quan.name)

print(dir(object))
print(dir(object()))

