import pygame
from tower import tower

class dart_monkey(tower):

    def __init__(self):
        image = pygame.image.load("images/tower.png")
        image.convert()
        image = pygame.transform.scale(image, (50, 50))
        self.image = image
        self.damage = 1
        self.attack_speed = 1