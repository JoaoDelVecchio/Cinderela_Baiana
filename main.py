import pygame
from Background import Background
from Bomb import Bomb
from Berinjela import Berinjela
from G_Loco import G
from Calabresa import Calabresa
from JS import JS
from Submarine import Submarine
from TitleScreen import TitleScreen
from Buttons import Button
import Rounds
from math import floor
from time import sleep


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
        quit_image = pygame.image.load("images/quit_image.png").convert_alpha()
        self.quit_button = Button(700, 420, quit_image, 0.9, self.screen)

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
                print(pos)
                if self.hold_image == 1 and self.money >= 100:
                    
                    calabresa = Calabresa()
                    if self.map.raio_do_lago(pos[0], pos[1]) == True or self.map.limites_laterais(pos[0], pos[1]) == False:
                        pass
                    else:
                        self.money = self.money - 100
                        calabresa.pos = pos
                        self.tower_instances.append(calabresa)
                    
                if self.hold_image == 2 and self.money >= 200:
                    
                    js = JS()
                    if self.map.raio_do_lago(pos[0], pos[1]) == True or self.map.limites_laterais(pos[0], pos[1]) == False:
                        pass
                    else:
                        self.money = self.money - 200
                        js.pos = pos
                        self.tower_instances.append(js)
                    
                if self.hold_image == 3 and self.money >= 300:
                    
                    submarine = Submarine()
                    if self.map.raio_do_lago(pos[0], pos[1]) == False:
                        pass
                    else:
                        self.money = self.money - 300
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

                    
                    action_start = False
                    action_quit = False
                    pos = pygame.mouse.get_pos()
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if self.start_button.rect.collidepoint(pos):
                                self.clicked = True
                                action_start = True
                            if self.quit_button.rect.collidepoint(pos):
                                self.clicked = True
                                action_quit = True
                        if event.type == pygame.MOUSEBUTTONUP:
                            self.clicked = False


                    self.title.draw(self.screen)
                    if self.start_button.draw(action_start):
                        self.which_screen = "game"
                        break
                    if self.quit_button.draw(action_quit):
                        self.X_clicked = True
                        break
                    
                    pygame.display.update()

    
game = Game()
game.loop()
