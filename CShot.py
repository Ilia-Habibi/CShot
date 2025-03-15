import pygame,random
import sys
from Basic_options import *

class PLAYER:
    def __init__(self,player_no):
        self.randomize_aim()
        self.bullet = pygame.image.load('Graphics/red.png') if player_no == 1 else pygame.image.load('Graphics/blue.png')
        self.shot_bullets = []

    def randomize_aim(self):
        self.x = random.randint(20,800)
        self.y = random.randint(80,480)
        self.aim = pygame.math.Vector2(self.x,self.y)
    
    def draw_shot(self):
        for i in self.shot_bullets:
            screen.blit(self.bullet,i)

class SCREEN:
    def __init__(self, jpg_name, x = 0, y = 0):
        self.jpj_name = pygame.image.load(jpg_name)
        self.x = x
        self.y = y
    def draw_game_jpg(self):
        screen.blit(self.jpj_name, (self.x, self.y))
    def draw(self):
        self.draw_game_jpg()   

def play_game():
    screen = pygame.display.set_mode(res)
    pygame.display.set_caption("CShot_menu")
    clock = pygame.time.Clock()
    icon = pygame.image.load('Graphics/cshot icon.png')
    pygame.display.set_icon(icon)
    main = SCREEN('Graphics/game BG.jpg')
    
    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 30 <= mouse[0] <= 110 and 437 <= mouse[1] <= 477:
                    return        
        main.draw()
        if 30 <= mouse[0] <= 110 and 437 <= mouse[1] <= 477:
            pygame.draw.rect(screen, Red, [30, 437, 80, 40])
            pygame.draw.rect(screen, Black, [28, 435, 84, 44], 2)
        else: 
            pygame.draw.rect(screen, Gray, [30, 437, 80, 40])
            pygame.draw.rect(screen, Gold, [28, 435, 84, 44], 2)
        screen.blit(text_exit_play, (45, 440))
        pygame.display.update()
        clock.tick(60)
def menu():
    screen = pygame.display.set_mode(res)
    pygame.display.set_caption("CShot_menu")
    clock = pygame.time.Clock()
    icon = pygame.image.load('Graphics/cshot icon.png')
    pygame.display.set_icon(icon)
    main = SCREEN('Graphics/game BG.jpg')
    
    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if width/2-80 <= mouse[0] <= width/2+70 and height/2+130 <= mouse[1] <= height/2+180:  
                    pygame.quit()
                if(width/2-80 <= mouse[0] <= width/2+70 and height/2-102 <= mouse[1] <= height/2-52):
                    play_game() 
        
        main.draw()        
        #show Quit 
        if width/2-50 <= mouse[0] <= width/2+50 and height/2+120 <= mouse[1] <= height/2+200:
            pygame.draw.ellipse(screen, Violet, (width/2-78, height/2+132, 150, 75))
            pygame.draw.ellipse(screen, Red, (width/2-78, height/2+132, 150, 75), 2)
            #pygame.draw.rect(screen, Cyan, [width/2-78, height/2+132, 146, 46])
            #pygame.draw.rect(screen, Black, [width/2-80, height/2+130, 150, 50], 2)
        else:  
            pygame.draw.ellipse(screen, Cyan, (width/2-78, height/2+132, 150, 75))
            pygame.draw.ellipse(screen, Black, (width/2-78, height/2+132, 150, 75), 2)
            #pygame.draw.rect(screen, Violet, [width/2-78, height/2+132, 146, 46])
            #pygame.draw.rect(screen, Red, [width/2-80, height/2+130, 150, 50], 2)
        #show Play
        if width/2-50 <= mouse[0] <= width/2+50 and height/2-112 <= mouse[1] <= height/2-32:
            pygame.draw.ellipse(screen, Violet, (width/2-78, height/2-110, 150, 75))
            pygame.draw.ellipse(screen, Red, (width/2-78, height/2-110, 150, 75), 2)
        else:  
            pygame.draw.ellipse(screen, Cyan, (width/2-78, height/2-110, 150, 75))
            pygame.draw.ellipse(screen, Black, (width/2-78, height/2-110, 150, 75), 2)
        #show Control
        if width/2-50 <= mouse[0] <= width/2+50 and height/2-30 <= mouse[1] <= height/2+50:
            pygame.draw.ellipse(screen, Violet, (width/2-78, height/2-25, 150, 75))
            pygame.draw.ellipse(screen, Red, (width/2-78, height/2-25, 150, 75), 2)
        else:  
            pygame.draw.ellipse(screen, Cyan, (width/2-78, height/2-25, 150, 75))
            pygame.draw.ellipse(screen, Black, (width/2-78, height/2-25, 150, 75), 2)
        
        screen.blit(text_play, (width/2-43, height/2-103))
        screen.blit(text_quit, (width/2-43, height/2+137))
        screen.blit(text_control, (width/2-67, height/2-10))
        pygame.display.update()
        clock.tick(60)

            #    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:  
            #        pygame.quit()
            #        sys.exit()
            #if event.type == pygame.KEYDOWN:
            #    if event.key == pygame.K_RETURN:
            #        main.player1.shot_bullets.append(main.player1.aim.copy()) 
            #    if event.key == pygame.K_SPACE:
            #        main.player2.shot_bullets.append(main.player2.aim.copy())

menu()

