import pygame

pygame.init()

screen = pygame.display.set_mode((480, 700))
background = pygame.image.load("./images/background.png")
# screen.blit(background, (0, 0))
hero = pygame.image.load("./images/me1.png")
# screen.blit(hero, (200 - 20, 500))
pygame.display.update()

# 设置英雄初始位置
hero_rect = pygame.Rect(240 - 51, 500, 102, 126)

# 设置时钟
clock = pygame.time.Clock()

# 游戏循环 -> 意味着游戏开始
i = 0

while True:
    # 绘制背景
    screen.blit(background, (0, 0))

    # 绘制英雄
    screen.blit(hero, hero_rect)

    # 刷新游戏界面
    pygame.display.update()

    # 控制游戏循环内部代码执行的频率60帧
    clock.tick(60)

    hero_rect.y -= 1

    if hero_rect.y < 0 - hero_rect.height:
        hero_rect.y = 700

    print(i)

    i += 1

    pass

pygame.quit()
