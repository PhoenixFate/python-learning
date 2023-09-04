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
i = 0
# 创建时钟对象
clock = pygame.time.Clock()
while True:
    print(i)
    i += 1
    # 设置刷新率 (每秒多少帧)，指定循环体内部执行的频率
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

# 游戏循环----end----
