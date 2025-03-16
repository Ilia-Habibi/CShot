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

class CONTROLS:
    def __init__(self):
        self.enter = pygame.image.load("Graphics/enter.PNG")
        self.arrows = pygame.image.load("Graphics/arrows.PNG")
        self.wasd = pygame.image.load("Graphics/wasd.PNG")
        self.space = pygame.image.load("Graphics/space.PNG")
        self.font = font2
        self.page_flip = page_flip
        self.b_font = font1
        self.b = self.b_font.render("BACK", True, ink_blue)
        self.b_rect = self.b.get_rect(center=(width//2, 433))
    
    def draw(self):
        p2 = self.font.render("player 2", True, ink_blue)
        p2_rect = p2.get_rect(center=(136,120))
        p2_move = self.font.render("move:", True, ink_blue)
        p2_move_rect = p2_move.get_rect(center=(136,177))
        p2_shoot = self.font.render("shoot:", True, ink_blue)
        p2_shoot_rect = p2_shoot.get_rect(center=(136,273))
        p1 = self.font.render("player 1", True, ink_red)
        p1_rect = p1.get_rect(center=(536,120))
        p1_move = self.font.render("move:", True, ink_red)
        p1_move_rect = p1_move.get_rect(center=(536,273))
        p1_shoot = self.font.render("shoot:", True, ink_red)
        p1_shoot_rect = p1_shoot.get_rect(center=(536,177))
        back = self.b_font.render("BACK", True, ink_blue)
        back_rect = back.get_rect(center=(width//2, 433))
        

        if back_rect.collidepoint(mouse):
            back = self.b_font.render("BACK", True, ink_red)

        screen.blit(p2, p2_rect)
        screen.blit(p2_move, p2_move_rect)
        screen.blit(self.wasd, (150,165))
        screen.blit(p2_shoot,p2_shoot_rect)
        screen.blit(self.space, (136,295))
        screen.blit(p1, p1_rect)
        screen.blit(p1_move, p1_move_rect)
        screen.blit(self.enter, (570,165))
        screen.blit(p1_shoot,p1_shoot_rect)
        screen.blit(self.arrows, (550,265))
        screen.blit(back, back_rect)
    
    def back(self):
        main.page = 0
        self.page_flip.play()

class MENU:
    def __init__(self):
        self.font = font1
        self.items = ["PLAY", "CONTROLS", "LEADERBOARD", "QUIT"]
        self.selected_item = 0
        self.page_flip = page_flip

    def draw(self):
        for i, item in enumerate(self.items):
            text = self.font.render(item, True, ink_blue)
            text_rect = text.get_rect(center=(width//2, 177+i*64))
        
            if text_rect.collidepoint(mouse):
                self.selected_item = i
            
            if i == self.selected_item:
                text = self.font.render(item, True, ink_red)
        
            screen.blit(text, text_rect)

    def select(self):
        if self.selected_item == 3:
            pygame.quit()
            exit()
        else:
            main.page = self.selected_item + 1
            self.page_flip.play()

class MAIN:
    def __init__(self):
        self.BG = pygame.image.load('Graphics/game BG.jpg')
        self.player1 = PLAYER(1)
        self.player2 = PLAYER(2)
        self.menu = MENU()
        self.controls = CONTROLS()
        ### page numbers: 0 = menu , 1 = name input , 2 = controls , 3 = leaderboard , 4 = game 
        self.page = 0

    def draw_controls(self):
        self.draw_BG()
        self.controls.draw()

    def draw_menu(self):
        self.draw_BG()
        self.menu.draw()

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

# fonts
font1 = pygame.font.Font("Fonts/Notera.ttf",36)
font2 = pygame.font.Font("Fonts/Scribble Markers.otf",36)

# colors
ink_blue = (0,51,102)
ink_red = (204,0,0)

# sounds
page_flip = pygame.mixer.Sound('SFX/page flip.mp3')

# main object 
main = MAIN()
    
while True:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if main.page == 0:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    main.menu.selected_item = (main.menu.selected_item + 1) % (len(main.menu.items))
                if event.key == pygame.K_UP:
                    main.menu.selected_item = (main.menu.selected_item - 1) % (len(main.menu.items))
                if event.key == pygame.K_RETURN:
                    main.menu.select()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, item in enumerate(main.menu.items):
                    text = main.menu.font.render(item, True, ink_blue)
                    text_rect = text.get_rect(center=(width//2, 177+i*64))
        
                    if text_rect.collidepoint(mouse):
                        main.menu.select()

            main.draw_menu()

        elif main.page == 1:
            pass
        elif main.page == 2: 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if main.controls.b_rect.collidepoint(mouse):
                    main.controls.back()
            
            main.draw_controls()

        elif main.page == 3:
            pass
        elif main.page == 4:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main.player1.shot_bullets.append(main.player1.aim.copy()) 
                if event.key == pygame.K_SPACE:
                    main.player2.shot_bullets.append(main.player2.aim.copy())
            
            main.draw_game()


    pygame.display.update()
    clock.tick(60)



