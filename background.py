import pygame

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