import pygame
from Enemy import Enemy

class RedBalloon(Enemy):

    def __init__(self):
        super(RedBalloon, self).__init__()
        image = pygame.image.load("images/enemy.png")
        image.convert()
        image = pygame.transform.scale(image, (60, 60))
        self.image = image
        self.health = 1
        self.speed = 0.8

    def take_damage(self):
        self.health = self.health - 1

        
    
    

