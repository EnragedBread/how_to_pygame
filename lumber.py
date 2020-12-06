import pygame
from pygame.locals import RLEACCEL

from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Lumber(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.surf = pygame.image.load('log.png').convert()
        self.surf.set_colorkey(pygame.Color('white'), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.bottomleft = (SCREEN_WIDTH, SCREEN_HEIGHT)
        self.speed = -5

        self.mask = pygame.mask.from_surface(self.surf)

    def render(self, screen):
        screen.blit(self.surf, self.rect)

    def update(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.right <= 0:
            self.rect.left = SCREEN_WIDTH