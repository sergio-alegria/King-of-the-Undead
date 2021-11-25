from enum import Enum

# Map variables
ROWS = 25
MAX_COLS = 100

class Dir(Enum):
    up = 0
    down = 1
    left = 2
    right = 3
    stall = 4
