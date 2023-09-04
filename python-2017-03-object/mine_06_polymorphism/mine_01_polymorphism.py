class Dog(object):
    def __init__(self, name):
        print("dog __init__ %s" % name)
        self.name = name

    def game(self):
        print("%s 简单的玩耍" % self.name)


class XiaoTianQuan(Dog):

    def game(self):
        print("%s 飞到天上玩耍" % self.name)


class Person(object):

    def __init__(self, name):
        self.name = name

    def play_with_dog(self, dog: Dog):
        print("%s 和 %s 在快乐的玩耍" % (self.name, dog.name))
        dog.game()


person = Person("小红")
common_dog = Dog("普通狗")
xiao_tian_quan = XiaoTianQuan("啸天犬")
person.play_with_dog(common_dog)
person.play_with_dog(xiao_tian_quan)
