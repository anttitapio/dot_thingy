#!/usr/env python3
import random
import pygame, sys
import time
from collections import deque

WIDTH = 640
HEIGHT = 480
STEP = 3
DOT_SIZE = 15

TOP = 0
LEFT = 0

INCREASE_CONSTANT = 6
GAMEOVER = False

OBS_X = 0
OBS_Y = 0

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

DIR = 3
SLEEP_TIME = 0.01
COLL_TOLERANCE = 15

SCORE = 0
INITIAL_HISTORY = [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]

p_hist = deque(INITIAL_HISTORY)

pygame.init()

windowSurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('dot thingy')
windowSurface.fill(WHITE)
font = pygame.font.Font(None, 20)
bigfont = pygame.font.Font(None, 50)
TEXT = font.render('Score: 0', True, BLACK)


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

    if event.key == pygame.K_UP and DIR != 1:
        DIR = 0
    elif event.key == pygame.K_DOWN and DIR != 0:
        DIR = 1
    elif event.key == pygame.K_LEFT and DIR != 3:
        DIR = 2
    elif event.key == pygame.K_RIGHT and DIR != 2:
        DIR = 3

def update_position():
    global LEFT
    global TOP

    p_hist.rotate()
    p_hist[0] = (LEFT, TOP)

    if DIR == 0:
        if TOP > 0:
            TOP -= STEP
    elif DIR == 1:
        if TOP < HEIGHT - DOT_SIZE:
            TOP += STEP
    elif DIR == 2:
        if LEFT > 0:
            LEFT -= STEP
    elif DIR == 3:
        if LEFT < WIDTH - DOT_SIZE:
            LEFT += STEP

    for left, top in p_hist:
        pygame.draw.rect(windowSurface, RED, (left, top, DOT_SIZE, DOT_SIZE))


def collision():
    return abs(LEFT - OBS_X) < COLL_TOLERANCE and abs(TOP - OBS_Y) < COLL_TOLERANCE


def check_gameover():
    global GAMEOVER
    if (LEFT, TOP) in p_hist and (LEFT, TOP) != (0, 0):
        GAMEOVER_TEXT = bigfont.render('Game Over! Score: {}'.format(SCORE), True, BLACK)
        windowSurface.blit(GAMEOVER_TEXT, (WIDTH / 4, HEIGHT / 2))
        pygame.display.update()
        GAMEOVER = True

def increase_length():
    global p_hist
    for _ in range(0, INCREASE_CONSTANT):
        p_hist.append(p_hist[0])


def update():
    global SCORE, TEXT
    windowSurface.fill(WHITE)
    update_position()
    draw_obstacle()
    if collision():
        update_obstacle_position()
        increase_length()
        SCORE += 1
        TEXT = font.render('Score: {}'.format(SCORE), True, BLACK)
    windowSurface.blit(TEXT, (10, 10))


update_obstacle_position()
while True:
    while not GAMEOVER:
        time.sleep(SLEEP_TIME)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                update_dir(event)
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        update()
        check_gameover()
        pygame.display.update()
    time.sleep(3)
    p_hist = deque(INITIAL_HISTORY)
    LEFT = 0
    TOP = 0
    SCORE = 0
    GAMEOVER = False
    DIR = 3
    TEXT = font.render('Score: {}'.format(SCORE), True, BLACK)
    update_obstacle_position()




