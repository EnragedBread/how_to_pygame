import time

import pygame

from background import Background
from hud import HUD
from lumber import Lumber
from player import Player
from raindrop import Raindrop
from scene import Scene

class GameScene(Scene):
    def __init__(self):
        super().__init__()
        self.ADDRAINDROP = pygame.USEREVENT + 1
        pygame.time.set_timer(self.ADDRAINDROP, 300)

        self.backgrounds = [Background(0), Background(1)]
        self.player = Player()
        self.lumber = Lumber()
        self.raindrops = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.obstacles.add(self.lumber)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.lumber)
        self.hud = HUD()

        self.collision = False

    def handle_event(self, event):
        if event.type == self.ADDRAINDROP:
            new_raindrop = Raindrop()
            self.raindrops.add(new_raindrop)
            self.all_sprites.add(new_raindrop)
            self.obstacles.add(new_raindrop)

        pressed_keys = pygame.key.get_pressed()
        self.player.handle_keys(pressed_keys)

    def render(self, screen):
        screen.fill(pygame.Color('lightgrey'))
        for background in self.backgrounds:
            background.render(screen)

        for entity in self.all_sprites:
            entity.render(screen)
        self.hud.render(screen)

        pygame.display.flip()

        if self.collision == True:
            time.sleep(2)
            self.player.kill()
            self.manager.quit()

    def update(self):
        self.player.update()
        self.lumber.update()
        self.raindrops.update()
        self.hud.update()

        for background in self.backgrounds:
            background.update()

        if pygame.sprite.spritecollideany(self.player, self.obstacles, pygame.sprite.collide_mask):
            self.collision = True