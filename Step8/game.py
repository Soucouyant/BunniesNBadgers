import pygame
import math
import random
from sys import exit

pygame.init()
width, height = 600,500
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

# Image Load
player = pygame.image.load("../BunniesNBadgers/resources/images/dude.png")
grass = pygame.image.load("../BunniesNBadgers/resources/images/grass.png")
castle = pygame.image.load("../BunniesNBadgers/resources/images/castle.png")
arrowImg = pygame.image.load("../BunniesNBadgers/resources/images/bullet.png")
badGuysImg1 = pygame.image.load("../BunniesNBadgers/resources/images/badguy.png")
healthBar = pygame.image.load("../BunniesNBadgers/resources/images/healthbar.png")
health = pygame.image.load("../BunniesNBadgers/resources/images/health.png")
badGuyImg = badGuysImg1

# Vars
keys = [False, False, False, False]
plrPos = [100,100]
acc = [0,0]
arrows = []
badTimer = 100
badTimer1 = 0
badGuys = [
    [640,100]
]
healthPoints = 194

while True:
    badTimer -= 1
    screen.fill(0)
    
    # Draw BG
    for x in range(width // grass.get_width()+1):
        for y in range(height // grass.get_height()+1):
            screen.blit(grass,(x*100,y*100))
    screen.blit(castle,(0,30))
    screen.blit(castle,(0,135))
    screen.blit(castle,(0,240))
    screen.blit(castle,(0,345 ))
    
    mousePos = pygame.mouse.get_pos()
    angle = math.atan2(mousePos[1]-(plrPos[1]+32), mousePos[0]-(plrPos[0]+26))
    plrRot = pygame.transform.rotate(player,360-angle*57.29)
    plrPos1 = (plrPos[0]-plrRot.get_rect().width/2, plrPos[1]-plrRot.get_rect().height/2)
    screen.blit(plrRot, plrPos1)
    
    for bullet in arrows:
        velx = math.cos(bullet[0]) * 10
        vely = math.sin(bullet[0]) * 10
        bullet[1] += velx
        bullet[2] += vely
        if bullet[1] <- 64 or bullet[1] > 640 or bullet[2] <- 64 or bullet[2] > 480:
            arrows.remove(bullet)
    for projectile in arrows:
        arrow1 = pygame.transform.rotate(arrowImg, 360-projectile[0] * 57.29)
        screen.blit(arrow1, (projectile[1] ,projectile[2]))
    
    if badTimer == 0:
        badGuys.append(
            [640, random.randint(50,430)]
        )
        badTimer = 100 - (badTimer1 * 2)
        if badTimer1 >= 35:
            badTimer1 = 35
        else:
            badTimer1+=5
    for badGuy in badGuys:
        if badGuy[0] <- 64:
            badGuys.remove(badGuy)
        badGuy[0] -= 7
        badrect = pygame.Rect(badGuyImg.get_rect())
        badrect.top = badGuy[1]
        badrect.left = badGuy[0]
        if badrect.left < 64:
            healthPoints -= random.randint(5,20)
            badGuys.remove(badGuy)
        for bullet in arrows:
            bullrect = pygame.Rect(arrowImg.get_rect())
            bullrect.left = bullet[1]
            bullrect.top = bullet[2]
            if badrect.colliderect(bullrect):
                acc[0] += 1
                badGuys.remove(badGuy)
                arrows.remove(bullet)
    for badGuy in badGuys:
        screen.blit(badGuyImg, badGuy)
        
    font = pygame.font.Font(None, 24)
    survivedtext = font.render(str("%.0f" % (pygame.time.get_ticks() / 120000))+":"+str( "%.0f" % (pygame.time.get_ticks() /1000 % 60)).zfill(2), True, (0,0,0))
    textRect = survivedtext.get_rect()
    textRect.topright=[580,10]
    screen.blit(survivedtext, textRect)
    screen.blit(healthBar, (5,5))
    for health1 in range(healthPoints):
        screen.blit(health, (health1+8,8))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            acc[1] += 1
            arrows.append([math.atan2(mousePos[1]-(plrPos1[1]+32),mousePos[0]-(plrPos1[0]+26)), plrPos1[0]+32, plrPos1[1]+32])
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
            
    pygame.display.update()
    clock.tick(60)