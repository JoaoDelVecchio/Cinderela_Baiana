import pygame
from Enemy import Enemy


class Bomb(Enemy):

    def __init__(self):
        super(Bomb, self).__init__()
        image = pygame.image.load("images/bomb_pix.png")
        image.convert()
        image = pygame.transform.scale(image, (80, 80))
        self.image = image
        self.health = 1
        self.speed = 2

    def take_damage(self):
        self.health = self.health - 1
