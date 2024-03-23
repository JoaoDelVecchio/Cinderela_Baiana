import pygame
from Enemy import Enemy


class GreenBalloon(Enemy):

    def __init__(self):
        super(GreenBalloon, self).__init__()
        image = pygame.image.load("images/enemy3.png")
        image.convert()
        image = pygame.transform.scale(image, (60, 60))
        self.image = image
        self.health = 3
        self.speed = 1.2

    def take_damage(self):
        self.health = self.health - 1
        if self.health == 2:
            image = pygame.image.load("images/enemy2.png")
            image.convert()
            image = pygame.transform.scale(image, (35, 35))
            self.image = image
            self.aux = self.aux * self.speed / 1.1
            self.speed = 1.1
        elif self.health == 1:
            image = pygame.image.load("images/enemy.png")
            image.convert()
            image = pygame.transform.scale(image, (55, 55))
            self.image = image
            self.aux = self.aux * self.speed / 1
            self.speed = 1
