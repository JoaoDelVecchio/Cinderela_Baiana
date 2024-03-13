import pygame
from Enemy import Enemy

class RedBalloon(Enemy):

    def __init__(self):
        super().__init__()
        self.name = 'Red Ballon'
        image = pygame.image.load("images/enemy.png")
        image.convert()
        image = pygame.transform.scale(image, (50, 50))
        self.image = image
        self.health = 1
        self.speed = 1
        self.area = 1
        
    
    

