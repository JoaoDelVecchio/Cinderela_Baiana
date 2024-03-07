import pandas
import pygame

class enemy:
    health = None
    image = None
    speed = None
    def __init__(self, type):
        if type == 1:
            self.health = 1
            self.speed = 1
            self.image = "C:/projeto 1 (csi-22)/images/enemy.png"
        if type == 2:
            self.health = 1
            self.speed = 1
            self.image = "C:/projeto 1 (csi-22)/images/enemy2.png"

    def draw(self):
        self.image = None

class tower:
    damage = None
    attack_speed = None
    image = None
    type = None
    def __init__(self, type):
        self.type = type
        if type == 1:
            self.damage = 1
            self.attack_speed = 1
            self.image = "C:/projeto 1 (csi-22)/images/tower.png"
        if type == 2:
            self.damage = 2
            self.attack_speed = 2
            self.image = None

    def draw(self):
        pass

class background:
    image = None

    def __init__(self):
        self.image = "C:/projeto 1 (csi-22)/images/background.png"

    def draw(self, screen):
        pass
        x = 0

class game:

    def __init__(self, screen, size):
        pass

    def loop(self):
        pass

Game = game()
