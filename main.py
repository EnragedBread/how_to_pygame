import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, K_w, K_s, K_a, K_d

class Player():
    def __init__(self):
        self.surf = pygame.Surface((100, 40))
        self.surf.fill(pygame.Color('blue'))
        self.rect = self.surf.get_rect()
    def render(self, screen):
        screen.blit(self.surf, self.rect)
    def handle_event(self, event):
        pass
    def update(self, keys):
        if keys[K_w]:
            self.rect.move_ip(0,-5)
        elif keys[K_s]:
            self.rect.move_ip(0,5)
        elif keys[K_a]:
            self.rect.move_ip(-5,0)
        elif keys[K_d]:
            self.rect.move_ip(5,0)

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 640:
            self.rect.right = 640
        elif self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > 480:
            self.rect.bottom = 480

pygame.init()
screen = pygame.display.set_mode((640, 480))
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