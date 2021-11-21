import sys
import numpy as np
import pygame
import scipy.signal

ROWS = 6
COL = 7
SQUARE_SIZE = 100
HEIGHT = (ROWS + 1) * SQUARE_SIZE
WIDTH = COL * SQUARE_SIZE
SIZE = (WIDTH, HEIGHT)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
EMPTY = 0
PLAYER_1 = 1
PLAYER_2 = 2