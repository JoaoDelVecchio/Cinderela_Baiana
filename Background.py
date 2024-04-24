import pygame
from math import sqrt

class Background:
    image = None
    margin = None
    tower_icon1 = None
    tower_icon2 = None
    tower_icon3 = None
    money_icon1 = None
    money_icon2 = None
    money_icon3 = None
    lago_range = 160
    x_lago, y_lago = [472,345]
    x_margem_l, x_margem_r, y_margem_s, y_margem_i = [40, 927, 71, 650]

    def __init__(self):
        image = pygame.image.load("images/MAPA CINDERELA BAHIANA(1).jpg")
        image.convert()
        image = pygame.transform.scale(image, (1024,768))
        self.image = image

        margin = pygame.image.load("images/new_margim2.png")
        margin.convert()
        margin = pygame.transform.scale(margin, (1000, 1000))
        self.margin = margin

        tower_icon1 = pygame.image.load("images/calabresa-removebg-preview.png")
        tower_icon1.convert()
        tower_icon1 = pygame.transform.scale(tower_icon1, (120, 120))
        self.tower_icon1 = tower_icon1

        tower_icon2 = pygame.image.load("images/js-removebg-preview.png")
        tower_icon2.convert()
        tower_icon2 = pygame.transform.scale(tower_icon2, (125, 125))
        self.tower_icon2 = tower_icon2
        
        tower_icon3 = pygame.image.load("images/submarine.png")
        tower_icon3.convert()
        tower_icon3 = pygame.transform.scale(tower_icon3, (140,140))
        self.tower_icon3 = tower_icon3

        font = pygame.font.SysFont('Calibri', 40, True)
        self.money_icon1 = font.render("Cost: 100", True, (0, 0, 0))
        self.money_icon2 = font.render("Cost: 200", True, (0, 0, 0))
        self.money_icon3 = font.render("Cost: 400", True, (0, 0, 0))

    def raio_do_lago(self, x0, y0):
        distance = sqrt(((self.x_lago) - x0)**2 + ((self.y_lago) - y0)**2)
        if( distance <= self.lago_range):
            return True
        else:
            return False
        
    def limites_laterais(self, x0, y0):
        if x0 - self.x_margem_l < 0 or x0 - self.x_margem_r > 0 or y0 - self.y_margem_s < 0 or y0 - self.y_margem_i > 0:
            return False
        else:
            return True
        
        
    def draw(self, screen):
        screen.blit(self.image, (0, 0))
        screen.blit(self.margin, (1024, -20))
        screen.blit(self.tower_icon1, (1040, 80))
        screen.blit(self.tower_icon2, (1046, 280))
        screen.blit(self.tower_icon3, (1046, 440))
        screen.blit(self.money_icon1, (1040, 20))
        screen.blit(self.money_icon2, (1040, 220))
        screen.blit(self.money_icon3, (1040, 420))
