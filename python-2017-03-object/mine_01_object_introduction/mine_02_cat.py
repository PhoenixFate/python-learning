class Cat:

    def eat(self):
        print("猫吃鱼")
        pass

    def drink(self):
        print("猫喝水")
        pass


# 创建猫对象
my_cat = Cat()
my_cat.drink()
my_cat.eat()

print(my_cat)
# %d十进制
print("%d" % id(my_cat))
# %x十六进制
print("%x" % id(my_cat))
