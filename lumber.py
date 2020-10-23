import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Lumber(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.surf = pygame.Surface((60,20))
        self.color = pygame.Color('chocolate4')
        self.surf.fill(self.color)
        self.rect = self.surf.get_rect()
        self.rect.bottomleft = (SCREEN_WIDTH, SCREEN_HEIGHT)
        self.speed = -5

    def render(self, screen):
        screen.blit(self.surf, self.rect)

    def update(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.right <= 0:
            self.rect.left = SCREEN_WIDTH