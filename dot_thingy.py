#!/usr/env python3
import random
import pygame, sys
import time

WIDTH = 640
HEIGHT = 480
STEP = 2
DOT_SIZE = 20

TOP = 0
LEFT = 0

OBS_X = 0
OBS_Y = 0

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

DIR = 2
SLEEP_TIME = 0.01

pygame.init()

windowSurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('dot thingy')
windowSurface.fill(WHITE)

def update_obstacle_position():
    global OBS_X
    global OBS_Y
    random.seed()
    OBS_X = random.randint(0, WIDTH - DOT_SIZE)
    OBS_Y = random.randint(0, HEIGHT - DOT_SIZE)


def draw_obstacle():
    pygame.draw.ellipse(windowSurface, GREEN, (OBS_X, OBS_Y, DOT_SIZE, DOT_SIZE))


def update_dir(event):
    global DIR

    if event.key == pygame.K_UP:
        DIR = 0
    elif event.key == pygame.K_DOWN:
        DIR = 1
    elif event.key == pygame.K_LEFT:
        DIR = 2
    elif event.key == pygame.K_RIGHT:
        DIR = 3

def update_position():
    global LEFT
    global TOP

    if DIR == 0:
        TOP -= STEP
        if TOP < 0:
            TOP = 0
    elif DIR == 1:
        TOP += STEP
        if TOP > HEIGHT - DOT_SIZE:
            TOP = HEIGHT - DOT_SIZE
    elif DIR == 2:
        LEFT -= STEP
        if LEFT < 0:
            LEFT = 0
    elif DIR == 3:
        LEFT += STEP
        if LEFT > WIDTH - DOT_SIZE:
            LEFT = WIDTH - DOT_SIZE
    pygame.draw.rect(windowSurface, RED, (LEFT, TOP, DOT_SIZE, DOT_SIZE))

def collision():
    return abs(LEFT - OBS_X) < 10 and abs(TOP - OBS_Y) < 10

def increase_speed():
    global SLEEP_TIME
    SLEEP_TIME -= 0.001

def update():
    windowSurface.fill(WHITE)
    update_position()
    draw_obstacle()
    if collision():
        update_obstacle_position()
        increase_speed()
    pygame.display.update()

update_obstacle_position()
while True:
    time.sleep(SLEEP_TIME)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            update_dir(event)
    update()


