import random

import pygame
from pygame.locals import RLEACCEL

from constants import SCREEN_HEIGHT, SCREEN_WIDTH


class Raindrop(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.image.load('raindrop.png').convert()
        self.surf.set_colorkey(pygame.Color('white'), RLEACCEL)
        self.rect = self.surf.get_rect(
            center = (
                random.randint(0, SCREEN_WIDTH),
                random.randint(-40, -10)
            )
        )
        self.speed = random.randint(5, 10)

        self.mask = pygame.mask.from_surface(self.surf)

    def render(self, screen):
        screen.blit(self.surf, self.rect)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()