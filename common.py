from enum import Enum

# Map variables
DISPLAY_ROWS = 13
DISPLAY_COLS = 13

TILE_SIZE = 45

ROWS = 20
MAX_COLS = 50

# Game variables
speed = 1

# Key = backforund image, values = tile that need that bg
NEED_BAKGROUND = {
    0 : [15, 16, 17, 18, 19, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 38]
}

WALL_TILES = [33]

class Dir(Enum):
    up = 0
    down = 1
    left = 2
    right = 3
    stall = 4
