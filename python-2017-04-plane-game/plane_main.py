# 导入模块顺序
# 1.官方标准模块导入
# 2.第三方模块导入
# 3.程序模块导入

from plane_scrites import *


class PlaneGame(object):
    """游戏大战主程序"""

    def __init__(self):
        print("游戏初始化")
        # 1.创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2.创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 3.创建精灵、精灵组
        self.__create_sprites()
        # 4.设置定时器事件，创建敌机   第一个参数 eventId，第二个参数，定时器时间间隔
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __create_sprites(self):
        # 创建背景精灵，背景精灵组
        background_sprite1 = BackgroundSprite(True)
        background_sprite2 = BackgroundSprite(False)
        self.background_sprite_group = pygame.sprite.Group(background_sprite1, background_sprite2)

        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄、英雄精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("游戏开始")
        while True:
            # 1.设置刷新帧率
            self.clock.tick(FRAME_PRE_SEC)
            # 2.事件监听
            self.__event_handler()
            # 3.碰撞检测
            self.__check_collide()
            # 4.更新/绘制精灵
            self.__update_sprites()
            # 5.更新显示
            pygame.display.update()

    def __event_handler(self):
        event_list = pygame.event.get()
        for event in event_list:
            # 判断是否退出程序
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                print("敌机出场")
                # 创建敌机精灵
                enemy = Enemy()
                # 将敌机精灵添加到敌机精灵组
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

            # 向右的键
            # 一直按着向右的键不一直触发，所以不使用下面的方法
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右移动...")
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            #     print("向左移动...")

        # 使用键盘提供的方法获取键盘按键
        keys_pressed = pygame.key.get_pressed()
        # 判断元组中对应的按键索引值
        if keys_pressed[pygame.K_RIGHT]:
            print("向右移动")
            self.hero.speed_x = 5
        elif keys_pressed[pygame.K_LEFT]:
            print("向左移动")
            self.hero.speed_x = -5
        elif keys_pressed[pygame.K_UP]:
            print("向上移动")
            self.hero.speed_y = -5
        elif keys_pressed[pygame.K_DOWN]:
            print("向上移动")
            self.hero.speed_y = 5
        else:
            self.hero.speed_x = 0
            self.hero.speed_y = 0

    def __check_collide(self):
        # 1.子弹碰撞敌机
        pygame.sprite.groupcollide(self.hero.bullet_group, self.enemy_group, True, True)

        # 2.敌机撞毁飞机
        enemy_list = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemy_list):
            # 让英雄牺牲
            self.hero.kill()
            # 结束游戏
            self.__game_over()

    def __update_sprites(self):
        # 背景精灵组
        self.background_sprite_group.update()
        self.background_sprite_group.draw(self.screen)

        # 敌机精灵组
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        # 英雄精灵组
        self.hero_group.update()
        self.hero_group.draw(self.screen)

        # 子弹精灵组
        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()
    # 启动游戏
    game.start_game()
