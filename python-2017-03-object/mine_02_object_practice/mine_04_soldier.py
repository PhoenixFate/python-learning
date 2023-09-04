import string


class Gun:
    """
    在定义属性或者方法时，在属性名或者方法名前面增加两个下划线，定义的就是私有属性或方法；
    """

    def __init__(self, model: string):
        # 1.枪到型号
        self.model = model
        # 2.子弹的数量
        self.bullet_count = 0
        self.__version = None

    def add_bullet(self, count):
        """装填子弹"""
        self.bullet_count += count

    def shoot(self):
        # 1.判断子弹数量
        if self.bullet_count <= 0:
            print("已经没有子弹可以射击")
            return
            # 2.发射子弹
        self.bullet_count -= 1
        # 3.提示发射信息
        print("[%s] 哒哒 (%d)" % (self.model, self.bullet_count))


class Soldier:

    def __init__(self, name: string):
        # 1.设置新兵的姓名
        self.name = name
        # 2.新兵没有枪
        self.gun = None

    def fire(self):
        # 士兵开枪
        # 1.判断是否有枪
        if self.gun is None:
            print("士兵 %s 没有装配枪，无法开枪" % self.name)
            return
        # 2.高喊口号
        print("准备开枪")
        # 3.让枪装填子弹
        self.gun.add_bullet(10)
        # 4.发射
        self.gun.shoot()


# 1.创建枪对象
ak47 = Gun("ak47")
# ak47.add_bullet(10)
# ak47.shoot()
# ak47.shoot()

soldier = Soldier("许三多")
soldier.gun = ak47
soldier.fire()
