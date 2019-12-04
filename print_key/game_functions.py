import sys
import pygame

def check_keydown_events(event):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        print(event.key)
    elif event.key == pygame.K_LEFT:
        print(event.key)
    elif event.key == pygame.K_UP:
        print(event.key)
    elif event.key == pygame.K_DOWN:
        print(event.key)


def check_events():
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event)



