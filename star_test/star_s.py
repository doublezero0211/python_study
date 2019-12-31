import pygame
from pygame.sprite import Group
from settings import Settings
from star import Star
import game_functions as gf

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    
    stars = Group()

    gf.create_stars(ai_settings, screen, stars)

    # 开始游戏主循环
    while True:
        gf.check_events(ai_settings, screen)
        gf.update_screen(ai_settings, screen, stars)

run_game()
