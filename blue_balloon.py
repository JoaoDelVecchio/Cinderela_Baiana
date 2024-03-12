import pygame
from enemy import enemy

class blue_balloon(enemy):

    def __init__(self):
        super(blue_balloon, self).__init__()
        image = pygame.image.load("images/enemy2.png")
        image.convert()
        image = pygame.transform.scale(image, (50, 50))
        self.image = image
        self.health = 2
        self.speed = 1.5
