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

class SCREEN:
    def __init__(self, jpg_name):
        self.jpj_name = pygame.image.load(jpg_name)
    def draw_game_jpg(self):
        screen.blit(self.jpj_name, (0, 0))
    def draw(self):
        self.draw_game_jpg()
 
def menu():
    main = SCREEN('Graphics/game BG.jpg')
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
        
        if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:  
            pygame.draw.rect(screen,Gold,[width/2,height/2,140,40])
        else:  
            pygame.draw.rect(screen,Gray,[width/2,height/2,140,40])
        
        screen.blit(text , (width/2+50,height/2)) 
        pygame.display.update()
        clock.tick(60)

menu()

