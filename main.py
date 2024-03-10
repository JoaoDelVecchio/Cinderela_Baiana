import pandas
import pygame
p

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


class tower:
    damage = None
    attack_speed = None
    image = None

    def __init__(self, type):
        if type == 1:
            image = pygame.image.load("images/tower.png")
            image.convert()
            image = pygame.transform.scale(image, (50, 50))
            self.image = image
            self.damage = 1
            self.attack_speed = 1
        if type == 2:
            pass

    def enemy_in_range(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, (200, 230))


class background:
    image = None

    def __init__(self):
        image = pygame.image.load("images/map.png")
        image.convert()
        image = pygame.transform.scale(image, (500, 500))
        self.image = image

    def draw(self, screen):
        screen.blit(self.image, (0, 0))

class game:
    width = 800
    height = 800
    screen = None
    map = None

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.map = background()
        self.map.draw(self.screen)

    def handle_events(self):
        pass

    def spawn_enemy(self, type):
        instance = enemy(type)

    def loop(self):
        i = 0

        t1 = 1
        t2 = 2
        enemy_instances = []
        instance1 = enemy(t1)
        instance2 = enemy(t2)
        enemy_instances.append(instance1)
        enemy_instances.append(instance2)

        tower_instances = []
        instance1 = tower(1)
        tower_instances.append(instance1)

        while i <= 100000:
            self.map.draw(self.screen)

            for ins in enemy_instances:
                ins.update()
                ins.movement(self.screen)

            for ins in tower_instances:
                ins.enemy_in_range()
                ins.draw(self.screen)

            i = i + 1
            pygame.display.update()



Game = game()
Game.loop()

