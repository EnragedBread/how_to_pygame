import random
import time

import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, K_w, K_s, K_a, K_d, K_SPACE, K_LEFT, K_RIGHT, RLEACCEL

from player import Player
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from raindrop import Raindrop
from lumber import Lumber

#things I kind of wat to do
#highscore saving, powerup(protects from raindrops), start screen

def hitbox_collision(player, entity):
    hitbox = player.hitbox
    rect = entity.rect
    if (rect.x + rect.width) > hitbox[0] and rect.x < (hitbox[0] + hitbox[2]):
        if (rect.y + rect.height) > hitbox[1] and rect.y < (hitbox[1] + hitbox[3]):
            return True

class Background():
    def __init__(self, id):
        self.image = pygame.image.load('mountain_background.png').convert()
        self.id = id
        self.rect = self.image.get_rect()
        self.rect.x = self.id * self.rect.width
        self.speed = -2

    def render(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.right <= 0:
            self.rect.left = self.rect.width

class HUD():
    def __init__(self):
        self.font = pygame.font.Font(None, 30)
        self.color = pygame.Color('black')
        self.label = self.font.render("Score: ", True, self.color)
        self.position = (20, 20)
        self.last_tick = pygame.time.get_ticks()

    def render(self, screen):
        screen.blit(self.label, self.position)
        screen.blit(self.score, (self.position[0] + self.label.get_width() + 5, self.position[1]))

    def update(self):
        self.last_tick = pygame.time.get_ticks()
        self.score = self.font.render(str(self.last_tick), True, self.color)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(pygame.Color('lightgrey'))
clock = pygame.time.Clock()

ADDRAINDROP = pygame.USEREVENT + 1
pygame.time.set_timer(ADDRAINDROP, 300)

background0 = Background(0)
background1 = Background(1)
player = Player()
lumber = Lumber()
raindrops = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
obstacles.add(lumber)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(lumber)
hud = HUD()

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
        elif event.type == ADDRAINDROP:
            new_raindrop = Raindrop()
            raindrops.add(new_raindrop)
            all_sprites.add(new_raindrop)
            obstacles.add(new_raindrop)
    pressed_keys = pygame.key.get_pressed()

    player.handle_keys(pressed_keys)
    player.update()
    lumber.update()
    raindrops.update()
    hud.update()
    background0.update()
    background1.update()

    screen.fill(pygame.Color('lightgrey'))

    background0.render(screen)
    background1.render(screen)
    for entity in all_sprites:
        entity.render(screen)
    hud.render(screen)

    pygame.display.flip()

    if pygame.sprite.spritecollideany(player, obstacles, hitbox_collision):
        time.sleep(2)
        player.kill()
        running = False

    clock.tick(60)