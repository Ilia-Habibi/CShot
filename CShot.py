import pygame,random
from sys import exit

class PLAYER:
    def __init__(self,player_no):
        self.randomize_aim()
        self.bullet = pygame.image.load('Graphics/red.png') if player_no == 1 else pygame.image.load('Graphics/blue.png')
        self.shot_bullets = []
        self.bullet_no = 20
        self.score = 0

    def randomize_aim(self):
        self.x = random.randint(50,756)
        self.y = random.randint(150,470)
        self.aim = pygame.math.Vector2(self.x,self.y)

    def shoot(self):
        if self.bullet_no > 0:
            self.shot_bullets.append(self.aim.copy())
            self.bullet_no -= 1
            gun_shot.play()
        else:
            empty_gun_shot.play() 
    
    def move_right(self):
        if self.aim.x+10 > 756:
            error_sound.play()
        self.aim.x = min(self.aim.x+10, 756)

    def move_left(self):
        if self.aim.x-10 < 50:
            error_sound.play()
        self.aim.x = max(self.aim.x-10, 50)

    def move_up(self):
        if self.aim.y-10 < 150:
            error_sound.play()
        self.aim.y = max(self.aim.y-10, 150)
    
    def move_down(self):
        if self.aim.y+10 > 470:
            error_sound.play()
        self.aim.y = min(self.aim.y+10, 470)    
    
    def draw_shot(self):
        for i in self.shot_bullets:
            screen.blit(self.bullet,i)

class TARGET:
    def __init__(self):
        self.img = pygame.image.load("Graphics/focus.png")
        self.randomize_pos()
    
    def randomize_pos(self):
        self.x = random.randint(50,715)
        self.y = random.randint(150,430)
        self.pos = pygame.math.Vector2(self.x,self.y)
        #if not self.spawn_check():
        #    self.randomize_pos()

    def spawn_check(self):
        if ((self.x-8<main.player1.aim.x<self.x+49) and (self.y-8<main.player1.aim.x<self.x+49)):
            return False
        if ((self.x-8<main.player2.aim.x<self.x+49) and (self.y-8<main.player2.aim.x<self.x+49)):
            return False
        else:
            return True
        
    def draw(self):
        screen.blit(self.img, self.pos)

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

# player name input page
class MAIN_PLAY:
    def __init__(self):
        self.font = font2
        self.page_flip = page_flip
        self.b_font = font1
        self.b = self.b_font.render("BACK", True, ink_blue)
        self.b_rect = self.b.get_rect(center=(120, 433))
        self.n_font = font1
        self.n = self.n_font.render("NEXT", True, ink_blue)
        self.n_rect = self.n.get_rect(center=(700, 433))
        self.p1_input_rect = pygame.Rect(240,106,120,50)
        self.p1_active = False
        self.p2_input_rect = pygame.Rect(240,267,120,50)
        self.p2_active = False
        self.reset()
        
        
    def draw(self):
        p2 = self.font.render("player 2:", True, ink_blue)
        p2_rect = p2.get_rect(center=(136,300))
        p2_text_surface = self.font.render(p2_name, True, ink_blue)
        p1 = self.font.render("player 1:", True, ink_red)
        p1_rect = p1.get_rect(center=(136,135))
        p1_text_surface = self.font.render(p1_name, True, ink_red)
        back = self.b_font.render("BACK", True, ink_blue)
        back_rect = back.get_rect(center=(120, 433))
        next = self.n_font.render("NEXT", True, ink_blue)
        next_rect = next.get_rect(center=(700, 433))

        if back_rect.collidepoint(mouse):
            back = self.b_font.render("BACK", True, ink_red)
        if next_rect.collidepoint(mouse) and p1_name != '' and p2_name != '':
            next = self.n_font.render("NEXT", True, ink_red)
            
        screen.blit(p1_text_surface, pygame.Rect(243,115,120,50))
        screen.blit(p2_text_surface, pygame.Rect(243,276,120,50))
        self.p1_input_rect.w = max(180, p1_text_surface.get_width() + 10)
        self.p2_input_rect.w = max(180, p2_text_surface.get_width() + 10)
        screen.blit(p2, p2_rect)
        screen.blit(p1, p1_rect)
        screen.blit(back, back_rect)
        screen.blit(next, next_rect)
        if self.p1_active:
            pygame.draw.rect(screen, "dark green", self.p1_input_rect, 2)
        else:
            pygame.draw.rect(screen, ink_red, self.p1_input_rect, 2)
        if self.p2_active:
            pygame.draw.rect(screen, "dark green", self.p2_input_rect, 2)
        else:
            pygame.draw.rect(screen, ink_blue, self.p2_input_rect, 2)
            
    def back(self):
        main.page = 0
        main.main_play.reset()
        self.page_flip.play()

    def next(self):
        if p1_name != '' and p2_name != '':
            main.page = 4
            self.page_flip.play()

    def reset(self):
        global p1_name
        global p2_name
        p1_name = ''
        p2_name = ''
        
class PLAY_GAME:
    def __init__(self):
        self.page_flip = page_flip
        self.win_sound = win_sound
        self.b_font = font3
        
        self.p1_font = font3
        self.p1_score = self.p1_font.render("PLAYER 1 SCORE:", True, ink_red)
        self.p1_score_rect = self.p1_score.get_rect(center=(110, 100))
        self.p1_shot = self.p1_font.render("PLAYER 1 BULLETS:", True, ink_red)
        self.p1_shot_rect = self.p1_shot.get_rect(center=(670, 100))
        
        self.p2_font = font3
        self.p2_score = self.p2_font.render("PLAYER 2 SCORE:", True, ink_blue)
        self.p2_score_rect = self.p2_score.get_rect(center=(110, 125))
        self.p2_shot = self.p2_font.render("PLAYER 2 BULLETS:", True, ink_blue)
        self.p2_shot_rect = self.p2_shot.get_rect(center=(670, 125)) 
        
    def draw(self):
        back = self.b_font.render("EXIT", True, ink_blue)
        back_rect = back.get_rect(center=(30, 50))
        
        pygame.draw.ellipse(screen, ink_blue, (5, 35, 50, 30), 2)
        if back_rect.collidepoint(mouse):
            back = self.b_font.render("EXIT", True, ink_red)
            pygame.draw.ellipse(screen, ink_red, (5, 35, 50, 30), 2)
        screen.blit(back, back_rect)
        screen.blit(self.p1_score, self.p1_score_rect)
        screen.blit(self.p2_score, self.p2_score_rect)
        screen.blit(self.p1_shot, self.p1_shot_rect)
        screen.blit(self.p2_shot, self.p2_shot_rect)
        
        p1_number_shot = self.p1_font.render(str(main.player1.bullet_no), True, "black")
        p1_number_shot_rect = p1_number_shot.get_rect(center=(750, 100))
        screen.blit(p1_number_shot, p1_number_shot_rect)
        p2_number_shot = self.p2_font.render(str(main.player2.bullet_no), True, "black")
        p2_number_shot_rect = p2_number_shot.get_rect(center=(750, 125))
        screen.blit(p2_number_shot, p2_number_shot_rect)
        
        p1_number_score = self.p1_font.render(str(main.player1.score), True, "black")
        p1_number_score_rect = p1_number_score.get_rect(center=(180, 100))
        screen.blit(p1_number_score, p1_number_score_rect)
        p2_number_score = self.p2_font.render(str(main.player2.score), True, "black")
        p2_number_score_rect = p2_number_score.get_rect(center=(180, 125))
        screen.blit(p2_number_score, p2_number_score_rect)

    def back(self):
        main.page = 1
        main.main_play.reset()
        main.player1.shot_bullets.clear()
        main.player2.shot_bullets.clear()
        main.player1.bullet_no = 20
        main.player2.bullet_no = 20
        main.player1.score = 0
        main.player2.score = 0
        self.page_flip.play()
    
    def next(self):
        main.page = 5
        main.player1.shot_bullets.clear()
        main.player2.shot_bullets.clear()
        self.player1_number_bullet = 20
        self.player2_number_bullet = 20
        self.player1_number_score = 0
        self.player2_number_score = 0
        self.win_sound.play()

class END_GAME:
    def __init__(self):
        self.page_flip = page_flip
        self.b_font = font1
        self.n_font = font1
        self.w_font = font2
        if winner_bool == 1:     
            self.winner = self.w_font.render("PLAYER1 WIIIIIN", True, ink_red)
            self.result_rect = self.winner.get_rect(center=(335, 205))
        elif winner_bool == 2:
            self.winner = self.w_font.render("PLAYER2 WIIIIIN", True, ink_blue)
            self.result_rect = self.winner.get_rect(center=(335, 205))
        else:
            self.winner = self.w_font.render("Draw :)", True, "dark green")
            self.result_rect = self.winner.get_rect(center=(410, 205))
        
        
    def draw(self):
        self.b = self.b_font.render("MENU", True, "gold")
        self.b_rect = self.b.get_rect(center=(230, 433))
        self.n = self.n_font.render("EXIT", True, "gold")
        self.n_rect = self.n.get_rect(center=(590, 433))

        if self.b_rect.collidepoint(mouse):
            self.b = self.b_font.render("MENU", True, ink_red)
        if self.n_rect.collidepoint(mouse):
            self.n = self.n_font.render("EXIT", True, ink_red)
    
        screen.blit(self.b, self.b_rect)
        screen.blit(self.n, self.n_rect)
        screen.blit(self.winner, self.result_rect)
    
    def menu(self):
        main.page = 0
        main.end_game = END_GAME()
        page_flip.play()
    
    def exit(self):
        pygame.quit()
        exit()
        
class MAIN:
    def __init__(self):
        self.BG = pygame.image.load('Graphics/game BG.jpg')
        self.player1 = PLAYER(1)
        self.player2 = PLAYER(2)
        self.menu = MENU()
        self.controls = CONTROLS()
        self.main_play = MAIN_PLAY()
        self.play_game = PLAY_GAME()
        self.end_game = END_GAME()
        self.target1 = TARGET()
        ### page numbers: 0 = menu , 1 = name input , 2 = controls , 3 = leaderboard , 4 = game , 5 = end game
        self.page = 0

    def draw_controls(self):
        self.draw_BG()
        self.controls.draw()
        
    def draw_main_play(self):
        self.draw_BG()
        self.main_play.draw()

    def draw_menu(self):
        self.draw_BG()
        self.menu.draw()

    def draw_BG(self):
        screen.blit(self.BG, (0,0))

    def draw_game(self):
        self.draw_BG()
        self.play_game.draw()
        self.player1.draw_shot()
        self.player2.draw_shot()
        self.target1.draw() 
    
    def draw_end_game(self):
        self.draw_BG()
        self.end_game.draw()

p1_name = ""
p2_name = ""
winner_bool = 0

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
font3 = pygame.font.Font("Fonts/Scribble Markers.otf",15)

# colors
ink_blue = (0,51,102)
ink_red = (204,0,0)

# sounds
page_flip = pygame.mixer.Sound('SFX/page flip.mp3')
gun_shot = pygame.mixer.Sound('SFX/gun-shot.mp3')
empty_gun_shot = pygame.mixer.Sound('SFX/empty gun shot.mp3')
error_sound = pygame.mixer.Sound('SFX/error sound.mp3')
win_sound = pygame.mixer.Sound('SFX/level win.mp3')

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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if main.main_play.b_rect.collidepoint(mouse):
                    main.main_play.back()
                if main.main_play.n_rect.collidepoint(mouse):
                    main.main_play.next()
                if main.main_play.p1_input_rect.collidepoint(mouse):
                    main.main_play.p1_active = True
                else:
                    main.main_play.p1_active = False
                if main.main_play.p2_input_rect.collidepoint(mouse):
                    main.main_play.p2_active = True
                else:
                    main.main_play.p2_active = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                        main.main_play.back()
                if main.main_play.p1_active == True:
                    if event.key == pygame.K_RETURN:
                        main.main_play.p1_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        p1_name = p1_name[:-1]
                    else:
                        p1_name += event.unicode
                if main.main_play.p2_active == True:
                    if event.key == pygame.K_RETURN:
                        main.main_play.p2_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        p2_name = p2_name[:-1]
                    else:
                        p2_name += event.unicode
            main.draw_main_play()
                    
        elif main.page == 2: 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if main.controls.b_rect.collidepoint(mouse):
                    main.controls.back()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main.controls.back()
            main.draw_controls()

        elif main.page == 3:
            pass
        
        elif main.page == 4:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main.player1.shoot()
                if event.key == pygame.K_SPACE:
                    main.player2.shoot()
                    
                if event.key == pygame.K_d:
                    main.player2.move_right()
                if event.key == pygame.K_a:
                    main.player2.move_left()
                if event.key == pygame.K_w:
                    main.player2.move_up()
                if event.key == pygame.K_s:
                    main.player2.move_down()
                    
                if event.key == pygame.K_RIGHT:
                    main.player1.move_right()
                if event.key == pygame.K_LEFT:
                    main.player1.move_left()
                if event.key == pygame.K_UP:
                    main.player1.move_up()
                if event.key == pygame.K_DOWN:
                    main.player1.move_down()
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if main.play_game.b_rect.collidepoint(mouse):
                    main.play_game.back()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main.play_game.back()

            if main.player1.bullet_no == 0 and main.player2.bullet_no == 0:
                if main.player1.score > main.player2.score:
                    winner_bool = 1
                elif main.player1.score < main.player2.score:
                    winner_bool = 2
                else:
                    winner_bool = 0
                main.play_game.next()
            main.draw_game()
            
        elif main.page == 5:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if main.end_game.b_rect.collidepoint(mouse):
                    main.end_game.menu()
                if main.end_game.n_rect.collidepoint(mouse):
                    main.end_game.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main.end_game.menu()
            main.draw_end_game()
            
    pygame.display.update()
    clock.tick(60)



