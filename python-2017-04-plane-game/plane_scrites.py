# 导入模块顺序
# 1.官方标准模块导入
# 2.第三方模块导入
# 3.程序模块导入
import random
import pygame

# 屏幕大小常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 每秒刷新的帧率
FRAME_PRE_SEC = 60
# 创建敌机定时器产量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """
    飞机大战的游戏精力对象
    """

    def __init__(self, image_name, speed=1, *groups):
        # 调用父类的初始化方法
        super().__init__(*groups)
        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self, *args):
        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed


class BackgroundSprite(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_first):
        # 1.调用父类方法实现精灵的创建
        super().__init__("./images/background.png")

        # 2.判断是否第一张图片
        if not is_first:
            self.rect.y = -self.rect.height

    def update(self, *args):
        # 1.调用父类的update
        super().update()
        # 2.判断是否移除屏幕，如果移除屏幕，则移动上屏幕上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = - self.rect.height


# 1.游戏启动后，每隔1秒 出现1架敌机
# 2.每架敌机 向屏幕下方飞行， 飞行速度各不相同
# 3.每架敌机出现的 水平位置 各不相同
# 4.当敌机从屏幕下方飞出，不会再飞回屏幕，并且del 该变量
class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):
        # 1.调用父类方法，创建敌机精灵，指定图片
        super().__init__("./images/enemy1.png")
        # 2.指定敌机的初始随机速度
        self.speed = random.randint(2, 3)
        # 3.指定敌机的初始随机位置
        # self.rect.y = -self.rect.height 下面这句话就是等价于这句话
        # bottom=y+height
        # y=bottom-height
        self.rect.bottom = 0
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)

    def update(self, *args):
        # 1.调用父类方法, 保持垂直方向上的飞行
        super().update()

        # 2.判断是否飞出屏幕，如果是，需要从精灵组中删除
        if self.rect.y >= SCREEN_RECT.height:
            print("飞机飞出屏幕，需要从精灵组中删除")
            # kill方法可以将精灵从所有精灵组中移出，一旦移除，会从内存中销毁该精灵
            self.kill()

    # 敌机销毁前调用
    def __del__(self):
        print("敌机挂了 %s" % self.rect)


class Hero(GameSprite):

    def __init__(self):
        # 调用父类方法，设置image speed
        super().__init__("./images/me1.png", 0)

        self.speed_x = 0
        self.speed_y = 0
        # 英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.bullet_group = pygame.sprite.Group()

    def update(self, *args):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # 控制英雄不能移除屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.bottom > SCREEN_RECT.bottom:
            self.rect.bottom = SCREEN_RECT.bottom

    def fire(self):
        print("飞机发射子弹")

        for i in (0, 1, 2):
            bullet = Bullet(self)
            bullet.rect.bottom = self.rect.y - i * 16
            bullet.rect.centerx = self.rect.centerx
            self.bullet_group.add(bullet)


class Bullet(GameSprite):
    """子弹精灵"""

    def __init__(self, hero):
        # 调用父类方法，设置子弹图片，设置初始速度
        super().__init__("./images/bullet1.png", -2)

    def update(self, *args):
        super().update()
        # 判断是否飞出屏幕，如果是，需要从精灵组中删除
        if self.rect.bottom <= 0:
            print("子弹飞出屏幕，需要从精灵组中删除")
            # kill方法可以将精灵从所有精灵组中移出，一旦移除，会从内存中销毁该精灵
            self.kill()

    # 子弹超出屏幕调用
    def __del__(self):
        print("子弹消失了 %s" % self.rect)
