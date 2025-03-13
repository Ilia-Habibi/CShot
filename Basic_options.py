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

smallfont = pygame.font.SysFont('Corbel',60)  
# rendering a text written in  
# this font  
text = smallfont.render('quit' , True , Black)