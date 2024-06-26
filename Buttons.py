import pygame

class Button():
    def __init__(self, x, y, image, scale, surface):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        self.surface = surface

    def draw(self, action):
        self.surface.blit(self.image, (self.rect.x, self.rect.y))

        return action


