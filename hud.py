import pygame

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
