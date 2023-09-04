# 使用类名() 创建对象时，python解释器会
# 1.调用__new__ 方法为对象分配内存空间
# 2.调用__init__


class MusicPlayer2(object):
    instance = None

    # 记录是否初始化
    init_flag = False

    @staticmethod
    def __new__(cls, *args, **kwargs):
        print(cls)
        print(args)
        print(kwargs)
        # 1.创建对象时，new方法会被自动调用
        # 2.为对象分配空间
        # 3.返回对象的引用
        return super().__new__(cls)

    def __init__(self):
        print("init ")

    @classmethod
    def test(cls, *args):
        print(args)
        print("test")

    @staticmethod
    def __test2__(*args):
        print(args)
        print("test2")

    # def __test3(self):
    #     print("test3")


MusicPlayer2.test()
player1 = MusicPlayer2()
player2 = MusicPlayer2()
print(player1)
print(player2)
player1.__test2__()
