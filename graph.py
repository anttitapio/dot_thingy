#!/usr/env python3
import pygame, sys
from pygame.locals import *

WIDTH = 640
HEIGHT = 480
STEP = 10
DOT_SIZE = 20

TOP = 0
LEFT = 0

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()

windowSurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('dot thingy')

def update_position(event):
    global LEFT
    global TOP

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            LEFT += STEP
            if LEFT > WIDTH - DOT_SIZE:
                LEFT = WIDTH - DOT_SIZE
        elif event.key == pygame.K_LEFT:
            LEFT -= STEP
            if LEFT < 0:
                LEFT = 0
        elif event.key == pygame.K_UP:
            TOP -= STEP
            if TOP < 0:
                TOP = 0
        elif event.key == pygame.K_DOWN:
            TOP += STEP
            if TOP > HEIGHT - DOT_SIZE:
                TOP = HEIGHT - DOT_SIZE
    windowSurface.fill(WHITE)
    pygame.draw.rect(windowSurface, RED, (LEFT, TOP, DOT_SIZE, DOT_SIZE))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        update_position(event)
        pygame.display.update()

