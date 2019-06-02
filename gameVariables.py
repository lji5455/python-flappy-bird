#!/usr/bin/env python
import pygame
from pygame.locals import *

#Global variables for the game
gameWidth = 300                         #Game window gameWidth
gameHeight = 500                        #Game window gameHeight
FPS = 60                                #Frames per second

birdHeight = 35                              #Height of the bird
birdWidth = 48                               #Width of the bird
jumpSteps = 10                               #Pixels to move
jumpPixels = 6                               #Pixels per frame Korean : 점프 속도 설정 default : 4
dropPixels = 5                               #Pixels per frame Korean : 하강 속도 설정 default : 3

groundHeight = 73                            #Height of the ground #default : 73
pipeWidth = 52                               #Width of a pipe
pipeHeight = 320                             #Max Height of a pipe
pipesSpace = 4 * birdHeight                  #Space between pipes
pipesAddInterval = 1150                      #Milliseconds

pixelsFrame = 3                              #Pixels per frame Korean : 맵 이동 설정
getNewPipe = USEREVENT + 1                   #Custom event

pygame.init()                                #Initialize pygame
screenResolution = pygame.display.Info()     #Get screen resolution
pygame.quit()                                #Close pygame

gameScore = 0                                #Game gameScore
waitClick = True                         
