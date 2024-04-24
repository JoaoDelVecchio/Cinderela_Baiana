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

    def draw(self):
        self.surface.blit(self.image, (self.rect.x, self.rect.y))
        action = False
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(pos):
                    self.clicked = True
                    action = True
            if event.type == pygame.MOUSEBUTTONUP:
                self.clicked = False

        return action


