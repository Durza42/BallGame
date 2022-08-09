import pygame, sys
from Sprite import Sprite

def main_loop(screen):
    character = Sprite('imgs/avatar.bmp')
    while True:
        manage_events(character)
        refresh(screen, character)

def manage_events(character):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                character.go_up()
            if event.key == pygame.K_LEFT:
                character.go_left()
            if event.key == pygame.K_DOWN:
                character.go_down()
            if event.key == pygame.K_RIGHT:
                character.go_right()


def refresh(screen, character):
    background = (0, 0, 0)
    screen.fill (background)

    pygame.Surface.blit(screen, character.get_look(),
                                character.get_pos())

    pygame.display.update()
