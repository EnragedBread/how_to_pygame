import pygame
from pygame.locals import KEYDOWN, K_SPACE

from scene import Scene
from game_scene import GameScene

class TitleScene(Scene):
    def __init__(self):
        super().__init__()
        self.font_large = pygame.font.Font(None, 60)
        self.font_small = pygame.font.Font(None, 20)
        self.title_text = self.font_large.render("Log Jumperover-er!!1!", True, pygame.Color('darkslategrey'))
        self.continue_text = self.font_small.render("press space to start!!!1!", True, pygame.Color('darkslategrey'))

    def handle_event(self, event):
        if event.type == KEYDOWN and event.key == K_SPACE:
            self.manager.switch_to(GameScene())

    def render(self, screen):
        screen.fill(pygame.Color('khaki'))
        y_offset = 0
        for text in [self.title_text, self.continue_text]:
            x = (screen.get_width() - text.get_width()) // 2
            y = (screen.get_height() - text.get_height()) // 2 + y_offset
            screen.blit(text, (x,y))
            y_offset += text.get_height() + 5

        pygame.display.flip()

    def update(self):
        pass