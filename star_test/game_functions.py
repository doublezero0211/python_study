import sys
import pygame
from star import Star 


def update_screen(ai_settings, screen, stars):
    screen.fill(ai_settings.bg_color)
    stars.draw(screen)
    pygame.display.flip()

def get_number_star_x(ai_settings, star_width):
    avaliable_space_x = ai_settings.screen_width - 2 * star_width
    number_stars_x = int(avaliable_space_x/(2 * star_width))
    return number_stars_x

def get_number_rows(ai_settings, star_height):
    avaliable_space_y = ai_settings.screen_height - 3 * star_height
    number_rows = int(avaliable_space_y / (star_height * 2))
    return number_rows

def create_star(ai_settings, screen, stars, star_number, row_number):
    star = Star(ai_settings, screen)
    star_width = star.rect.width
    star.x = star_width + 2 * star_width * star_number
    star.rect.x = star.x
    star.rect.y = star.rect.height + 2 * star.rect.height * row_number

    stars.add(star)

def create_stars(ai_settings, screen, stars):
    star = Star(ai_settings, screen)
    number_stars_x = get_number_star_x(ai_settings, star.rect.width)
    number_rows = get_number_rows(ai_settings, star.rect.height)
    
    for row_number in range(number_rows):
        for star_number in range(number_stars_x):
            create_star(ai_settings, screen, stars, star_number, row_number)

def check_events(ai_settings, screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()



