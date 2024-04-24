import pygame
from Enemy import Enemy


class G(Enemy):

    def __init__(self):
        super(G, self).__init__()
        image = pygame.image.load("images/G-removebg-preview.png")
        image.convert()
        image = pygame.transform.scale(image, (80, 80))
        self.image = image
        self.health = 3
        self.speed = 4.5

    def take_damage(self):
        self.health = self.health - 1
        if self.health == 2:
            image = pygame.image.load("images/berinjela.png")
            image.convert()
            image = pygame.transform.scale(image, (100, 100))
            self.image = image

            self.speed = 4.0
            self.aux = self.aux / (4.0 / 4.5)
            
        elif self.health == 1:
            image = pygame.image.load("images/bomb_pix.png")
            image.convert()
            image = pygame.transform.scale(image, (80, 80))
            self.image = image

            self.speed = 3.0
            self.aux = self.aux / (3.0 / 4.0)

