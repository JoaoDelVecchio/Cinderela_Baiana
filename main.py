import pygame
from Background import Background
from Bomb import Bomb
from Berinjela import Berinjela
from G_Loco import G
from Calabresa import Calabresa
from SuperMonkey import SuperMonkey
from Submarine import Submarine
from TitleScreen import TitleScreen
from Buttons import Button
import Rounds
from math import floor


class Game:
    width = 1200
    height = 768
    screen = None
    map = None
    money = 300
    health = 100
    enemy_instances = []
    tower_instances = []
    round = 0
    round_balloons = []
    X_clicked = False
    which_screen = "title"
  

    # auxiliares
    RBE = 0
    hold_image = 0
    tower_icon = None

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.title = TitleScreen()
        self.map = Background()
        self.map.draw(self.screen)
        start_image = pygame.image.load("images/play_button_official.png").convert_alpha()
        self.start_button = Button(250, 420, start_image, 0.35, self.screen)

    def health_money_icons(self, screen):
        font = pygame.font.SysFont('Calibri', 40, True)

        health_icon = font.render("Health:" + str(self.health), True, (0,0,0))
        money_icon = font.render("Money:" + str(self.money), True, (0,0,0))
        round_icon = font.render("Round:" + str(self.round), True, (0,0,0))
        screen.blit(health_icon, (210, 730))
        screen.blit(money_icon, (470, 730))
        screen.blit(round_icon, (730, 730))

    def handle_events_game(self):

        if self.hold_image != 0:
            pos = pygame.mouse.get_pos()
            pos = (pos[0] - 33, pos[1] - 33)
            self.screen.blit(self.tower_icon, pos)

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                pos = (pos[0] - 15, pos[1] - 15)
                
                if self.hold_image == 1 and self.money >= 100:
                    self.money = self.money - 100
                    dart_monkey = Calabresa()
                    dart_monkey.pos = pos
                    self.tower_instances.append(dart_monkey)
                if self.hold_image == 2 and self.money >= 200:
                    self.money = self.money - 200
                    super_monkey = SuperMonkey()
                    super_monkey.pos = pos
                    self.tower_instances.append(super_monkey)
                    
                if self.hold_image == 3 and self.money >= 300:
                    self.money = self.money - 300
                    submarine = Submarine()
                    submarine.pos = pos
                    self.tower_instances.append(submarine)
                    
                self.hold_image = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.hold_image = 1
                    self.tower_icon = pygame.image.load("images/calabresa-removebg-preview.png")
                    self.tower_icon.convert()
                    self.tower_icon = pygame.transform.scale(self.tower_icon, (75, 75))
                if event.key == pygame.K_2:
                    self.hold_image = 2
                    self.tower_icon = pygame.image.load("images/js-removebg-preview.png")
                    self.tower_icon.convert()
                    self.tower_icon = pygame.transform.scale(self.tower_icon, (120, 120))
                    
                if event.key == pygame.K_3:
                    self.hold_image = 3
                    self.tower_icon = pygame.image.load("images/submarine_front.png")
                    self.tower_icon.convert()
                    self.tower_icon = pygame.transform.scale(self.tower_icon, (150, 150))

            if event.type == pygame.QUIT:
                self.X_clicked = True

    def loop(self):
        while not self.X_clicked and self.health >= 0:
            if self.which_screen == "game":
                while not self.X_clicked:
                    self.map.draw(self.screen)

                    self.handle_events_game()

                    if self.RBE <= 0:
                        i = 0 # time step
                        self.round = self.round + 1
                        self.round_balloons = Rounds.rounds(self.round)
                        self.RBE = self.round_balloons[0] + 2 * self.round_balloons[1] + 3 * self.round_balloons[2]
                        self.money = self.money + 100

                    if i % 50 == 0 and self.round_balloons[0] > 0:
                        self.round_balloons[0] = self.round_balloons[0] - 1
                        instance = Bomb()
                        self.enemy_instances.append(instance)
                    if i % floor(1000 / (self.round_balloons[1] + 1)) == 0 and self.round_balloons[1] > 0:
                        self.round_balloons[1] = self.round_balloons[1] - 1
                        instance = Berinjela()
                        self.enemy_instances.append(instance)
                    if i % floor(1000 / (self.round_balloons[2] + 1)) == 0 and self.round_balloons[2] > 0:
                        self.round_balloons[2] = self.round_balloons[2] - 1
                        instance = G()
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
                        enemy.movement(self.screen, self.round)
                        
                        for tower in self.tower_instances:
                            tower.attack(self.enemy_instances)
                            tower.draw(self.screen)

                        self.health_money_icons(self.screen)

                    i = i + 1
                    pygame.display.update()

            if self.which_screen == "title":
                while True:
                    self.title.draw(self.screen)
                    if self.start_button.draw():
                        self.which_screen = "game"
                        break
                    pygame.display.update()

    
game = Game()
game.loop()
