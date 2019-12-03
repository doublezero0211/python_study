import pygame
class Rocket():
    def __init__(self, ai_settings, screen):
        """初始化并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/rocket.bmp')

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.center = self.screen_rect.center
        # 在属性center中存储小数值
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False
    def update(self):
        """根据移动标志调整飞船位置"""
        # 更新center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.rocket_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.rocket_speed_factor
        if self.moving_top and self.rect.top > 0:
            self.centery -= self.ai_settings.rocket_speed_factor
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.rocket_speed_factor
    
        # 根据self.center更新rect对象
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
    def blitme(self):
        self.screen.blit(self.image, self.rect)
