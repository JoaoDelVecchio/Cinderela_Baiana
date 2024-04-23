import pygame


class Background:
    image = None
    margin = None
    tower_icon1 = None
    tower_icon2 = None
    money_icon1 = None
    money_icon2 = None

    def __init__(self):
        image = pygame.image.load("images/MAPA_CINDERELA BAHIANA.jpg")
        image.convert()
        image = pygame.transform.scale(image, (1024,768))
        self.image = image

        margin = pygame.image.load("images/margin.png")
        margin.convert()
        margin = pygame.transform.scale(margin, (100, 768))
        self.margin = margin

        tower_icon1 = pygame.image.load("images/tower.png")
        tower_icon1.convert()
        tower_icon1 = pygame.transform.scale(tower_icon1, (150, 150))
        self.tower_icon1 = tower_icon1

        tower_icon2 = pygame.image.load("images/tower2.png")
        tower_icon2.convert()
        tower_icon2 = pygame.transform.scale(tower_icon2, (150, 150))
        self.tower_icon2 = tower_icon2

        font = pygame.font.SysFont(None, 40)
        self.money_icon1 = font.render("cost: 200", True, (250, 0, 0))
        self.money_icon2 = font.render("cost: 400", True, (250, 0, 0))

    def draw(self, screen):
        screen.blit(self.image, (0, 0))
        screen.blit(self.margin, (1024, 0))
        screen.blit(self.tower_icon1, (1026, 100))
        screen.blit(self.tower_icon2, (1026, 300))
        screen.blit(self.money_icon1, (1026, 75))
        screen.blit(self.money_icon2, (1026, 275))
