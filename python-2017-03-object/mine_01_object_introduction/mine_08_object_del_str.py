class Cat:
    def __init__(self, name):
        print("创建对象的时候会调用初始化方法__init__,name: %s" % name)
        self.name = name

    def eat(self):
        print("%s eat" % self.name)

    def drink(self):
        print("%s drink" % self.name)

    def __del__(self):
        print("%s 对象被销毁" % self.name)

    def __str__(self):
        return "__str__: " + self.name


tom = Cat("tom")
tom.eat()
tom.drink()
print(tom.name)

lazy_cat = Cat(name="懒猫")
lazy_cat.eat()
lazy_cat.drink()

del tom
print(lazy_cat)
