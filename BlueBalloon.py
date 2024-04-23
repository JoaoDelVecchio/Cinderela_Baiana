import pygame
from Enemy import Enemy


class BlueBalloon(Enemy):

    def __init__(self):
        super(BlueBalloon, self).__init__()
        image = pygame.image.load("images/berinjela.png")
        image.convert()
        image = pygame.transform.scale(image, (70, 70))
        self.image = image
        self.health = 2
        self.speed = 1.5

    def take_damage(self):
        self.health = self.health - 1
        image = pygame.image.load("images/enemy.png")
        image.convert()
        image = pygame.transform.scale(image, (55, 55))
        self.image = image

        self.aux = self.aux * self.speed
        self.speed = 1
