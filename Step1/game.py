import pygame
from sys import exit

width, height = 640,480
pygame.init()
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

player = pygame.image.load("../BunniesNBadgers/resources/images/dude.png")
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    screen.fill(0)
    
    # sRGB profile error / ImageMagick script
    screen.blit(player,(100,100))
    
    pygame.display.update()
    clock.tick(60)
