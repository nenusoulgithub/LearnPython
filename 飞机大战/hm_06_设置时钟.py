import pygame

pygame.init()

screen = pygame.display.set_mode((480, 700))
background = pygame.image.load("./images/background.png")
screen.blit(background, (0, 0))
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200 - 20, 500))
pygame.display.update()

# 设置时钟
clock = pygame.time.Clock()

# 游戏循环 -> 意味着游戏开始
i = 0

while True:
    # 控制游戏循环内部代码执行的频率60帧
    clock.tick(1)

    print(i)

    i += 1

    pass

pygame.quit()
