class Animal3:

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


class Dog3(Animal3):

    def bark(self):
        print("汪汪汪")


# 继承的特效：传递性
class XiaoTianQuan3(Dog3):
    def fly(self):
        print("fly")

    def bark(self):
        print("啸天犬 专有咆哮")


animal = Animal3()
animal.eat()
animal.drink()
animal.run()
animal.sleep()

dog = Dog3()
dog.eat()
dog.drink()
dog.sleep()
dog.bark()

xiao_tian_quan = XiaoTianQuan3()
xiao_tian_quan.fly()
xiao_tian_quan.bark()
