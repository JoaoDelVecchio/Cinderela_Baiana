import pygame
from Background import Background
from RedBalloon import RedBalloon
from BlueBalloon import BlueBalloon
from GreenBalloon import GreenBalloon
from DartMonkey import DartMonkey
from SuperMonkey import SuperMonkey
import Rounds
from math import floor


class Game:
    width = 1200
    height = 768
    screen = None
    map = None
    money = 100
    health = 100
    enemy_instances = []
    tower_instances = []
    round = 0
    round_balloons = []

    # auxiliares
    RBE = 0
    hold_image = 0
    tower_icon = None

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.map = Background()
        self.map.draw(self.screen)

    def health_money_icons(self, screen):
        font = pygame.font.SysFont('Calibri', 40)

        health_icon = font.render("Health:" + str(self.health), True, (0,0,0))
        money_icon = font.render("Money:" + str(self.money), True, (0,0,0))
        round_icon = font.render("Round:" + str(self.round), True, (0,0,0))
        screen.blit(health_icon, (180, 720))
        screen.blit(money_icon, (440, 720))
        screen.blit(round_icon, (700, 720))


    def handle_events(self):

        if self.hold_image != 0:
            pos = pygame.mouse.get_pos()
            pos = (pos[0] - 33, pos[1] - 33)
            self.screen.blit(self.tower_icon, pos)

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                pos = (pos[0] - 15, pos[1] - 15)
                if self.hold_image == 1 and self.money >= 200:
                    self.money = self.money - 200
                    dart_monkey = DartMonkey()
                    dart_monkey.pos = pos
                    self.tower_instances.append(dart_monkey)
                if self.hold_image == 2 and self.money >= 400:
                    self.money = self.money - 400
                    super_monkey = SuperMonkey()
                    super_monkey.pos = pos
                    self.tower_instances.append(super_monkey)
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

        while True:
            self.map.draw(self.screen)

            self.handle_events()
            #print(self.RBE)

            if self.RBE <= 0:
                i = 0
                self.round = self.round + 1
                self.round_balloons = Rounds.rounds(self.round)
                self.RBE = self.round_balloons[0] + 2 * self.round_balloons[1] + 3 * self.round_balloons[2]
                self.money = self.money + 100

            if i % 50 == 0 and self.round_balloons[0] > 0:
                self.round_balloons[0] = self.round_balloons[0] - 1
                instance = RedBalloon()
                self.enemy_instances.append(instance)
            if i % floor(1000 / (self.round_balloons[1] + 1)) == 0 and self.round_balloons[1] > 0:
                self.round_balloons[1] = self.round_balloons[1] - 1
                instance = BlueBalloon()
                self.enemy_instances.append(instance)
            if i % floor(1000 / (self.round_balloons[2] + 1)) == 0 and self.round_balloons[2] > 0:
                self.round_balloons[2] = self.round_balloons[2] - 1
                instance = GreenBalloon()
                self.enemy_instances.append(instance)

            for enemy in self.enemy_instances:
                for tower in self.tower_instances:
                    for projectile in tower.projectiles:
                        if enemy.detect_projectile(projectile.x, projectile.y):
                            enemy.take_damage()
                            self.RBE = self.RBE - 1
                            self.money = self.money + 1
                            tower.projectiles.remove(projectile)
                if enemy.end_of_track():
                    self.enemy_instances.remove(enemy)
                    self.health = self.health - enemy.health
                    self.RBE = self.RBE - enemy.health
                elif enemy.health <= 0:
                    self.enemy_instances.remove(enemy)
                enemy.movement(self.screen)
                

            for tower in self.tower_instances:
                tower.attack(self.enemy_instances)
                tower.draw(self.screen)

            self.health_money_icons(self.screen)

            i = i + 1
            pygame.display.update()


game = Game()
game.loop()
