import pygame,random
import sys
from Basic_options import *

class PLAYER:
    def __init__(self,player_no):
        self.randomize_aim()
        self.bullet = pygame.image.load('Graphics/red.png') if player_no == 1 else pygame.image.load('Graphics/blue.png')
        self.shot_bullets = []

    def randomize_aim(self):
        self.x = random.randint(50,750)
        self.y = random.randint(150,480)
        self.aim = pygame.math.Vector2(self.x,self.y)
    
    def draw_shot(self):
        for i in self.shot_bullets:
            screen.blit(self.bullet,i)

class MAIN:
    def __init__(self):
        self.BG = pygame.image.load('Graphics/game BG.jpg')
        self.player1 = PLAYER(1)
        self.player2 = PLAYER(2)
        ### page numbers: 0 = menu , 1 = name input , 2 = game , 3 = controls , 4 = leaderboard
        self.page = 0

    def draw_game_jpg(self):
        screen.blit(self.BG, (0,0))

    def draw_game(self):
        self.draw_game_jpg() 
        self.player1.draw_shot()
        self.player2.draw_shot()  

    def draw_menu(self):
        pass

screen = pygame.display.set_mode(res)
pygame.display.set_caption("CShot")
clock = pygame.time.Clock()
icon = pygame.image.load('Graphics/cshot icon.png')
pygame.display.set_icon(icon)
main = MAIN()
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                main.player1.shot_bullets.append(main.player1.aim.copy()) 
            if event.key == pygame.K_SPACE:
                main.player2.shot_bullets.append(main.player2.aim.copy())

    main.draw_game()
    pygame.display.update()
    clock.tick(60)



