import pygame,sys
from pygame.locals import *
import time

mel  =  "me.jpg"
fly  =  "fly.png"

pygame.init()
screen =  pygame.display.set_mode((400,300),0,32)
#pygame.display.set_caption("Pygame")
background = pygame.image.load(mel).convert()
mouse_c       = pygame.image.load(fly).convert_alpha()


 
    
x,y = 0,0
movex,movey = 0,0

while True:

    for event in pygame.event.get():
        if event.type  ==  QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if
             
        
