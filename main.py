import pygame
from background import background
from tower import tower
from enemy import enemy
from red_ballon import red_ballon

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

    def handle_events(self):
        pass

    def loop(self):
        i = 0


        enemy_instances = []
        instance1 = red_ballon()
        enemy_instances.append(instance1)

        tower_instances = []
        instance1 = tower(1)
        tower_instances.append(instance1)

        while i <= 100000:
            self.map.draw(self.screen)

            for ins in enemy_instances:
                ins.movement(self.screen)

            for ins in tower_instances:
                ins.enemy_in_range()
                ins.draw(self.screen)

            i = i + 1
            pygame.display.update()



Game = game()
Game.loop()

