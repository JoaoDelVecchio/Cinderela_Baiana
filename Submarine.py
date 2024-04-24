import pygame
from Tower import Tower

class Submarine(Tower):

    def __init__(self):
        image = pygame.image.load("images/submarine_front.png")
        image.convert()
        image = pygame.transform.scale(image, (150, 150))
        self.image = image
        self.damage = 3
        self.attack_speed = 1.5
        self.range = 1000
        
    