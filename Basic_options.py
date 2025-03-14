import pygame,random
import sys
from color import *

res = (820, 500)
# Initializing pygame and creating a screen
pygame.init()
screen = pygame.display.set_mode(res)
pygame.display.set_caption("CShot")
clock = pygame.time.Clock()
icon = pygame.image.load('Graphics/cshot icon.png')
pygame.display.set_icon(icon)
# stores the width of the  
# screen into a variable  
width = screen.get_width()  
# stores the height of the  
# screen into a variable  
height = screen.get_height()

font_1 = pygame.font.SysFont('timesnewroman',  45)
font_2 = pygame.font.SysFont('timesnewroman',  40)
# rendering a text written in  
# this font  
text_quit = font_1.render('Quit', True, Black)
text_play = font_1.render('Play', True, Black)
text_control = font_2.render('Control', True, Black)