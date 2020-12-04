import pygame

class Hitbox(pygame.sprite.Sprite):
    def __init__(self, player):
        self.player = player
        player_rect = self.player.rect
        self.rect = pygame.Rect(player_rect.x + 10, player_rect.y + 10, player_rect.width - 20, player_rect.height -  20)

    def update(self):
        player_rect = self.player.rect
        self.rect = pygame.Rect(player_rect.x + 10, player_rect.y + 10, player_rect.width - 20, player_rect.height -  20)

    def render(self, screen):
        pygame.draw.rect(screen, pygame.Color('yellow'), self.rect, 2)
