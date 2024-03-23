import pygame
from Enemy import Enemy


class RedBalloon(Enemy):

    def __init__(self):
        super(RedBalloon, self).__init__()
        image = pygame.image.load("images/enemy.png")
        image.convert()
        image = pygame.transform.scale(image, (55, 55))
        self.image = image
        self.health = 1
        self.speed = 1

    def take_damage(self):
        self.health = self.health - 1
