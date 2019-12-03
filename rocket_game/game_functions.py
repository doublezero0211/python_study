import sys
import pygame

def check_keydown_events(event, rocket):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = True
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = True
    elif event.key == pygame.K_UP:
        rocket.moving_top = True
    elif event.key == pygame.K_DOWN:
        rocket.moving_bottom = True

def check_keyup_events(event, rocket):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = False
    elif event.key == pygame.K_UP:
        rocket.moving_top = False
    elif event.key == pygame.K_DOWN:
        rocket.moving_bottom = False

def check_events(rocket):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, rocket)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, rocket)



def update_screen(ai_settings, screen, rocket):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时，重绘屏幕
    screen.fill(ai_settings.bg_color)
    rocket.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()
