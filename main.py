import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

class Player():
    def __init__(self):
        self.surf = pygame.Surface((100, 40))
        self.surf.fill(pygame.Color('blue'))
    def render(self, screen):
        screen.blit(self.surf, (30,30))

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
    clock.tick(60)
    player.render(screen)
    pygame.display.flip()