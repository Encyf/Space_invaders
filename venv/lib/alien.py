import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        self.image = pygame.image.load('/Users/RBa/PycharmProjects/Space_invaders/venv/images/FishEgg-icon.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.right
        self.rect.y = self.rect.top

        #self.x = float(self.rect.x)

print(Alien.__dict__)