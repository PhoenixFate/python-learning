import pygame

pygame.init()
# 创建游戏窗口  480*700
screen = pygame.display.set_mode((480, 700))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
