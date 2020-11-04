import pygame

class Hitbox():
    @staticmethod
    def collision(player, entity):
        rect = entity.rect
        if (rect.x + rect.width) > player.hitbox.x() and rect.x < (player.hitbox.x() + player.hitbox.width()):
            if (rect.y + rect.height) > player.hitbox.y() and rect.y < (player.hitbox.y() + player.hitbox.height()):
                return True

    def __init__(self, player):
        self.player = player
        player_rect = self.player.rect
        self.hitbox = pygame.Rect(player_rect.x + 10, player_rect.y + 10, player_rect.width - 20, player_rect.height -  20)

    def x(self):
        return self.hitbox.x

    def y(self):
        return self.hitbox.y

    def height(self):
        return self.hitbox.height

    def width(self):
        return self.hitbox.width

    def update(self):
        player_rect = self.player.rect
        self.hitbox = pygame.Rect(player_rect.x + 10, player_rect.y + 10, player_rect.width - 20, player_rect.height -  20)

    def render(self, screen):
        pass
