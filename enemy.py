class enemy:
    x = 0
    y = 190
    aux = 0
    health = None
    image = None
    speed = None

    def __init__(self):
        print('oi')

    def movement(self, screen):
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

        screen.blit(self.image, (self.x, self.y))