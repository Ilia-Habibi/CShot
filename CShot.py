import pygame,random
import sys

class PLAYER:
    def __init__(self,player_no):
        self.randomize_aim()
        self.bullet = pygame.image.load('Graphics/red.png') if player_no == 1 else pygame.image.load('Graphics/blue.png')

    def randomize_aim(self):
        self.x = random.randint(20,780)
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


# Initializing pygame and creating a screen
pygame.init()
screen = pygame.display.set_mode((820,500))
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


    
    main.draw()
    pygame.display.update()
    clock.tick(60)