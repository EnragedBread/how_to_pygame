import pygame
from pygame.locals import K_w, K_s, K_a, K_d, K_SPACE, K_LEFT, K_RIGHT, RLEACCEL

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from hitbox import Hitbox

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.image.load('player_1.png').convert()
        self.surf.set_colorkey(pygame.Color('white'), RLEACCEL)
        self.rect = self.surf.get_rect(
            center = (
                (SCREEN_WIDTH - self.surf.get_width()) // 2,
                SCREEN_HEIGHT - (self.surf.get_height() // 2)
            )
        )
        self.speed_x = 0
        self.speed_y = 0
        self.jumping = False
        self.gravity = 5
        self.hitbox = Hitbox(self)

    def render(self, screen):
        screen.blit(self.surf, self.rect)

    def handle_keys(self, keys):
        if keys[K_a] or keys[K_LEFT]:
            self.speed_x = -10
        elif keys[K_d] or keys[K_RIGHT]:
            self.speed_x = 10
        else:
            self.speed_x = 0
        if (keys[K_SPACE] or keys[K_w]) and not self.jumping:
            self.jumping = True
            self.speed_y = -50

        self.speed_y += self.gravity

    def update(self):
        self.rect.move_ip(self.speed_x, self.speed_y)

        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.jumping = False

        self.hitbox.update()