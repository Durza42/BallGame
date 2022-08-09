import pygame
from pygame.locals import *
import pygame, sys

def init():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption('Hello World!')
    return screen

def main_loop(screen):
    while True:
        sysFont = pygame.font.SysFont("None", 32)
        rendered = sysFont.render('Hello World', 0, (255,100, 100))
        screen.blit(rendered, (100, 100))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

def main():
    screen = init()
    main_loop(screen)

main()