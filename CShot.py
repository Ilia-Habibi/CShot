import pygame,random
import sys
from Basic_options import *

class PLAYER:
    def __init__(self):
        self.randomize_aim()

    def randomize_aim(self):
        self.x = random.randint(20,800)
        self.y = random.randint(80,480)
        self.aim = pygame.math.Vector2(self.x,self.y)

class MAIN:
    def __init__(self):
        self.BG = pygame.image.load('Graphics/game BG.jpg')

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
