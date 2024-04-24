import pygame
from Tower import Tower


class Calabresa(Tower):

    def __init__(self):
        image = pygame.image.load("images/calabresa-removebg-preview.png")
        image.convert()
        image = pygame.transform.scale(image, (80, 80))
        self.image = image
        self.damage = 1
        self.attack_speed = 1.5
        self.range = 200
