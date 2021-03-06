import random
import pygame
import math

class Pong:
    pygame.init()
    def __init__(self):
        self.myFont = pygame.font.SysFont("Times New Roman", 36)
        self.score = 0
        self.loop = True
        self.title_screen = "Pong"
        self.width_screen = 800
        self.height_screen = 600
        self.background_screen = (70,95,70)
        self.clock = pygame.time.Clock()
        self.pygame = pygame
        

    def event(self):
        self.events = self.pygame.event.get()

        for e in self.events:
            if e.type == pygame.QUIT:
                self.loop = False

        self.player_one.event()
        self.player_two.event()
        self.ball.event()
        self.point.event()

    def render(self):
        self.canvas.fill(self.background_screen)
        # player_score = self.myFont.render(str(self.score), 1, (255,0,0))
        # self.canvas.blit(player_score, (520,20))
        ###
        self.player_one.render()
        self.player_two.render()
        self.ball.render()
        # self.point.render()
        ###
        self.clock.tick(60)
        self.pygame.display.flip()

    def start(self):
        # self.pygame.init()
        self.pygame.display.set_caption(self.title_screen)
        self.canvas = self.pygame.display.set_mode((self.width_screen,self.height_screen))
        # Init
        self.player_one = Player(self,1)
        self.player_two = Player(self,2)
        self.ball = Ball(self)
        self.point = Point(self)
        while self.loop:
            # Handle Event
            self.event()
            # Handle Render
            self.render()
            
class Player:
    def __init__(self,game,player):
        self.game = game

        self.width = 30
        self.height = 120

        self.player = player
        self.speed_y = 10
        # 
        self.x = 0
        if self.player != 1:
            self.x = self.game.width_screen - self.width
        self.y = 0
        #
        self.pygame = self.game.pygame
        self.canvas = self.game.canvas
        self.image = self.pygame.image.load("paddle.png")
    
    def event(self):
        pressed = self.game.pygame.key.get_pressed()

        keyUp = None
        keyDown = None

        if self.player == 1:
            keyUp = pygame.K_w
            keyDown = pygame.K_s
        else:
            keyUp = pygame.K_UP
            keyDown = pygame.K_DOWN


        if pressed[keyUp]:
            if self.y <= 0:
                self.y = 0
            else:
                self.y -= self.speed_y
        elif pressed[keyDown]:
            if self.y >= self.game.height_screen - self.height:
                self.y = self.game.height_screen - self.height
            else:
                self.y += self.speed_y


    def render(self):
        player_score = self.game.myFont.render(str(self.game.score), 1, (255,0,0))
        if self.player != 1:  
            self.canvas.blit(player_score, (520,20))
        elif self.player == 1:
            self.canvas.blit(player_score, (280,20))
        self.canvas.blit(self.image, (self.x,self.y))

class Ball:
    def __init__(self,game):
        # game = Pong
        self.game = game

        self.speed_y = random.randint(3, 9)
        self.speed_x = random.randint(3, 9)

        self.width = 20
        self.height = 20
        
        self.x = (self.game.width_screen / 2) - (self.width / 2)
        self.y = random.randint((self.height / 2)    ,   self.game.height_screen  - (self.height / 2))
        #
        self.pygame = self.game.pygame
        self.canvas = self.game.canvas
        self.image = self.pygame.image.load("ball.png")

    def event(self):

        # Va ch???m v??o t?????ng ph???i - tr??i
        if self.x >= self.game.width_screen - self.width:
            self.x = self.game.width_screen - self.width
            self.speed_x *= -1
            self.game.score = self.game.score + 1
        if self.x <= 0:
            self.x = 0
            self.speed_x *= -1
            self.game.score = self.game.score + 1
        # Va ch???m v??o t?????ng tr??n - d?????i
        if self.y >= self.game.height_screen - self.height:
            self.y = self.game.height_screen - self.height
            self.speed_y *= -1
            

        if self.y <= 0:
            self.y = 0
            self.speed_y *= -1
            

        self.x += self.speed_x
        self.y += self.speed_y


    def render(self):
        self.canvas.blit(self.image, (self.x,self.y))

class Point():
    def __init__(self,game):
        self.game = game
        self.width = 20
        self.height = 20
        
        self.pygame = self.game.pygame
        self.canvas = self.game.canvas
        # self.myFont = pygame.font.SysFont("Times New Roman", 18)

    def event(self):
        if self.game.score == 10:
            self.game.score == 0
            # player_win = self.game.myFont.render("player win", 1, (255,0,0))
            # self.canvas.blit(player_win, (400,300))
pong = Pong()
pong.start()