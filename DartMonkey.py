import pygame
from Tower import Tower


class DartMonkey(Tower):

    def __init__(self):
        image = pygame.image.load("images/tower.png")
        image.convert()
        image = pygame.transform.scale(image, (40, 40))
        self.image = image
        self.damage = 1
        self.attack_speed = 1.5
        self.range = 100
