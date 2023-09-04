class Cat:
    def __init__(self, name):
        print("创建对象的时候会调用初始化方法__init__")
        self.name = name

    def eat(self):
        print(self.name + " is eating")

    def drink(self):
        print(self.name + " is drinking")


tom = Cat("tom")
tom.eat()
tom.drink()
print(tom.name)
