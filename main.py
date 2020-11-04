import random
import time

import pygame
from pygame.locals import (K_ESCAPE, K_LEFT, K_RIGHT, K_SPACE, KEYDOWN, QUIT, RLEACCEL, K_a, K_d, K_s, K_w)

from background import Background
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from hud import HUD
from lumber import Lumber
from player import Player
from raindrop import Raindrop

#things I kind of want to do
#highscore saving, powerup(protects from raindrops), start screen

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(pygame.Color('lightgrey'))
clock = pygame.time.Clock()

ADDRAINDROP = pygame.USEREVENT + 1
pygame.time.set_timer(ADDRAINDROP, 300)

backgrounds = [Background(0), Background(1)]
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

    screen.fill(pygame.Color('lightgrey'))
    for background in backgrounds:
        background.update()
        background.render(screen)

    for entity in all_sprites:
        entity.render(screen)
    hud.render(screen)

    pygame.display.flip()

    if pygame.sprite.spritecollideany(player.hitbox, obstacles):
        time.sleep(2)
        player.kill()
        running = False

    clock.tick(60)
