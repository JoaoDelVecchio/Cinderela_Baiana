import pygame

class background:
    image = None

    def __init__(self):
        image = pygame.image.load("images/map.png")
        image.convert()
        image = pygame.transform.scale(image, (500, 500))
        self.image = image

    def draw(self, screen):
        screen.blit(self.image, (0, 0))

print('teste')