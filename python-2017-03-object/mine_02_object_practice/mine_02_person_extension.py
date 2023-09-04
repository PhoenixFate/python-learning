class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字叫%s, 体重%.2f公斤" % (self.name, self.weight)

    def run(self):
        print("%s 爱跑步" % self.name)
        self.weight -= 0.5

    def eat(self):
        print("%s 是个吃货，爱吃东西" % self.name)
        self.weight += 0.3

 
person1 = Person("小明", 75.6434)
print(person1)
person1.run()
print(person1)
person1.eat()
print(person1)

person2 = Person("小美", 45.64)
print(person2)
person2.run()
print(person2)
person2.eat()
print(person2)
