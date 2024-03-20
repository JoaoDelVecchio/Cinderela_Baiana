import math
from math import sqrt


class Tower:
    damage = None
    attack_speed = None
    range = None
    pos = (0, 0)
    image = None
    projectiles = []

    def __init__(self):
        pass

    def enemy_in_range(self, enemy_instances):
        min_distance = math.inf
        x = 0
        y = 0
        for enemy in enemy_instances:
            distance = sqrt((enemy.x - self.pos[0])**2 + (enemy.y - self.pos[1])**2)
            if distance <= self.range:
                if distance < min_distance:
                    x = enemy.x
                    y = enemy.y
        return x, y

    def attack(self, enemy_instances):
        (x, y) = self.enemy_in_range(self, enemy_instances)
        if (x, y) == (0, 0):
            pass
        else:
            pass

    def draw(self, screen):
        screen.blit(self.image, self.pos)