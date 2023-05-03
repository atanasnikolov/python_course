
# Importing the library
import pygame
import sys
 
# Initializing Pygame modules
pygame.init()
 
# Initializing surface
screen = pygame.display.set_mode((800, 600))
figure_surface = pygame.image.load('hexagon.png').convert()
figure_rect = figure_surface.get_rect(midbottom = (400, 300))
 
# Initializing RGB Color
color = (255, 255, 255)

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()
      
    # if left arrow key is pressed
    if keys[pygame.K_LEFT] and x>0:
          
        # decrement in x co-ordinate
        x -= vel
          
    # if left arrow key is pressed
    if keys[pygame.K_RIGHT] and x<500-width:
          
        # increment in x co-ordinate
        x += vel
         
    # if left arrow key is pressed   
    if keys[pygame.K_UP] and y>0:
          
        # decrement in y co-ordinate
        y -= vel
          
    # if left arrow key is pressed   
    if keys[pygame.K_DOWN] and y<500-height:
        # increment in y co-ordinate
        y += vel

    screen.fill(color)
    screen.blit(figure_surface, figure_rect)    
# Changing surface color
    
    pygame.display.flip()