import pygame
from pygame.locals import *
from time import *

pygame.init()

WIDTH=600
HEIGHT=600

screen = pygame.display.set_mode((WIDTH,HEIGHT))

player_x=200
player_y=200

keys=[False,False,False,False]#this is list of 4 arrows

player = pygame.image.load("Lesson 5/image/character.png")

background=pygame.image.load("Lesson 5/image/background.png")

while player_y<HEIGHT:
    screen.blit(background,(0,0))
    screen.blit(player,(player_x,player_y))
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)
        #check if any key is pressed
        if event.type==pygame.KEYDOWN:
            if event.key==K_UP:
                keys[0]=True
            elif event.key==K_LEFT:
                keys[1]=True
            elif event.key==K_DOWN:
                keys[2]=True
            elif event.key==K_RIGHT:
                keys[3]=True

        #check if key is released
        if event.type==pygame.KEYUP:
            if event.key==K_UP:
                keys[0]=False
            elif event.key==K_LEFT:
                keys[1]=False
            elif event.key==K_DOWN:
                keys[2]=False
            elif event.key==K_RIGHT:
                keys[3]=False

    if keys[0]==True:
       if player_y>0:
          player_y-=10

    elif keys[2]==True:
         if player_y<530:
            player_y+=10

    elif keys[1]==True:
         if player_x>0:
            player_x-=10

    elif keys[3]==True:
         if player_x<530:
            player_x+=10
    
    #When there isn't clicked anything rocket will fall down.
    player_y+=5
    sleep(0.01)


print("Game Over")


    

