import pygame

class TitleScreen:
    image = None

    def __init__(self):
        image = pygame.image.load("images/title.jpg")
        image.convert()
        image = pygame.transform.scale(image, (1200, 768))
        self.image = image


    def draw(self, screen):
        screen.blit(self.image, (0,0))