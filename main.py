import pygame

from scene_manager import SceneManager

#things I kind of want to do
#highscore saving, powerup(protects from raindrops), start screen

def main():
    scenemanager = SceneManager()
    scenemanager.loop()

if __name__ == "__main__":
    pygame.init()
    main()