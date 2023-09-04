# 一个类默认是继承object类的，
# 在python2中 需要强制写(object)
# 在python3中 可以不写(object)


class Animal2(object):

    def __init__(self):
        pass

    def eat(self):
        print("eat")

    def drink(self):
        print("drink")

    def run(self):
        print("run")

    def sleep(self):
        print("sleep")


class Dog2(Animal2):

    def bark(self):
        print("汪汪汪")


# 继承的特效：传递性
class XiaoTianQuan(Dog2):
    def fly(self):
        print("fly")


animal = Animal2()
animal.eat()
animal.drink()
animal.run()
animal.sleep()

dog = Dog2()
dog.eat()
dog.drink()
dog.sleep()
dog.bark()

xiao_tian_quan = XiaoTianQuan()
xiao_tian_quan.fly()
