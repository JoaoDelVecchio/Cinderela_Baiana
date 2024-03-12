import pygame
from background import background
from red_balloon import red_balloon
from blue_balloon import blue_balloon
from dart_monkey import dart_monkey

money = 0
health = 100

class game:
    width = 800
    height = 800
    screen = None
    map = None

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.map = background()
        self.map.draw(self.screen)

    def health_money_icons(self, screen):
        font = pygame.font.SysFont(None, 30)

        health_icon = font.render("health:" + str(health), True, (250, 0, 0))
        money_icon = font.render("money:" + str(money), True, (250, 0, 0))
        screen.blit(health_icon, (50, 25))
        screen.blit(money_icon, (200, 25))

    def handle_events(self):
        pass

    def loop(self):

        i = 0

        enemy_instances = []
        instance1 = red_balloon()
        instance2 = blue_balloon()
        enemy_instances.append(instance1)
        enemy_instances.append(instance2)

        tower_instances = []
        instance1 = dart_monkey()
        tower_instances.append(instance1)

        while i <= 100000:
            self.map.draw(self.screen)

            for ins in enemy_instances:
                ins.movement(self.screen)

            for ins in tower_instances:
                ins.enemy_in_range()
                ins.draw(self.screen)

            self.health_money_icons(self.screen)

            i = i + 1
            pygame.display.update()


Game = game()
Game.loop()
