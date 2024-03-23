import pygame
from Enemy import Enemy

class BlueBalloon(Enemy):

    def __init__(self):
        super(BlueBalloon, self).__init__()
        image = pygame.image.load("images/enemy2.png")
        image.convert()
        image = pygame.transform.scale(image, (40, 40))
        self.image = image
        self.health = 2
        self.speed = 1

    def take_damage(self):
        self.health = self.health - 1
        image = pygame.image.load("images/enemy.png")
        image.convert()
        image = pygame.transform.scale(image, (60, 60))
        self.image = image
