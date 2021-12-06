from enum import Enum

# Map variables
DISPLAY_ROWS = 13
DISPLAY_COLS = 13

TILE_SIZE = 44

ROWS = 25
MAX_COLS = 100

# Game variables
speed = 3

# Key = backforund image, values = tile that need that bg
NEED_BAKGROUND = {
    0 : [1,2,3]
}

class Dir(Enum):
    up = 0
    down = 1
    left = 2
    right = 3
    stall = 4
