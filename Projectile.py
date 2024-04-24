import math

import pygame
from math import sqrt, acos


class Projectile:
    x = None
    y = None
    x_speed = None
    y_speed = None
    image = None
    velocity_constant = 20

    def __init__(self, enemy_x, enemy_y, tower_x, tower_y):
        image = pygame.image.load("images/projectile.png")
        image.convert()
        image = pygame.transform.scale(image, (25, 25))
        self.image = image
        self.x = tower_x
        self.y = tower_y

        distance = sqrt((enemy_x - tower_x)**2 + (enemy_y - tower_y)**2)
        if enemy_y - tower_y <= 0:
            # O ângulo inicial de -135 graus é para rotacionar a imagem para o ângulo 0 (deve-se ao jeito que a imagem
            # está na pasta) e depois rotacionar a imagem do ângulo desejado
            self.image = pygame.transform.rotate(self.image, acos((enemy_x - tower_x) / distance) * 180 / math.pi - 135)
        else:
            # O ângulo inicial de -135 graus é para rotacionar a imagem para o ângulo 0 (deve-se ao jeito que a imagem
            # está na pasta) e depois rotacionar a imagem do ângulo desejado
            self.image = pygame.transform.rotate(self.image, - acos((enemy_x - tower_x) / distance) * 180 / math.pi - 135)
        self.x_speed = self.velocity_constant * ((enemy_x - tower_x) / distance)
        self.y_speed = self.velocity_constant * ((enemy_y - tower_y) / distance)
