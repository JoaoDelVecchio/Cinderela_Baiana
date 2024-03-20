import pygame
from Enemy import Enemy

class RedBalloon(Enemy):

    def __init__(self):
        super().__init__()
        self.name = 'Red Ballon'
        image = pygame.image.load("images/enemy.png")
        image.convert()
        image = pygame.transform.scale(image, (55, 55))
        self.image = image
        self.health = 1
        self.speed = 0.8
        self.area = 1
        
    
    

