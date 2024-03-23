import math
from math import sqrt
from Projectile import Projectile


class Tower:
    damage = None
    attack_speed = None
    range = None
    pos = (0, 0)
    image = None
    projectiles = []
    cooldown = 101

    def __init__(self):
        pass

    def enemy_in_range(self, enemy_instances):
        track_length = 0
        x = 0
        y = 0
        for enemy in enemy_instances:
            distance = sqrt((enemy.x - self.pos[0])**2 + (enemy.y - self.pos[1])**2)
            if distance <= self.range:
                if enemy.track_length >= track_length:
                    track_length = enemy.track_length
                    x = enemy.x
                    y = enemy.y

        return x, y

    def attack(self, enemy_instances):
        self.cooldown = self.cooldown + self.attack_speed
        if self.cooldown <= 100:
            pass
        else:
            self.cooldown = 0
            (x, y) = self.enemy_in_range(enemy_instances)
            if (x, y) == (0, 0):
                pass
            else:
                self.projectiles.append(Projectile(x, y, self.pos[0], self.pos[1]))
                self.projectiles = self.projectiles.copy()

    def draw(self, screen):
        screen.blit(self.image, self.pos)
        for projectile in self.projectiles:
            projectile.x = projectile.x + projectile.x_speed
            projectile.y = projectile.y + projectile.y_speed
            screen.blit(projectile.image, (projectile.x, projectile.y))
