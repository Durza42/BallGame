import pygame

class Sprite:
    look = pygame.Surface((50, 50))
    pos = pygame.Rect(100, 200, 50, 50)

    def __init__(self, path):
        self.look = pygame.image.load(path).convert()
        pass
    def get_look(self):
        return self.look
    def get_pos(self):
        return self.pos

    def go_right(self):
        self.pos[0] += 10
    def go_left(self):
        self.pos[0] -= 10
    def go_up(self):
        self.pos[1] -= 10
    def go_down(self):
        self.pos[1] += 10
