import pygame
import math
from sys import exit


width, height = 600,500
pygame.init()
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()


# Images
player = pygame.image.load("../BunniesNBadgers/resources/images/dude.png")
grass = pygame.image.load("../BunniesNBadgers/resources/images/grass.png")
castle = pygame.image.load("../BunniesNBadgers/resources/images/castle.png")

# Vars
keys = [False, False, False, False]
plrPos = [100,100]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                keys[0] = True
            elif event.key == pygame.K_a:
                keys[1] = True
            elif event.key == pygame.K_s:
                keys[2] = True
            elif event.key == pygame.K_d:
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys[0] = False
            if event.key == pygame.K_a:
                keys[1] = False
            if event.key == pygame.K_s:
                keys[2] = False
            if event.key == pygame.K_d:
                keys[3] = False
        if keys[0]:
            plrPos[1] -= 5
        elif keys[2]:
            plrPos[1] += 5
        if keys[1]:
            plrPos[0] -=5
        elif keys[3]:
            plrPos[0] += 5
                        
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
    # Movement is bugged
    mousePos = pygame.mouse.get_pos()
    angle = math.atan2(mousePos[1]-(plrPos[1]+32), mousePos[0]-(plrPos[0]+26))
    plrRot = pygame.transform.rotate(player,360-angle*57.29)
    plrPos1 = (plrPos[0]-plrRot.get_rect().width/2, plrPos[1]-plrRot.get_rect().height/2)
    screen.blit(plrRot, plrPos1)

    
    pygame.display.update()
    clock.tick(60)
