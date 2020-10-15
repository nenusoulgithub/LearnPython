import pygame

pygame.init()

# 加载素材
background = pygame.image.load("./images/background.png")
hero = pygame.image.load("./images/me1.png")
# 设置界面
screen = pygame.display.set_mode((480, 700))
# 绘制背景
screen.blit(background, (0, 0))
# 设置英雄初始位置
hero_rect = pygame.Rect(240 - 51, 500, 102, 126)
# 绘制英雄
screen.blit(hero, hero_rect)
# 刷新界面
pygame.display.update()

# 设置时钟
clock = pygame.time.Clock()

# 游戏循环 -> 意味着游戏开始
i = 0

while True:
    # 控制游戏循环内部代码执行的频率60帧
    clock.tick(60)

    # 事件监听
    event_list = pygame.event.get()
    for event in event_list:
        print(event)

        # 监听关闭按钮
        if event.type == pygame.QUIT:
            print("退出游戏")

            pygame.quit()

            # 直接退出系统
            exit()

    # 更新英雄位置
    hero_rect.y -= 1

    # 绘制背景
    screen.blit(background, (0, 0))

    # 绘制英雄
    screen.blit(hero, hero_rect)

    # 刷新游戏界面
    pygame.display.update()

    if hero_rect.y < 0 - hero_rect.height:
        hero_rect.y = 700

    pass
