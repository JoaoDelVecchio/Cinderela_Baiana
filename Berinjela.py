import pygame
from Enemy import Enemy


class Berinjela(Enemy):

    def __init__(self):
        super(Berinjela, self).__init__()
        image = pygame.image.load("images/berinjela.png")
        image.convert()
        image = pygame.transform.scale(image, (100, 100))
        self.image = image
        self.health = 2
        self.speed = 4.0

    def take_damage(self):
        self.health = self.health - 1
        image = pygame.image.load("images/bomb_pix.png")
        image.convert()
        image = pygame.transform.scale(image, (80, 80))
        self.image = image

        self.aux = self.aux * self.speed
        self.speed = 1
