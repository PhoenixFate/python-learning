# 使用类名() 创建对象时，python解释器会
# 1.调用__new__ 方法为对象分配内存空间
# 2.调用__init__


class MusicPlayer(object):
    instance = None

    # 记录是否初始化
    init_flag = False

    def __new__(cls, *args, **kwargs):
        print(args)
        print(kwargs)
        # 1.创建对象时，new方法会被自动调用
        # 2.为对象分配空间
        # 3.返回对象的引用
        print("MusicPlayer new")
        if cls.instance is None:
            # object.__new__
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        # 1.判断是否进行过初始化操作
        if MusicPlayer.init_flag:
            return
        # 2.如果没有执行过，执行初始化操作
        print("music player init 初始化操作")
        # 3.修改属性标记
        MusicPlayer.init_flag = True

    @classmethod
    def test(cls):
        print("test")

    def __test2__(self):
        print("test2")

    # def __test3(self):
    #     print("test3")


player1 = MusicPlayer()
player2 = MusicPlayer()
print(player1)
print(player2)
MusicPlayer.test()
player1.__test2__()
# player1.__test3()
