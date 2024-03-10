import pygame

class enemy:
    health = None
    image = None
    speed = None
    x = 0
    y = 190
    aux = 0

    def __init__(self, type):
        if type == 1:
            image = pygame.image.load("images/enemy.png")
            image.convert()
            image = pygame.transform.scale(image, (50, 50))
            self.image = image
            self.health = 1
            self.speed = 1
        if type == 2:
            image = pygame.image.load("images/enemy2.png")
            image.convert()
            image = pygame.transform.scale(image, (50, 50))
            self.image = image
            self.health = 5
            self.speed = 0.5

    def movement(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update(self):
        self.aux = self.aux + 1
        if self.aux * self.speed <= 225:
            self.x = self.x + self.speed
        elif 225 < self.aux * self.speed <= 340:
            self.y = self.y - self.speed
        elif 340 < self.aux * self.speed <= 425:
            self.x = self.x - self.speed
        elif 425 < self.aux * self.speed <= 730:
            self.y = self.y + self.speed
        elif 730 < self.aux * self.speed <= 810:
            self.x = self.x - self.speed
        elif 810 < self.aux * self.speed <= 920:
            self.y = self.y - self.speed
        elif 920 < self.aux * self.speed <= 1145:
            self.x = self.x + self.speed
        elif 1145 < self.aux * self.speed <= 1280:
            self.y = self.y - self.speed
        elif 1280 < self.aux * self.speed <= 1340:
            self.x = self.x + self.speed
        elif 1340 < self.aux * self.speed <= 1540:
            self.y = self.y + self.speed
        elif 1540 < self.aux * self.speed <= 1680:
            self.x = self.x - self.speed
        elif 1540 < self.aux * self.speed <= 1690:
            self.x = self.x - self.speed
        elif 1690 < self.aux * self.speed <= 1820:
            self.y = self.y + self.speed

