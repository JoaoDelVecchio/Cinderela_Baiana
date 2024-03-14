import pygame
from Background import Background
from RedBalloon import RedBalloon
from BlueBalloon import BlueBalloon
from DartMonkey import DartMonkey
from SuperMonkey import SuperMonkey


class Game:
    width = 800
    height = 800
    screen = None
    map = None
    money = 0
    health = 100
    enemy_instances = []
    tower_instances = []

    hold_image = 0
    tower_icon = None

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.map = Background()
        self.map.draw(self.screen)

    def health_money_icons(self, screen):
        font = pygame.font.SysFont(None, 30)

        health_icon = font.render("health:" + str(self.health), True, (250, 0, 0))
        money_icon = font.render("money:" + str(self.money), True, (250, 0, 0))
        screen.blit(health_icon, (50, 25))
        screen.blit(money_icon, (200, 25))

    def handle_events(self):

        if self.hold_image != 0:
            pos = pygame.mouse.get_pos()
            self.screen.blit(self.tower_icon, pos)

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.hold_image == 1:
                    self.tower_instances.append(SuperMonkey())
                if self.hold_image == 2:
                    self.tower_instances.append(DartMonkey())
                self.hold_image = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.hold_image = 1
                    self.tower_icon = pygame.image.load("images/tower.png")
                    self.tower_icon.convert()
                    self.tower_icon = pygame.transform.scale(self.tower_icon, (75, 75))
                if event.key == pygame.K_2:
                    self.hold_image = 2
                    self.tower_icon = pygame.image.load("images/tower2.png")
                    self.tower_icon.convert()
                    self.tower_icon = pygame.transform.scale(self.tower_icon, (75, 75))


    def loop(self):

        i = 0

        instance1 = DartMonkey()
        self.tower_instances.append(instance1)

        while i <= 100000:
            self.map.draw(self.screen)

            self.handle_events()

            if i % 200 == 0:
                instance = RedBalloon()
                self.enemy_instances.append(instance)

            if i % 400 == 0:
                instance = BlueBalloon()
                self.enemy_instances.append(instance)

            for ins in self.enemy_instances:
                ins.movement(self.screen)
                if ins.detect_projectile():
                    ins.take_damage()
                    self.money = self.money + 1

            for ins in self.tower_instances:
                ins.enemy_in_range()
                ins.draw(self.screen)

            self.health_money_icons(self.screen)

            i = i + 1
            pygame.display.update()


game = Game()
game.loop()
