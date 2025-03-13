import pygame,random
import sys
from Basic_options import *

class PLAYER:
    def __init__(self,player_no):
        self.randomize_aim()
        self.bullet = pygame.image.load('Graphics/red.png') if player_no == 1 else pygame.image.load('Graphics/blue.png')

    def randomize_aim(self):
        self.x = random.randint(20,800)
        self.y = random.randint(80,480)
        self.aim = pygame.math.Vector2(self.x,self.y)
    
    def shot(self):
        screen.blit(self.bullet,self.aim)

class MAIN:
    def __init__(self):
        self.BG = pygame.image.load('Graphics/game BG.jpg')
        self.player1 = PLAYER(1)
        self.player2 = PLAYER(2)

    def draw(self):
        self.draw_game_BG()

    def draw_game_BG(self):
        screen.blit(self.BG,(0,0))

main = MAIN()
def menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:  
                    pygame.quit()  
            main.draw()
            mouse = pygame.mouse.get_pos()
            screen.blit(text , (width/2+50,height/2))   
            pygame.display.update()
            clock.tick(60)
menu()

