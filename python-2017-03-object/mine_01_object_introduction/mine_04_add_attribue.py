class Cat:

    def __init__(self):
        self.name = None

    # 普通方法（实例方法）
    def eat(self):
        # 哪一个对象调用的方法，self就是哪一个对象的引用
        print("%s猫吃鱼" % self.name)
        pass

    def drink(self):
        print("猫喝水")
        pass


# 创建猫对象
my_cat = Cat()
my_cat.name = "tom"

my_cat.drink()
my_cat.eat()

print(my_cat)
# %d十进制
print("%d" % id(my_cat))
# %x十六进制
print("%x" % id(my_cat))
# 在不修改类的前提下，给对象添加属性
print("name:%s" % my_cat.name)

# 再创建一个对象
lazy_cat = Cat()
lazy_cat.name = "大懒猫"
lazy_cat.eat()
lazy_cat.drink()

print(lazy_cat)

lazy_cat2 = lazy_cat
print(lazy_cat2)
