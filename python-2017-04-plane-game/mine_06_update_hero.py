import pygame

pygame.init()

# 游戏初始化----start----
# 创建游戏窗口  480*700
screen = pygame.display.set_mode((480, 700))
# 绘制背景图像
# 1.加载图片对象
background_image = pygame.image.load("./images/background.png")
# 2.blit绘制图像
screen.blit(background_image, (0, 0))
# 3.update更新图像
# pygame.display.update()
# 绘制英雄图像
hero_image = pygame.image.load("./images/me1.png")
screen.blit(hero_image, (200, 300))
# 可以在screen完成了所有的blit操作后，统一执行pygame.display.update()
pygame.display.update()
# 游戏初始化----end----


# 游戏循环----start----
# 这里的意思是：循环运行整个文件的代码，直到点击关闭按钮，内部应该是设定了延时防止卡死
# 创建时钟对象
clock = pygame.time.Clock()

# 1.定义Rect对象记录飞机的初始位置
hero_width = 102
hero_height = 126
hero_rect = pygame.Rect(150, 300, hero_width, hero_height)
while True:
    # 设置刷新率 (每秒多少帧)，指定循环体内部执行的频率
    clock.tick(60)

    # 绘制背景图，遮挡一切
    screen.blit(background_image, (0, 0))

    # 2.修改飞机的位置
    hero_rect.y -= 1
    if (hero_rect.y + hero_height) <= 0:
        hero_rect.y = 700

    # 3.调用blit方法绘制对象
    screen.blit(hero_image, hero_rect)

    # 4.调用update更新
    pygame.display.update()

    # pygame.event.get() 捕获事件
    even_list = pygame.event.get()
    if len(even_list) > 0:
        print(even_list)
    for event in even_list:
        # 判断用户是否点击了关闭按钮
        if event.type == pygame.QUIT:
            print("游戏退出...")
            # 卸载pygame各种模块
            pygame.quit()
            # 直接退出程序
            exit()

# 游戏循环----end----
