import random

import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH

class Raindrop(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.surf = pygame.Surface((20,20))
        self.color = pygame.Color('blue')
        self.surf.fill(self.color)
        self.rect = self.surf.get_rect(
            center = (
                random.randint(0, SCREEN_WIDTH),
                random.randint(-40, -10)
            )
        )
        self.speed = random.randint(5, 10)

    def render(self, screen):
        screen.blit(self.surf, self.rect)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()