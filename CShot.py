import pygame
from sys import exit

pygame.init()
pygame.display.set_mode((800,500))
pygame.display.set_caption("CShot")
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    
    pygame.display.update()