from enum import Enum

# Map variables
DISPLAY_ROWS = 12

ROWS = 25
MAX_COLS = 100

# Game variables
speed = 3

class Dir(Enum):
    up = 0
    down = 1
    left = 2
    right = 3
    stall = 4
