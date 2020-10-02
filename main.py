import random
import time

import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, K_w, K_s, K_a, K_d, K_SPACE, RLEACCEL

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

def hitbox_collision(player, entity):
    hitbox = player.hitbox
    rect = entity.rect
    if (rect.x + rect.width) > hitbox[0] and rect.x < (hitbox[0] + hitbox[2]):
        if (rect.y + rect.height) > hitbox[1] and rect.y < (hitbox[1] + hitbox[3]):
            return True

class Enemy(pygame.sprite.Sprite):
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
        self.hitbox = pygame.Rect(self.rect.x + 10, self.rect.y + 10, self.rect.width - 20, self.rect.height -  20)

    def render(self, screen):
        screen.blit(self.surf, self.rect)
        #pygame.draw.rect(screen, pygame.Color('yellow'), self.hitbox, 2)

    def handle_keys(self, keys):
        #if keys[K_w]:
            #self.rect.move_ip(0, -self.speed)
        #elif keys[K_s]:
            #self.rect.move_ip(0, self.speed)
        if not self.jumping:
            if keys[K_a]:
                self.speed_x = -10
            elif keys[K_d]:
                self.speed_x = 10
            elif keys[K_SPACE]:
                self.jumping = True
                self.speed_y = -50
            else:
                self.speed_x = 0

        if self.jumping:
            self.speed_y += self.gravity

    def update(self):
        self.rect.move_ip(self.speed_x, self.speed_y)

        if self.rect.left <= 0:
            self.rect.left = 0
            self.speed_x = 0
        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.speed_x = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.jumping = False
            self.speed_y = 0

        self.hitbox = pygame.Rect(self.rect.x + 10, self.rect.y + 10, self.rect.width - 20, self.rect.height -  20)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(pygame.Color('lightgrey'))
clock = pygame.time.Clock()

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

player = Player()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
    pressed_keys = pygame.key.get_pressed()

    player.handle_keys(pressed_keys)
    player.update()
    enemies.update()

    screen.fill(pygame.Color('lightgrey'))
    for entity in all_sprites:
        entity.render(screen)

    pygame.display.flip()

    if pygame.sprite.spritecollideany(player, enemies, hitbox_collision):
        time.sleep(2)
        player.kill()
        running = False

    clock.tick(60)