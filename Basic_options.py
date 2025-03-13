import pygame,random
import sys

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