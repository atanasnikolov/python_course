import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
color = (255, 255, 255)

clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit() 

    surface.fill(color)
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)

pygame.quit()