import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, K_w, K_s, K_a, K_d, RLEACCEL

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Player():
    def __init__(self):
        self.surf = pygame.image.load('player_1.png')
        self.surf.set_colorkey(pygame.Color('white'), RLEACCEL)
        #use for custom no transparent background image
        #self.surf =  pygame.image.load('yourimagehere.png').convert()
        self.rect = self.surf.get_rect()
        self.speed = 5

    def render(self, screen):
        screen.blit(self.surf, self.rect)

    def handle_event(self, event):
        pass

    def update(self, keys):
        if keys[K_w]:
            self.rect.move_ip(0, -self.speed)
        elif keys[K_s]:
            self.rect.move_ip(0, self.speed)
        elif keys[K_a]:
            self.rect.move_ip(-self.speed, 0)
        elif keys[K_d]:
            self.rect.move_ip(self.speed, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        elif self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(pygame.Color('lightgrey'))
clock = pygame.time.Clock()

player = Player()

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    clock.tick(60)
    screen.fill(pygame.Color('lightgrey'))
    player.render(screen)
    pygame.display.flip()