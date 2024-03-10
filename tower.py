import pygame

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


