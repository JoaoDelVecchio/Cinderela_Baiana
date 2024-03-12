import pygame
from enemy import enemy

class red_balloon(enemy):

    def __init__(self):
        super(red_balloon, self).__init__()
        image = pygame.image.load("images/enemy.png")
        image.convert()
        image = pygame.transform.scale(image, (50, 50))
        self.image = image
        self.health = 1
        self.speed = 1
