import pygame

pygame.init()

# 创建游戏窗口  480*700
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 1.加载图片对象
background_image = pygame.image.load("./images/background.png")
# 2.blit绘制图像
screen.blit(background_image, (0, 0))
# 3.update更新图像
pygame.display.update()

# 这里的意思是：循环运行整个文件的代码，直到点击关闭按钮，内部应该是设定了延时防止卡死
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
