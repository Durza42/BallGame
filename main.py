import pygame
import game

def init():
    pygame.init()

    screen = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption('Hello World!')

    return screen

def main():
    screen = init()
    game.main_loop(screen)

main()