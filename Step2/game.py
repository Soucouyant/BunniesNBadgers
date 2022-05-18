import pygame
from sys import exit


width, height = 600,500
pygame.init()
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()


# Images
player = pygame.image.load("../BunniesNBadgers/resources/images/dude.png")
grass = pygame.image.load("../BunniesNBadgers/resources/images/grass.png")
castle = pygame.image.load("../BunniesNBadgers/resources/images/castle.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    screen.fill(0)
    
    # Draw BG
    for x in range(width // grass.get_width()+1):
        for y in range(height // grass.get_height()+1):
            screen.blit(grass,(x*100,y*100))
    screen.blit(castle,(0,30))
    screen.blit(castle,(0,135))
    screen.blit(castle,(0,240))
    screen.blit(castle,(0,345 ))

    
    
    
    # sRGB profile error / ImageMagick script
    screen.blit(player,(100,100))
    
    pygame.display.update()
    clock.tick(60)
