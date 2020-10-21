import random
import time

import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, K_w, K_s, K_a, K_d, K_SPACE, K_LEFT, K_RIGHT, RLEACCEL
from pygame.math import Vector2

#things I kind of wat to do
#Background, highscore saving, powerup(protects from raindrops), start screen

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

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
        self.position = Vector2(20, 20)
        self.last_tick = pygame.time.get_ticks()

    def render(self, screen):
        screen.blit(self.label, self.position)
        screen.blit(self.score, (self.position.x + self.label.get_width() + 5, self.position.y))

    def update(self):
        self.last_tick = pygame.time.get_ticks()
        self.score = self.font.render(str(self.last_tick), True, self.color)

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

class Puddle(pygame.sprite.Sprite):
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


        self.hitbox = pygame.Rect(self.rect.x + 10, self.rect.y + 10, self.rect.width - 20, self.rect.height -  20)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(pygame.Color('lightgrey'))
clock = pygame.time.Clock()

ADDRAINDROP = pygame.USEREVENT + 1
pygame.time.set_timer(ADDRAINDROP, 300)

background0 = Background(0)
background1 = Background(1)
player = Player()
puddle = Puddle()
raindrops = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
obstacles.add(puddle)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(puddle)
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
    puddle.update()
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