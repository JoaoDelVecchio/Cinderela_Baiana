import pygame
from Background import Background
from RedBalloon import RedBalloon
from BlueBalloon import BlueBalloon
from DartMonkey import DartMonkey


class Game:
    width = 800
    height = 800
    screen = None
    map = None
    money = 0
    health = 100

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
        pass

    def loop(self):

        i = 0

        enemy_instances = []
        instance1 = RedBalloon()
        instance2 = BlueBalloon()
        enemy_instances.append(instance1)
        enemy_instances.append(instance2)

        tower_instances = []
        instance1 = DartMonkey()
        tower_instances.append(instance1)

        while i <= 100000:
            self.map.draw(self.screen)

            for ins in enemy_instances:
                ins.movement(self.screen)
                if ins.detect_projectile():
                    ins.take_damage()
                    self.money = self.money + 1

            for ins in tower_instances:
                ins.enemy_in_range()
                ins.draw(self.screen)

            self.health_money_icons(self.screen)

            i = i + 1
            pygame.display.update()


game = Game()
game.loop()
