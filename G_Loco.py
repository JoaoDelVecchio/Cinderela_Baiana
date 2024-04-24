import pygame
from Enemy import Enemy


class G(Enemy):

    def __init__(self):
        super(G, self).__init__()
        image = pygame.image.load("images/G-removebg-preview.png")
        image.convert()
        image = pygame.transform.scale(image, (60, 60))
        self.image = image
        self.health = 3
        self.speed = 2.0

    def take_damage(self):
        self.health = self.health - 1
        if self.health == 2:
            image = pygame.image.load("images/berinjela.png")
            image.convert()
            image = pygame.transform.scale(image, (100, 100))
            self.image = image
            
            self.aux = self.aux * self.speed / 1.1
            self.speed = 1.1
            
        elif self.health == 1:
            image = pygame.image.load("images/bomb_pix.png")
            image.convert()
            image = pygame.transform.scale(image, (80, 80))
            self.image = image
            self.aux = self.aux * self.speed / 1
            self.speed = 1
