import random
import pygame

# 使用常量控制窗口大小
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 定义屏幕刷新率
FRAME_PER_SEC: int = 60
# 背景图像路径
BACKGROUND_PATH = "./images/background.png"
# 敌机图像路径
ENEMY_PATH = "./images/enemy1.png"
# 定义闯将敌机事件常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 定义英雄的图片路径
HERO_PATH = "./images/me1.png"
# 定义英雄的移动速度
HERO_SPEED = 2
# 定义发射子弹的事件
EVENT_BULLET = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """
    飞机大战游戏精灵
    """

    def __init__(self, image_name, speed=1, *groups):
        # 调用父类的初始化方法
        super().__init__(*groups)

        # 定义对子昂的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在屏幕垂直方向上面移动
        self.rect.y += self.speed


class BackGround(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):
        # 初始化背景图像
        super().__init__(image_name=BACKGROUND_PATH)

        # 如果是替换背景图像，则调整背景图像位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 1. 调用父类的update()方法
        super().update()

        # 2. 调正背景图像位置
        if self.rect.y > SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    def __init__(self):
        # 调用父类的init方法初始化敌机
        super().__init__(ENEMY_PATH)

        # 设置敌机的初始速度
        self.speed = random.randint(1, 3)

        # 设置敌机初始位置
        self.rect.bottom = 0
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)

    def update(self):
        # 调用父类的update方法来使敌机在Y抽方向运动
        super().update()

        # 一旦敌机飞出屏幕则销毁敌机
        if self.rect.y > SCREEN_RECT.height:
            # 销毁敌机
            self.kill()

    def __del__(self):
        # print("敌机被摧毁...")
        pass


class Hero(GameSprite):
    def __init__(self):
        # 调用父类的初始化方法
        super().__init__(HERO_PATH, speed=0)

        # 设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 新建子弹精灵组
        self.bullet_group = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed

        # 控制英雄飞机不能飞出屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        for i in range(0, 3):
            bullet = Bullet()
            bullet.rect.centerx = self.rect.centerx
            bullet.rect.y = self.rect.y - i * 20
            self.bullet_group.add(bullet)


class Bullet(GameSprite):
    def __init__(self):
        super().__init__("./images/bullet1.png", -2)

    def update(self):
        # 调用父类的update方法让子弹向上飞行
        super().update()

        # 子弹飞出屏幕上方则被销毁
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        # 销毁字典
        print("子弹被销毁...")