from 飞机大战.plane_sprites import *


class PlaneGame(object):
    """飞机大战朱游戏类"""

    def __init__(self):
        print("初始化游戏")

        # 1. 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2. 创建游戏始终
        self.clock = pygame.time.Clock()
        # 3. 调用私有方法，创建游戏精灵和精灵组
        self.__create_sprites()
        # 4. 定义创建敌机的定时器 1s
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        # 5. 定义发射子弹的定时器 500ms
        pygame.time.set_timer(EVENT_BULLET, 500)

    def __create_sprites(self):
        # 建立游戏背景精灵
        background_1 = BackGround()
        background_2 = BackGround(is_alt=True)
        background_2.rect.y = -background_2.rect.height
        self.background_group = pygame.sprite.Group(background_1, background_2)

        # 建立敌机精灵组
        self.enemy_group = pygame.sprite.Group()

        # 建立英雄精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("开始游戏")
        while True:
            # 1. 定义屏幕刷新率
            self.clock.tick(FRAME_PER_SEC)
            # 2. 定义事件监听
            self.__event_handler()
            # 3. 定义碰撞检测
            self.__check_collide()
            # 4. 定义精灵更新
            self.__update_sprites()
            # 5. 更新屏幕显示
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            # 监听关闭窗口事件
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # print("敌机出场了...")
                # 新建敌机
                enemy = Enemy()
                # 将敌机加入敌机精灵组
                self.enemy_group.add(enemy)
            elif event.type == EVENT_BULLET:
                # 发射子弹
                self.hero.fire()

        # 捕获键盘事件
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_a] == 1:
            self.hero.speed = -HERO_SPEED
        elif key_pressed[pygame.K_d] == 1:
            self.hero.speed = HERO_SPEED
        else:
            self.hero.speed = 0

    def __check_collide(self):
        pygame.sprite.groupcollide(self.enemy_group, self.hero.bullet_group, True, True)
        enemies = pygame.sprite.groupcollide(self.hero_group, self.enemy_group, True, True)
        if len(enemies) > 0:
            self.hero.kill()
            PlaneGame.__game_over()

    def __update_sprites(self):
        self.background_group.update()
        self.background_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.display.quit()
        exit()


if __name__ == '__main__':
    """
    
    """

    # 创建飞机大战主游戏类对象实例
    game = PlaneGame()

    # 启动启动飞机大战
    game.start_game()
