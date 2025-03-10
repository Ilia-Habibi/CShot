import pygame
from sys import exit

# Initializing pygame and creaing a screen
pygame.init()
pygame.display.set_mode((800,500))
pygame.display.set_caption("CShot")
clock = pygame.time.Clock()
icon = pygame.image.load('Graphics/cshot icon.png')
pygame.display.set_icon(icon)

    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    
    pygame.display.update()
    clock.tick(60)