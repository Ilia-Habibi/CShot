import pygame,random
from sys import exit

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
        self.page = 2

    
    def draw_BG(self):
        screen.blit(self.BG, (0,0))

    def draw_game(self):
        self.draw_BG()
        self.player1.draw_shot()
        self.player2.draw_shot()  

    
# Initializing pygame and creating a screen
pygame.init()
width = 820
height = 500
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("CShot")
clock = pygame.time.Clock()
icon = pygame.image.load('Graphics/cshot icon.png')
pygame.display.set_icon(icon)

#fonts
font1 = pygame.font.Font('Fonts/WSBH.ttf',30)

main = MAIN()
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if main.page == 0:
            pass
        elif main.page == 1:
            pass
        elif main.page == 2: 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main.player1.shot_bullets.append(main.player1.aim.copy()) 
                if event.key == pygame.K_SPACE:
                    main.player2.shot_bullets.append(main.player2.aim.copy())
            
            main.draw_game()
            
        elif main.page == 3:
            pass
        elif main.page == 4:
            pass


    pygame.display.update()
    clock.tick(60)



